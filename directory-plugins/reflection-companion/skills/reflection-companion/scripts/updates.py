#!/usr/bin/env python3
"""Check releases; explicitly prepare, upgrade or roll back the Codex Git install.

Python 3.11+; stdlib only. No diary paths, state migration, background service or
Claude-account writes. JSON receipts describe disk installation, not chat reload.
"""
import argparse
from contextlib import contextmanager
from datetime import datetime, timezone
import hashlib
import io
import json
import os
from pathlib import Path, PurePosixPath
import re
import subprocess
import sys
import tempfile
import tomllib
from urllib.request import Request, urlopen
import zipfile

NAME = 'reflection-companion'
PLUGIN_ID = NAME + '@' + NAME
REPO = 'zhenglimindesign-ing/reflection-companion'
PUBLIC = 'https://github.com/' + REPO
SOURCE = PUBLIC + '.git'
PLUGIN = 'plugins/' + NAME
MAX_DOWNLOAD = 32 * 1024 * 1024
STABLE = re.compile(r'^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)$')


def sha(data):
    return hashlib.sha256(data).hexdigest()


def stable(version):
    if not isinstance(version, str) or not STABLE.fullmatch(version):
        raise ValueError('Select a formal x.y.z release; prereleases and branches are excluded')
    return tuple(map(int, version.split('.')))


def read_json(path):
    return json.loads(Path(path).read_text())


def write_json(path, value):
    path = Path(path)
    temporary = path.with_suffix(path.suffix + '.tmp')
    temporary.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')
    temporary.replace(path)


def inventory(root):
    root = Path(root)
    if root.absolute() != root.resolve() or root.is_symlink() or not root.is_dir():
        raise ValueError('Missing or symlinked installation/package directory')
    result = {}
    for path in root.rglob('*'):
        if path.is_symlink():
            raise ValueError('Symlink in package/installation')
        if path.is_file():
            result[path.relative_to(root).as_posix()] = sha(path.read_bytes())
    return result


def safe_name(name):
    path = PurePosixPath(name)
    if not name or path.is_absolute() or '..' in path.parts or '\\' in name or str(path) != name:
        raise ValueError('Unsafe release inventory/archive path')
    return name


def verify_bundle(root):
    root = Path(root)
    actual = inventory(root)
    manifest = read_json(root / 'release-manifest.json')
    stable(manifest['version'])
    if manifest.get('schema_version') != 1 or manifest.get('repository') != PUBLIC:
        raise ValueError('Unexpected release identity/schema')
    compatibility = manifest.get('state_compatibility')
    if compatibility is None and manifest['version'] not in ('0.4.0', '0.5.0'):
        raise ValueError('Missing state compatibility declaration; do not guess migration safety')
    if compatibility is not None and compatibility != {'schema_version': 1, 'migration': 'none'}:
        raise ValueError('This updater supports only schema-v1 releases without migration')
    expected = manifest['files_sha256']
    if not isinstance(expected, dict) or set(actual) != set(expected) | {'release-manifest.json'}:
        raise ValueError('Release inventory mismatch')
    for name, digest in expected.items():
        safe_name(name)
        if actual[name] != digest:
            raise ValueError('Release hash mismatch: ' + name)
    plugin = root / PLUGIN
    verify_plugin(plugin, manifest['version'])
    catalog = read_json(root / '.agents/plugins/marketplace.json')
    if catalog.get('name') != NAME or len(catalog.get('plugins', [])) != 1:
        raise ValueError('Unexpected marketplace identity')
    entry = catalog['plugins'][0]
    if entry.get('name') != NAME or entry.get('source') != {'source': 'local', 'path': './' + PLUGIN}:
        raise ValueError('Unexpected marketplace plugin source')
    return manifest


def verify_plugin(root, version):
    stable(version)
    data = read_json(Path(root) / '.codex-plugin/plugin.json')
    if data.get('name') != NAME or data.get('version') != version or data.get('skills') != './skills/':
        raise ValueError('Installed plugin identity/version mismatch')
    if not (Path(root) / 'skills' / NAME / 'SKILL.md').is_file():
        raise ValueError('Missing installed Skill')
    return inventory(root)


