# Source-first diary and review composition

Use after resolving sources, recording detail and output options, before composing any completed diary/review. Work transiently in the current context; this workflow does not authorize saving a private plan, source copy or receipt. Use the selected personal destination only when saving is authorized. A body-only request hides the working map, not the audit.

## 1. Extract, then select

Read the in-scope original material and corrections. Make a compact working map of eligible threads: source ID/date, speaker, **exact supporting excerpt**, corrected facts, expressed meaning, useful historical AI contribution, and genuinely unknown outcomes. Keep these as separate fields rather than a draft narrative. Apply recording criteria; mark incidental omissions as editorial choices, without supplying a resolution status.

For supported dated Markdown notes, obtain the index with `scripts/source_notes.py --source <authorized note> --ids <in-scope IDs>`. Extract excerpts from that index before writing. Otherwise use actual messages and their metadata directly; do not create a local source export merely to use this helper.

Corrections change the factual map before prose is written. Nearby statements do not supply a causal relationship. No time of day, companion, motive, acceptance or result in the excerpt means no such detail in factual narration. A missing outcome is unknown, not a failed or continuing task. When compressing an unknown, retain the source's knowledge/verification verb: “not checked” cannot become “does not exist,” and “not received a reply” cannot become “they have nothing to say.” Likewise, “not intending to make a plan” does not prove “never made a plan.” Keep the status clause close to the original wording; knowledge, intention, action and outcome are different claims. Retain the user's own feeling/thinking verb: considering a question does not establish worry, and a pleasant moment does not establish relief.

## 2. Compose within each narrator's evidence

Organize the selected threads into readable thematic paragraphs. For each factual sentence, retain its supporting excerpt in the working map. Start each user paragraph from the selected original sentences; edit their order, remove repetition and connect supported clauses. Prefer retaining the source wording over adding a smoother but ungrounded scene. Paraphrase the supported meaning; do not write an attractive scene first and find loose source associations afterward. A heading can connect topics for navigation without giving them a shared psychological cause.

- **User narrative:** first person changes the pronouns of supported user material. It does not add a new belief, reason or lesson. Detailed writing expands existing details, reasoning and useful historical answers; sparse material may produce an equally short entry. Keep an unresolved question unresolved.
- **Historical AI:** label the condensed passage as an earlier AI answer/correction/suggestion, and address the user as “you.” Apply the user's voice setting only to their narrative. Summarize what the AI contributed, rather than replaying the user's scene. An earlier AI idea remains an idea unless the user adopted it. A choice about one item does not extend to an adjacent AI proposal. Keep the object of a decision or commitment in the user's source wording; “both” or “the above items” can silently widen it.
- **New AI observation:** include only when enabled, separately labeled and tentative. Do not put a new explanation in the user's “I” even with “maybe.” Do not relabel an earlier answer as a new observation, or a new interpretation as an earlier answer.

Example of the boundary (not a template to copy): a user says “It was raining when I left; I waited by the door.” “I waited by the door because it was raining” adds a causal claim; “The rain helped me enjoy a quiet pause” adds a feeling and interpretation. Keep the observed rain and waiting without either addition. Richer prose is useful only when it preserves the available meaning.

## 3. Audit the actual draft, then repair

Compare **every factual clause**, including modifiers and implied relationships, with its excerpt. For each, ask: who owns this claim; does the source state this exact meaning; have I added when, why, with whom, how it felt, adoption, success or resolution? Compare the factual verbs and modifiers as well as the theme. Seeing an inscription on a bookshelf does not establish entering a library or opening a book. A plausible way the scene happened is still an additional event. If the edited verb/action is not supported, restore the source verb instead of treating it as stylistic filler. Evidence for two events does not support a relationship between them. Delete unsupported additions, or move a useful tentative interpretation to an enabled AI component. Do not patch it merely by adding “perhaps.”

For labeled dated Markdown sources, run `source_notes.py --source <file> --ids <IDs> --audit-draft` with JSON on stdin:

