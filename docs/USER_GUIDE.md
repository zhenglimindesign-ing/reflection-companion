# Reflection Companion user guide

[简体中文](USER_GUIDE.zh-CN.md) | **English**

[Purpose and value](../README.md) · [Installation and platform status](PLATFORMS.md)

This guide connects first use, diaries, weekly reviews, exploration, saving and schedules in one process. Current Codex public candidate: v0.4.0-rc.1, including the independent discovery catalog. Claude packages are not released as supported platforms before actual validation.

## 1. Start with something you are already thinking about

Follow the [installation guide](PLATFORMS.md), enable/select Reflection Companion and describe what you want. No personal profile, saving setup or capability selection is required.

If you already discuss things with AI, say:

> Review this week's discussions about this project. How did my decision criteria change? First explain which sources you can actually read. Do not save yet.

It should retrieve sources before comparison. Missing history access should be disclosed specifically; use the current conversation or selected supplied material without pretending to read the whole account or requiring a reconstructed archive.

Without history, try:

> I keep revising this proposal and cannot tell which preparation is necessary. Help me check my judgment, one decision-relevant question at a time.

Add facts, reject an explanation, change direction or stop. A useful one-off conversation need not produce a lasting conclusion.

## 2. One Skill, different situations

The four capabilities are Reflect, Challenge, Expand, and Preserve & Compound. Scenarios combine them as needed; they are neither separate new features nor steps to complete in order.

| Situation | Material | Say | Expected result |
| --- | --- | --- | --- |
| End-of-day diary | Accessible conversations that day or one event you choose to describe. | “Review today's material and write a short diary. Ask about gaps; no growth lesson yet.” | Grounded events and feelings, with interpretation separate. |
| Weekly review | Scoped chats or selected journal files. | “Compare my earlier and later judgments this week.” | Evidence of change, changed circumstances and uncertainty. |
| Uncertain decision | Current discussion, with relevant history if useful. | “Find the information most likely to change my conclusion; also consider support for it.” | A specific gap or alternative; the current view may be supported. |
| A broader perspective | Current question or scoped historical theme. | “Give me a relevant perspective beyond my usual approach.” | A new angle, its connection and a way to explore further. |
| Unsure what to ask | No history required, or use current context. | “Offer two different exercises and begin after I choose.” | A few options with purposes and material requirements. |
| Continue an earlier theme | Current conversation or authorized saved records. | “Read that earlier takeaway and reconsider it against this situation.” | Earlier qualifications and corrections remain available; conclusions can change. |
| A light bedtime chat | A moment you choose to share. | “No analysis today; let's just talk.” | Conversation without a compulsory lesson. |

Use existing material first. A diary is an optional form; daily manual input is not a prerequisite.

## 3. From a diary to a weekly review and a correction

This continuous demonstration uses author-invented events, not actual user experience.

**On the day:** You say, “I did not share my idea in today's meeting and feel disappointed; help me record it.” The assistant may ask which moment matters. You add, “I had two sentences ready, but the meeting ended as I was about to speak.” A diary can preserve that experience; it cannot infer “I fear speaking” without evidence.

**At the weekend:** You supply Tuesday and Friday's records. Tuesday attributes silence to lack of preparation; Friday shows preparation but no opportunity. The review should compare circumstances and explain why preparation alone cannot cover both, rather than repeat both entries. It should say “based on these two records,” not claim a complete week.

**Correction:** You say, “Tuesday was a quote from my colleague, not about me.” Retract the corresponding inference. If saved earlier, you can request a correction so it is not used to describe you again. Report a successful record ID/location, and use the corrected content on later reads.

This connects reflection, checking judgment and preserving corrections. Expansion can help anywhere useful, such as exploring ways to get an earlier speaking opportunity. Not every answer needs all four capabilities. More [specific dialogues](EXAMPLES.md) are optional references.

## 4. Exploration: the library supplies material; the Skill guides the process

Name a gentle roast or ask for a suitable method. After selection, continue here, using your answers for follow-up, evidence checks and revision. Copying a question into an ordinary chat is also valid. The Skill keeps selection, execution and continuation within a shared method.

| Source | How it works | What can be claimed |
| --- | --- | --- |
| 18 original base exercises | Available offline, selected by theme/material. | Reusable methods, not a popularity chart. |
| Contextual exercise | Written for your current question. | Original for this discussion, not a web discovery. |
| Independent catalog (candidate addition) | Refreshed when asking for something new; failures disclose the bundled snapshot date. | Newly curated is not newly published; flag checks older than 30 days. |
| Live web search | Verify original pages, dates and observable engagement. | No popularity claim without evidence; search snippets do not replace the original. |

