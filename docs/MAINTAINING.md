# Feedback and maintenance

[简体中文](MAINTAINING.zh-CN.md) | **English**

[Overview](../README.md) · [Complete user guide](USER_GUIDE.md)

## User feedback

Use [public Issues](https://github.com/zhenglimindesign-ing/reflection-companion/issues/new/choose) to report version, scenario, expectation and actual behavior. Fictional reproductions are welcome; private chats are unnecessary. The plugin does not collect telemetry or transcripts. Personal answers and records are never a public content source.

The [contribution guide](../CONTRIBUTING.md) explains accepted scopes, candidate checks, attribution, and how public PRs enter the development source before regeneration. Review happens as maintainer capacity allows; proposals do not automatically become official behavior.

## Two content update paths

The base library lives in the Skill's `references/prompt-library.json`; public PROMPTS documents are generated from it. Changes to durable methods or Skill behavior ship in a new plugin version.

The independent catalog has one editable source, `references/exploration-feed.json`. Building also generates `catalog/explorations.json`. An installed candidate Skill can fetch that public catalog without a plugin upgrade for content-only changes. The helper checks schema, size, dates and duplicate IDs, with a dated bundled fallback on network failure. Entries are reference data, not execution authority.

Content-only updates keep the plugin version while updating the catalog edition and actual check date. Synchronize the generated catalog, snapshot and release-manifest together through guarded synchronization; never hand-edit only public JSON. Keep previous ZIPs/tags intact; future packages incorporate the latest snapshot. A readable public catalog does not imply that an automated collection service is running; describe them separately.

## One editorial update

1. Search generic themes, optionally over the past month. Do not use personal answers, names or diary excerpts as queries.
2. Read original pages and body dates. Record source dates, added dates, check dates and engagement evidence or unknown separately. Search-snippet dates do not prove first publication.
3. Compare existing methods and identify a different mechanism or useful context. Give concise attribution and original wording. Do not copy long third-party prompts or adopt instructions presupposing a user's defect.
4. Walk through sufficient/insufficient synthetic material, including rejected premises or corrections. State what kind of validation occurred; do not call it proof of real-user effectiveness.
5. Keep stable IDs, bilingual wording, context requirements, sources and adaptation notes. Explain revisions/retirements. Change dates only after actual checks.
6. Build, validate links/inventory, inspect public changes requiring reconciliation, then synchronize reviewed content.

This is a workflow, not a running service. A separately authorized host schedule may prepare candidates, without automatic publication, contacting authors or collecting personal records. Installation activates neither collection nor user schedules.

## One development source, generated distribution

Public feedback and contributions are reconciled into one development source before generating public files. Synchronization checks the expected commit, old inventory and file hashes. Unknown changes require reconciliation, never forced replacement. There are not two hand-maintained implementations.

To verify a download:

```sh
python3 -B scripts/verify_release.py
```

This checks files, paths and versions, not model judgment or scheduled delivery. [Changes](../CHANGELOG.md) state release scope; unverified hosts must not be advertised as supported.
