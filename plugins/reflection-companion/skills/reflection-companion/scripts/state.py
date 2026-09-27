#!/usr/bin/env python3
"""Local Companion state. One JSON request on stdin; JSON result on stdout.

No network, model calls, account-memory edits, or implicit initialization.
"""
import argparse
from contextlib import contextmanager
from datetime import datetime, timedelta, timezone
import json
import os
from pathlib import Path
import sys
import tempfile
import uuid
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError


class StateError(Exception):
    def __init__(self, code, message):
        self.code, self.message = code, message
        super().__init__(message)


def require(ok, code, message):
    if not ok:
        raise StateError(code, message)


def now():
    return datetime.now(timezone.utc).isoformat()


def string(value, field):
    require(isinstance(value, str) and bool(value.strip()), 'INVALID', f'{field} must be nonempty text')
    return value


def timestamp(value):
    string(value, 'timestamp')
    try:
        dt = datetime.fromisoformat(value.replace('Z', '+00:00'))
    except ValueError:
        raise StateError('INVALID', 'Timestamp must be ISO 8601 with an offset')
    require(dt.tzinfo is not None, 'INVALID', 'Timestamp needs an offset')
    return dt


def source(value, user=False):
    require(isinstance(value, dict), 'INVALID', 'Source must be an object')
    require(set(value) == {'uri', 'at', 'role'}, 'INVALID', 'Source requires uri, at, role only')
    string(value['uri'], 'source.uri')
    timestamp(value['at'])
    require(value['role'] in ('user', 'assistant', 'external'), 'INVALID', 'Invalid source role')
    require(not user or value['role'] == 'user', 'CONSENT_REQUIRED', 'User-authored authorization reference required')
    return dict(value)


def topics(value):
    require(isinstance(value, list), 'INVALID', 'topics must be an array')
    return sorted(set(string(v, 'topic').strip().casefold() for v in value))


def consent(req):
    require(req.get('consent') is True, 'CONSENT_REQUIRED', 'Explicit user consent required')
    return source(req.get('authorization'), user=True)


KINDS = {'decision', 'learning', 'open_question', 'reflection', 'observation', 'preference'}
STATUSES = {'active', 'superseded', 'dismissed', 'resolved'}
READS = {'inspect', 'context', 'get', 'export', 'novelty'}
MUTATIONS = {'add', 'confirm', 'correct', 'dismiss', 'resolve', 'delete', 'purge', 'settings', 'expose', 'delete_exposure'}


def validate_entry(entry):
    require(isinstance(entry, dict), 'INVALID', 'Entry must be an object')
    require(entry.get('kind') in KINDS, 'INVALID', 'Unknown entry kind')
    string(entry.get('id'), 'entry.id')
    string(entry.get('text'), 'entry.text')
    require(topics(entry.get('topics')) == entry['topics'], 'INVALID', 'Stored topics must be canonical')
    require(entry.get('status') in STATUSES, 'INVALID', 'Invalid entry status')
    require(entry.get('authority') in ('user_confirmed', 'ai_proposed'), 'INVALID', 'Invalid authority')
    sources = entry.get('sources')
    require(isinstance(sources, list) and len(sources) > 0, 'INVALID', 'At least one source required')
    for item in sources:
        source(item)
    if entry['authority'] == 'user_confirmed':
        source(entry.get('confirmation'), user=True)
    elif entry.get('confirmation') is not None:
        raise StateError('INVALID', 'Proposed entry cannot have a confirmation')
    timestamp(entry.get('created_at'))
    timestamp(entry.get('updated_at'))
    source(entry.get('save_authorization'), user=True)
    return entry


def validate_settings(settings):
    require(isinstance(settings, dict), 'INVALID', 'Invalid settings')
    for key in ('enabled', 'continuity_log'):
        require(type(settings.get(key)) is bool, 'INVALID', f'{key} must be boolean')
    try:
        ZoneInfo(string(settings.get('timezone'), 'timezone'))
    except (ZoneInfoNotFoundError, ValueError):
        raise StateError('INVALID', 'Use a valid IANA timezone')
    require(topics(settings.get('excluded_topics')) == settings['excluded_topics'], 'INVALID', 'Stored exclusions must be canonical')


