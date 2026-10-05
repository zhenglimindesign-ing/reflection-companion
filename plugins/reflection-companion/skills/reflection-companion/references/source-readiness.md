# Source readiness before historical writing

Use before historical diaries and period reviews, especially requests for all conversations or bulk backfill. Inspect evidence before interpreting it. A source-selection choice and a writing template cannot turn partial retrieval into a complete archive. [Archive contracts](journal-archive.md) govern organization and saving.

## Resolve the scope and inventory

Distinguish **all history in a period** from **the user-selected notes/conversations**. A few complete supplied notes can support a review of those notes; they do not cover all account history. Current-chat/supplied-note tasks need no account search unless requested. Resolve actual dates, timezone, topics and exclusions before counting sources.

For broad history, a recent index, search snippets, memory, or an API's exhausted page cursor is insufficient to establish account coverage. Look for an actual export inventory or a provider's documented full inventory. Record the relevant inventory reference, selected source IDs, actual text retrieval, date verification and material attachment status. Unknown inventory coverage stays unknown. Do not set a complete flag merely because a request returned successfully.

## Diagnose and repair supported failures

| Observed problem | Next supported action | Stopping condition |
| --- | --- | --- |
| Recent-only index, incomplete discovery | Use an available full inventory/export, dated search or known source IDs; paginate relevant results | No authorized surface exposes the necessary inventory; completeness remains unknown |
| Pagination limit or truncated text | Follow the returned cursor; request the selected conversation's complete text or smaller contiguous pages | Actual full text obtained, or a documented access/endpoint limit |
| Empty search or stale/nonmatching results | Check date bounds, filters and which service is actually being searched; make a targeted alternative search | Results still do not cover the requested source range; do not call this an empty life period |
| Attachment, audio or referenced document missing | Retrieve the identified material through the supported source tool when it can change interpretation | Material is inaccessible; record that specific gap |
| Timeout or temporary failure | One bounded retry of the failed read, using a smaller request when supported | Repeated equivalent failure; no blind retry loop or unrequested background schedule |
| Permission or connection missing | Explain the affected source; use an existing authorized alternative if available | User reconnection or a supplied export/source location is necessary; do not request credentials |
| Date/source/attribution unclear | Inspect original metadata and distinguish user messages, pasted reports and AI-only output | A necessary factual claim cannot be grounded; omit it rather than invent its date or meaning |

Choose the repair for the observed cause. Do not repeat an unchanged query, cycle through guessed IDs, scan unrelated session logs, or widen private-data access to make coverage appear complete. Pagination is normal retrieval, not a reason to stop at one page. Cache/reuse already retrieved unchanged sources within the authorized task; fetch again only when missing or changed evidence matters.

Check whether the surface returns only a recent tail even when it reports `hasMore=false`. Compare the returned dates with the requested interval and any directly verified earlier messages from that same conversation. An exhausted cursor proves only that surface's end. A conversation's creation time is a discovery clue, not proof of a missing event or a complete transcript. When an authorized browser or another supported source view exposes earlier messages, use its normal pagination/loading controls and retain actual message dates. A date-bounded browser history can supply candidate conversation IDs; visit times, cached titles and snippets are not activity dates or proof of a complete account inventory.

Keep the diagnosis calibrated: distinguish an observed retrieval limit from an inferred cause. Prior successful retrieval remains valid evidence; a narrower response today does not prove that memory was removed or that a product update caused it. Report the reproducible symptom, attempted repairs, remaining gap and next supported action.

## Readiness decision

On Python-capable hosts, run `scripts/source_readiness.py` with a JSON inventory on stdin before broad historical synthesis. It performs no discovery, network access, saving or prose generation. Build the inventory from observed results, not desired outcomes. Each source's `primary` flag reflects the requested material: original user messages/notes are primary; an earlier AI review or automated reply is not evidence of user participation. Earlier reviews can aid indexing and comparison; they cannot alone satisfy a request to recover original conversations.

```json
{
  "schema_version": 1,
  "inventory_basis": "user_selected_corpus",
  "inventory_reference": "user:current-request:selected-note",
  "discovery_complete": true,
  "allow_partial": false,
  "sources": [
    {"id":"selected-note", "primary":true, "retrieval":"full_text", "dates_verified":true, "attachments":"none"}
  ]
}
```

