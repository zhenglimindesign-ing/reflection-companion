#!/usr/bin/env python3
"""Read explicitly selected dated Markdown notes and check dates/quotes.

Supports headings such as '## E13 2025年9月20日' or
'## E13 · 2025-09-20'. No storage, discovery, network or synthesis.
"""
import argparse
import hashlib
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



SPEAKER = re.compile(r'^(用户(?:更正|陈述)?|历史\s*AI(?:\s*(?:答复|建议|更正))?|User(?: correction)?|Historical AI(?: answer| suggestion| correction)?)[：:]\s*', re.I)
FIRST_PERSON = re.compile(r'我|\b(?:I|me|my|mine|we|us|our|ours)\b', re.I)
QUOTED = re.compile(r'“[^”]*”|「[^」]*」|"[^"]*"')
STATUS_QUALIFIER = re.compile(r'(?:没有|尚未|还没|还未|未|没)\s*(?:看|查|核实|验证|了解|打算|计划|决定|尝试)|未知|不清楚|不知道|不确定|未明确|(?:没有|尚无|缺乏|暂无)(?:证据|依据|信息|数据)|\b(?:unknown|unclear|uncertain)|\bno (?:evidence|information|data)|\b(?:not|haven.t|hasn.t|hadn.t)\s+(?:yet\s+)?(?:checked|seen|verified|observed|reviewed|planned|decided|tried)\b', re.I)
ABSENCE = re.compile(r'没有|没|尚无|不存在|\b(?:no|none|nothing|not)\b', re.I)

# Attention cues, not a sentiment classifier or proof of meaning. Restore source
# wording after a flag; other emotions/negations still need semantic comparison.
AFFECT = re.compile(r'担心|害怕|焦虑|难过|欣慰|释然|羞愧|愧疚|安心|兴奋|失落|烦躁|庆幸|平静|心动|\b(?:worried|afraid|anxious|relieved|ashamed|guilty|excited|disappointed|calm)\b', re.I)
CJK = re.compile(r'[\u4e00-\u9fff]')


def draft_audit(notes, draft):
    """Mechanical evidence/role checks plus a bounded processing note.

    Does not judge paraphrase entailment, inferred motives or editorial quality.
    The comparison is returned for a separate semantic review of the actual draft.
    """
    if not isinstance(draft, dict) or set(draft) != {'sentences', 'omitted', 'language', 'source_appendix'}:
        raise ValueError('Draft requires sentences, omitted, language and source_appendix')
    if draft['language'] not in ('en', 'zh-CN') or draft['source_appendix'] not in ('off', 'links', 'agreed_originals'):
        raise ValueError('Unsupported language or source appendix')
    if not isinstance(draft['sentences'], list) or not draft['sentences']:
        raise ValueError('Supply actual factual sentences')
    omitted = draft['omitted']
    if not isinstance(omitted, list) or any(not isinstance(v, str) for v in omitted) or len(set(omitted)) != len(omitted):
        raise ValueError('Omitted IDs must be unique strings')
    by_id = {note['id']: note for note in notes}
    errors, comparison, used = [], [], set()
    for index, sentence in enumerate(draft['sentences']):
        if (not isinstance(sentence, dict) or set(sentence) != {'text', 'voice', 'evidence'}
                or not isinstance(sentence['text'], str) or not sentence['text'].strip()
                or sentence['voice'] not in ('user', 'historical_ai', 'new_ai')
                or not isinstance(sentence['evidence'], list) or not sentence['evidence']):
            raise ValueError('Invalid sentence or missing evidence')
        if sentence['voice'] == 'historical_ai' and FIRST_PERSON.search(QUOTED.sub('', sentence['text'])):
            errors.append({'sentence': index, 'error': 'first person in historical AI paraphrase; distinguish its narrator'})
        checked = []
        for excerpt in sentence['evidence']:
            if (not isinstance(excerpt, dict) or set(excerpt) != {'id', 'text'}
                    or not isinstance(excerpt['id'], str) or not isinstance(excerpt['text'], str)
                    or not excerpt['text'].strip()):
                raise ValueError('Evidence requires source ID and exact labeled excerpt')
            note = by_id.get(excerpt['id'])
            if note is None or excerpt['text'] not in note['text']:
                errors.append({'sentence': index, 'id': excerpt['id'], 'error': 'outside selection or not verbatim'})
                continue
            used.add(excerpt['id'])
            match = SPEAKER.match(excerpt['text'])
            # An excerpt must belong to one explicitly labeled turn, not bridge speakers.
            remainder = excerpt['text'][match.end():] if match else ''
            another = any(SPEAKER.match(line) for line in remainder.splitlines()[1:])
            owner = ('user' if match and match.group(1).lower().startswith(('用户', 'user'))
                     else 'historical_ai' if match else None)
            if owner is None or another or sentence['voice'] != 'new_ai' and owner != sentence['voice']:
                errors.append({'sentence': index, 'id': excerpt['id'], 'error': 'source speaker mismatch or unlabeled/mixed excerpt'})
            checked.append({'id': excerpt['id'], 'date': note['date'], 'speaker': owner, 'text': excerpt['text']})
        if sentence['voice'] == 'user' and checked:
            source_body = '\n'.join(SPEAKER.sub('', e['text']) for e in checked)
            # Skip obvious script-changing paraphrases; this is not a language/translation detector.
            if bool(CJK.search(sentence['text'])) == bool(CJK.search(source_body)):
                added = [cue for cue in AFFECT.findall(QUOTED.sub('', sentence['text']))
                         if cue.casefold() not in source_body.casefold()]
                if added:
                    errors.append({'sentence': index, 'error': 'possible added user affect; restore expressed source wording', 'cues': sorted(set(added))})
        # Conservative attention gate: preserve a source knowledge/intention qualifier.
        # It is not a semantic verifier. Literal sourced absence clauses remain valid.
        if sentence['voice'] == 'user' and any(STATUS_QUALIFIER.search(e['text']) for e in checked):
            clauses = re.split(r'[。；，;,.!?！？]', sentence['text'])
            negatives = [c.strip() for c in clauses if ABSENCE.search(c)]
            if (negatives and not STATUS_QUALIFIER.search(sentence['text'])
                    and any(not any(c in e['text'] for e in checked) for c in negatives)):
                errors.append({'sentence': index, 'error': 'potential loss of source status qualifier; compare absence claim with knowledge/intention evidence'})
        comparison.append({'text': sentence['text'], 'voice': sentence['voice'], 'evidence': checked})
    if set(omitted) - set(by_id) or set(omitted) & used:
        errors.append({'error': 'omitted IDs outside selection or also used as evidence'})
    if set(by_id) - used - set(omitted):
        errors.append({'error': 'unaccounted source IDs', 'ids': sorted(set(by_id) - used - set(omitted))})
    note_text = None
    if draft['source_appendix'] != 'off':
        dates = sorted({note['date'] for note in notes})
        span = dates[0] if len(dates) == 1 else dates[0] + '–' + dates[-1]
        ids = ', '.join(by_id)
        if draft['language'] == 'zh-CN':
            note_text = f'材料：所提供的 {span} 记录（{ids}），仅涵盖这些材料。加工：按主题选编、压缩重复内容。'
            if omitted:
                note_text += '部分材料未进入正文，属于编辑取舍；不表示相关事项已解决。'
        else:
            note_text = f'Material: the supplied {span} records ({ids}); coverage is limited to these sources. Editing: selected by topic and condensed.'
            if omitted:
                note_text += ' Some material was omitted as an editorial choice; this does not establish that the matters were resolved.'
    digest = hashlib.sha256(json.dumps({'notes': notes, 'draft': draft}, ensure_ascii=False, sort_keys=True).encode()).hexdigest()
    return {'ok': not errors, 'errors': errors, 'comparison': comparison, 'draft_sha256': digest if not errors else None,
            'processing_note': note_text, 'semantic_review_required': True}


