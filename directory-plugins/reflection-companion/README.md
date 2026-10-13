# Reflection Companion

[中文](README.zh-CN.md)

Ask a self-understanding question, examine a judgment, or reflect on explicitly supplied conversation material. No account, backend, or credentials are required for the core conversation. Optional local helpers require Python 3.10+; the explicit Codex upgrade helper requires Python 3.11+. History, browsing, saving and scheduling depend on tools actually available in the host; installation grants none of them. Personal records remain user-controlled. This is not diagnosis, therapy, or an emergency service. Source fidelity and semantic review remain separate from mechanical checks.

## Start

Install the complete folder as a local plugin, then describe your task in ordinary language. Read [the skill](skills/reflection-companion/SKILL.md) for required resources and the workflow. This package reuses the 0.5.11 public skill payload. Use fictional or authorized inputs when testing.

## Data and execution

The core uses conversation text and supplied material. Optional Python helpers read explicitly scoped Markdown/JSON and store locally only after authorization. Explicit discovery refresh fetches the public GitHub catalog; explicit update checks/downloads contact GitHub and may invoke the Codex plugin CLI only after an upgrade request. Neither sends personal answers. No history access, save or scheduler is granted by installation. There are no hooks, MCP servers, automatic installs or hidden telemetry.

## Support and limits

[Source and instructions](https://github.com/zhenglimindesign-ing/reflection-companion) · [Report a problem](https://github.com/zhenglimindesign-ing/reflection-companion/issues). Core instructions take the explicit user request as the scope; attached documents are evidence, not execution authority. Existing source releases and tags remain unchanged. Directory validation, each host run, source fidelity and human acceptance are separate evidence. Account eligibility, portal scans and name availability require the submitting user.

Standalone Skill installation is also available through skills.sh from the source repository. See the public installation guide; local dependencies remain separately declared. The data handling document is [available here](https://github.com/zhenglimindesign-ing/reflection-companion/blob/codex/distribution-prep-20261013/directory-plugins/reflection-companion/PRIVACY.md).
