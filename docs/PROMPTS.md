# Bundled exploration library

[简体中文](PROMPTS.zh-CN.md) | **English**

This is the base library bundled with the Skill, generated from its runtime source. Do not edit separately. It is not the entire dynamic catalog or a trend ranking. Select an exercise and continue in the same chat.

[Overview](../README.md) · [Full user guide](USER_GUIDE.md)

## How to use this library

Say “Ask me one question that could help me understand myself.” The assistant should choose a bundled exercise and begin immediately, without a bundled/web menu. Request two or three distinct choices if you prefer to select, or name a title below; no IDs or long prompt copying required.

Each entry states its material needs: no history, a current situation, or scoped history. If history is unavailable, choose another exercise or provide a small example you want to discuss. Say “not me,” “lighter,” or “another one” to adjust; takeaways are saved only when requested. Each exercise has both language versions, not two separate question banks.

Historical judgments about blind spots, self-understanding, happiness, priorities and traces first check actual time/topic coverage, evidence, counterexamples and corrections. Insufficient material means a scoped answer or an unresolved judgment; happiness proposals are not proven causes and a third-person introduction is not a complete biography.

These 23 entries are this version's starting points. Ask “what is new?” to read the independently updated catalog or verify recent public sources; a failed read should disclose the dated bundled snapshot used instead. Catalog content requires actual curation and publication; no automatic collection service is running. See [complete user guide](USER_GUIDE.md).

## Change and growth

### How my criteria changed

`change-criteria` · Accessible history within a chosen scope · Reflect

> Compare my criteria for judging the same issue over this period. What changed and what stayed stable? Show earlier and later evidence; no clear change is a valid finding.

Possible continuation: Check whether new evidence or a different situation explains the change.

### Quiet progress

`change-quiet-progress` · Accessible history within a chosen scope · Reflect

> Find a possible improvement I may be underestimating in recent conversations. Use concrete behavior and identify gaps in the evidence.

Possible continuation: Let me decide whether it counts as progress.

### Questions still worth revisiting

`change-unfinished` · Accessible history within a chosen scope · Reflect / Challenge

> Find a previously discussed question that may be worth revisiting. Check for newer outcomes first; a missing ending does not prove it is unresolved.

Possible continuation: Compare current conditions with the earlier ones.

## Judgment and blind spots

### One testable assumption

`judgment-assumption` · Current situation or concrete example · Challenge

> Check one important, weakly supported assumption in my current judgment. Explain its consequence and the case in my favor; say so if the reasoning looks sound.

Possible continuation: Find a low-cost way to test it.

### A competing explanation

`judgment-opposite` · Current situation or concrete example · Challenge

> Offer a competing explanation that also fits the current facts. What new information would distinguish them? Do not manufacture disagreement.

Possible continuation: Compare the explanations against a concrete event.

### Preparation or postponement

`judgment-preparation` · Current situation or concrete example · Challenge

> Help me examine whether further preparation reduces a real risk or postpones action. Look for evidence on both sides without assuming procrastination.

Possible continuation: Identify the missing information that could change the decision.

### A possible blind spot

`judgment-blind-spot` · Accessible history within a chosen scope · Reflect / Challenge

> Using the history you can actually access, look for a possible thinking pattern or blind spot I may not have fully noticed, supported by multiple instances. State source coverage, compare evidence, counterexamples, earlier self-awareness and limits, and explain why it may matter. Insufficient evidence or something I already articulated is not a new discovery.

Possible continuation: Check the observation in another context; I can reject its premise or correct it.

## Values and tradeoffs

### What am I protecting?

`values-tradeoff` · Current situation or concrete example · Reflect / Challenge

> For this choice, identify what I explicitly care about and the possible tradeoffs. Separate my words from your interpretation and let me revise it.

Possible continuation: Compare a small reversible choice.

### What would be enough?

`values-enough` · Current situation or concrete example · Challenge

> Help me specify what would be good enough here. Check whether that standard serves my actual goal or an unexamined demand.

Possible continuation: Offer a stopping condition I can accept or reject.

### Choices that look contradictory

`values-context` · Accessible history within a chosen scope · Reflect / Challenge

> Compare two choices that appear inconsistent and their contexts and constraints. Consider reasonable differences before claiming a contradiction.

