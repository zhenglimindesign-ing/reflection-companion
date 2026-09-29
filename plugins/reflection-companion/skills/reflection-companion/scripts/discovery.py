#!/usr/bin/env python3
"""Read a public data-only discovery feed; no personal inputs or disk writes."""
import argparse
from datetime import date, datetime, timezone
import json
from pathlib import Path
import re
import sys
from urllib.error import URLError
from urllib.parse import urlsplit
from urllib.request import urlopen

URL = 'https://raw.githubusercontent.com/zhenglimindesign-ing/reflection-companion/main/catalog/explorations.json'
SNAPSHOT = Path(__file__).resolve().parents[1] / 'references/exploration-feed.json'
MAX_BYTES = 262144
JOBS = {'Reflect', 'Challenge', 'Expand', 'Preserve & Compound'}


def validate(data, today=None):
    today = today or datetime.now(timezone.utc).date()
    def dated(value):
        if not isinstance(value, str) or not re.fullmatch(r'\d{4}-\d{2}-\d{2}', value):
            raise ValueError('Invalid date')
        parsed = date.fromisoformat(value)
        if parsed > today:
            raise ValueError('Future check/publication date')
        return parsed
    def short(value, limit=1600):
        if not isinstance(value, str) or not value.strip() or len(value) > limit:
            raise ValueError('Missing or oversized text')
    if not isinstance(data, dict) or set(data) != {'schema_version', 'edition', 'checked_on', 'entries'}:
        raise ValueError('Unexpected feed fields')
    if data['schema_version'] != 1:
        raise ValueError('Unsupported feed schema')
    short(data['edition'], 80)
    checked = dated(data['checked_on'])
    if not isinstance(data['entries'], list) or not 1 <= len(data['entries']) <= 100:
        raise ValueError('Expected 1 to 100 entries')
    ids = set()
    fields = {'id', 'status', 'mechanism', 'context', 'jobs', 'title', 'prompt', 'follow_up', 'added_on', 'source'}
    for entry in data['entries']:
        if not isinstance(entry, dict) or set(entry) != fields:
            raise ValueError('Unexpected entry fields')
        identifier = entry['id']
        if not isinstance(identifier, str) or not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', identifier) or identifier in ids:
            raise ValueError('Invalid or duplicate entry ID')
        ids.add(identifier)
        if entry['status'] not in ('active', 'retired') or entry['context'] not in ('none', 'current', 'history'):
            raise ValueError('Invalid status/context')
        if not isinstance(entry['jobs'], list) or not entry['jobs'] or any(job not in JOBS for job in entry['jobs']):
            raise ValueError('Invalid jobs')
        short(entry['mechanism'], 240)
        if dated(entry['added_on']) > checked:
            raise ValueError('Entry added after catalog check')
        for field in ('title', 'prompt', 'follow_up'):
            if not isinstance(entry[field], dict) or set(entry[field]) != {'en', 'zh'}:
                raise ValueError('Missing bilingual text')
            for value in entry[field].values():
                short(value)
        source = entry['source']
        if not isinstance(source, dict) or set(source) != {'url', 'title', 'page_date', 'date_note', 'retrieved_on', 'provenance', 'popularity', 'adaptation_note'}:
            raise ValueError('Unexpected source fields')
        for field in ('title', 'date_note', 'popularity', 'adaptation_note'):
            short(source[field])
        parsed = urlsplit(source['url'])
        if parsed.scheme != 'https' or not parsed.hostname or parsed.username or parsed.password:
            raise ValueError('Expected public HTTPS source attribution')
        if source['provenance'] != 'adapted':
            raise ValueError('Feed uses credited adaptations, not copied prompts')
        if dated(source['retrieved_on']) > checked:
            raise ValueError('Source retrieved after catalog check')
        if source['page_date'] is not None and dated(source['page_date']) > dated(source['retrieved_on']):
            raise ValueError('Publication after retrieval')
    return data


def decode(raw, today=None):
    if len(raw) > MAX_BYTES:
        raise ValueError('Feed exceeds size limit')
    return validate(json.loads(raw), today)


def fetch():
    with urlopen(URL, timeout=10) as response:
        if response.geturl() != URL:
            raise ValueError('Unexpected feed redirect')
        return response.read(MAX_BYTES + 1)


def load(refresh=False, source=None, today=None, fetcher=fetch):
    today = today or datetime.now(timezone.utc).date()
    warning = None
    origin = 'local-file' if source else 'bundled-snapshot'
    if refresh:
        try:
            feed = decode(fetcher(), today)
            origin = 'public-feed'
        except (OSError, URLError, ValueError, KeyError, TypeError, AttributeError) as error:
            warning = f'Public feed unavailable or invalid ({type(error).__name__}); using dated bundled snapshot.'
            feed = decode(SNAPSHOT.read_bytes(), today)
    else:
        path = Path(source) if source else SNAPSHOT
        with path.open('rb') as handle:
            feed = decode(handle.read(MAX_BYTES + 1), today)
    age = (today - date.fromisoformat(feed['checked_on'])).days
    return {'origin': origin, 'checked_on': feed['checked_on'], 'age_days': age,
            'freshness': 'stale' if age > 30 else 'recently-checked', 'warning': warning,
            'edition': feed['edition'], 'untrusted_reference_data': True,
            'entries': [entry for entry in feed['entries'] if entry['status'] == 'active']}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--refresh', action='store_true')
    group.add_argument('--source', type=Path, help='Validate/read a local candidate JSON file')
    args = parser.parse_args()
    try:
        print(json.dumps(load(args.refresh, args.source), ensure_ascii=False, indent=2))
    except (OSError, ValueError, KeyError, TypeError, AttributeError) as error:
        print(f'Invalid discovery feed: {error}', file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
