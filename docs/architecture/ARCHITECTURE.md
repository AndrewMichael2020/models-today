# Architecture: deterministic boundaries for agentic publishing

This companion defines the publishing harness: typed candidates, bounded orchestration, host registries, MCP adapters, AST compilation, geometry checks, and controlled release. The contract source and synthetic tests provide the starting implementation.

## Writing model and autonomy

The architecture assigns editorial writing to a GPT-6-family model. Exact model selection follows harness completion. Record the actual model ID, provider, generation settings, and observation date in each run. The inference gate must approve the editorial fields that leave the machine. Local-only mode requires a separately evaluated local writer. Autonomous operation is conditional on completed gates, recorded evaluations, and the approved operating policy.

## 1. The typed contract

![Sheet 01: The Typed Contract](../../assets/eng_01_typed_contract.png)

The [Pydantic source](../../src/contracts/publication_candidate.py) defines all seven fields shown in Sheet 01:

| Field | Responsibility |
|---|---|
| `schema_version` | Only `1.0` is accepted |
| `run_id` | Identifies the producing execution |
| `subject_release_id` | Binds the candidate and its claims to one release |
| `model_parameters` | Records worker identity and generation settings |
| `evidence` | Carries source IDs and snapshot hashes |
| `claims` | Connects assertions, confidence, release identity, and evidence |
| `content_ast` | Orders typed publication blocks |

All nested objects inherit strict validation and forbid additional fields. IDs and strings have length bounds; evidence and claims are capped at 64 each, blocks at 128, evidence references per claim at 16, and claim references per block at 32. Numeric confidence and temperature must be finite and within their declared ranges. Image blocks require asset revisions; their text is alt text.

The implementation rejects duplicate IDs, mismatched release identities, and unresolved claim/evidence references. Its flat content AST has six node kinds: heading, paragraph, callout, product sidebar, ledger row, and image. Structured product metadata, ledger cells, nested layout nodes, and trusted component mappings are extension points.

### Hashes and host checks

`candidate_sha256` revalidates the current payload and hashes UTF-8 JSON with sorted keys, compact separators, preserved Unicode, and no non-finite numbers. List order is significant. The digest includes `run_id` and model settings: it identifies an exact candidate revision, not equivalent prose across separate runs. This is a documented Python encoding, not a claim of universal cross-language canonical JSON.

Evidence snapshot hashes identify stored source bytes. The host observation registry must compare both source identity and digest, confirm the subject release, and resolve asset revisions against an approval registry. Shape validation alone cannot detect a fabricated observation, establish that evidence supports a claim, or approve a product image. Model confidence is metadata only.

Approval must be an independently stored host record over the exact candidate, asset and template revisions, and gate report. Never infer approval from a field written by a worker. Revalidate serialized candidates at every boundary; model objects and their nested lists are not immutable authorization tokens.

## 2. Runtime sequence

![Sheet 02: Runtime Sequence](../../assets/eng_02_runtime_sequence.png)

The state sequence is:

```text
Raw Source → MCP Fetch → Extraction → Typed Candidate
           → Gate Engine → AST Compiler → DOM Verification → Release
```

The coordinator creates a durable run record with an event key, policy revision, absolute deadline, and budget reservations. Source observations are stored before workers consume them. Bounded research and composition workers return checked handoffs. Accepted content moves through validation and preview; exact-revision approval precedes release intent.

| Limit | Required enforcement |
|---|---|
| 180 s run deadline | Monotonic deadline checked before and during every stage; cancel pending work |
| 3 total model calls | Atomic reservation before dispatch, including repair calls |
| 1 format repair | Repair consumes both the call allowance and remaining deadline |
| 10 s source attempt, 1 retry | At most 2 read attempts; retain timeout evidence |
| 4,000 input / 1,200 output tokens per call | Count complete input with provider tokenizer; constrain output and account for usage |
| 12,000 input / 3,600 output total | Arithmetic ceiling, not measured consumption or a cost estimate |

These limits describe a bounded small text-update run. They do not cover image synthesis or experimental workloads; those require separate explicit envelopes. Hidden provider retries must count toward policy or be disabled. A missing usage report cannot silently free reserved capacity.

Malformed output is eligible for one format repair. Unsupported claims enter review; missing sources enter hold. Exhausted budgets and deadline expiry terminate generation. Persist partial results and reasons without promoting a failed candidate. A later resumed execution must retain its relationship to the original event and obey a separately authorized budget.

### Release and recovery

