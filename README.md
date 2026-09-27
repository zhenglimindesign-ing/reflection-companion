# Reflection Companion

[简体中文](README.zh-CN.md) | **English**

Use conversations you already have to understand what changed, question assumptions, discover new ways to look at yourself, and carry useful learning forward.

**0.3.0 · Public alpha · Codex plugin with one Skill · MIT**

## Five ways to use it

| When you want to… | Try saying… |
| --- | --- |
| Notice change | “Review my recent conversations. What changed in how I judge this question?” |
| Check a judgment | “What might I be missing? Consider the strongest case for my current view too.” |
| Broaden your perspective | “Connect this concern to a useful idea outside my usual frame.” |
| Find self-exploration ideas | “Suggest a few different ways to understand myself. Keep it light today.” |
| Keep useful learning | “Save this conclusion. That older interpretation was wrong; use this correction.” |

You can start with a question, a current situation, or accessible past conversations. No journaling homework, saving setup or fixed command sequence is required. Daily, weekly, topic-based and bedtime conversations are optional rhythms.

## What a conversation can look like

*Fictional illustration, not a real user's history or a test result.*

> **You:** I have three quotes but keep requesting more. Am I using preparation to put off a decision?
>
> **Companion:** The count alone doesn't establish that. More research may help if a material cost is missing; otherwise it may add little. What unanswered question could change your choice?
>
> **You:** Whether maintenance is included.
>
> **Companion:** Then ask that specific question. The evidence supports closing a concrete gap; it doesn't justify labeling you a procrastinator.

The point is a useful, revisable interpretation. A sound judgment can stay sound. Read the [four complete examples](docs/EXAMPLES.md) or browse the [exploration library](https://github.com/zhenglimindesign-ing/reflection-companion/blob/main/docs/PROMPTS.md).

## Get started

In Codex, ask:

> Install Reflection Companion from https://github.com/zhenglimindesign-ing/reflection-companion at release v0.3.0. Check the version and avoid enabling duplicate older copies. Keep saving and scheduling off.

For the Codex CLI:

```sh
codex plugin marketplace add zhenglimindesign-ing/reflection-companion --ref v0.3.0
codex plugin add reflection-companion@reflection-companion
```

Open a fresh chat and select the plugin if required. Say: **“Use Reflection Companion. Suggest something worth exploring about myself.”** Or ask a specific question immediately.

The [full guide](docs/USER_GUIDE.md) covers ZIP installation, updates, local saving, corrections, scheduling and troubleshooting. Download the [versioned release](https://github.com/zhenglimindesign-ing/reflection-companion/releases/tag/v0.3.0) if you prefer a local package.

## Exploration that stays useful

The bundled library contains 18 original bilingual exercises across change, judgment, values, strengths, possibilities and playful expression. It can recommend from the library, adapt to your context, or search for recent public inspiration when you ask. Choose an option or ask it to choose, then continue in the same chat. “Not me,” “lighter,” “already discussed,” and “another direction” are useful feedback.

Recent examples are labeled separately from verified popularity. Personal answers do not enter the public library. New library editions ship with releases; [maintenance and contribution](docs/MAINTAINING.md) explains how.

## Before you use it

- Verified installation target: macOS with Codex CLI/desktop. Other hosts and operating systems are not certified by this release. Python 3.10+ is needed only for the optional local state helper.
- Historical reflection needs sources your host can actually retrieve. The plugin does not unlock complete account history or other providers. Without history it can work with the current conversation, with narrower claims.
- Saving is optional, in a folder you choose. Local records are plaintext; relevant content is still processed by the host/model under its policies. There is no developer-operated backend or telemetry.
- Scheduling is separately opt-in and host-dependent. Creating a schedule and receiving a successful first delivery are different outcomes. Always-on delivery is not promised.
- This supports your own interpretation and decisions. You can reject, correct or delete saved observations.

## Feedback and updates

The creator has used the earlier candidate and accepted public use. The new discovery workflow is included in this alpha; technical validation and synthetic examples do not establish usefulness for every user. We improve it through continued use and voluntary feedback.

[Report an issue or suggestion](https://github.com/zhenglimindesign-ing/reflection-companion/issues/new/choose) using the version, what you tried, expected behavior and what happened. Public issues are public: a small fictional reproduction is welcome; private chat transcripts are unnecessary. See [changes](CHANGELOG.md), [contribution guidance](docs/MAINTAINING.md), and [license](LICENSE).
