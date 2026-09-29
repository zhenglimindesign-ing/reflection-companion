# Choose an entry and install

[简体中文](PLATFORMS.zh-CN.md) | **English**

[Overview](../README.md) · [Mobile introduction](MOBILE.md) · [Scenarios](USER_GUIDE.md)

Public candidate **v0.4.0-rc.1** provides the Codex plugin, Claude Code project Skill and Claude web Skill. [Download your platform package](https://github.com/zhenglimindesign-ing/reflection-companion/releases/tag/v0.4.0-rc.1). All three share one core, with packaging for each host.

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

## Codex: the public release

Ask Codex to install `https://github.com/zhenglimindesign-ing/reflection-companion` at `v0.4.0-rc.1`, verify the version and avoid duplicate enabled copies. Leave saving and scheduling off initially. Start a fresh chat, select the Skill and describe a scenario. The [full guide](USER_GUIDE.md) covers CLI installation and upgrades. The older v0.3.0 remains available without the new dynamic catalog.

## Claude Code: published candidate package

Download `reflection-companion-claude-code-0.4.0-rc.1.zip`, check it against `SHA256SUMS-claude-code.txt` on the same release, and extract into a chosen personal project. The resulting entry is `.claude/skills/reflection-companion/SKILL.md`; `.claude` is hidden. Inspect and preserve an existing copy before replacing it. No clone of the development repository is required.

Start Claude Code in that project and enter:

```text
/reflection-companion Help me write today's diary, one question at a time. Use this conversation only; do not save yet.
```

If the Skill is missing or has an old description, check the path and reopen the project session. Core conversation needs no Python; local state and the catalog helper require Python 3.10+. Saving/correction must return actual locations and readback. Installation grants no additional history access.

## Claude web: install, begin and download a record

1. Download `reflection-companion-claude-web-0.4.0-rc.1.zip` from the release and check `SHA256SUMS-claude-web.txt`. Do not extract it or upload the whole Codex distribution.
2. Open Customize → Skills in Claude, add the ZIP and confirm that `reflection-companion` is enabled with 11 files in Contents. The account needs Skills and the required file/code-execution capabilities; check official account requirements if the entry is absent.
3. Start a new chat: “Use Reflection Companion to help me write a diary about one small event today, one question at a time. Do not save yet.” Start with your material; no long prompt needs memorizing.
4. Correct an interpretation by supplying facts or saying it does not fit. For a file, ask: “Export the corrected entry as a downloadable **English Markdown** file; do not add it to a learning store.”
5. Click **Download** on the reply's file card, save to a chosen folder and open it to check. Supply that file again when you want to continue in another conversation.

This actual installation screenshot shows the upload's Claude `v1` label. The project's release version is `0.4.0-rc.1`, identified by the ZIP filename and release page.

![Actual enabled installation with 11 files in Contents](images/claude-web-installed.jpg)

The screenshot below is a real check using explicitly fictional Chinese material. The generated diary is on the right; its download card is on the left. It is neither a real person's experience nor a required template.

![Fictional Chinese diary check with a corrected explanation and Download button](images/claude-web-export.jpg)

You still need to download an export; a container path is not a file on your computer. Installing the Skill does not enable permanent cross-chat records or schedules. For exploration, ask for two newer methods with dates and attribution and begin one here. Catalog refresh depends on the current account's network capabilities; this does not establish online access for every environment.

## Verification boundaries

The candidate build checks core-byte equality, entry format, relative links and archive integrity for both Claude packages. Actual Claude Code results accompany the candidate verification receipt. The Code and web checks are scoped below; full domestic-host capability remains unverified. The mobile text entry can be tried first, with results checked in the user's own app.

Personal records belong in a chosen workspace, not necessarily the installation, public repository or development source. Installation grants neither full account history nor saving/scheduling permission.

## Actual verification scope (2026-09-29)

Claude Code 2.1.218 completed fictional-input checks for Skill discovery/invocation, diary facts versus inference, a supplied weekly file with a later correction, an in-conversation exploration, and local save/readback using the bundled helper. No personal chats or real continuity store were used.

A combined initialize/save/correct/readback request timed out before its final response. File inspection confirmed the old entry was superseded, but that request is not counted as a completed conversation. A smaller save/readback request then completed. Restricted command permissions caused retries; review storage operations when the host asks. Unattended scheduled delivery was not tested, and model execution is not guaranteed identical each time.

Claude web checks in one account covered upload/enabling, actual Skill reading, diary reflection, later factual correction, Markdown creation/download, live catalog refresh and starting an exploration. Downloading the installed package confirmed all 11 core files match the candidate byte-for-byte. Only fictional material was used.

The first export was English despite Chinese context. An explicit request produced a Chinese file, which was downloaded and read back. The example export request therefore specifies a language; users should still check the result. Permanent cross-chat storage, unattended delivery and every account/model combination were not tested. Failure fallback has script tests; this web run succeeded online and did not force an outage.

This main-branch guide follows subsequent validation; the frozen Codex ZIP retains its packaging-time platform-status text. Use this page and the release notes for current status.