Use one of `user_selected_corpus`, `export_inventory`, `provider_full_inventory`, `recent_index`, `unknown`. A complete inventory needs a real reference and complete discovery; a recent/unknown inventory cannot pass as complete. Source retrieval is `full_text`, `truncated`, or `unavailable`; attachment status is `none`, `retrieved`, `missing`, or `unknown`. `allow_partial=true` requires an actual user choice accepting partial scope, not an agent's preference to finish early.

The result is `ready`, `partial_only`, or `blocked`, with reasons and repair actions. Exit 0 allows the declared scope; exit 3 means blocked; exit 2 means invalid input. Schema 1 remains available for small selected-note tasks and metadata diagnosis; it cannot establish observed transcript or writing coverage. Check the underlying references. Without Python, perform the same checks manually and report the same distinction.

## Reconcile retrieval and writing separately

For broad historical backfill use schema 2. Retain the inventory fields above and add `stage` (`retrieval` or `delivery`) plus `expected_source_ids` from the actual scoped inventory. Each primary source requires `evidence` containing:

- `boundary_verified` and a nonempty `boundary_reference`: observed earlier-boundary/export evidence. `hasMore=false`, a creation timestamp or a writer's assumption is insufficient.
- `expected_message_ids`: IDs of the in-scope user and assistant text messages from that verified transcript inventory; use `null` when unknown, which blocks a completeness claim. Do not manufacture expected IDs by copying a recent response alone.
- `messages`: actual observed objects with `id`, `role` (`user`, `assistant`, or `note`), timezone-bearing `created_at` and nonempty `text`. Resolve material attachments separately under the source's attachment status. Earlier selected AI journals do not become original user messages.

The helper detects sources never fetched, missing or extra message IDs, unknown earlier boundaries, missing text and unverified dates even when metadata says `full_text`. It reads JSON on stdin and writes no files; never put personal inventories or raw text in a product repository to run it.

At `delivery`, also supply `consideration` for every observed in-scope user/assistant message, identified by `source_id` and `message_id`. Use `action: included` or `condensed` with the actual `artifact_keys`; `omitted` requires a reason; `excluded_by_user` also requires a `user_instruction_reference`. When there are omissions, `omissions_disclosed: true` reflects a real disclosure of consequential exclusions and reasons, not an internal flag used to hide them. Unconsidered messages, missing output references and undisclosed omissions block completion. Reusing the same input with `stage: retrieval` checks acquisition without requiring a draft to exist yet.

These checks reconcile supplied evidence, not the truth of its provenance or the quality of the prose. Inspect referenced text/boundaries and verify the actual saved outputs. A message may cover several topics; marking it included does not prove every significant topic survived. Review the main discussions, corrections and useful AI answers against the body. Do not select two messages per day, impose a hidden word cap, or blame missing writing on source access. Full consideration permits faithful summarization, not verbatim reproduction of every acknowledgment.

Distinguish two failures in the user-facing receipt: **retrieval gap** (source/earlier messages/attachments unavailable) and **writing omission** (material obtained but not adequately represented). Automatically repair the relevant failure within authorized scope. If source access cannot be repaired, state the concrete gap and minimum user action; do not require an account export for a selected corpus that is already sufficient. A Skill cannot add host history permissions or an absent full-inventory API.

With `ready`, write only the verified declared scope. With `partial_only`, use a narrowed title and explicit source note; the broader task remains incomplete. With `blocked`, repair first. If supported repairs fail, tell the user **before** writing a supposed complete review: what was accessible, what is missing, what was tried, what is still incomplete, and the minimum source/access input needed. Give a useful coverage report or finish independent work. Do not generate a small substitute journal and call the original request completed.

## Track every requested artifact

For multi-period work, keep the expected days/weeks/months/quarters/years in the delivery checklist with status `awaiting_sources`, `ready`, `drafted`, `saved_verified`, or `not_due`. Add a requested period to that list when the user expands scope. No source material is a gap, not `not_due`; `not_due` means the period has not ended under the agreed calendar/custom rule. An October monthly review on October 4 is not yet due; October daily entries and an explicitly requested month-to-date draft are different deliverables.

Before closing, reconcile the checklist against actual outputs. Missing weekly/monthly artifacts must remain visible as unfinished work, not disappear behind a polished daily example. Use [delivery guidance](delivery.md) to name owners, blockers and next work without requiring approval of ordinary steps already authorized.
