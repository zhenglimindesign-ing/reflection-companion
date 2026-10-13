#!/usr/bin/env python3
"""Reconcile declared topic units with observed text and saved artifact readbacks.

Read-only: no source discovery, file writes, network or semantic classification.
"""
import json
import sys


DISALLOWED_REASONS = {'no_action_result', 'too_abstract', 'not_main_story', 'length_limit'}
ROLES = {'user', 'assistant', 'note'}
ACTIONS = {'included', 'condensed', 'omitted', 'excluded_by_user', 'pending'}


def check(data):
    if not isinstance(data, dict) or data.get('schema_version') != 1:
        raise ValueError('Expected topic reconciliation schema version 1')
    retrieval = data.get('retrieval_result')
    if not isinstance(retrieval, dict) or retrieval.get('decision') not in {'ready', 'partial_only', 'blocked'}:
        raise ValueError('Provide the actual source_readiness.py result')
    if type(retrieval.get('broader_scope_complete')) is not bool:
        raise ValueError('retrieval_result requires broader_scope_complete')
    if retrieval['decision'] == 'ready' and not retrieval['broader_scope_complete']:
        raise ValueError('Inconsistent source readiness result')
    if retrieval['decision'] != 'ready' and retrieval['broader_scope_complete']:
        raise ValueError('Incomplete retrieval cannot claim broader completion')
    issues = []

    def issue(code, repair, topic_id=None):
        row = {'code': code, 'repair': repair}
        if topic_id is not None:
            row['topic_id'] = topic_id
        issues.append(row)

    def records(name):
        rows = data.get(name)
        if not isinstance(rows, list) or any(not isinstance(r, dict) for r in rows):
            raise ValueError(name + ' must be a list of objects')
        return rows

    messages = {}
    for message in records('messages'):
        key = (message.get('source_id'), message.get('message_id'))
        if any(not isinstance(k, str) or not k.strip() for k in key) or key in messages:
            raise ValueError('Message source/ID pairs must be nonempty and unique')
        if message.get('role') not in ROLES or not isinstance(message.get('text'), str) or not message['text'].strip():
            raise ValueError('Messages require observed text and role')
        messages[key] = message
        if message.get('topics_reviewed') is not True:
            issue('message_topics_unreviewed', 'review_each_question_argument_correction_and_useful_answer')
    if not messages:
        issue('no_observed_messages', 'obtain_the_requested_material')

    artifacts = {}
    for artifact in records('artifacts'):
        key = artifact.get('key')
        if not isinstance(key, str) or not key.strip() or key in artifacts:
            raise ValueError('Artifact keys must be nonempty and unique')
        if not isinstance(artifact.get('text'), str):
            raise ValueError('Artifacts require actual readback text')
        artifacts[key] = artifact

    ids, covered_messages = set(), set()
    omitted = 0
    topics = records('topics')
    for topic in topics:
        identifier = topic.get('id')
        if not isinstance(identifier, str) or not identifier.strip() or identifier in ids:
            raise ValueError('Topic IDs must be nonempty and unique')
        ids.add(identifier)
        key = (topic.get('source_id'), topic.get('message_id'))
        message = messages.get(key)
        if message is None:
            issue('topic_source_unknown', 'reconcile_with_observed_source_text', identifier)
        else:
            covered_messages.add(key)
        evidence = topic.get('evidence')
        if not isinstance(evidence, str) or not evidence.strip() or message is None or evidence not in message['text']:
            issue('topic_evidence_missing', 'identify_an_exact_observed_source_excerpt', identifier)
        if topic.get('priority') not in {'material', 'incidental'}:
            raise ValueError('Topic priority must be material or incidental')
        action = topic.get('action')
        if action not in ACTIONS:
            raise ValueError('Unknown topic action')
        if action == 'pending':
            issue('topic_not_reconciled', 'write_or_explain_the_topic_before_completion', identifier)
        elif action in {'included', 'condensed'}:
            refs = topic.get('artifact_refs')
            if not isinstance(refs, list) or not refs:
                issue('topic_output_missing', 'map_to_actual_saved_output_text', identifier)
                continue
            if message and message['role'] == 'assistant' and topic.get('attribution') != 'historical_assistant':
                issue('historical_answer_attribution_missing', 'keep_ai_answer_separate_from_user_facts', identifier)
            for ref in refs:
                if not isinstance(ref, dict):
                    raise ValueError('Each artifact reference must be an object')
                artifact = artifacts.get(ref.get('artifact_key'))
                excerpt = ref.get('excerpt')
                if artifact is None or not isinstance(excerpt, str) or not excerpt.strip() or excerpt not in artifact['text']:
                    issue('topic_output_unverified', 'read_back_and_identify_the_actual_saved_passage', identifier)
                elif not isinstance(artifact.get('readback_reference'), str) or not artifact['readback_reference'].strip():
                    issue('artifact_readback_missing', 'verify_the_persisted_destination', identifier)
        else:
            omitted += 1
            reason = topic.get('reason')
            if not isinstance(reason, str) or not reason.strip():
                issue('topic_omission_unexplained', 'explain_what_was_left_out_and_why', identifier)
            if topic.get('reason_code') in DISALLOWED_REASONS:
                issue('invalid_topic_selection', 'retain_meaningful_discussion_without_requiring_action_or_one_main_story', identifier)
            if action == 'excluded_by_user':
                ref = topic.get('user_instruction_reference')
                if not isinstance(ref, str) or not ref.strip():
                    issue('topic_exclusion_unauthorized', 'verify_the_users_actual_exclusion', identifier)
            elif topic['priority'] == 'material':
                issue('material_topic_omitted', 'restore_the_material_topic_or_verify_a_user_exclusion', identifier)
    for key in set(messages) - covered_messages:
        issue('message_has_no_topic_units', 'inventory_the_topics_in_each_observed_message')
    if omitted and data.get('omissions_disclosed') is not True:
        issue('topic_omissions_undisclosed', 'disclose_selection_and_reasons')
    coverage_passed = not issues
    decision = 'blocked' if issues or retrieval['decision'] == 'blocked' else retrieval['decision']
    return {'schema_version': 1, 'decision': decision, 'issues': issues,
            'topic_count': len(topics), 'observed_message_count': len(messages),
            'declared_topic_coverage_passed': coverage_passed,
            'broader_scope_complete': decision == 'ready' and retrieval['broader_scope_complete'],
            'limits': 'Checks supplied topic units, exact source excerpts and saved-output mappings only. '
                      'Does not prove all topics were identified, semantic fidelity, readback authenticity or account completeness.'}


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
