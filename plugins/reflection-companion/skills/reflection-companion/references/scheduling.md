# Optional host-native delivery

Scheduled reflection and expansion are first-release workflows, enabled only on request. Use the available host scheduling tool; for Codex desktop, discover `automation_update` and follow its current schema. Prefer the same-task recurring mechanism unless the user asks for a new task per run. Do not substitute Runwork, OS cron, a local loop or a cloud backend.

## Set up

1. Resolve job(s), review period (`daily`, `weekly`, `monthly`, `quarterly`, `yearly` when applicable), cadence, local time, IANA timezone, source scope/exclusions, destination and absolute Companion workspace. A quarterly or yearly review is still on demand unless recurrence is requested. Ask only for missing choices. Inspect an existing matching schedule before creating a duplicate.
2. Confirm the skill is available in the target task and history/state can be accessed there. At each actual run, resolve the enabled installation's version and root from supported host information or the read-only update inspector, then read that root's `SKILL.md` and the references/template required for this run. A repository checkout, old cache path or this chat's prior reading is not proof of the loaded version. If a required minimum version or readable rules cannot be verified, retain the pending work and report the specific dependency under the agreed notification policy; a scheduled run does not authorize an upgrade. Use the selected personal workspace; an isolated Git worktree must not accidentally create a different state store.
3. Prepare a readable prompt using the template below. Store the user's job, time/window, source scope, destination, options, priority and concurrency/permission constraints there; route general writing rules to the current Skill instead of copying a second potentially stale specification. Each run retrieves the user's history/state; this setup conversation is not the whole corpus. State whether it uses live saved output preferences or fixed, user-selected options. Temporary choices from this chat do not become recurring defaults automatically. Do not encode private conclusions into the schedule prompt.
4. Create/update through the host tool only when authorized. Report its returned schedule identity/status and read back if supported. A prepared local prompt is not an activated schedule.
5. Test one immediate run when authorized. Verify history access, state path, timezone window and delivery. An `ACTIVE` status proves configuration, not delivery. Leave this runtime check pending if it cannot be performed.

## Prompt template

Verify the enabled Reflection Companion installation and read its current entrypoint, needed references and chosen template for this run. Perform [chosen review period or expansion]. Local workspace: [absolute workspace]. State: [existing authorized state path, or disabled]. Timezone: [IANA zone]. Source scope: [agreed topics and exclusions]. Window: [agreed calendar period, completed period or custom interval]. Options: [live saved preferences in the selected personal workspace, or fixed user-selected options]. Priority/catch-up: [agreed order, runtime window and bounded batch, or no catch-up requested]. For daily review, cover the agreed local calendar day up to execution time, or the preceding completed day when that is the agreed job. A weekly scheduled review can use seven completed local calendar days when agreed; monthly, quarterly and yearly reviews can cover the preceding completed calendar period. Resolve actual dates/cutoff at runtime. Keep an existing schedule's window until the user requests a change.

Retrieve source conversations and relevant active state before interpretation. Disclose material coverage limits. Honor confirmed corrections, distinguish proposed observations, and avoid repeating answered questions or expansion themes. Save only under existing permission; log shown items only if enabled. Do not silently initialize/relocate state. Deliver the requested result in the agreed task. If no useful new material exists, keep the response minimal; avoid filler. Report failures preventing delivery. Do not change this schedule or create another during the run.

Replace every bracketed field before saving. The host owns recurrence representation; do not manually edit its configuration files.

## Catch-up and independent progress

When catch-up is requested, agree whether current delivery or the oldest pending period has priority. Track daily and period keys independently, including actual source coverage, editorial decisions and saved readback. An older retrieval gap must not silently hold up a newer period that can be faithfully delivered within the agreed priority and batch. It also cannot disappear from the queue or be treated as complete. A weekly/monthly review with missing material remains partial even when some days were saved. Use original material and corrections; smaller reviews are indexes, not substitutes for it.

Respect the user's runtime window and concurrency constraints before heavy retrieval and writing. Retain pending work when the host is unavailable, a shared writer is active or the batch is exhausted. Resume only on a later permitted trigger; catch-up is not permission for a continuous loop, another schedule or daytime work. Quiet deferral must not be reported as delivered. Keep source indexes, rule-version/readback receipts and queues in the authorized personal progress area, with only a short source note in the diary.

“Can this run monthly?” asks about capability. “Run this every month” requests recurrence. Use context, not isolated keywords, to distinguish them. Installing new templates does not migrate existing schedules or change a previous Long View prompt.

## Change, pause, stop

Use the host schedule ID or inspect matching schedules. Apply only the requested change and verify returned status. Stopping proactive delivery must pause/delete the host schedule; disabling Companion storage alone does not stop it. A paused schedule does not delete personal records. Explain those effects when relevant. Keep notification settings in the host's supported fields.

## Host limits and evidence

September 25 official documentation supports scheduled prompts invoking skills and local-project execution. Local files require the machine to be on and the app running; web tasks cannot directly access the local folder. History access must be checked in the actual scheduled task/account. This package cannot promise delivery while the local host is unavailable.

Sources: [Scheduled tasks](https://learn.chatgpt.com/docs/automations), [Skills and scheduling](https://learn.chatgpt.com/guides/best-practices#use-scheduled-tasks-for-repeated-work).

If the host lacks scheduling or required permissions, identify the limitation and retain manual use. Do not advertise that environment as passing proactive delivery. Installing this package creates no recurring job or external provider call.
