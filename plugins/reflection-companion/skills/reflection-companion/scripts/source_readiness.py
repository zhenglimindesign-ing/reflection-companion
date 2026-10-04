#!/usr/bin/env python3
"""Read-only declared-source readiness check; not archive discovery or proof."""
import json
import sys


BASES = {'user_selected_corpus', 'export_inventory', 'provider_full_inventory', 'recent_index', 'unknown'}
RETRIEVAL = {'full_text', 'truncated', 'unavailable'}
ATTACHMENTS = {'none', 'retrieved', 'missing', 'unknown'}


def check(data):
    if not isinstance(data, dict) or data.get('schema_version') != 1:
        raise ValueError('Expected source inventory schema version 1')
    basis = data.get('inventory_basis')
    if basis not in BASES:
        raise ValueError('Unknown inventory basis')
    for name in ('discovery_complete', 'allow_partial'):
        if type(data.get(name)) is not bool:
            raise ValueError(name + ' must be a boolean')
    reference = data.get('inventory_reference')
    if not isinstance(reference, str):
        raise ValueError('inventory_reference must be a string')
    sources = data.get('sources')
    if not isinstance(sources, list):
        raise ValueError('sources must be a list')
    ids = set()
    for source in sources:
        if not isinstance(source, dict):
            raise ValueError('Each source must be an object')
        identifier = source.get('id')
        if not isinstance(identifier, str) or not identifier.strip() or identifier in ids:
            raise ValueError('Source IDs must be nonempty and unique')
        ids.add(identifier)
        if source.get('retrieval') not in RETRIEVAL or source.get('attachments') not in ATTACHMENTS:
            raise ValueError('Unknown retrieval or attachment status')
        for name in ('primary', 'dates_verified'):
            if type(source.get(name)) is not bool:
                raise ValueError('Source ' + name + ' must be a boolean')

    issues = []
    def issue(code, action, identifier=None):
        row = {'code': code, 'repair': action}
        if identifier is not None:
            row['source_id'] = identifier
        issues.append(row)

    if basis in {'recent_index', 'unknown'} or not data['discovery_complete'] or not reference.strip():
        issue('inventory_incomplete', 'obtain_or_verify_inventory')
    primary = [source for source in sources if source['primary']]
    if not primary:
        issue('no_primary_sources', 'obtain_requested_source_material')
    usable = []
    for source in primary:
        identifier = source['id']
        if source['retrieval'] != 'full_text':
            issue('text_' + source['retrieval'], 'retrieve_complete_text', identifier)
        if not source['dates_verified']:
            issue('dates_unverified', 'verify_original_dates', identifier)
        if source['attachments'] in {'missing', 'unknown'}:
            issue('attachments_' + source['attachments'], 'retrieve_or_resolve_attachments', identifier)
        if source['retrieval'] == 'full_text' and source['dates_verified'] and source['attachments'] in {'none', 'retrieved'}:
            usable.append(identifier)
    if not issues:
        decision = 'ready'
    elif data['allow_partial'] and usable:
        decision = 'partial_only'
    else:
        decision = 'blocked'
    return {
        'schema_version': 1,
        'decision': decision,
        'issues': issues,
        'usable_source_ids': usable,
        'declared_primary_source_count': len(primary),
        'broader_scope_complete': not issues,
        'limits': 'Checks declared metadata only; verify source references and actual retrieval. No account completeness proof.'
    }


def main():
    try:
        result = check(json.load(sys.stdin))
    except (ValueError, TypeError) as error:
        print(json.dumps({'decision': 'blocked', 'error': str(error)}, ensure_ascii=False))
        return 2
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 3 if result['decision'] == 'blocked' else 0


if __name__ == '__main__':
    sys.exit(main())
