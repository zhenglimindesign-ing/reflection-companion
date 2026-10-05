#!/usr/bin/env python3
"""Read-only source and message reconciliation; no discovery, saving or prose."""
from datetime import datetime
import json
import sys


BASES = {'user_selected_corpus', 'export_inventory', 'provider_full_inventory', 'recent_index', 'unknown'}
RETRIEVAL = {'full_text', 'truncated', 'unavailable'}
ATTACHMENTS = {'none', 'retrieved', 'missing', 'unknown'}


def check(data):
    if isinstance(data, dict) and data.get('schema_version') == 2:
        return check_evidence(data)
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


def unique_ids(value, name):
    if not isinstance(value, list) or any(not isinstance(i, str) or not i.strip() for i in value):
        raise ValueError(name + ' must contain nonempty string IDs')
    if len(value) != len(set(value)):
        raise ValueError(name + ' must contain unique IDs')
    return set(value)


def check_evidence(data):
    """Reconcile observed text against a verified inventory and delivery choices.

    IDs/boundary references must come from the source, not from the prose writer.
    This detects gaps in supplied evidence; it cannot authenticate its provenance.
    """
    stage = data.get('stage')
    if stage not in {'retrieval', 'delivery'}:
        raise ValueError('stage must be retrieval or delivery')
    declared = dict(data, schema_version=1)
    result = check(declared)
    issues = result['issues']
    def issue(code, repair, source_id=None, message_id=None):
        row = {'code': code, 'repair': repair}
        if source_id is not None:
            row['source_id'] = source_id
        if message_id is not None:
            row['message_id'] = message_id
        issues.append(row)

    expected_sources = unique_ids(data.get('expected_source_ids'), 'expected_source_ids')
    actual_sources = {s['id'] for s in data['sources']}
    for identifier in sorted(expected_sources - actual_sources):
        issue('source_missing', 'retrieve_inventory_source', identifier)
    for identifier in sorted(actual_sources - expected_sources):
        issue('source_outside_inventory', 'resolve_requested_scope', identifier)

    observed = {}
    usable_observed = set()
    for source in data['sources']:
        if not source['primary']:
            continue
        identifier = source['id']
        evidence = source.get('evidence')
        if not isinstance(evidence, dict):
            issue('message_evidence_missing', 'obtain_observed_message_text', identifier)
            continue
        if evidence.get('boundary_verified') is not True or not isinstance(evidence.get('boundary_reference'), str) or not evidence['boundary_reference'].strip():
            issue('text_boundary_unknown', 'verify_earlier_boundary_or_export', identifier)
        expected = evidence.get('expected_message_ids')
        if expected is None:
            issue('message_inventory_unknown', 'obtain_verified_message_inventory', identifier)
            expected = set()
        else:
            expected = unique_ids(expected, 'expected_message_ids')
        messages = evidence.get('messages')
        if not isinstance(messages, list):
            raise ValueError('evidence.messages must be a list')
        ids = unique_ids([m.get('id') for m in messages if isinstance(m, dict)], 'message IDs')
        if len(ids) != len(messages):
            raise ValueError('Each message must be an object')
        for mid in sorted(expected - ids):
            issue('message_missing', 'retrieve_missing_message', identifier, mid)
        if evidence.get('expected_message_ids') is not None:
            for mid in sorted(ids - expected):
                issue('message_outside_inventory', 'reconcile_message_inventory', identifier, mid)
        has_user = False
        for message in messages:
            mid = message['id']
            role = message.get('role')
            if role not in {'user', 'assistant', 'note'}:
                raise ValueError('Message role must be user, assistant or note')
            has_user |= role in {'user', 'note'}
            text = message.get('text')
            if not isinstance(text, str) or not text.strip():
                issue('message_text_missing', 'retrieve_text_or_material_attachment', identifier, mid)
            dated = True
            try:
                stamp = datetime.fromisoformat(message.get('created_at', '').replace('Z', '+00:00'))
                if stamp.tzinfo is None:
                    raise ValueError('timezone missing')
            except (ValueError, TypeError, AttributeError):
                dated = False
                issue('message_date_unverified', 'verify_original_message_date', identifier, mid)
            observed[(identifier, mid)] = message
            if identifier in result['usable_source_ids'] and role in {'user', 'note'} and dated and isinstance(text, str) and text.strip():
                usable_observed.add((identifier, mid))
        if not has_user:
            issue('no_observed_user_material', 'obtain_requested_user_messages', identifier)

    considered = set()
    omitted = 0
    if stage == 'delivery':
        choices = data.get('consideration')
        if not isinstance(choices, list):
            raise ValueError('delivery requires a consideration list')
        for choice in choices:
            if not isinstance(choice, dict):
                raise ValueError('Each consideration must be an object')
            key = (choice.get('source_id'), choice.get('message_id'))
            if key in considered:
                raise ValueError('Duplicate message consideration')
            if key not in observed:
                issue('unknown_considered_message', 'reconcile_with_observed_text', *key)
            considered.add(key)
            action = choice.get('action')
            if action not in {'included', 'condensed', 'omitted', 'excluded_by_user'}:
                raise ValueError('Unknown consideration action')
            if action in {'included', 'condensed'}:
                unique_ids(choice.get('artifact_keys'), 'artifact_keys')
                if not choice['artifact_keys']:
                    issue('artifact_reference_missing', 'identify_actual_output', *key)
            else:
                omitted += 1
                if not isinstance(choice.get('reason'), str) or not choice['reason'].strip():
                    issue('omission_reason_missing', 'explain_selection', *key)
                if action == 'excluded_by_user' and not choice.get('user_instruction_reference'):
                    issue('exclusion_not_authorized', 'verify_user_exclusion', *key)
        for key in sorted(set(observed) - considered):
            issue('message_not_considered', 'consider_before_selecting', *key)
        if omitted and data.get('omissions_disclosed') is not True:
            issue('omissions_not_disclosed', 'disclose_material_selection_and_reasons')

    result.update(schema_version=2, stage=stage,
                  decision='ready' if not issues else ('partial_only' if data['allow_partial'] and usable_observed else 'blocked'),
                  broader_scope_complete=not issues,
                  observed_message_count=len(observed),
                  considered_message_count=len(considered),
                  all_retrieved_messages_considered=stage == 'delivery' and bool(observed) and not (set(observed) - considered),
                  limits='Reconciles supplied inventory, text and choices only. Verify boundary references and provenance; inspect prose for facts, attribution and topic coverage. No account access or semantic completeness proof.')
    return result


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