def validate(doc):
    require(isinstance(doc, dict), 'CORRUPT', 'State must be an object')
    require(type(doc.get('schema_version')) is int and doc['schema_version'] == 1, 'SCHEMA_UNSUPPORTED', 'Unknown schema; no automatic migration')
    string(doc.get('store_id'), 'store_id')
    require(type(doc.get('revision')) is int and doc['revision'] >= 0, 'INVALID', 'Invalid revision')
    validate_settings(doc.get('settings'))
    source(doc.get('initial_authorization'), user=True)
    require(isinstance(doc.get('entries'), list) and isinstance(doc.get('exposures'), list), 'INVALID', 'Invalid collections')
    ids = set()
    for entry in doc['entries']:
        validate_entry(entry)
        require(entry['id'] not in ids, 'INVALID', 'Duplicate entry ID')
        ids.add(entry['id'])
    exposure_ids = set()
    for item in doc['exposures']:
        require(isinstance(item, dict), 'INVALID', 'Invalid exposure')
        for field in ('id', 'theme', 'text'):
            string(item.get(field), f'exposure.{field}')
        require(item['id'] not in exposure_ids, 'INVALID', 'Duplicate exposure ID')
        exposure_ids.add(item['id'])
        timestamp(item.get('at'))
        source(item.get('source'))
        require(topics(item.get('topics')) == item['topics'], 'INVALID', 'Stored topics must be canonical')
    return doc


def safe_paths(root):
    require(root.is_absolute() and root.name == '.reflection-companion', 'PATH', 'Use an absolute dedicated .reflection-companion directory')
    require(not root.is_symlink(), 'PATH', 'State directory must not be a symlink')
    if os.name == 'posix' and root.is_dir():
        require(root.stat().st_mode & 0o077 == 0, 'PERMISSIONS', 'State directory must be private to its owner; inspect permissions before retrying')
    for name in ('state.json', '.lock', '.gitignore'):
        path = root / name
        require(not path.is_symlink(), 'PATH', f'{name} must not be a symlink')
        require(not path.exists() or path.is_file(), 'PATH', f'{name} must be a regular file')


def read(root):
    safe_paths(root)
    path = root / 'state.json'
    require(path.is_file(), 'NOT_INITIALIZED', 'Saving is not initialized at this location')
    try:
        return validate(json.loads(path.read_text(encoding='utf-8')))
    except (ValueError, KeyError, TypeError) as exc:
        raise StateError('CORRUPT', 'State is invalid; original file left untouched') from exc


@contextmanager
def lock(root):
    safe_paths(root)
    path = root / '.lock'
    try:
        fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    except FileExistsError:
        raise StateError('BUSY', 'State is locked; inspect the owner before handling a stale lock')
    try:
        with os.fdopen(fd, 'w') as handle:
            handle.write(json.dumps({'pid': os.getpid(), 'at': now()}))
        yield
    finally:
        path.unlink()


def write(root, doc):
    validate(doc)
    safe_paths(root)
    fd, temporary = tempfile.mkstemp(prefix='.state-', suffix='.tmp', dir=root)
    try:
        with os.fdopen(fd, 'w', encoding='utf-8') as handle:
            json.dump(doc, handle, ensure_ascii=False, indent=2)
            handle.write('\n')
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, root / 'state.json')
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)


def scoped(doc, entries, wanted):
    excluded = set(doc['settings']['excluded_topics'])
    desired = set(topics(wanted))
    return [e for e in entries if not excluded.intersection(e['topics']) and (not desired or desired.intersection(e['topics']))]


def result(doc, **values):
    return {'ok': True, 'store_id': doc['store_id'], 'revision': doc['revision'], **values}


