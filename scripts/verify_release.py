#!/usr/bin/env python3
"""Verify a public checkout/extracted release without dependencies or network."""
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import sys
from urllib.parse import unquote, urlsplit


def safe_path(name):
    p = PurePosixPath(name)
    if not name or p.is_absolute() or '..' in p.parts or '\\' in name or str(p) != name:
        raise ValueError(f'Unsafe inventory path: {name}')
    return p


def verify(root):
    root = Path(root).resolve()
    errors = []
    manifest_path = root / 'release-manifest.json'
    if manifest_path.is_symlink():
        raise ValueError('Symlinked manifest')
    manifest = json.loads(manifest_path.read_text())
    inventory = manifest['files_sha256']
    for name, digest in inventory.items():
        relative = safe_path(name)
        path = root.joinpath(*relative.parts)
        if any(part.is_symlink() for part in [path, *path.parents] if part != root.parent):
            errors.append(f'Symlink: {name}')
            continue
        if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != digest:
            errors.append(f'Missing/changed file: {name}')
    actual = {p.relative_to(root).as_posix() for p in root.rglob('*')
              if (p.is_file() or p.is_symlink()) and '.git' not in p.relative_to(root).parts}
    expected = set(inventory) | {'release-manifest.json'}
    if actual != expected:
        errors.append(f'Inventory mismatch: extra={sorted(actual-expected)}, missing={sorted(expected-actual)}')
    for name in sorted(expected & actual):
        if not name.endswith('.md'):
            continue
        path = root / name
        if path.is_symlink():
            continue
        text = re.sub(r'^```[^\n]*\n.*?^```\s*$', '', path.read_text(), flags=re.M | re.S)
        text = re.sub(r'`[^`\n]*`', '', text)
        for target in re.findall(r'\]\(([^)]+)\)', text):
            url = urlsplit(target)
            if url.scheme or url.netloc or not url.path:
                continue
            destination = (path.parent / unquote(url.path)).resolve()
            if not destination.is_relative_to(root) or not destination.is_file():
                errors.append(f'Broken/local escaping link: {name}: {target}')
    catalog = json.loads((root / '.agents/plugins/marketplace.json').read_text())
    entry = catalog['plugins'][0]
    plugin = root / entry['source']['path']
    data = json.loads((plugin / '.codex-plugin/plugin.json').read_text())
    if data['version'] != manifest['version'] or data['name'] != entry['name']:
        errors.append('Version/plugin identity mismatch')
    if not (plugin / data['skills'] / 'reflection-companion/SKILL.md').is_file():
        errors.append('Missing Skill entrypoint')
    return errors


def main():
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]
    try:
        errors = verify(root)
    except (OSError, ValueError, KeyError, TypeError) as error:
        errors = [str(error)]
    if errors:
        print('\n'.join(errors), file=sys.stderr)
        return 1
    print('PASS: public file inventory, hashes, local links, plugin paths and version')
    return 0


if __name__ == '__main__':
    sys.exit(main())
