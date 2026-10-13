# Submission preparation: reflection-companion

[中文](SUBMISSION.zh-CN.md)

This is a review candidate, version 0.5.11-distribution.3, on `codex/distribution-prep-20261013`. Existing Releases and Tags are unchanged. The maintainer must review this branch before publishing it. Generated public source projects must reconcile changes with their canonical source before the next Release; published inventory hashes are deliberately not rewritten here.

## OpenAI

The complete ZIP includes portable, Codex and Claude manifests, square icons, three prompts, dependency and privacy documentation. Product scope is declared in `skills/*/agents/openai.yaml`.

The conversation entry is scoped to CHAT and CODEX. Codex source-notes preview and an authenticated Claude counterexample task pass. History retrieval remains intact and requires user-scoped sources and host capabilities. ChatGPT/Work native execution, cloud saving and scheduling are NOT VERIFIED.

Developer identity and write access must be verified in the submitting account. Use https://platform.openai.com/plugins → upload new plugin → skills-only ZIP, inspect conversion and automatic findings, then fix blocking findings. Current draft and scan results are recorded separately in the task handoff; local package validation alone does not establish them. Formal submission and binding attestations require the account holder's authorization.

## Claude

Source: `zhenglimindesign-ing/reflection-companion`; path: `directory-plugins/reflection-companion`; branch: `codex/distribution-prep-20261013`. Use https://claude.ai/directory/manage → Submit new → Plugin bundle → Validate. Push access is verified; the final task handoff records whether portal validation and a saved draft actually succeeded. Local Claude installation/discovery and the bounded authenticated tasks pass; directory runtime is NOT VERIFIED.

The manifest points to [the branch privacy document](https://github.com/zhenglimindesign-ing/reflection-companion/blob/codex/distribution-prep-20261013/directory-plugins/reflection-companion/PRIVACY.md). Policy consultation is handled separately; no core feature was removed for presumed policy compliance. Do not infer official policy approval from validation. Review contact, intended age audience, binding compliance acknowledgments and formal submission remain account-holder decisions. No formal review or publication is authorized in this preparation task.

## skills.sh

Repository discovery, complete copies and fresh-session loading already passed with telemetry disabled. The paired public README documents the verified command. Default-branch installs use the currently published source; these proposed docs and instruction fixes become default only after maintainer review. Keyword/search indexing is separate and NOT VERIFIED; no ranking feature or install telemetry was added.