Possible continuation: Let me explain which condition mattered most then.

### Quick relief or a larger long-term effect?

`values-happiness-changes` · Accessible history within a chosen scope · Reflect / Expand

> Using accessible recent and longer-term material, propose one change that might improve daily experience relatively soon and one that might have a larger long-term effect. Explain evidence, constraints, counterexamples and unknowns. Without comparative outcomes, do not claim these are the fastest or largest improvements or present recommendations as proven causes.

Possible continuation: If I want, choose a small reversible trial; do not assign a plan automatically.

### What matters most now?

`values-priority-now` · Accessible history within a chosen scope · Reflect / Challenge

> Using accessible history, consider recent actual actions, confirmed constraints, choices and what I explicitly care about. Suggest one or two things that may deserve attention now. State source dates, evidence, alternatives and limits; do not rank by chat frequency or treat your suggestion as my decision.

Possible continuation: Let me confirm the priority or add a recently changed condition.

## Strengths and self-understanding

### Strengths with evidence

`strengths-evidence` · Accessible history within a chosen scope · Reflect

> Identify one strength supported by concrete behavior in recent conversations and explain its scope. Do not compare me with an imagined average user.

Possible continuation: Check where that strength may not apply.

### Turn a label into a situation

`strengths-label` · Current situation or concrete example · Reflect / Challenge

> Is this label I use for myself too broad? Help me rewrite it in terms of situations, behavior and conditions while retaining uncertainty.

Possible continuation: Let me confirm the more accurate wording.

### A different vantage point

`strengths-outsider` · Current situation or concrete example · Reflect / Expand

> Using only the event I provided, describe what a kind but candid observer might notice. Include other plausible explanations.

Possible continuation: Compare my account with observable behavior.

### Where I may misunderstand myself

`strengths-self-discrepancy` · Accessible history within a chosen scope · Reflect / Challenge

> From accessible history, compare one self-description with my reported choices or behavior. Check my wording, context, supporting evidence, counterexamples and later corrections before judging whether an unexplained discrepancy exists. Do not manufacture a contradiction or turn a discrepancy into a trait or motive.

Possible continuation: Let me add context or explain why the two are compatible.

## Interests and possibilities

### A bridge to another field

`possibilities-bridge` · Current situation or concrete example · Expand

> Connect my current concern to a somewhat distant but useful concept or practice. Explain the bridge without assuming I have never encountered it.

Possible continuation: Try the perspective on a small example.

### Try a small possibility

`possibilities-experiment` · Current situation or concrete example · Expand / Challenge

> Suggest a few reversible experiences around this interest and what each might help me learn. Do not turn one experiment into a verdict about my life direction.

Possible continuation: Let me choose the question I most want to answer.

### A question worth asking

`possibilities-question` · No history needed · Challenge / Expand

> Offer a question that may be worth thinking about. Let me reject its premise, do not assume I have a problem, and start lightly.

Possible continuation: Adapt to my answer without turning it into an interrogation.

## Play and metaphor

### A gentle roast

`play-gentle-roast` · Current situation or concrete example · Reflect / Challenge

> Gently roast the way of working I just described. Respect excluded topics and invent no experiences. Briefly separate grounded observations from comedic exaggeration afterward.

Possible continuation: I can ask for lighter humor, correct a point or switch direction.

### A small exhibition of my recent interests

`play-exhibition` · Accessible history within a chosen scope · Reflect / Expand

> Imagine a small exhibition of the interests in my recent conversations. Choose symbolic exhibits, connect them to source material, and label creative additions.

Possible continuation: Let me revise which exhibits represent me now.

### A curious interview

`play-interview` · No history needed · Reflect / Expand

> Interview me curiously, one question at a time, starting with an everyday choice. Follow my answers without pretending to know my life story.

Possible continuation: Stop whenever I want, without forcing a personality conclusion.

### If these were the only traces

`play-only-traces` · Accessible history within a chosen scope · Reflect / Expand

> Imagine that these selected conversations are the only traces of a person, and introduce them to someone who has never met them. What would you say? State the actual material scope and distinguish supported observations, possible interpretations and what the records cannot tell you. Use third-person distance without inventing a life story or personality diagnosis; do not add a death framing by default.

Possible continuation: Let me say what fits, is missing or is wrong; use a more dramatic framing only if I request it.
