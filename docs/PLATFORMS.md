# Platform installation details and verification

[简体中文](PLATFORMS.zh-CN.md) | **English**

[Introduction and quick start](../README.md) · [Mobile introduction](MOBILE.md) · [Scenarios and further use](USER_GUIDE.md)

Basic installation and a first conversation are covered in the README. This page provides host-specific details, screenshots, update instructions and dated verification records for questions about a particular platform.

Public Alpha **v0.5.6** provides the Codex plugin, Claude Code project Skill and Claude web Skill. [Download your platform package](https://github.com/zhenglimindesign-ing/reflection-companion/releases/tag/v0.5.6). All three share one core, with packaging for each host.

## Claude Code versus Claude web

| | Claude Code | Claude web |
| --- | --- | --- |
| Suitable for | People working with projects and local files, usually from a terminal. | People using Skills in browser conversations. |
| Installation | Put the Skill in a selected project's `.claude/skills/reflection-companion/`. | Upload the dedicated ZIP in Customize → Skills with required execution capabilities enabled. |
| Invocation | `/reflection-companion` or a matching natural-language request. | Enable the Skill and describe the request; do not assume the same slash command. |
| Materials | Current context and authorized project/local files. | This chat, supplied uploads and actually available tools. |
| Diary destination | An authorized local folder, with readback. | A downloadable artifact; not proof of saving on the user's computer or permanent cross-chat retention. |
| Scheduling | Depends on host tools and operating conditions. | Also depends on account tools; uploading a Skill creates no task. |

The difference covers access, permissions and file lifetime, not just invocation. Both packages are generated from one core Skill. References: [Claude Code Skills](https://code.claude.com/docs/en/skills) and [custom Claude Skills](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills).

## Account memory and conversation-history access

Signing in with the same provider account does **not** mean every surface exposes the same personal history.

- **ChatGPT ↔ Codex:** Codex can use a ChatGPT account for sign-in and has its own memory features, but Codex remains a separate experience with separate chat history. Do not treat ChatGPT Memory or a remembered summary as proof that Codex can read the underlying ChatGPT conversations. See [Using Codex with your ChatGPT plan](https://help.openai.com/en/articles/11369540-using-codex-with-your-chatgpt-plan), [ChatGPT Work and Codex](https://help.openai.com/en/articles/20001275/) and [Memory in ChatGPT](https://help.openai.com/en/articles/8590148-memory-in-chatgpt).
- **Claude ↔ Claude Code:** Claude chat memory applies to supported chat surfaces; Claude Code uses its own project/session context such as `CLAUDE.md` and auto-memory. A shared subscription/login does not establish shared historical evidence. See [Claude chat search and memory](https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context) and the [Claude Code cheatsheet](https://support.claude.com/en/articles/14553413-claude-code-cheatsheet).

For Reflection Companion, memory may help orient a conversation, but historical interpretation should be grounded in the original conversations, notes, files or exports the current host can actually retrieve. If that source scope is unavailable, narrow the claim or disclose the gap.

## Codex: the public release

### First installation

The [README](../README.md) shows the pinned Git marketplace route for v0.5.6. Run the marketplace registration before `codex plugin add`: the install command needs the selector `reflection-companion@reflection-companion`, identifying both the plugin and its marketplace. See [OpenAI's marketplace source documentation](https://developers.openai.com/plugins/build/plugins#build-your-own-curated-plugin-list).

Alternatively, download `reflection-companion-0.5.6.zip` from the release and check its digest against that release's `SHA256SUMS.txt`. Extract the complete package into a stable local directory. The marketplace root is the extracted `reflection-companion-0.5.6` folder containing `.agents/plugins/marketplace.json` and `plugins/reflection-companion/`, **not** the ZIP itself or the inner Skill folder. `.agents` is hidden on some systems.

Replace the example path below with that extracted root:

```sh
codex plugin marketplace add /path/to/reflection-companion-0.5.6
codex plugin add reflection-companion@reflection-companion
codex plugin list --marketplace reflection-companion --json
```

Choose one source route for the first installation; keep a local source available for later refreshes. The list should show an enabled, installed entry at version `0.5.6`. If your CLI lacks these subcommands, record `codex --version` and the result of `codex plugin --help`; no Linux-specific support claim follows from these instructions.

After installation, refresh as the interface requires, start a fresh CLI session with `codex` or a new desktop chat with Reflection Companion enabled, and try a fictional request: “Help me write a diary about an imaginary walk, one question at a time; do not save.” Confirm that the Skill is actually available in that chat. A successful install/list command alone does not establish a successful invocation.

### Existing installations and updates

If `reflection-companion` is already registered, inspect the existing installation and follow the update procedure below instead of replacing its source with the first-install commands.

Ask to check for a newer release, upgrade to a selected formal version or return to the prior version. A check leaves installation unchanged. A pinned ref does not advance automatically. Keep the same plugin ID, `reflection-companion@reflection-companion`, and preserve the journal/preference directory outside the plugin cache.

**Release 0.5.1** includes a Python 3.11+ helper with check, verified preparation, upgrade and receipt-based rollback. It backs up the existing plugin, uses the native CLI, checks actual installed bytes and unrelated settings, and attempts recovery once on failure. Native recovery requires the Git source available; a retained backup does not establish automatic offline restoration. Details and commands are in [installation updates](../plugins/reflection-companion/skills/reflection-companion/references/updates.md). Published 0.5.0 does not contain this helper; a reviewed current checkout or host-assisted installation is needed for that first transition.

Report “installed” separately from “loaded in this chat”; follow the host's reload instructions and check a fresh invocation. For a recovery failure, keep its receipt and backup and resolve the named failure. Do not remove the whole marketplace or overwrite unrelated settings. See [maintenance and recovery](MAINTAINING.md).

## Claude Code: public Alpha package

Download `reflection-companion-claude-code-0.5.6.zip`, check it against `SHA256SUMS.txt` on the same release, and extract into a chosen personal project. The resulting entry is `.claude/skills/reflection-companion/SKILL.md`; `.claude` is hidden. Inspect and preserve an existing copy before replacing it. No clone of the development repository is required.

Start Claude Code in that project and enter:

```text
/reflection-companion Help me write today's diary, one question at a time. Use this conversation only; do not save yet.
```

If the Skill is missing or has an old description, check the path and reopen the project session. Core conversation needs no Python; local state and the catalog helper require Python 3.10+. Saving/correction must return actual locations and readback. Installation grants no additional history access.

For an update, preserve the exact existing Skill folder outside `.claude/skills`, verify the selected replacement ZIP, and replace that folder without overlaying obsolete files. Retain the old folder for rollback and keep project journals/state in place. This is a standalone Skill distribution; Claude plugin-marketplace auto-update settings apply only to plugins installed through that other channel. See [Claude's plugin update documentation](https://code.claude.com/docs/en/discover-plugins#keep-plugins-updated).

## Claude web: install, begin and download a record

1. Download `reflection-companion-claude-web-0.5.6.zip` from the release and check `SHA256SUMS.txt`. Do not extract it or upload the whole Codex distribution.
2. Open Customize → Skills in Claude, add the ZIP and confirm that `reflection-companion` is enabled with 35 files in Contents. The account needs Skills and the required file/code-execution capabilities; check official account requirements if the entry is absent.
3. Start a new chat: “Use Reflection Companion to help me write a diary about one small event today, one question at a time. Do not save yet.” Start with your material; no long prompt needs memorizing.
4. Correct an interpretation by supplying facts or saying it does not fit. For a file, ask: “Export the corrected entry as a downloadable **Markdown** file; do not add it to a learning store.”
5. Click **Download** on the reply's file card, save to a chosen folder and open it to check. Supply that file again when you want to continue in another conversation.

Replies and exported files default to the current conversational language. An explicit account preference, such as “all deliverables in English,” can override that default. If they conflict, clarify the preference once rather than require a language reminder on every export. This screenshot records the original rc.1 installation; Claude's `v1` / `v2` labels belong to the uploaded item. The ZIP filename and release page identify the project release.

![Actual enabled installation with 11 files in Contents](images/claude-web-installed.jpg)

The screenshot below is a real check using explicitly fictional Chinese material. The generated diary is on the right; its download card is on the left. It is neither a real person's experience nor a required template.

![Fictional Chinese diary check with a corrected explanation and Download button](images/claude-web-export.jpg)

You still need to download an export; a container path is not a file on your computer. Installing the Skill does not enable permanent cross-chat records or schedules. For exploration, ask for two newer methods with dates and attribution and begin one here. Catalog refresh depends on the current account's network capabilities; this does not establish online access for every environment.

To update the custom Skill, retain the old ZIP and use the account's current Skills UI to update the existing item, then verify its contents and a fresh chat. If replacement is unavailable, use the offered workflow and keep only the chosen copy enabled. Rollback uses the retained old ZIP. A prepared local ZIP is not a completed upload; chats, diary downloads and cloud files are separate. See [custom Skill guidance](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills).

## Verification boundaries

The release build checks core-byte equality, entry format, relative links and archive integrity for both Claude packages. Earlier Claude Code results are dated below; the new five-period authoring rules were tested on Codex in this round. The Code and web checks are scoped below; full domestic-host capability remains unverified. The mobile text entry can be tried first, with results checked in the user's own app.

Personal records belong in a chosen workspace, not necessarily the installation, public repository or development source. Installation grants neither full account history nor saving/scheduling permission.

## Five-period checks (2026-10-03)

Codex CLI 0.145.0 runs use an isolated project, frozen packaged Skill files and fictional dated notes. The suite covers all five periods, English annual writing, temporary component switches, separately identified AI observation, saved weekly preferences used in a fresh process, technical-log non-triggering, a scheduling-capability question and additional material absent from the bundled examples. No model or reasoning-effort override is requested; the command evidence does not establish an exact hidden runtime model.

Earlier attempts exposed unsupported first-person meaning, miscopied dates, changed speaker attribution and an invented shared purpose between separate activities. The core now requires source checks and a factual motive/cause audit. The read-only helper checks submitted dates and exact quotes; it cannot validate every interpretation or detect unsubmitted claims. Generated prose still needs review for excessive generalization, implied motives and scope notes. These checks establish scoped behavior, not human usefulness or guaranteed output quality.

The two Claude 0.5.0 packages contain the same 29-file core. This round does not run the new authoring rules on Claude Code or upload the new package to Claude web. Earlier Claude evidence below remains tied to its original package. Real phone use, cloud writes and unattended delivery are not covered here.

## Desktop checks in this round (2026-10-02)

Claude Code 2.1.218 used an isolated project, fictional material and fresh sessions to check local save/readback, replacement of an old record, a fresh session using the corrected decision, and disabling saving while preserving history. Testing found that the model appended unconfirmed wording and retained a corrected conclusion as an active preference. Version 0.4.0 strengthens verbatim-save and replacement instructions; the affected behaviors were checked again. An independent read-only Codex CLI 0.145.0 session also used the corrected active record without changing the store.

Claude also completed a weekly review with later corrections, Chinese Markdown readback and immediate exploration. Its missing-history explanation contained inaccurate date/store statements, leading to a focused scope rule. Claude reached its session limit during the verbatim-save regression; that interrupted run is not counted as a pass. Codex CLI completed the subsequent verbatim-save, scope and offline-snapshot checks. Host command permissions may still need review. These tool-backed checks cover this environment and do not guarantee identical execution by every model.

All three 0.4.0 packages are generated from the same core. The new package was not uploaded again to a Claude web account in this round. Earlier web diary, language and download evidence is below; the new saving rules were mainly accepted against a local desktop store. Permanent web cross-chat storage, real phone use and unattended scheduling remain unverified. Installation enables neither personal saving nor tasks.

## Earlier web and desktop checks (2026-09-29)

Claude Code 2.1.218 completed fictional-input checks for Skill discovery/invocation, diary facts versus inference, a supplied weekly file with a later correction, an in-conversation exploration, and local save/readback using the bundled helper. No personal chats or real continuity store were used.

A combined initialize/save/correct/readback request timed out before its final response. File inspection confirmed the old entry was superseded, but that request is not counted as a completed conversation. A smaller save/readback request then completed. Restricted command permissions caused retries; review storage operations when the host asks. Unattended scheduled delivery was not tested, and model execution is not guaranteed identical each time.

Claude web checks in one account covered upload/enabling, actual Skill reading, diary reflection, later factual correction, Markdown creation/download, live catalog refresh and starting an exploration. Downloading the installed package confirmed all 11 core files match the candidate byte-for-byte. Only fictional material was used.

The earlier web check produced English artifacts during a Chinese conversation. A later retest verified that the test account explicitly required all deliverables in English. That account preference affected the result; attributing it solely to a Skill defect was incomplete. rc.2 strengthens the language rule for exported artifacts while retaining explicit user language choices. Chinese and English Claude Code export checks passed without added language instructions.

The temporary web authentication error has cleared. With only that general account preference set aside for the test, the installed Skill produced a Chinese filename, headings, body and table; the actual downloaded Markdown was inspected. The trace showed reads of the installed SKILL.md and scenarios.md. No account settings were changed for this test. This verifies the default in that scoped context, not identical behavior under every personal instruction. The installed web v2 core files still match rc.2.

Permanent web continuity, unattended delivery and every account/model combination remain untested. A temporary web container is not a permanent learning store; supply downloaded files again to continue in another chat. Scheduling belongs to the host, and installing a Skill does not start a scheduling service. Catalog fallback has script tests; the earlier web run succeeded online without a forced outage.

The public main branch guide evolves with verification; each archive retains its packaging-time record. Old assets and tags remain unchanged. rc.2 shipped the language fix, 0.4.0 the saving/onboarding rules, and 0.5.0 the five-period specifications and configurable output. 0.5.1 adds the installation lifecycle helper and host-specific update/recovery guidance.

## External installation report (2026-10-04)

[Cid-oe's PR #4](https://github.com/zhenglimindesign-ing/reflection-companion/pull/4) reports an attempted installation on Linux with Codex CLI 0.159.2 and the v0.5.0 Public Alpha ZIP. The contributor downloaded and extracted the package, then stopped before a first invocation because the README and platform guide did not provide marketplace registration commands or the required installation path/selector.

This is a contributor-reported blocked attempt, without attached command logs; it is not a verified Linux installation or a general compatibility result. The maintainer separately checked the published v0.5.0 documents and confirmed that the CLI installation commands were absent. The current main-branch guides now explain the Git and extracted-ZIP routes; the historical v0.5.0 tag and archives keep their original contents.

## Maintainer installation check (2026-10-05)

On macOS with Codex CLI 0.145.0, separate isolated configuration directories were used to run marketplace registration, plugin installation and plugin listing through both the pinned v0.5.3 Git route and the verified v0.5.3 ZIP route. Both returned an enabled plugin at version 0.5.3, and the installed plugin files matched the published package bytes. No new model invocation or Linux test was performed in this check.
