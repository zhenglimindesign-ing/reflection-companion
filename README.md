# Reflection Companion

[简体中文](README.zh-CN.md) | **English**

**Turn your AI conversations into personal understanding you can revisit, question and revise.**

You may already discuss choices, projects, interests and uncertainties with AI. Reflection Companion connects the conversations actually available: revisit changes in your thinking, test explanations, explore relevant perspectives and, when you choose, preserve useful learning for the next conversation.

It is for people who regularly think with AI and want lasting value from those discussions. You do not need to maintain a complete parallel diary or rewrite a long reflection prompt each time.

[Start using it](docs/USER_GUIDE.md) · [Installation and platform status](docs/PLATFORMS.md)

## Why install a Skill instead of keeping a few prompts?

An ordinary prompt is enough for an occasional good question. This Skill is useful for repeated use: it organizes source reading, interpretation, correction and optional records into a reusable process, reducing the work of arranging those steps yourself.

| What you want | What the Skill handles |
| --- | --- |
| “Review this week” | Read accessible sources within your authorized scope, state coverage and compare changes. Disclose missing access. |
| “Find a blind spot” | Check your words, evidence and competing explanations, including the possibility that your current judgment is sound. |
| “That earlier interpretation was wrong” | Correct the discussion; if saved, update the record when requested so later reads use the correction. |
| “Explore something different” | Choose a suitable method from the base library, current context or public sources and continue after selection. Optional exposure records help reduce repetition. |
| “Return to this next week” | With saving enabled, read relevant learning from the same workspace and reconsider it against new material. |

A Skill is guidance for the model, with references and helpers such as the local state program. It has no exclusive model capability and does not guarantee a better answer than your own prompt. You can arrange the same process yourself. The reason to install is to reuse and maintain that process. Occasional questions without ongoing reflection do not require installing a prompt library.

## How one issue develops over time

This is an invented demonstration, not an observed user result.

On Tuesday you say, “I keep revising the proposal; perhaps I am procrastinating.” Friday's material adds, “The client only supplied the budget today.” A weekly review should adjust the explanation: missing information may explain the delay; repeated editing alone does not establish avoidance.

You can say, “Keep that learning for this case, but do not turn it into a fixed trait.” When something similar happens later, the Companion should consider that limitation alongside new evidence instead of restarting from “you always procrastinate.” This combines reflection, checking judgment and preserving corrections. If useful, it can also explore how to identify missing information earlier.

Saving is your choice. Without it, you can still reflect in the current conversation, without a promise of cross-chat continuity.

## Start with what you need now

| Situation | Say | Capabilities involved |
| --- | --- | --- |
| End of a day | “Use today's accessible conversations to review the day; ask about gaps. Do not save yet.” | Reflect; optionally turn it into a diary. |
| End of a week | “How did my view of this question change this week?” | Reflect, check judgment, optionally preserve. |
| An uncertain decision | “What might I have missed? Also consider support for my current view.” | Check judgment and expand perspectives. |
| A different perspective | “Give me a relevant perspective beyond my usual approach.” | Expand, with further discussion if useful. |
| Something new | “Suggest two light self-exploration exercises; start here after I choose.” | Discovery as an entry, using the four capabilities as needed. |
| Learning to keep | “Preserve this; correct the earlier record with this version.” | Preserve and compound. |

The four capabilities remain **Reflect, Challenge, Expand, and Preserve & Compound**. Diaries, weekly reviews and exploration are situations in which you use them. A manual message or a schedule starts the same Skill. The complete process lives in [one user guide](docs/USER_GUIDE.md).

## Sources and records

Installation does not unlock all account history. Access depends on host tools, your scope and supplied files. The host manages original chats. A diary can be exported as a readable document. Selected learning can be saved in a personal workspace's `.reflection-companion/state.json`, with inspection, correction and deletion.

Saving and scheduling are separate choices. A schedule starts the same process at an agreed time; it does not guarantee execution with the device off or invent a day with no source material. You can say “not me,” “another direction,” “no analysis yet,” or “stop.”

## Availability

The current public candidate is **v0.4.0-rc.2 / Codex, Claude Code and Claude web**, adding the independent discovery catalog and consolidated diary/weekly guidance. [Download the release](https://github.com/zhenglimindesign-ing/reflection-companion/releases/tag/v0.4.0-rc.2). Catalog updates still require actual checks and maintenance; no weekly collection service is running. The v0.3.0 archive and tag remain available.

Claude Code and web packages are published after fictional-input checks; web checks also covered diary downloads and the live catalog. See actual screenshots and scope in [platform status](docs/PLATFORMS.md). The [mobile text sample](docs/MOBILE.md) demonstrates one conversational method. It is not the full Skill or verified adaptation for domestic Chinese apps.

MIT licensed. The plugin is the installation/update package containing one Skill. There is no separate application panel or developer data server; your host's model-processing policy still applies. [Changes](CHANGELOG.md) · [Feedback and maintenance](docs/MAINTAINING.md) · [License](LICENSE)
