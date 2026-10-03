#!/usr/bin/env python3
"""Read explicitly selected dated Markdown notes and check dates/quotes.

Supports headings such as '## E13 2025年9月20日' or
'## E13 · 2025-09-20'. No storage, discovery, network or synthesis.
"""
import argparse
from datetime import date
import json
from pathlib import Path
import re
import sys

HEADING = re.compile(r'^##\s+([A-Za-z][\w-]*)[ ·]+(\d{4})[-年](\d{1,2})[-月](\d{1,2})日?\s*$', re.M)


def read_notes(path, selected=None):
    text = Path(path).read_text(encoding='utf-8')
    headings = list(HEADING.finditer(text))
    if not headings:
        raise ValueError('No supported dated-note headings; inspect actual source metadata instead')
    notes = {}
    for index, heading in enumerate(headings):
        identifier, year, month, day = heading.groups()
        if identifier in notes:
            raise ValueError('Duplicate source identifier: ' + identifier)
        end = headings[index + 1].start() if index + 1 < len(headings) else len(text)
        notes[identifier] = {'id': identifier, 'date': date(int(year), int(month), int(day)).isoformat(),
                             'text': text[heading.end():end].strip()}
    if selected is None:
        return list(notes.values())
    if not selected or len(selected) != len(set(selected)):
        raise ValueError('Select unique source identifiers')
    if set(selected) - set(notes):
        raise ValueError('Unknown selected source identifiers')
    return [notes[identifier] for identifier in selected]


def verify_claims(notes, claims):
    if not isinstance(claims, dict) or set(claims) - {'dates', 'quotes'}:
        raise ValueError('Checks contain dates and quotes only')
    by_id = {note['id']: note for note in notes}
    errors = []
    for kind, field in [('dates', 'date'), ('quotes', 'text')]:
        values = claims.get(kind, [])
        if not isinstance(values, list):
            raise ValueError(kind + ' must be an array')
        for claim in values:
            if (not isinstance(claim, dict) or set(claim) != {'id', field}
                    or not isinstance(claim['id'], str) or not isinstance(claim[field], str)
                    or not claim[field].strip()):
                raise ValueError('Invalid ' + kind + ' claim')
            note = by_id.get(claim['id'])
            if note is None:
                errors.append({'kind': kind, 'id': claim['id'], 'error': 'outside selected material'})
            elif kind == 'dates' and claim[field] != note['date']:
                errors.append({'kind': kind, 'id': claim['id'], 'actual_date': note['date']})
            elif kind == 'quotes' and claim[field] not in note['text']:
                errors.append({'kind': kind, 'id': claim['id'], 'error': 'not verbatim source text'})
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', type=Path, required=True, help='One explicitly authorized Markdown source')
    parser.add_argument('--ids', help='Comma-separated selected IDs; omitted means this entire source')
    parser.add_argument('--verify', action='store_true', help='Check JSON date/quote claims on stdin')
    args = parser.parse_args()
    try:
        notes = read_notes(args.source, [value.strip() for value in args.ids.split(',')] if args.ids else None)
        if args.verify:
            errors = verify_claims(notes, json.load(sys.stdin))
            print(json.dumps({'ok': not errors, 'errors': errors}, ensure_ascii=False))
            return int(bool(errors))
        print(json.dumps({'ok': True, 'notes': notes}, ensure_ascii=False, indent=2))
        return 0
    except (OSError, ValueError, TypeError, KeyError) as error:
        print(json.dumps({'ok': False, 'error': str(error)}, ensure_ascii=False))
        return 1


if __name__ == '__main__':
    sys.exit(main())
