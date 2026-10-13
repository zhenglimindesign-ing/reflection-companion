# Diaries and period reviews

Use the [artifact guide](artifacts.md) for writing and the [preferences guide](preferences.md) for natural-language intent and settings. Manual requests and scheduled runs start the same writing task; they differ in source availability and delivery permission. A bedtime chat or a small note need not become a full artifact.

## Gather and choose the scope

Resolve the period from the user's intent and current timezone. For “this week/month/quarter/year,” use the local calendar period up to the observed cutoff; a current period is not complete. “Last week” refers to that completed calendar week. Preserve a requested rolling/custom interval. A scheduled weekly run can cover seven completed local days when that is the agreed window; do not change an existing schedule's scope silently.

Use supplied material or retrieve authorized, actually accessible source messages/files before interpretation. Consider topics broadly within that scope rather than seeding only familiar subjects. Do not count a destination chat, preloaded memory or previous AI review as full cross-chat coverage. When an actual retrieval is empty or unexpectedly narrow, make one useful broader retry if supported; then state the specific gap. A requested full backfill remains incomplete; do not silently replace it with a narrow review. For a user-chosen partial review, narrow its title/body to the material actually retrieved. Do not iterate through unrelated sources merely to make coverage look complete. Continuing an archive or bulk backfill requires the [archive contract](journal-archive.md) before writing.

For a single-day diary, one concrete experience can be enough. When useful material is missing, invite one memorable event and the user's experience of it, one question at a time. No usable material produces a narrow explanation, not an invented entry or empty completed form.

Compare important earlier and later source evidence at the chosen scale. Older material outside the interval is a labeled baseline. Check correction records before reusing a prior interpretation. The user may reject a premise or leave a contradiction unresolved.

## Produce the artifact

Resolve default, saved and current choices, then load only the appropriate daily/weekly/monthly/quarterly/yearly template. Apply the period's writing task from the artifact guide; do not concatenate shorter summaries. Use the [source-first composition workflow](journal-composition.md) before writing the final artifact. Write in the user's chosen voice and language. Preserve exact original words where selected, leave unsupported components out, and keep AI interpretation separately identifiable.

Apply the recording criteria and recording-detail choice before filling template components. A template controls presentation, not whether every chat turn deserves inclusion. On first substantial diary use, follow the preferences guide's optional brief choice; scheduled runs use resolved choices without reopening onboarding.

Resolve options even when the user names no choices: use the bundled options file, or the read-only helper at the known selected workspace. Keep the effective voice, processing and enabled components available while writing, and check the actual body against them before delivery. No known store is not a reason to skip defaults or require setup.

A short free-prose request may override the visible template while preserving scope and attribution. Existing sources/settings do not make setup mandatory before useful writing. A completed output must honor switches such as no AI analysis, no experiment or no closing question.

## Save a document versus keep learning or preferences

A diary/review is a readable document. Selected learning/decisions and output preferences live in Companion state when explicitly enabled; the state store is not the full journal archive. Installing the Skill saves none of these.

For requested files, reuse the user's selected destination and verified existing document/tab convention under the [archive contract](journal-archive.md). Suggested file layouts are `journals/daily/date.md`, `journals/weekly/start_to_end.md`, or matching monthly/quarterly/yearly folders only when no prior convention governs the destination; they are suggestions, not automatic directories. Keep private records outside plugin/public source folders. Use available file tools, read the completed file back and report its actual location only after success. Inspect existing content before editing; preserve human corrections and avoid duplicate scheduled overwrites. Carry requested saving and verification through the authorized scope; do not stop at a chat-only draft and treat the file task as complete.

An authorized cloud document export uses an actually available connector and its workflow. It does not establish cloud continuity, synchronization or a saved learning. If tools or write access are missing, provide a usable chat/download draft and explain that the requested save was not completed.

Use [state operations](state.md) for selected meaning or persistent output preferences under the user's specific instruction. Exporting a diary never consents to capturing every personal interpretation.

## Scheduled variants

Read [scheduling](scheduling.md) for recurring delivery:

- A reminder invites input and waits; it does not manufacture an unanswered day.
- An automatic draft uses only agreed accessible material, is labeled a draft, and follows agreed missing-material behavior.
- A period review applies its own daily/weekly/monthly/quarterly/yearly writing rules and the agreed date window.
- Exploration delivery offers relevant new perspectives without inventing personal experience.

Settle missing cadence, time/timezone, source scope/exclusions, destination, workspace, options and saving behavior before activation. Task configuration, first delivered result, document storage and later continuity have separate evidence requirements. Existing ChatGPT tasks are not migrated or changed by installing these templates.
