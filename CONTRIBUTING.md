# Contributing to Reflection Companion

[简体中文](CONTRIBUTING.zh-CN.md) | **English**

[Overview](README.md) · [Maintenance](docs/MAINTAINING.md) · [Open contribution tasks](https://github.com/zhenglimindesign-ing/reflection-companion/issues?q=is%3Aissue%20is%3Aopen%20label%3A%22help%20wanted%22)

Reflection Companion welcomes focused contributions. The maintainer reviews proposals and decides what enters the official version. This is a small public Alpha; review happens as capacity allows, without a guaranteed response or release date.

## What to contribute

- Documentation corrections, clearer installation instructions, and English / Simplified Chinese translation fixes.
- Fictional reproductions of misleading interpretations, unsupported claims, repeated questions, or failures to honor corrections.
- Installation and use reports on an existing documented host, with the actual Skill version, app / model version when available, steps, and observed result.

For template, exploration-method, prompt, or helper changes, open an Issue to discuss the proposed behavior before doing substantial work. Product direction, psychological interpretation boundaries, saving / scheduling permissions, new dependencies or hosts, and release decisions need maintainer agreement. A contribution does not grant repository access or release authority.

## Report a problem

Use [the feedback form](https://github.com/zhenglimindesign-ing/reflection-companion/issues/new?template=feedback.yml). Include the version and host, the situation, what you expected, what happened, and the smallest useful reproduction. For interpretation problems, explain which claim lacks support or which user correction was missed. A correction is useful even when you cannot reproduce a model's exact wording.

Issues and PRs are public. Use fictional material; do not upload private chats, diaries, personal records, credentials, or identifiable third-party information. Describe unavailable evidence as unavailable. Do not turn a synthetic example into a user testimonial.

A blocked installation is useful evidence too: identify the last step reached, the exact version and route, and any command output you can safely share. Say when logs or a first invocation are unavailable. Maintainer reproductions are recorded separately from contributor reports; a documentation correction does not turn a blocked attempt into a successful host check.

## Submit a focused PR

1. Read the relevant guide and existing Issues. Choose an unclaimed task labeled `good first issue` or `help wanted`, or open an Issue for your proposal. Mention the Issue when starting so work can be coordinated.
2. Fork this public repository and create a branch for one change. Before editing, optionally verify the clean download with `python3 -B scripts/verify_release.py`. Report if you could not run a check.
3. Edit the relevant public file. For bilingual documentation, update both editions when possible; otherwise state exactly which translation needs maintainer help. For behavior changes, include fictional input, expected behavior, actual output, and the affected host / version.
4. Open a PR using the provided template. Explain the problem, changed behavior or wording, and checks actually performed. A documentation-only fix can use a focused diff and link review; it does not need a model run. For behavior changes, show before / after results and check relevant cases such as insufficient material or a user correction.

The public repository is generated from one development source. PRs are proposals against the public files; contributors do not need access to that development source or its internal test suite.

| Public file | How to contribute |
| --- | --- |
| READMEs, guides, contribution documents, or files under `plugins/reflection-companion/` | Propose a focused edit; the maintainer transfers accepted changes to the source. |
| `docs/PROMPTS.md` / `docs/PROMPTS.zh-CN.md` | Change the Skill's `references/prompt-library.json`; these documents are generated from it. |
| `catalog/explorations.json` | Propose content in the Skill's `references/exploration-feed.json`; the catalog is generated from that source. |
| `release-manifest.json`, package archives, version fields, generated marketplace metadata, or checksums | Leave regeneration and release changes to the maintainer. |

The release verifier checks the original inventory and hashes. Edited candidates can fail that integrity check until the maintainer regenerates the distribution; this alone does not invalidate a proposed edit. Do not update hashes by hand to make the candidate pass. State the validation you performed and any remaining gaps.

## Review, credit, and release

The maintainer checks the proposal, requests changes if needed, and transfers accepted edits to the development source with the public PR reference and contributor attribution. Contributor authorship is retained where possible; when integration needs rewriting, credit can be recorded with the GitHub username and PR link without asking for a personal email.

Accepted source changes are checked and regenerated before the official public files are updated. A PR may be integrated through a regenerated commit rather than a direct merge of its branch. The PR records the outcome and resulting public commit. Installation packages and versioned release assets change only through a separate release; existing tags and archives retain their original contents.

Package integrity proves file consistency. Model output checks establish behavior in the tested case. Neither establishes another person's value judgment or general host support.

Contributions to the distributed project use its [MIT license](LICENSE). Identify the source and applicable license of any third-party material; use your own wording and keep private or unlicensed material out of the contribution.
