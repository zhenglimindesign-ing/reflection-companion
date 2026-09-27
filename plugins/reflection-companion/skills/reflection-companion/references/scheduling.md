# Optional host-native delivery

Scheduled reflection and expansion are first-release workflows, enabled only on request. Use the available host scheduling tool; for Codex desktop, discover `automation_update` and follow its current schema. Prefer the same-task recurring mechanism unless the user asks for a new task per run. Do not substitute Runwork, OS cron, a local loop or a cloud backend.

## Set up

1. Resolve job(s), cadence, local time, IANA timezone, scope/exclusions, destination and absolute Companion workspace. Ask only for missing choices. Inspect an existing matching schedule before creating a duplicate.
2. Confirm the skill is available in the target task and history/state can be accessed there. Use the selected local workspace; an isolated Git worktree must not accidentally create a different state store.
3. Prepare a readable prompt using the template below. Each run retrieves the user's history/state; this setup conversation is not the whole corpus. Do not encode private conclusions into the schedule prompt.
4. Create/update through the host tool only when authorized. Report its returned schedule identity/status and read back if supported. A prepared local prompt is not an activated schedule.
5. Test one immediate run when authorized. Verify history access, state path, timezone window and delivery. An `ACTIVE` status proves configuration, not delivery. Leave this runtime check pending if it cannot be performed.

## Prompt template

Use the installed Reflection Companion to perform the user's chosen review/expansion. Local workspace: [absolute workspace]. State: [absolute workspace]/.reflection-companion. Timezone: [IANA zone]. Scope: [agreed topics and exclusions]. For daily review, cover the agreed local calendar day up to execution time; for weekly review, cover seven completed local calendar days unless the user chose another interval. Resolve dates at runtime.

Retrieve source conversations and relevant active state before interpretation. Disclose material coverage limits. Honor confirmed corrections, distinguish proposed observations, and avoid repeating answered questions or expansion themes. Save only under existing permission; log shown items only if enabled. Do not silently initialize/relocate state. Deliver the requested result in the agreed task. If no useful new material exists, keep the response minimal; avoid filler. Report failures preventing delivery. Do not change this schedule or create another during the run.

Replace every bracketed field before saving. The host owns recurrence representation; do not manually edit its configuration files.

## Change, pause, stop

Use the host schedule ID or inspect matching schedules. Apply only the requested change and verify returned status. Stopping proactive delivery must pause/delete the host schedule; disabling Companion storage alone does not stop it. A paused schedule does not delete personal records. Explain those effects when relevant. Keep notification settings in the host's supported fields.

## Host limits and evidence

September 25 official documentation supports scheduled prompts invoking skills and local-project execution. Local files require the machine to be on and the app running; web tasks cannot directly access the local folder. History access must be checked in the actual scheduled task/account. This package cannot promise delivery while the local host is unavailable.

Sources: [Scheduled tasks](https://learn.chatgpt.com/docs/automations), [Skills and scheduling](https://learn.chatgpt.com/guides/best-practices#use-scheduled-tasks-for-repeated-work).

If the host lacks scheduling or required permissions, identify the limitation and retain manual use. Do not advertise that environment as passing proactive delivery. Installing this package creates no recurring job or external provider call.