def download(url, limit=MAX_DOWNLOAD):
    # Release/API URLs are fixed public sources; no tokens or user material.
    request = Request(url, headers={'User-Agent': 'reflection-companion-updates',
                                   'Accept': 'application/vnd.github+json'})
    with urlopen(request, timeout=30) as response:
        if not response.url.startswith('https://'):
            raise ValueError('Insecure release redirect')
        data = response.read(limit + 1)
    if len(data) > limit:
        raise ValueError('Release download exceeds size limit')
    return data


def release_info(version=None, fetch=download):
    suffix = 'latest' if version is None else 'tags/v' + version
    if version is not None:
        stable(version)
    data = json.loads(fetch('https://api.github.com/repos/' + REPO + '/releases/' + suffix, 1024 * 1024))
    tag = data.get('tag_name', '')
    selected = tag.removeprefix('v')
    stable(selected)
    if tag != 'v' + selected or data.get('draft') or data.get('prerelease') or (version and selected != version):
        raise ValueError('Not the selected formal public release')
    expected_url = PUBLIC + '/releases/tag/' + tag
    if data.get('html_url') != expected_url:
        raise ValueError('Unexpected release URL')
    assets = {item['name']: item['browser_download_url'] for item in data.get('assets', [])}
    filename = NAME + '-' + selected + '.zip'
    for name in (filename, 'SHA256SUMS.txt'):
        if assets.get(name) != PUBLIC + '/releases/download/' + tag + '/' + name:
            raise ValueError('Missing or unexpected release asset')
    return {'version': selected, 'tag': tag, 'url': expected_url,
            'published_at': data.get('published_at'), 'notes': str(data.get('body') or '')[:12000],
            'archive_url': assets[filename], 'checksums_url': assets['SHA256SUMS.txt']}


def prepare(version, out, fetch=download, home=None):
    info = release_info(version, fetch)
    checksum_text = fetch(info['checksums_url'], 65536).decode()
    filename = NAME + '-' + info['version'] + '.zip'
    matches = re.findall(r'^([a-f0-9]{64})  ' + re.escape(filename) + r'$', checksum_text, re.M)
    if len(matches) != 1:
        raise ValueError('Missing/ambiguous package checksum')
    archive = fetch(info['archive_url'])
    if sha(archive) != matches[0]:
        raise ValueError('Package checksum mismatch; installation unchanged')
    # Validate all members before creating even a staging directory.
    files = {}
    prefix = NAME + '-' + info['version'] + '/'
    with zipfile.ZipFile(io.BytesIO(archive)) as package:
        if sum(item.file_size for item in package.infolist()) > MAX_DOWNLOAD:
            raise ValueError('Expanded package exceeds size limit')
        for item in package.infolist():
            if item.is_dir() or not item.filename.startswith(prefix):
                raise ValueError('Unexpected archive member')
            name = safe_name(item.filename[len(prefix):])
            if name in files or (item.external_attr >> 16) & 0o170000 == 0o120000:
                raise ValueError('Duplicate/symlinked archive member')
            files[name] = package.read(item)
    out = new_output(out, home)
    tree = out / (NAME + '-' + info['version'])
    for name, data in files.items():
        path = tree / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
    try:
        verify_bundle(tree)
    except Exception:
        write_json(out / 'prepared.json', {'status': 'invalid', 'installation_changed': False})
        raise
    (out / filename).write_bytes(archive)
    result = dict(info, status='prepared', package=str(tree), archive_sha256=sha(archive),
                  manifest_sha256=sha((tree / 'release-manifest.json').read_bytes()), installation_changed=False)
    write_json(out / 'prepared.json', result)
    return result


def new_output(out, home=None):
    out = Path(out).expanduser().absolute()
    if out != out.resolve() or '.reflection-companion' in out.parts:
        raise ValueError('Select a new ordinary directory outside personal state')
    if home and (out.is_relative_to(home) or home.is_relative_to(out)):
        raise ValueError('Recovery/output directory must be outside Codex home')
    out.mkdir(parents=True, exist_ok=False)
    return out


