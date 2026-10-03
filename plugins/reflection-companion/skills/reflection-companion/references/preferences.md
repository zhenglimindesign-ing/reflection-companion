# Output choices and natural-language intent

Use when producing diaries/reviews, changing output options, or keeping recurring preferences. These instructions govern meaning and authorization; the examples are not a keyword allowlist or a parser grammar.

## Recognizing the requested action

| User intent and example | Action |
| --- | --- |
| “Write today's diary.” / “What changed this month?” / “Look back over this quarter/year.” | Produce the relevant artifact from available authorized material; no saving or schedule implied. |
| “This time, shorter.” / “Don't analyze me today.” | Apply a temporary override; do not save a preference. |
| “From now on, weekly reviews should keep more quotes and omit experiments.” | Save that period's output preference when the chosen local store is available and the persistent instruction is clear. If storage is not set up, explain the location once; meanwhile apply it in the current chat without claiming cross-chat persistence. |
| “Save this diary in my selected folder.” / “Export this one to my Drive folder.” | Save/export the completed artifact to the known authorized destination; confirm missing location, not already-given permission. |
| “Keep this insight for later.” | Use selected-learning state with accurate authority; an AI hypothesis remains proposed unless its meaning is confirmed. |
| “Every Sunday at 19:00, make this review.” | Use host scheduling after resolving missing timezone, source scope, destination and saving behavior. |
| “Can this be scheduled?” / “Are monthly reviews possible?” | Explain capability; a question about capability does not activate a task. |
| “Log this error.” / “Write the annual financial report.” / “Review this code.” | Follow the actual technical/business request; isolated words do not start personal journaling. |

Use nearby context to resolve “this,” “same as last time” or a period. If the user wants one small note, do not upgrade it to a complete retrospective. A topic/project reflection can use an agreed interval without forcing one of five rhythms. Clarify only a consequential ambiguity, such as which year or whether a request is recurring. No exact trigger phrase is required. Discovery metadata allows normal implicit Skill selection; actual host selection is not guaranteed by these examples.

## Choices and defaults

The [options schema](../assets/artifact-options.json) defines concrete choices; the [artifact guide](artifacts.md) defines how to write them. Start with useful defaults or offer a few presets only when a choice would help. Do not require an onboarding form.

| Choice | Supported values and effect |
| --- | --- |
| Preset | `faithful`, `edited`, `long_view`; presets expand into editable processing/observation/experiment/question settings. |
| Processing | `faithful` preserves wording with light organization; `edited` permits compression/reordering without new meaning; `reflective` permits separately attributed interpretation. |
| Layout and voice | Prose, sections, raw notes or a custom form; first, second or third person. Custom titles/structure come from the user's actual instruction. |
| Length | Light, standard or expanded; select fewer threads or add supported detail, never pad. |
| Quotes and originals | Quotes off, selected or more; source appendix off, links or agreed originals. Selecting originals does not authorize a broader archive or export. |
| Themes | Automatic importance-based selection, or selected themes; honor exclusions in retrieval where possible and throughout writing. |
| Title, language and tone | Content/date-only/custom title; follow user language or a specified language; plain, warm or direct tone. Tone does not change certainty. |
| AI observation | Off, gentle or deep; deep adds useful competing explanations and counterevidence rather than stronger certainty. |
| Takeaways, knowledge, moments | Each independently off, inline or its own section; supported content only, no repeated filler. |
| Open questions | Off or supported useful questions only. |
| Experiment | Off, user-chosen action only, or at most one explicitly optional AI suggestion. |
| Closing question | On means at most one useful question; off means omit it. |
| Time basis | Calendar, completed days or custom; resolve actual dates/cutoff and scheduling window separately. |

Daily defaults are edited first-person prose with reflection and closing question off. Weekly defaults use Long View; monthly/quarterly/yearly retain reflection but use chosen actions only. Quotes and supported takeaways/knowledge/moments are selected or inline across periods. All defaults are overridable except factual scope, quotation accuracy, correction precedence and attribution.

Source permissions, saving destination/authorization, long-term meaning and host schedules are separate operations, never formatting fields. A preference cannot silently open Drive, scan all chats, enable saving or create recurrence.

## Resolve temporary and durable preferences

Order: this request > saved period preference > saved global preference > defaults. A preset applied at a given layer expands there; explicit fields in the same layer win over the preset. Directly turning AI observation on also selects reflective processing unless that layer explicitly requests a conflicting processing mode; users need not name this dependency. Explicit faithful or edited processing disables AI observations and AI-suggested experiments; the resolver reports those conflicts as adjustments. Disabling AI observation also disables a suggested AI experiment. Supported comparisons can remain without personal interpretation.

Map “no analysis today” to AI observation off, and “add a separate observation today” to an observation level on. “No questions” turns off both open-question and closing-question components; “no last question” affects only the closing question. Keep these choices scoped to the requested output or durable period. The `custom` layout/title selections require actual user-supplied structure/title; this v1 options object stores the selection, not an arbitrary custom-template document. Do not claim such a document was saved as a reusable template.

Read saved preferences only in the exact selected Companion workspace. Unknown location is not permission to search personal directories. Without a store, use the options file directly, or the helper's read-only `artifact_options` operation when the workspace is known. It does not initialize anything. With disabled continuity, saved preferences are not applied; current requests and defaults remain usable.

Illustrative read-only request to `scripts/state.py` using its documented absolute `--root`:

```json
{"op":"artifact_options","period":"weekly","overrides":{"experiment":"off","quotes":"more"}}
```

This returns effective options, dependency adjustments, saved preference layers when enabled, and the current revision. It performs no network operation and creates no state or artifact. Options describe writing choices; the helper does not synthesize the review.

For an explicit “from now on” request, read the latest preferences/revision, change only the intended global or period fields, and call `settings` with `artifact_preferences`. Preserve unrelated layers. The object replaces that whole preference value, so do not construct it from stale assumptions. Keep actual user authorization and `expected_revision`; conflicts require a fresh read and reconciliation.

The preferences shape is:

```json
{"global":{"length":"light"},"periods":{"weekly":{"experiment":"off","quotes":"more"}}}
```

Use `{}` or remove a period override in the full object to restore defaults at that scope. No store is needed for a temporary choice. If durable storage is unavailable, apply current-chat choices and name the narrow limit. Never claim a preference was saved after only changing the reply.