Persist approved revision plus release intent before sending an export. Use a stable event key and durable uniqueness constraint for idempotent release. On an uncertain network outcome, reconcile with the publication destination before retrying; do not create a second logical publication. Approval and event identity solve different problems: revision digests protect content integrity, while event keys prevent duplicates.

Release, rollback, interrupted-run recovery, and clean restore need fixtures against the actual implementation. These fixtures belong to the coordinator and release service.

## 3. Quality gates and the AST compiler

![Sheet 03: Quality Gates Matrix](../../assets/eng_03_quality_gates.png)

> Deterministic gates block release. Model judges advise; editors assess meaning and quality. No average cancels a failed critical gate.

| Gate | Mechanism and failure outcome |
|---|---|
| Contract | Schema and internal references; reject, with at most one format repair |
| Grounding | Source comparison and accountable review of each material claim; hold or rewrite |
| AST verification | Allowlisted typed nodes and resolved references; reject executable or dangling nodes |
| DOM geometry checks | Bounding boxes, overflow and clipping checks plus visual review; fix and rerender |
| Access and budget | Host permissions, approval, and reservations; deny or hold |
| Fidelity and voice | Approved assets and independent rubric dimensions; revise and review |
| Idempotency and recovery | Duplicate and restore fixtures; block release or restore |

Grounding and editorial meaning require accountable judgment. Deterministic checks enforce their recorded prerequisites but do not turn semantic assessment into a proof. The release voice threshold is at least 4/5 on each rubric dimension, with editor acceptance during the pilot.

The compiler must map accepted node kinds to fixed components. The trusted template owns column dimensions, type scale, spacing, and responsive breakpoints. Content enters escaped text slots; asset IDs resolve to approved local resources. Workers supply no arbitrary CSS, raw executable HTML, scripts, or fetch instructions.

For the two-column editorial layout, the template reserves a narrative region and a product rail. Callouts occupy explicit slots; ledger rows follow one consistent column specification. If content exceeds a slot, reject or recompose within the run envelope. Do not silently shrink essential text or hide overflow to manufacture a passing screenshot.

Measure rendered geometry after fonts and images settle at 360, 768, and 1440 CSS-pixel widths. Apply the sheet’s 1 CSS px rounding tolerance, and explicitly identify allowed scroll regions and intentional overlays. Inspect essential text, reading order, missing assets, and long-content fixtures. A DOM test does not replace visual/editorial review or prove print readiness.

Replay requires stored accepted inputs and pinned schemas, templates, assets, fonts, and browser dependencies. Record viewport and screenshot comparison tolerance. A fresh model invocation is a new live run, not a deterministic replay.

## 4. Trust boundaries and sovereign isolation

![Sheet 04: Trust Boundaries](../../assets/eng_04_trust_boundaries.png)

| Zone | Authority and data |
|---|---|
| Local coordinator | Owns policy, budgets, approval lookup, and state transitions |
| Local model workers | Receive scoped inference context; no publication credentials |
| Private run store | Retains observations, provenance, revisions, and gate records |
| Trusted renderer | Uses approved templates and asset revisions |
| Source fetch gate | Enforces destination allowlists, redirect policy, size limits, and quarantine |
| External inference gate | Selects approved fields and destinations; records transfers |
| Release service | Verifies exact revision and export policy; alone holds publication authority |
| Public website | Receives only the reviewed export package |

Model workers cannot publish because generating candidate content must not confer authority over credentials or release state. Enforce this with process/tool permissions and secret scoping. Prompt instructions and MCP annotations do not enforce access control.

Treat retrieved content as untrusted, including instructions embedded in source pages. Validate redirect destinations and network targets before fetching; keep imported text separate from host policy. Require explicit field selection before an inference request leaves the local boundary. Public export must exclude private observations, credentials, internal logs, and unpublished drafts.

Offline mode disables every network crossing and uses staged evidence plus local weights. Connected mode selectively enables source retrieval, optional inference APIs, and approved exports. Claims of sovereign isolation or zero egress require runtime network-denial tests and retained evidence. 

## 5. Evidence needed for the autonomous case study

Each claimed compiled spread must link to its input payload, source and asset revisions, coordinator trace, compiler revision, gate outcomes, browser environment, rendered DOM, screenshot, and intervention record. A zero-manual-adjustment claim requires that record to show no per-edition CSS/HTML edits. Print claims need export-specific checks in addition to browser geometry.

The first vertical slice must demonstrate one accepted publication preview, one malformed handoff, one unsupported claim, one forced timeout, and duplicate-release recovery before expanding autonomy.
