# Daily diaries and weekly reviews

Scenarios describe what the user wants. Reflect, Challenge, Expand and Preserve & Compound are the methods used inside them. Manual requests and scheduled runs are independent ways to start the same scenario. Exploration can stand alone or lead into a diary; it is not a required first step.

## End-of-day diary

Resolve the user's local date/timezone only when the date matters. Begin with the supplied material or authorized conversations for that day. If little is available, ask for one memorable moment and how it felt; one question at a time. Do not turn ordinary diary writing into a compulsory lesson or interrogation.

Return a readable short diary in the user's preferred voice. Ground first-person statements in their own words. Keep interpretation separate, use tentative language, and do not invent events, emotions or achievements to fill the day. Offer an optional unanswered question only if it is useful. Material gaps are allowed. “No source material today” must never become a fabricated diary.

## Weekly review

Resolve the interval (default seven completed local calendar days), accessible sources and exclusions. Compare earlier and later evidence, rather than concatenate daily summaries. Include a few changes, something that remained stable, and unresolved questions only when supported. User corrections override earlier AI summaries. If using diary files, keep source filenames/dates visible. One week need not produce a grand narrative or a new goal.

## Save a diary versus keep a learning

A diary is a readable document. Companion state is selected learning/decisions with provenance and corrections; it is not a complete journal archive. Neither is saved by installation.

When the user requests a diary file, agree on the destination once and reuse that choice. In a local workspace, a suggested layout is `journals/daily/YYYY-MM-DD.md` and `journals/weekly/YYYY-MM-DD_to_YYYY-MM-DD.md`. The paths are suggestions, not automatic defaults. Keep private records outside the public source/plugin directories. Use available file tools, then read back the written file and report its real path. Existing content must be read before editing; repeated scheduled runs should not create duplicate entries or overwrite a human correction. Preserve prior wording or ask about an ambiguous replacement. When filesystem access is absent, provide Markdown to copy/download and name that limitation.

Suggested document sections: source coverage; diary/review; optional tentative observations. These describe section purposes, not literal English headings: write the exported document in the user's conversational language unless they request otherwise. Mark any synthetic demo as a demo in that same language in the file itself. Save a selected learning into [state](state.md) only under the separate user instruction for that store. Never infer it from permission to export a diary.

## Scheduled variants

Use [scheduling](scheduling.md). Distinguish these user choices:

- A reminder to write: asks the user for today's input; does not manufacture an entry if they do not reply.
- Automatic draft: uses only the agreed accessible materials; labels it a draft; names missing coverage.
- Weekly review: reads the agreed date range, conversations or journal folder and produces a comparison.
- Exploration delivery: suggests a few ideas without personal analysis; saves nothing unless authorized.

Before activation, settle cadence, time/timezone, source scope, destination, saving permission and the behavior when there is no new material. Confirm setup separately from an actual delivered run. Installing this package never starts these tasks.
