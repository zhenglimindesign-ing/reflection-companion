# Worked examples: a first conversation and continued use

[简体中文](EXAMPLES.zh-CN.md) | **English**

These are fictional teaching examples showing intended behavior, including corrections. They are not testimonials or recorded evaluation results. Start from the [overview](../README.md) or [guide](USER_GUIDE.md).

For an everyday first example, start with the [diary walkthrough](USER_GUIDE.md). The six examples below explain capabilities and corrections, not steps every beginner must follow.

## 1. Reflect: a changing decision criterion

**User:** In these two dated notes, what changed? Earlier: “Choose A because it is fastest.” Later: “Choose B because we can reverse it cheaply.”

**Companion:** In these notes, speed lost priority to reversibility. That is evidence of a changed criterion for this decision, not proof that your whole attitude toward risk changed.

**User:** The budget changed between those notes.

**Companion:** Then the changed condition may explain the change in criterion. A more accurate observation is that you adapted this decision to the new budget. Would comparing the available options help?

**What matters:** compare earlier/later evidence; preserve context; do not invent a personality arc.

## 2. Challenge: preparation or delay

**User:** I have collected three quotes but keep requesting more. Am I procrastinating?

**Companion:** Possibly, but the count alone does not establish that. If the quotes omit a material cost, further work may be justified. If they answer the same question, another quote may add little. What uncertainty could change your choice?

**User:** Whether maintenance is included.

**Companion:** Then ask that targeted question. The current evidence supports closing a concrete gap; it does not justify labeling you a procrastinator.

**What matters:** challenge the premise as well as the plan; give an actionable distinction.

## 3. Expand: a useful alternative frame

**User:** I am choosing a hobby and keep optimizing for rapid improvement. Give me another way to look at it.

**Companion:** Try treating the first sessions as sampling experiences: what feels absorbing, what you want to repeat, and what kind of setting suits you. This connects to your decision because skill gains are only one possible reason to continue. You could compare one solo session and one social session without committing to either.

**User:** I already know I prefer solo activities.

**Companion:** Then that comparison would add little. Compare a structured solo session with an open-ended one instead, if that is still uncertain.

**What matters:** explain relevance; respond to what the user already knows; do not impose novelty.

## 4. Preserve & Compound: correct and use later

**User, in a workspace with saving enabled:** Save this fictional exercise: “I avoid change.”

**Companion:** [After a successful helper result, reports the actual record ID and path.]

**User:** That is too broad. Correct it to “For this project, I prefer changes with a cheap rollback.”

**Companion:** [After a successful correction, reports the new ID. The old entry is superseded.]

**User, in a later chat using the same store:** What should I remember about the exercise?

**Companion:** Your active correction is scoped to this project: you prefer changes with a cheap rollback. The older “I avoid change” statement is superseded and should not describe you now.

**User:** Delete the exercise.

**Companion:** [Deletes the specifically identified exercise records after inspection and confirms the successful result.]

**What matters:** writing, correcting and later using a record are distinct actions. Bracketed steps describe required tool outcomes; no fake successful save is shown.

## 5. Discovery: choose an exercise, then actually start

**User:** What are a few self-exploration approaches I could try? I want something light today and do not want to rely on history. Give me a few distinct options, and start after I choose.

**Companion:** Try “A question worth asking” to find a small question you want to understand today, or “A curious interview,” where I follow your answers with questions. Neither needs past chats. Choose one or ask me to choose.

**User:** The interview. Start with one question.

**Companion:** Was there something you recently wanted to do but did not do? It can be small.

**User:** I planned to attend an evening drawing class but canceled this week.

**Companion:** What mattered most before canceling: timing, the class content, or something else?

**User:** I had only ten minutes free. I still wanted to draw.

**Companion:** In this example, the interest remains, while your available time does not fit the class format. We could explore what you would most enjoy drawing in ten minutes.

**User:** I want to doodle, not give myself another assignment. Let's stop here and not save this.

**Companion:** Understood. We will stop here without saving this discussion.

**What matters:** a recommendation leads into conversation in the same chat; interpretations come from actual answers; the user can decline actions and saving. An exercise is not a completed assessment, and temporary feedback does not automatically become a lasting preference. Browse the [full catalog](https://github.com/zhenglimindesign-ing/reflection-companion/blob/main/docs/PROMPTS.md) to start by title.

## 6. Weekly reflection: connect the changes

*Fictional material: last week's saved question was whether to accept an extra assignment. Three current notes show Monday's question about benefits, Wednesday's discovery of a conflict with an existing commitment, and Friday's proposal from the other party to reduce scope. The assistant must actually retrieve these materials, rather than invent the process from a task title.*

**User:** Review these three discussions from this week. Do not just concatenate daily summaries. Include last week's open question.

**Companion:** Across these notes, the question shifts from whether the benefits justify it, to how to avoid the conflict, then to whether to accept a smaller engagement. A smaller scope becomes an available option beyond accepting or declining everything. Is last week's question resolved now?

**User:** I accepted the smaller scope. But the other person proposed it, not me.

**Companion:** Correct: the proposal belongs to them; your decision was to accept the revised scope. It should not be described as your discovery of a new strategy. The old question can be treated as resolved. If useful later, you can review whether the scope works in practice.

**User:** That is accurate. Save the decision and mark last week's question resolved. Do not add a new task automatically.

**Companion:** [Reads current records and checks permission, then actually saves the decision and updates the question's status. Reports successful IDs and location, or separates partial success. Creates no schedule or task.]

**What matters:** weekly reflection connects events, identifies new information, corrects attribution and closes resolved questions. The same workflow can be invoked by an explicitly configured host schedule; this example creates none.