```json
{
  "sentences": [
    {"text": "A final factual sentence", "voice": "user", "evidence": [
      {"id": "source ID", "text": "exact labeled source excerpt"}
    ]}
  ],
  "omitted": ["source IDs omitted by editorial selection"],
  "language": "en",
  "source_appendix": "links"
}
```

Use `voice: user`, `historical_ai` or `new_ai`; excerpts include their original speaker label (`用户：`, `用户更正：`, `历史 AI 答复：` / `建议：` / `更正：`, or corresponding `User:` / `Historical AI:` labels). A record with several speakers must use the excerpt for the actual owner. Supply the **actual draft's factual sentences**, not a shortened stand-in. Clearly attributed exact quotations may use the existing `--verify` quote check separately; do not rewrite them as AI paraphrases. The audit returns the draft alongside its verbatim evidence, rejects out-of-scope/missing excerpts and mismatched labeled speakers, flags an unquoted user “I” in a historical-AI summary, cues a few potentially added user affect words with a conservative literal check (skipped for script-changing paraphrases), and flags possible loss of a knowledge/intention qualifier in a negative paraphrase. This last check is conservative: compare the actual clause; an explicitly sourced absence remains valid. Prefer restoring the source wording when compression has changed its meaning. Read that comparison and repair the prose; `ok` validates these mechanical checks only, not semantic entailment or completeness. Recheck changed sentences. **A tool pass on an earlier draft does not cover rewritten final prose.** Other source formats, unsupported speaker labels/languages or an unavailable tool require the same direct comparison, not a claimed tool pass.

Check selected dates and original quotes with `--verify` too when applicable. Finally compare the full draft with the selected material: no material thread/correction silently lost, no duplicated story in the AI part, and disabled components absent. Do not output the working map or tool receipt as the diary.

For supported labeled Markdown sources with `source_appendix: links/off`, deliver through `--render-draft` on the same helper: add `title` (single line, empty when the user wants no title), `sections` and `audit_sha256` (the `draft_sha256` returned by the successful audit) to the checked payload. Each section contains `heading` (empty for free prose), `voice` and `indices` (zero-based indices into `sentences`). Group sentences into thematic paragraphs in their `text`; do not create a new sentence after checking. All sentences must appear exactly once and match the section's narrator. Read the returned comparison as a semantic pass before rendering: check the subject, action, object and status in each actual clause, especially a user choice beside an AI suggestion. The renderer requires the prior source-and-draft digest, reruns the mechanical checks and returns the final Markdown, including the enabled bounded source note. **Use this returned body unchanged as the final artifact; do not switch pronouns or recompose it during delivery.** If prose needs improvement, edit its source-backed payload, run the audit again, review the new comparison and render again. The digest binds the source and text between these steps; it is not a semantic approval or an authorization token. With `agreed_originals`, use the draft audit and the existing agreed-originals appendix/export workflow; this small renderer does not assemble an originals archive. For other formats, make the equivalent final-text comparison after the last edit; a checked stand-in is insufficient.

## 4. Keep provenance factual and secondary

With `source_appendix` enabled, use the audit's `processing_note` for supported labeled Markdown input. It states only the actual supplied date/ID range, thematic editing and that omissions are editorial decisions; it never asserts omitted queries were answered or completed. Keep that note unchanged except for a verified source link or a necessary coverage gap. For other sources, use the same bounded pattern: “Material: [actually read source range and limits]. Editing: selected by topic and condensed; omitted [category] as an editorial choice.” Do not explain a category by guessing outcomes, significance to the user's whole life or absence from unavailable chats.

Historical AI attribution belongs next to its passage even when the source appendix is off. An enabled footer is part of a completed artifact, including an output-only request. With `source_appendix: off`, omit it entirely. A consequential retrieval gap belongs early; a selection note does not replace gap disclosure. Keep routine provenance short so the narrative remains the main reading experience.
