# Diary and period-review artifact specification

Use for completed diaries or weekly, monthly, quarterly and yearly reviews, including requested exports and scheduled drafts. A light conversation need not become a document. Resolve output choices through [preferences](preferences.md); gathering, saving and recurrence follow [scenarios](scenarios.md).

## Selecting and writing material

Consider the authorized period's material before selecting a few worthwhile threads. Rank by the user's expressed significance, real-world consequences, changed judgment or behavior, memorable experience, useful uncertainty and repeated evidence. Recency, discussion length, distress and demonstrable output alone do not determine importance. A dominant topic may deserve most space; do not manufacture diversity or fill every life domain.

A review thread connects specific material with its earlier/later relationship and what remains uncertain. “You grew” is not sufficient. Write scenes and relationships in connected prose; avoid repeating the same point as fact, shift and signal. A diary can preserve a small happy, sad, ordinary or contradictory moment without turning it into a lesson.

Do not upgrade an event with unsupported success/timing language: “delivered” does not imply “on time,” and reported repair does not imply firsthand verification. A connection between separate activities does not establish a shared motive or purpose; present a warranted connection as an AI possibility rather than the user's expressed reason.

Before delivery, audit factual clauses that say **why** someone acted, what an activity was **for**, or what one event **caused**. Locate the explicit source statement for each such relationship, not just sources for the two activities. Two plans mentioned near each other can have different or unstated purposes. If the relationship is absent, remove it from factual narration; a useful thematic possibility must be separately qualified as AI interpretation. For example, wanting to publish an event recap and separately considering a creative video does not establish that the video is intended to make that event count as an outcome. Compression must not silently supply this missing purpose.

Separate reported events, the user's expressed meaning and AI interpretation. Facts sections contain supported facts; an inference belongs where it is identified as such. First-person narration never adopts AI-proposed feelings, motives or conclusions as the user's own. Past reviews are revisable baselines and discovery aids, not independent evidence: verify important facts from their sources when available. Preserve the older user's view as something held then; correct mistaken facts or AI interpretations without erasing genuine change.

Keep who said, understood or reported each point intact. When one note contains somebody else's remark followed by the user's response, retain those as distinct claims; do not rewrite the user's recognition or doubt as advice that the other person gave. This applies to compressed annual/quarterly narration as well as direct quotes.

Keep selected original wording exactly, with the available date/source. Mark omissions; paraphrases do not stay in quotation marks. An edited title or AI-written synthesis is not a user quote. Prefer concise source notes at the end; disclose a consequential coverage gap early and narrow the title/body accordingly. Missing notes do not prove a quiet life, missing outcomes do not prove open loops, and repeated AI summaries do not establish a pattern.

Copy dates from the actual dated source heading/message metadata, never from an entry ID or its number. Before delivery, recheck every stated event date against that source; omit an uncertain date rather than infer it.

For Markdown notes with dated headings like `## E13 2025年9月20日` or `## E13 · 2025-09-20`, use the bundled read-only `scripts/source_notes.py --source <authorized file> --ids <selected comma-separated IDs>` to obtain an explicit ID/date/text index. Do not widen the requested selection. Before delivery, check retained event dates and original quotes with the same source/selection and `--verify`. Send JSON on stdin with `dates` entries shaped as `{"id":"E13","date":"2025-09-20"}` and `quotes` entries shaped as `{"id":"E13","text":"the actual verbatim wording"}`. Use actual selected IDs/values; these examples specify fields, not claims to copy. Correct mismatches in the body; a successful check validates only submitted claims, not interpretation, attribution or unsubmitted text. For other formats or unavailable Python, inspect actual source metadata directly and omit uncertain event dates. The tool writes nothing and does not discover sources or grant access.

## Period tasks and defaults

| Period | Task | Default form |
| --- | --- | --- |
| Daily | Help the user remember concrete experience from this day. | Edited first-person prose; selected quotes; supported discoveries, knowledge and moments inline; AI observation and closing question off. |
| Weekly | Compare near-term facts, shifts and supported candidate signals. | Second-person Long View sections; one optional AI experiment and at most one useful closing question. |
| Monthly | Trace evolving threads, evidence and attention across the month. | Second-person reflective sections; user-chosen actions only; at most one closing question. |
| Quarterly | Check direction, context and patterns across months. | Second-person reflective sections; explicit limits/counterexamples; user-chosen actions only. |
| Yearly | Form source-grounded chapters of a year worth remembering. | Second-person reflective chapters; ordinary life and unfinished experience; user-chosen wishes, not compulsory goals. |

These are editable defaults. The [options file](../assets/artifact-options.json) is the machine-readable source for defaults and choices. Users can rename, combine or reorder components, or request free prose. Accurate scope, attribution and corrections remain required in any layout. Read only the selected template; substantial examples are available when needed, not mandatory context on every invocation.