class CodexInstall:
    def __init__(self, home, executable='codex'):
        self.home = Path(home).expanduser().absolute()
        if self.home != self.home.resolve():
            raise ValueError('Symlinked Codex home is unsupported')
        self.config = self.home / 'config.toml'
        self.executable = executable

    def config_bytes(self):
        if self.config.is_symlink():
            raise ValueError('Symlinked config is unsupported')
        return self.config.read_bytes()

    def inspect(self):
        config = tomllib.loads(self.config_bytes().decode())
        source = config.get('marketplaces', {}).get(NAME, {})
        if source.get('source_type') != 'git' or source.get('source') != SOURCE:
            raise ValueError('Only the existing official Codex Git marketplace install is supported')
        version = source.get('ref', '').removeprefix('v')
        stable(version)
        if source['ref'] != 'v' + version:
            raise ValueError('Current install must be pinned to a formal release')
        enabled = {key for key, value in config.get('plugins', {}).items()
                   if key.startswith(NAME + '@') and value.get('enabled') is True}
        if enabled != {PLUGIN_ID}:
            raise ValueError('Enable only the intended existing plugin before updating')
        root = self.home / 'plugins/cache' / NAME / NAME / version
        hashes = verify_plugin(root, version)
        snapshot = self.home / '.tmp/marketplaces' / NAME
        manifest = read_json(snapshot / 'release-manifest.json')
        prefix = PLUGIN + '/'
        expected = {key[len(prefix):]: digest for key, digest in manifest['files_sha256'].items()
                    if key.startswith(prefix)}
        if manifest.get('version') != version or manifest.get('repository') != PUBLIC or hashes != expected:
            raise ValueError('Cache/snapshot drift or local customization; reconcile before replacement')
        return {'status': 'inspected', 'plugin_id': PLUGIN_ID, 'version': version, 'ref': source['ref'],
                'source': SOURCE, 'installed_root': str(root), 'files_sha256': hashes,
                'config_sha256': sha(self.config_bytes()), 'chat_reload_verified': False}

    def run(self, *args):
        env = dict(os.environ, CODEX_HOME=str(self.home))
        try:
            result = subprocess.run([self.executable, 'plugin', *args, '--json'], env=env,
                                    text=True, capture_output=True, timeout=90)
            if result.returncode:
                raise ValueError('Codex ' + ' '.join(args[:2]) + ' failed; inspect the recovery receipt')
            data = json.loads(result.stdout)
            if data.get('errors'):
                raise ValueError('Codex marketplace reported errors')
            return data
        except subprocess.TimeoutExpired as error:
            raise ValueError('Codex command timed out; recovery will be attempted once') from error

    def set_ref(self, ref, expected_hash=None):
        original = self.config_bytes()
        if expected_hash and sha(original) != expected_hash:
            raise ValueError('Config changed since inspection; no update applied')
        text = original.decode()
        before = tomllib.loads(text)
        # Current CLI cannot change an existing marketplace ref with `add`.
        # Preserve the document and assert the complete parsed diff is one field.
        section = re.search(r'^\[marketplaces\.reflection-companion\]\s*\n(?P<body>.*?)(?=^\[|\Z)', text, re.M | re.S)
        if not section:
            raise ValueError('Unsupported config layout; do not rewrite the whole config')
        body, count = re.subn(r'^ref\s*=.*$', 'ref = ' + json.dumps(ref), section['body'], flags=re.M)
        if count != 1:
            raise ValueError('Missing/ambiguous marketplace ref')
        changed = text[:section.start('body')] + body + text[section.end('body'):]
        expected = json.loads(json.dumps(before))
        expected['marketplaces'][NAME]['ref'] = ref
        if tomllib.loads(changed) != expected:
            raise ValueError('Config edit would change unrelated settings')
        # Atomic replacement prevents a truncated TOML on interruption. Other
        # host writers do not share this helper's lock, so check again directly
        # before the replacement and after the native operations.
        mode = self.config.stat().st_mode & 0o777
        descriptor, temporary_name = tempfile.mkstemp(prefix='.reflection-companion-config-', dir=self.home)
        temporary = Path(temporary_name)
        try:
            with os.fdopen(descriptor, 'wb') as stream:
                stream.write(changed.encode())
                stream.flush()
                os.fsync(stream.fileno())
            temporary.chmod(mode)
            if self.config_bytes() != original:
                raise ValueError('Config changed during preparation')
            temporary.replace(self.config)
        finally:
            if temporary.exists():
                temporary.unlink()

    def install(self, ref):
        self.set_ref(ref)
        self.run('marketplace', 'upgrade', NAME)
        self.run('add', PLUGIN_ID)

    @contextmanager
    def lock(self):
        path = self.home / 'plugins' / '.reflection-companion-update.lock'
        try:
            descriptor = os.open(path, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
        except FileExistsError as error:
            raise ValueError('Another/interrupted update holds the lock; inspect its receipt before removing it') from error
        try:
            os.write(descriptor, str(os.getpid()).encode())
            os.close(descriptor)
            yield
        finally:
            path.unlink()


def unrelated(config_bytes):
    data = tomllib.loads(config_bytes.decode())
    market = data['marketplaces'][NAME]
    for key in ('ref', 'last_updated', 'last_revision'):
        market.pop(key, None)
    return data


def copy_plugin(source, destination, expected):
    if inventory(source) != expected:
        raise ValueError('Installation changed before backup')
    for name in expected:
        target = destination / name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes((source / name).read_bytes())
    if inventory(destination) != expected:
        raise ValueError('Recovery backup failed integrity check')


def switch(install, target_plugin, version, out, apply=False, recovery_receipt=None):
    target_plugin = Path(target_plugin)
    target_hashes = verify_plugin(target_plugin, version)
    current = install.inspect()
    if current['version'] == version:
        if current['files_sha256'] != target_hashes:
            raise ValueError('Same version has different bytes; reconcile without reinstalling')
        return {'status': 'already_installed', 'version': version, 'installation_changed': False,
                'chat_reload_verified': False}
    if recovery_receipt is None and stable(version) < stable(current['version']):
        raise ValueError('Use rollback with a verified receipt for a downgrade')
    result = {'status': 'planned', 'from_version': current['version'], 'to_version': version,
              'plugin_id': PLUGIN_ID, 'personal_records_accessed': False,
              'chat_reload_verified': False, 'installation_changed': False}
    if not apply:
        return result
    with install.lock():
        if install.inspect() != current:
            raise ValueError('Installation/config changed since plan')
        out = new_output(out, install.home)
        before_config = install.config_bytes()
        copy_plugin(Path(current['installed_root']), out / 'previous-plugin', current['files_sha256'])
        # Receipts contain only this plugin, hashes and its recovery ref; no
        # whole-config copy, credentials, chats, diary text or preference values.
        result.update(previous=current, target_files_sha256=target_hashes,
                      started_at=datetime.now(timezone.utc).isoformat(),
                      recovery_receipt=str(recovery_receipt) if recovery_receipt else None)
        receipt = out / 'receipt.json'
        result['status'] = 'switching'
        write_json(receipt, result)
        try:
            install.set_ref('v' + version, current['config_sha256'])
        except (OSError, ValueError) as error:
            result.update(status='aborted', error=str(error), receipt=str(receipt))
            write_json(receipt, result)
            return result
        try:
            install.run('marketplace', 'upgrade', NAME)
            install.run('add', PLUGIN_ID)
            installed = install.inspect()
            if installed['files_sha256'] != target_hashes or unrelated(install.config_bytes()) != unrelated(before_config):
                raise ValueError('Installed bytes or unrelated settings do not match')
            result.update(status='installed', installation_changed=True,
                          installed_version=installed['version'], rollback_receipt=str(receipt))
        except (OSError, ValueError, KeyError, TypeError) as error:
            result.update(status='recovering', error=str(error), installation_changed=True)
            write_json(receipt, result)
            try:
                now = install.config_bytes()
                selected = tomllib.loads(now.decode())['marketplaces'][NAME]
                if selected.get('ref') != 'v' + version or unrelated(now) != unrelated(before_config):
                    raise ValueError('Configuration changed outside this update; preserve it and inspect recovery')
                install.install(current['ref'])
                recovered = install.inspect()
                if recovered['files_sha256'] != current['files_sha256']:
                    raise ValueError('Recovered files differ from backup')
                if unrelated(install.config_bytes()) != unrelated(before_config):
                    raise ValueError('Unrelated settings changed; preserve and reconcile')
                result.update(status='failed_recovered', installed_version=current['version'])
            except (OSError, ValueError, KeyError, TypeError) as recovery_error:
                result.update(status='needs_recovery', recovery_error=str(recovery_error),
                              previous_plugin=str(out / 'previous-plugin'))
        write_json(receipt, result)
        result['receipt'] = str(receipt)
        return result


def rollback(install, receipt_path, out, apply=False):
    receipt_path = Path(receipt_path).absolute()
    receipt = read_json(receipt_path)
    if receipt.get('status') != 'installed' or receipt.get('plugin_id') != PLUGIN_ID:
        raise ValueError('Select a successful update receipt; interrupted recovery needs inspection')
    current = install.inspect()
    if current['version'] != receipt['to_version'] or current['files_sha256'] != receipt['target_files_sha256']:
        raise ValueError('Installation changed since this receipt; select the matching receipt')
    previous = receipt['previous']
    backup = receipt_path.parent / 'previous-plugin'
    if previous['plugin_id'] != PLUGIN_ID or previous['ref'] != 'v' + previous['version']:
        raise ValueError('Invalid rollback identity/ref')
    if inventory(backup) != previous['files_sha256']:
        raise ValueError('Rollback backup changed; preserve it and stop')
    return switch(install, backup, previous['version'], out, apply, receipt_path)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--codex-home', type=Path, default=Path(os.environ.get('CODEX_HOME', str(Path.home() / '.codex'))))
    subs = parser.add_subparsers(dest='op', required=True)
    subs.add_parser('inspect')
    check = subs.add_parser('check')
    check.add_argument('--version')
    stage = subs.add_parser('prepare')
    stage.add_argument('--version', required=True)
    stage.add_argument('--out', type=Path, required=True)
    upgrade = subs.add_parser('upgrade')
    upgrade.add_argument('--package', type=Path, required=True)
    upgrade.add_argument('--out', type=Path, required=True)
    upgrade.add_argument('--apply', action='store_true')
    back = subs.add_parser('rollback')
    back.add_argument('--receipt', type=Path, required=True)
    back.add_argument('--out', type=Path, required=True)
    back.add_argument('--apply', action='store_true')
    args = parser.parse_args()
    install = CodexInstall(args.codex_home)
    try:
        if args.op == 'inspect':
            result = install.inspect()
        elif args.op == 'check':
            current = install.inspect()
            latest = release_info(args.version)
            result = {'status': 'checked', 'installed_version': current['version'],
                      'available': latest, 'newer': stable(latest['version']) > stable(current['version']),
                      'installation_changed': False, 'chat_reload_verified': False}
        elif args.op == 'prepare':
            result = prepare(args.version, args.out, home=install.home)
        elif args.op == 'upgrade':
            manifest = verify_bundle(args.package)
            result = switch(install, args.package / PLUGIN, manifest['version'], args.out, args.apply)
        else:
            result = rollback(install, args.receipt, args.out, args.apply)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 1 if result['status'] in ('failed_recovered', 'needs_recovery', 'aborted') else 0
    except (OSError, ValueError, KeyError, TypeError, zipfile.BadZipFile) as error:
        print(json.dumps({'status': 'error', 'error': str(error)}, ensure_ascii=False))
        return 1


if __name__ == '__main__':
    sys.exit(main())