For example: “What's new? No strengths theme again; offer two directions needing no history.” One possibility is a three-line snapshot of what matters now, what you are trying and what is uncertain. Returning later can reveal changes; completing an entire questionnaire is unnecessary.

Say “already discussed,” “not me,” “lighter,” or “stop.” Feedback applies immediately in the current chat. Cross-chat repetition checks need accessible exposure records; durable preferences need your saving instruction. Personal answers never enter the public library.

Catalog updates can be independent of plugin versions, but someone must actually collect, verify and publish them. No collection schedule is running. The public catalog is read when you request new content. Base exercises, the dated snapshot and live search remain separate options. See [maintenance](MAINTAINING.md).

## 5. Saving: three different records

| Record | Location | Use |
| --- | --- | --- |
| Original conversations | Managed by the AI host. | Read actually accessible, authorized material; no extra full-account archive. |
| Readable diaries/reviews | Your chosen folder or downloaded file. | Export on request; read and edit yourself. |
| Selected learning and corrections | Personal workspace `.reflection-companion/state.json`. | Continue later, separating confirmed content from tentative observations. |

For first setup: “Set up a local learning store; explain the location first and save only what I request.” Choose a personal workspace and timezone. Explain plain-text storage, ordinary Git exclusion and backup implications. Installation and public product directories should not hold personal records. The helper requires Python 3.10+; installing the Skill does not consent to saving.

Then say “Keep this conclusion, limited to this case,” “Show what is saved,” “Correct that record with what I just said,” or “Delete it.” The assistant should verify the operation before reporting a path/ID. An unsuccessful write is not a successful save. You do not need to edit JSON.

For readable files, `journals/daily/date.md` or `journals/weekly/start_to_end.md` are suggested structures, not automatically created folders. Saving a diary does not authorize extracting durable personal conclusions. Read existing files before editing, preserve human changes, and avoid duplicate runs overwriting them.

To continue across chats, use the same workspace or provide its location. If unknown, clarify rather than create another empty store; read before interpreting. Temporary web files are not files on your computer: provide downloads and explain retention limits. Stopping saving does not delete host chats/exports; removing Companion records does not remove host or backup copies.

## 6. Manual requests and scheduled runs

A message starts manual use; a host schedule runs the same method at an agreed time. Scheduling grants no extra source access.

| Scheduled mode | What happens |
| --- | --- |
| Diary reminder | Invite you to write and wait; do not invent an unanswered day. |
| Automatic diary draft | Use agreed sources and disclose gaps; report or skip absent material as agreed. |
| Weekly review | Compare scoped conversations or diaries in the chosen interval. |
| Exploration suggestions | Refresh a catalog or search for a few options without invented personal analysis. |

First run the desired result manually. Then request, for example: “Every Sunday at 20:00 Asia/Shanghai, review the preceding seven completed local calendar days from my selected journal folder. Deliver here without writing a file; disclose missing material.” Resolve needed time, timezone, sources, exclusions, output destination and saving permission; check access and use the host scheduling tool.

**Verify configuration and the first delivered run separately.** Installing a Skill, writing schedule instructions or having a store does not activate a task. Local Codex execution needs the app/device available; other hosts depend on actual account tools. Pause the host task to stop delivery. Disabling saving does not pause sending; pausing a task does not delete journals.

## 7. Install, update and give feedback

Current public Codex commands:

```sh
codex plugin marketplace add zhenglimindesign-ing/reflection-companion --ref v0.4.0-rc.1
codex plugin add reflection-companion@reflection-companion
```

Or ask Codex to install v0.4.0-rc.1 from that repository, verify the version and avoid duplicate enabled copies. Refresh as needed and open a new chat. Pinned refs do not automatically advance: inspect the current source/version before updating to a chosen ref, preserving the personal record directory. Claude packages and status are in the [platform guide](PLATFORMS.md).

The [mobile text sample](MOBILE.md) lets someone try one method. It does not carry Skill references, storage helpers, cross-chat state or scheduling, and is not verified native adaptation for domestic apps.

Feedback needs only the scenario, expectation and actual result. Fictional reproductions can replace private transcripts. See [feedback and maintenance](MAINTAINING.md). You can always stop or correct the model's interpretation.
