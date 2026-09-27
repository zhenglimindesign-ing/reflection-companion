# Reflection Companion user guide

[简体中文](USER_GUIDE.zh-CN.md) | **English**

Version 0.3.0, public alpha. Start with the [overview](../README.md), [four complete examples](EXAMPLES.md), and [maintenance guide](MAINTAINING.md).

## Start directly

Review changes, check a judgment, broaden perspectives, discover self-exploration ideas, or keep useful learning. Daily, weekly, custom periods, topics and light bedtime conversations are composable ways to use it. Installation does not require saving or scheduling and does not automatically scan all history.

- “Review the past week. What changed in my thinking?”
- “Check this judgment and consider the evidence supporting it too.”
- “Connect this concern to a new perspective.”
- “I don't know where to start. Suggest a few light exercises.”
- “Find recent public self-exploration prompts; explain sources and popularity evidence.”
- “I agree with this takeaway; save it. That other inference is wrong; correct it to…”

A selected exercise runs in this conversation; no copying a long prompt or switching Skills. Say “not me,” “already discussed,” “lighter,” “deeper,” or “another direction.” Without usable history the assistant should state the scope and use current material or an exercise that does not need history.

## Install and update

The verified target is macOS with Codex CLI/desktop; other platforms are not certified. Optional saving requires Python 3.10+ and uses only the standard library.

Ask Codex to install from `https://github.com/zhenglimindesign-ing/reflection-companion` at `v0.3.0`, verify the version and avoid duplicate enabled copies. CLI:

```sh
codex plugin marketplace add zhenglimindesign-ing/reflection-companion --ref v0.3.0
codex plugin add reflection-companion@reflection-companion
```

Alternatively download a ZIP from [Releases](https://github.com/zhenglimindesign-ing/reflection-companion/releases), extract with hidden directories intact, and keep the README, `.agents`, plugins and inventory. Have the assistant verify SHA256SUMS and the inventory, register the actual local directory and install. Preserve that directory while it is a registered source.

Refresh the app if needed, then open a fresh chat and select the plugin. You need not work in the development project. Ask a real question after confirming 0.3.0; there is no requirement to repeat a developer acceptance checklist.

A pinned source does not automatically advance to a new version. For updates, give the assistant the target version: read back the current source/version and release notes, update the same source to the desired ref (or remove and re-register that source when required by the host), reinstall and verify. Preserve rollback information and your personal state directory; do not enable both an old candidate source and the public source. Updating the plugin should not change personal records. See [official plugin documentation](https://developers.openai.com/plugins/build/plugins).

## Optional continuity

Choose a personal workspace you own, outside shared folders, installation caches and temporary extraction directories. Say: “Use this workspace for Companion records. Explain the exact location and privacy first. Write only when I ask to keep or correct something.” Provide your actual timezone. After confirmation the assistant creates `.reflection-companion/state.json` in that workspace. Use the same workspace in later chats; give the original location if you move elsewhere.

Records are local plaintext. Relevant material is still processed by the host/model under its policies; this product adds no encryption, cross-device sync or developer backend.

Natural operations include “save this,” “correct it to…,” “resolved,” “stop using this observation,” “show saved records,” “export here,” “delete this,” “clear and pause saving,” and “exclude this topic.” Report the actual ID/path only after a successful write. Correction removes the old version from active use. Deletion does not remove original chats, past replies, exports or system backups.

Separately enable logging of shown questions/exploration themes if you want less repetition across chats. It is off by default. Shown does not mean endorsed. Exposure records older than 90 days are removed on a later exposure write; the default comparison window is 14 days. Semantic repetition still needs judgment; perfect novelty is not promised. Current-chat feedback works without storage; cross-chat preference saving needs explicit authority.

## Optional scheduling

Choose content, time, timezone, scope and workspace, then request setup, readback and a first-run check. For example: “In this workspace, each Sunday at 19:00 in my specified timezone, review seven complete calendar days, excluding personal relationships. Verify setup and first delivery.” Use your actual chosen time/timezone.

Reviews, questions, expansion and exploration suggestions can use the same behavior/source rules on a schedule. Delivery depends on the host, device and workspace access; cloud execution cannot automatically read local state. This release activates no schedule and does not promise delivery with the device off. See [host automation documentation](https://learn.chatgpt.com/docs/automations).

“Pause delivery” pauses the host schedule. Pausing saving does not pause delivery. Installation does not migrate existing schedules. A scheduled output does not prove it was read.

## Privacy, failures and feedback

There is no telemetry, automatic reporting, paid product account or product API key. Host account/usage limits still apply. History comes only from accessible sources; complete archives, attachments, audio, all past Codex chats and other providers are not guaranteed. Reject or correct AI observations; they are not diagnoses or decisions about what your life means.

Plugin missing: inspect source, hidden files, version and enablement, then refresh if necessary. History unavailable: identify the gap and work with current material; do not upload private transcripts merely to pass a check. Save failure/lock: preserve the original and inspect path/permissions, without resetting data or deleting locks. Continuity missing: check workspace and pause state; do not silently create a competing store.

Point out inaccurate, repetitive or unhelpful responses directly. Voluntary public feedback goes to [Issues](https://github.com/zhenglimindesign-ing/reflection-companion/issues/new/choose); version, expected and actual behavior are sufficient. Do not attach private conversations publicly. The assistant does not submit feedback automatically.
