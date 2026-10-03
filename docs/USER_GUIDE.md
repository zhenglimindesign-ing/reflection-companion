# Reflection Companion scenarios and further-use guide

[简体中文](USER_GUIDE.zh-CN.md) | **English**

[Introduction and quick start](../README.md) · [Platform installation details and verification](PLATFORMS.md)

The README contains the introduction, installation and examples needed for first use. This guide develops diaries, weekly reviews, recurring-pattern checks, exploration, saving and schedules as needed, including how to select material, continue a discussion and keep results. It covers public Alpha v0.4.0.

## 1. Choose material and continue a question you already have

After installing and starting through the [README](../README.md), use existing discussions or describe something happening now. Your choice of material determines what this discussion can cover.

If you already discuss things with AI, say:

> Review this week's discussions about this project. How did my decision criteria change? First explain which sources you can actually read. Do not save yet.

It should retrieve sources before comparison. Missing history access should be disclosed specifically; use the current conversation or selected supplied material without pretending to read the whole account or requiring a reconstructed archive.

Without history, try:

> I keep revising this proposal and cannot tell which preparation is necessary. Help me check my judgment, one decision-relevant question at a time.

Add facts, reject an explanation, change direction or stop. A useful one-off conversation need not produce a lasting conclusion.

## 2. Choose a situation that fits your need

These common situations show the material needed and the result to expect. Describe your need in ordinary language.

| Situation | Material | Say | Expected result |
| --- | --- | --- | --- |
| End-of-day diary | Accessible conversations that day or one event you choose to describe. | “Review today's material and write a short diary. Ask about gaps; no growth lesson yet.” | Grounded events and feelings, with interpretation separate. |
| Weekly review | Scoped chats or selected journal files. | “Compare my earlier and later judgments this week.” | Evidence of change, changed circumstances and uncertainty. |
| Look for recurring patterns | Multiple accessible discussions across a period, ideally from different contexts. | “Looking across these discussions, is there a way of thinking that keeps showing up but I may not have noticed? Treat it as something to test.” | Concrete evidence, scope and counterexamples or limits; one event does not become a stable trait. |
| The end of a period or experience | Selected material from a month, project or topic. | “Look back on this experience from the beginning. How was I thinking at first, which judgments changed later, and which criteria stayed consistent?” | Connect experiences, changes and questions worth considering across a period. |
| Uncertain decision | Current discussion, with relevant history if useful. | “Find the information most likely to change my conclusion; also consider support for it.” | A specific gap or alternative; the current view may be supported. |
| A broader perspective | Current question or scoped historical theme. | “Give me a relevant perspective beyond my usual approach.” | A new angle, its connection and a way to explore further. |
| Unsure what to ask | No history required, or use current context. | “What are a few different self-exploration approaches I could try? Give me distinct options, and start one after I choose.” | A few options with purposes and material requirements. |
| Continue an earlier theme | Current conversation or authorized saved records. | “Read that earlier takeaway and reconsider it against this situation.” | Earlier qualifications and corrections remain available; conclusions can change. |
| A light bedtime chat | A moment you choose to share. | “No analysis today; let's just talk.” | Conversation without a compulsory lesson. |

Use existing material first. A diary is an optional form; daily manual input is not a prerequisite.

## 3. A concrete example: do I still enjoy drawing?

This teaching example is invented, not an actual user experience or evaluation result. The three discussions use an event that day, two records and a takeaway you choose to keep.

**That day, clarify an experience:** You say, “I did not draw again tonight. Have I stopped enjoying it?” During the discussion you add, “I had ten minutes after work, but the class lasts an hour.” The confirmed issue is a mismatch between class length and available time. A diary can record the experience and question; missing the class alone does not establish lost interest.

**At the weekend, connect the experiences:** You supply two records: on Tuesday you missed an hour-long class; on Friday you enjoyed sketching freely for ten minutes. A review might say, “These two records support that you still enjoy drawing; short, informal sessions may fit better right now.” This adds an understanding beyond repeating the daily summaries, while retaining the scope of two records.

**Later, continue or revise:** You can request saving: “This week, ten minutes of informal drawing fitted my schedule better than an hour-long class.” When that record is read next time, continue with your current circumstances. If you later prefer a structured class, revise the takeaway's scope. Successful saves or corrections should report an actual location or record ID. Earlier understanding can change with new experience.

The discussions clarify an event, connect two experiences and bring a takeaway into later thinking. Saving is your choice, and continuing later requires actually reading the record. See [complete examples](EXAMPLES.md) for more detailed conversations.

## 4. Exploration: the library supplies material; the Skill guides the process

Exploration includes the bundled library, independently updated catalog, exercises designed for your situation and live search. Eighteen is the current base library's count, not a limit on all exploration. New catalog entries do not require reinstalling the Skill.

Name a gentle roast or ask for a suitable method. After selection, continue here, using your answers for follow-up, evidence checks and revision. Copying a question into an ordinary chat is also valid. The Skill keeps selection, execution and continuation within a shared method.

| Source | How it works | What can be claimed |
| --- | --- | --- |
| 18 original base exercises | Available offline, selected by theme/material. | Reusable methods, not a popularity chart. |
| Contextual exercise | Written for your current question. | Original for this discussion, not a web discovery. |
| Independent catalog | Refreshed when asking for something new; failures disclose the bundled snapshot date. | Newly curated is not newly published; flag checks older than 30 days. |
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

To continue across chats, use the same workspace or provide its location. If unknown, clarify rather than create another empty store; read before interpreting. In Claude web, ask for a downloadable Markdown file without writing to a learning store. Replies and exported files should follow your current conversational language; name a different language only when you want a translation. Click Download on the file card, then open it to check; the [platform guide](PLATFORMS.md) includes actual screenshots. Temporary web files are not computer files or permanent cross-chat storage; supply the export again to continue later. Stopping saving does not delete host chats/exports; removing Companion records does not remove host or backup copies.

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

## 7. Update and give feedback

Basic installation is in the [README](../README.md). Before upgrading, inspect the current source and version, update to your chosen version, avoid duplicate enabled copies and preserve your personal record directory. Pinned versions do not automatically advance. Package checksums, detailed host instructions and tested scope are in the [platform guide](PLATFORMS.md).

The [mobile text sample](MOBILE.md) lets someone try one method. It does not carry Skill references, storage helpers, cross-chat state or scheduling, and is not verified native adaptation for domestic apps.

Feedback needs only the scenario, expectation and actual result. Fictional reproductions can replace private transcripts. See [feedback and maintenance](MAINTAINING.md). You can always stop or correct the model's interpretation.