| Template | 简体中文 | English |
| --- | --- | --- |
| Daily | [日记](../assets/templates/daily-diary.zh-CN.md) | [Diary](../assets/templates/daily-diary.en.md) |
| Weekly | [周回顾](../assets/templates/weekly-review.zh-CN.md) | [Weekly](../assets/templates/weekly-review.en.md) |
| Monthly | [月回顾](../assets/templates/monthly-review.zh-CN.md) | [Monthly](../assets/templates/monthly-review.en.md) |
| Quarterly | [季度回顾](../assets/templates/quarterly-review.zh-CN.md) | [Quarterly](../assets/templates/quarterly-review.en.md) |
| Yearly | [年回顾](../assets/templates/yearly-review.zh-CN.md) | [Yearly](../assets/templates/yearly-review.en.md) |

Use the user's language, translating labels for other languages. Authoring placeholders are not final text. Populate retained sections and delete omitted headings/placeholders; a requested blank template may retain them. [Chinese complete examples and configuration variant](../assets/examples/reviews.zh-CN.md), [English examples](../assets/examples/reviews.en.md), and their [fictional source notes](../assets/examples/fictional-notes.zh-CN.md) demonstrate selection and provenance without importing private user history.

## Daily writing

Use date plus an optional concrete title. Write one or a few supported scenes with the user's expressed thoughts and feelings. Retain a phrase when its wording matters. A takeaway, knowledge point or favorite moment can be integrated into the story or shown separately; do not repeat it merely to fill a component. Leave unresolved material only when useful. With reflection enabled, keep any AI observation separate and limited to this evidence. One day cannot establish a stable personal pattern.

For first-person prose under any processing level, check each assertion against the selected user's material. Reflection opt-in does not authorize adding feelings, motives or judgments to the user's “I” narration. A thought or goal absent from the note was not necessarily consciously rejected. Omit a new interpretation from that body or place it in the separate AI observation. The voice choice applies to the user's narrative; write AI observations as “the notes may suggest…” or address the user as “you,” not as an unquoted “I” that appears to express the user's own understanding. Source notes should state the actual material range concisely, including a single supplied note when that is all the diary covers.

## Weekly Long View

**Facts:** distinguish what happened, what advanced and what actually reached an outcome. Include memorable ordinary experience when supported, not only achievements.

**Shifts:** compare an earlier judgment/action with new evidence and the present position. Address the user's corrections before extending an older story. No supported change is a valid finding.

**Signals:** propose a small, situated observation supported by independent events or time points. Name the conditions and available counterevidence or limitations. One instance may prompt a question; it does not establish a stable pattern. With AI observation off, omit personal-pattern interpretation while retaining supported factual comparisons.

**Open questions:** distinguish missing external outcomes, uncertain meaning and deliberate deferral. Verify newer evidence before carrying an old question forward.

**Experiment:** when enabled, offer at most one small reversible suggestion and explain what it could distinguish. Identify it as optional, not a commitment or instruction. With `chosen_only`, include only an action the user actually chose. End with at most one useful, unanswered question if enabled; do not force it.

## Monthly zoom-out

Trace a few monthly threads through their beginning, turning points and current state. Ask what gained real-world evidence, what continued to consume attention without new support, what experiences expanded or narrowed the recorded life, and which interpretations need revision. Distinguish repeated concern from increasing evidence. Preserve worthwhile knowledge, quotes and ordinary moments. Treat preferences and proposed next-month experiments separately from actual choices.

Use raw notes to check claims inherited from weekly reviews. A short monthly appendix to a week can be useful, but does not automatically constitute a full monthly review. Missing discussion of a topic cannot show that the user's world narrowed there.

## Quarterly direction

Connect beginning, turning points and present position across the quarter. Examine candidate patterns across months, including contexts where they fail. Relate known commitments to the user's current needs, burdens and nourishing experience; without data, do not invent time shares or measure all life by output. Preserve continuity as well as change. Continuing, adjusting or setting aside something requires evidence or a user choice, not an imposed quarterly goal.

## Yearly chapters

Organize actual phases, events or themes into a few readable chapters; twelve equal month summaries are not required. Use dated original words and turning points to trace judgment and choice. Allow losses, contradictions, ordinary pleasures and unfinished experiences without a completed-growth narrative. Recheck old explanations and their corrections instead of accumulating an identity label. A word for the year, annual goals or a letter to the future self is optional and user-selected. Sparse coverage produces chapters of the available records, not a biography of the whole year.

## Delivery checks

Check date/interval and cutoff, source coverage, language, voice and selected options. Every retained quote must match its source; important comparisons must have an identifiable earlier and later basis or an explicit inability to compare. Apply corrections, keep proposed observations tentative, and remove empty sections, placeholders, duplicated insights and unauthorized commitments.

After exporting, read the actual file and verify those same properties, including disabled components and user edits. Distinguish chat output, export, saved output preferences, selected-learning continuity and scheduled delivery. A successful package or preference resolver does not prove model writing quality or live delivery.