def render_draft(notes, draft):
    """Render exactly the audited sentences; no narrative or outcome generation."""
    if not isinstance(draft, dict) or set(draft) != {'sentences', 'omitted', 'language', 'source_appendix', 'title', 'sections', 'audit_sha256'}:
        raise ValueError('Rendering adds title, sections and the prior audit_sha256 to the audit payload')
    if draft['source_appendix'] == 'agreed_originals':
        raise ValueError('Agreed originals need the existing appendix/export workflow; this renderer handles links/off only')
    checked = draft_audit(notes, {k: v for k, v in draft.items() if k not in ('title', 'sections', 'audit_sha256')})
    if not checked['ok']:
        raise ValueError('Draft failed mechanical audit: ' + json.dumps(checked['errors'], ensure_ascii=False))
    if draft['audit_sha256'] != checked['draft_sha256']:
        raise ValueError('Missing/stale source-and-draft audit; run --audit-draft, review comparison and render the same text')
    if not isinstance(draft['title'], str) or '\n' in draft['title']:
        raise ValueError('Title must be a single line; empty means no title')
    if not isinstance(draft['sections'], list) or not draft['sections']:
        raise ValueError('Supply sections with narrator and sentence indices')
    indices, blocks = [], (['# ' + draft['title']] if draft['title'].strip() else [])
    for section in draft['sections']:
        if (not isinstance(section, dict) or set(section) != {'heading', 'voice', 'indices'}
                or not isinstance(section['heading'], str) or '\n' in section['heading']
                or section['voice'] not in ('user', 'historical_ai', 'new_ai')
                or not isinstance(section['indices'], list) or not section['indices']):
            raise ValueError('Invalid section')
        if section['heading']:
            blocks.append('## ' + section['heading'])
        for index in section['indices']:
            if type(index) is not int or not 0 <= index < len(draft['sentences']):
                raise ValueError('Invalid sentence index')
            if draft['sentences'][index]['voice'] != section['voice']:
                raise ValueError('Section narrator does not match sentence narrator')
            indices.append(index)
            blocks.append(draft['sentences'][index]['text'])
    if sorted(indices) != list(range(len(draft['sentences']))):
        raise ValueError('Every audited sentence must be rendered exactly once')
    if checked['processing_note'] is not None:
        blocks.append('*' + checked['processing_note'] + '*')
    return '\n\n'.join(blocks) + '\n'

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', type=Path, required=True, help='One explicitly authorized Markdown source')
    parser.add_argument('--ids', help='Comma-separated selected IDs; omitted means this entire source')
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument('--verify', action='store_true', help='Check JSON date/quote claims on stdin')
    mode.add_argument('--audit-draft', action='store_true', help='Compare JSON factual draft sentences with labeled excerpts on stdin')
    mode.add_argument('--render-draft', action='store_true', help='Render final Markdown from the audited payload without rewriting')
    args = parser.parse_args()
    try:
        notes = read_notes(args.source, [value.strip() for value in args.ids.split(',')] if args.ids else None)
        if args.render_draft:
            print(render_draft(notes, json.load(sys.stdin)), end='')
            return 0
        if args.audit_draft:
            result = draft_audit(notes, json.load(sys.stdin))
            print(json.dumps(result, ensure_ascii=False, indent=2))
            return int(not result['ok'])
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