def new_entry(req, auth, stamp):
    data = req.get('entry')
    require(isinstance(data, dict), 'INVALID', 'entry object required')
    require(set(data) <= {'kind', 'text', 'topics', 'sources', 'authority', 'confirmation'}, 'INVALID', 'Unsupported entry field')
    entry = {**data, 'id': str(uuid.uuid4()), 'topics': topics(data.get('topics', [])),
             'status': 'active', 'created_at': stamp, 'updated_at': stamp,
             'confirmation': data.get('confirmation'), 'save_authorization': auth}
    return validate_entry(entry)


def run(root, req):
    require(isinstance(req, dict), 'INVALID', 'Request must be an object')
    op = req.get('op')
    require(op in READS | MUTATIONS | {'init'}, 'INVALID', 'Unknown operation')
    safe_paths(root)
    if op == 'init':
        auth = consent(req)
        settings = {'timezone': req.get('timezone'), 'enabled': True,
                    'continuity_log': req.get('continuity_log', False),
                    'excluded_topics': topics(req.get('excluded_topics', []))}
        validate_settings(settings)
        require(root.parent.is_dir(), 'PATH', 'Selected workspace must already exist')
        root.mkdir(mode=0o700, exist_ok=True)
        with lock(root):
            require(not (root / 'state.json').exists(), 'EXISTS', 'Existing store will not be reinitialized')
            # Refuse to overwrite a pre-existing ignore file.
            ignore = root / '.gitignore'
            if not ignore.exists():
                with ignore.open('x', encoding='utf-8') as handle:
                    handle.write('*\n')
            else:
                require(ignore.read_text().strip() == '*', 'PATH', 'Existing ignore file needs inspection')
            doc = {'schema_version': 1, 'store_id': str(uuid.uuid4()), 'revision': 0,
                   'initial_authorization': auth, 'settings': settings, 'entries': [], 'exposures': []}
            write(root, doc)
        return result(doc, path=str(root / 'state.json'), settings=settings)

    if op in READS:
        doc = read(root)
        if op in ('inspect', 'export'):
            return result(doc, state=doc)
        if op == 'get':
            entry = next((e for e in doc['entries'] if e['id'] == req.get('id')), None)
            require(entry is not None, 'NOT_FOUND', 'Entry not found')
            return result(doc, entry=entry)
        require(doc['settings']['enabled'], 'DISABLED', 'Saving/continuity is disabled; explicit inspection is still available')
        entries = scoped(doc, [e for e in doc['entries'] if e['status'] == 'active'], req.get('topics', []))
        days = req.get('days', 14)
        require(type(days) is int and 1 <= days <= 90, 'INVALID', 'days must be 1 through 90')
        cutoff = datetime.now(timezone.utc) - timedelta(days=days)
        exposures = scoped(doc, [e for e in doc['exposures'] if timestamp(e['at']) >= cutoff], req.get('topics', []))
        if op == 'novelty':
            theme = string(req.get('theme'), 'theme').strip().casefold()
            return result(doc, exact_matches=[e for e in exposures if e['theme'].strip().casefold() == theme],
                          recent=exposures, semantic_check_required=True)
        return result(doc, confirmed=[e for e in entries if e['authority'] == 'user_confirmed'],
                      tentative=[e for e in entries if e['authority'] == 'ai_proposed'], exposures=exposures,
                      settings=doc['settings'])

    require(root.is_dir(), 'NOT_INITIALIZED', 'Saving is not initialized')
    with lock(root):
        doc = read(root)
        expected = req.get('expected_revision')
        require(type(expected) is int and expected == doc['revision'], 'CONFLICT', 'Read current state and reconcile; expected_revision is stale or missing')
        if op not in ('settings', 'delete', 'purge', 'delete_exposure'):
            require(doc['settings']['enabled'], 'DISABLED', 'Saving is disabled')
        auth = consent(req) if op != 'expose' or not doc['settings']['continuity_log'] else None
        stamp, payload = now(), {}
        if op in ('add', 'correct'):
            entry = new_entry(req, auth, stamp)
            require(not set(entry['topics']).intersection(doc['settings']['excluded_topics']), 'SCOPE', 'Entry uses excluded topics')
            if op == 'correct':
                old = next((e for e in doc['entries'] if e['id'] == req.get('id')), None)
                require(old is not None and old['status'] == 'active', 'NOT_FOUND', 'Active entry not found')
                require(entry['authority'] == 'user_confirmed', 'INVALID', 'Correction must preserve user-confirmed replacement meaning')
                old.update(status='superseded', superseded_by=entry['id'], updated_at=stamp)
                entry['supersedes'] = old['id']
            doc['entries'].append(entry)
            payload = {'entry': entry}
        elif op in ('confirm', 'dismiss', 'resolve', 'delete'):
            entry = next((e for e in doc['entries'] if e['id'] == req.get('id')), None)
            require(entry is not None, 'NOT_FOUND', 'Entry not found')
            if op == 'delete':
                doc['entries'].remove(entry)
                for other in doc['entries']:
                    for field in ('supersedes', 'superseded_by'):
                        if other.get(field) == entry['id']:
                            del other[field]
                payload = {'deleted_id': entry['id']}
            else:
                require(entry['status'] == 'active', 'INVALID', 'Only active entries can transition')
                if op == 'confirm':
                    entry.update(authority='user_confirmed', confirmation=auth)
                else:
                    if op == 'resolve':
                        require(entry['kind'] == 'open_question', 'INVALID', 'Only an open question can be resolved')
                    entry.update(status='dismissed' if op == 'dismiss' else 'resolved', disposition_authorization=auth)
                entry['updated_at'] = stamp
                payload = {'entry': entry}
        elif op == 'purge':
            doc['entries'], doc['exposures'] = [], []
            doc['settings'].update(enabled=False, continuity_log=False)
            payload = {'purged': True, 'host_history_and_exports_unchanged': True}
        elif op == 'settings':
            changes = req.get('settings')
            require(isinstance(changes, dict) and set(changes) <= {'timezone', 'enabled', 'continuity_log', 'excluded_topics'}, 'INVALID', 'Unsupported settings')
            changes = dict(changes)
            if 'excluded_topics' in changes:
                changes['excluded_topics'] = topics(changes['excluded_topics'])
            doc['settings'].update(changes)
            validate_settings(doc['settings'])
            doc['settings_authorization'] = auth
            payload = {'settings': doc['settings']}
        elif op == 'expose':
            data = req.get('exposure')
            require(isinstance(data, dict) and set(data) == {'theme', 'text', 'topics', 'source'}, 'INVALID', 'Exposure requires theme, text, topics, source')
            item = {'id': str(uuid.uuid4()), 'theme': string(data['theme'], 'theme'),
                    'text': string(data['text'], 'text'), 'topics': topics(data['topics']),
                    'source': source(data['source']), 'at': stamp}
            require(not set(item['topics']).intersection(doc['settings']['excluded_topics']), 'SCOPE', 'Exposure uses excluded topics')
            cutoff = datetime.now(timezone.utc) - timedelta(days=90)
            doc['exposures'] = [e for e in doc['exposures'] if timestamp(e['at']) >= cutoff] + [item]
            payload = {'exposure': item}
        elif op == 'delete_exposure':
            matches = [e for e in doc['exposures'] if e['id'] == req.get('id')]
            require(bool(matches), 'NOT_FOUND', 'Exposure not found')
            doc['exposures'].remove(matches[0])
            payload = {'deleted_id': req['id']}
        doc['revision'] += 1
        write(root, doc)
        return result(doc, **payload)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, required=True)
    args = parser.parse_args()
    try:
        request = json.load(sys.stdin)
        response = run(args.root, request)
    except StateError as exc:
        response = {'ok': False, 'error': exc.code, 'message': exc.message}
    except (OSError, ValueError, TypeError, KeyError):
        response = {'ok': False, 'error': 'IO_OR_INVALID', 'message': 'Operation failed; do not claim success. Inspect permissions/input/store without overwriting it.'}
    print(json.dumps(response, ensure_ascii=False))
    return 0 if response['ok'] else 1


if __name__ == '__main__':
    sys.exit(main())
