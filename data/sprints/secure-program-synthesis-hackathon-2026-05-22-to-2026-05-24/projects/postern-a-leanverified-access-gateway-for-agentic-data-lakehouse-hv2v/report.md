Postern: a Lean-verified access gateway for agentic data lakehouses 

Secure Program Synthesis Hackathon 2026 — Track 3 research artifact 

Vincent, FractalBox 

### **Abstract** 

We address access control for data lakehouses queried by LLM agents. An agent’s effective rights are context-driven — which principal it acts for, which task it is invoked under, which scope the caller granted — and the static _identity →role →permission_ chain of RBAC cannot encode any of those axes. Per-engine row- and column-level security does not survive the ETL boundary; physical tenant segregation forfeits the cross-source joins that motivate the lakehouse. We propose plan-level rewriting against a **Biscuit-Datalog** policy (Clever Cloud and contributors 2024) and present **Postern** , an artifact in three parts: (i) a rewriter rewrite ∶ _Catalog_ → _Policy_ → _Principal_ → _Plan_ → _Option Plan_ mechanised in Lean~4 (Moura and Ullrich 2021), inspired by Cedar’s Lean authorization core (Cutler et al. 2024) but stated over plan-level outputs rather than per-request decisions, with nine `sorry` -free theorems (axioms bounded by `propext` and `Quot.sound` ) plus a partly-mechanised Horn-fragment Datalog evaluator; (ii) a Rust capability-tracking layer inspired by Odersky et al. (Odersky et al. 2026) — invariant brand lifetimes, sealed types, opaque-receipt sinks; and (iii) a reference-conformance harness binding Rust to the Lean reference on 18 cases. We evaluate on the Kaggle `transactions-fraud-datasets` schema and identify Biscuit attenuation, audience, expiry, key rotation, cross-relation joins, and differentially-private aggregation as the principal open problems. 

# **Introduction** 

Production agentic systems increasingly read context from data-lakehouse stores at inference time, compacting heterogeneous sources into engine-agnostic columnar formats — Apache Arrow Parquet on S3-class object storage — queried by in-process engines such as DuckDB (Raasveldt and Mühleisen 2019), often colocated with on-prem or edge runtimes hosting local models. The access-control consequence is sharp: the entity issuing queries is no longer a human analyst on a stable role but an LLM agent mediated by tool-call protocols such as the 

1 

Model Context Protocol (Anthropic 2024). Agent access is short-term, contextual, and task-oriented; role-based access control — and its temporally-scoped variant TRBAC — does not fit. Two existing responses each concede something. Per-engine row- and column-level security (PostgreSQL Global Development Group 2024) does not survive ETL into an engine-agnostic Parquet store, forcing per-source policy duplication that scales poorly with source count and churn. Physical tenant segregation across object-storage prefixes queried by disjoint engines restores safety but forfeits the cross-source joins that motivate the lakehouse in the first place. Neither addresses the deeper mismatch: an agent’s effective permissions depend on the principal it acts for, the task it is invoked under, and the calling context — none of which the static _identity →role →permission_ chain of RBAC encodes. The same agent code called by two principals, or invoked by one principal under two tasks, may legitimately need two different views. We propose plan-level rewriting against a column-grant policy as a third point in this design space, gated under the agent’s task-scoped identity at query time. **Postern** , the artifact we present, has three components: a Lean~4-mechanised plan rewriter, a Rust capability-tracking layer constraining the agent’s downstream computation, and a reference-conformance harness binding the two. 

## **Contributions** 

1. A Plan IR ( _Scan_ / _Project_ / _Filter_ ), a Biscuit-Datalog policy language (Horn-fragment with ground `right(p, r, c)` facts compiled from the surface column-grant syntax), and a rewriter, mechanised in Lean~4 (Moura and Ullrich 2021). The rewriter is inspired by Cedar’s Leanmechanised authorization core (Cutler et al. 2024); we transpose the technique from per-request _authorize_ decisions to plan-level outputs over an IR, and so prove soundness of a _transformation_ rather than a classification. The rewriter side comprises nine `sorry` -free theorems: output-column soundness, filter-predicate soundness, schema subset, idempotence under repeated application, monotonicity in the policy, two no-new-column lemmas, and explicit-refusal lemmas for unknown relations and for filter predicates over forbidden columns (§4). The Datalog evaluator ( `verifier/lean/Datalog.lean` ) contributes a further `eval_monotone` theorem (proved modulo one isolated combinatorial obligation, `herbrandBound_mono` ) plus four `sorry` -free specialisation lemmas covering the rule-free regime that all our scenarios use today. Two further evaluator meta-theorems — `eval_sound` and `eval_terminates` — are stated with `sorryAx` obligations named explicitly in `CheckAxioms.lean` . Axiom dependencies for proved declarations are bounded by `propext` and `Quot.sound` ; two rewriter theorems depend on none. 

2. A Rust capability-tracking layer ( `postern-guardrail` ) implementing three composable mechanisms: sealed `Cap<'sc, C>` tokens whose construction is private to the crate, an invariant brand lifetime `'sc` 

2 

enforced by `PhantomData<fn(&'sc ()) -> &'sc ()>` and gated by a universally-quantified scope combinator, and opaque-receipt sinks that consume both the `Cap` and the carrier `Tagged` without exposing the underlying value. Three lexical bypass attempts (forging `Cap` , projecting `Tagged::value` , escaping the brand) are pinned as `compile_fail` doctests. The agent-facing surface is `no_std` -compatible (§3). 

3. A Rust implementation of the rewriter ( `postern-core` ) structurally mirroring the Lean reference, and a reference-conformance harness ( `postern-diff` ) that asserts byte-equivalence between the Rust output and the Lean reference on a corpus of 18 hand-curated cases (15 accept, 3 refusal). The gateway’s Datalog evaluation surface is designed around `biscuit-auth` ’s public `biscuit_auth::datalog::World` evaluator (Clever Cloud and contributors 2024); the in-tree `postern-core` migration to that backend is in progress, with the column-grant DSL serving as the byte-equivalent stand-in until the migration lands. We label the procedure _reference-conformance testing_ rather than QuickCheckstyle differential testing, reserving the latter term for property-based generation; the latter is among the open problems of §6. 

4. A case study over the Kaggle `transactions-fraud-datasets` schema, with three principals (CRM, Card Operations, Fraud Risk) exercising PII redaction, cross-departmental refusal, and minimum-necessary disclosure (§5). Each row of the evaluation table corresponds to a corpus case driving the conformance harness. 

# **Plan IR** 

We state the IR before the threat model so §2 may reference its operators directly. Plans are single-relation expressions built from three constructors: 

_Plan_ ∶∶= _Scan_ (𝑟) ∣ _Project_ ( _Plan_ , _cs_ ) ∣ _Filter_ ( _Plan_ , 𝑐) 

where 𝑟∈ _Relation_ , 𝑐∈ _Column_ , and _cs_ ∈ _List Column_ . We write 𝜎(𝑞) for the output schema of plan 𝑞 under a catalog _cat_ , defined inductively: 𝜎( _Scan_ (𝑟)) = _cat_ (𝑟); 𝜎( _Project_ (𝑝, _cs_ )) = 𝜎(𝑝) ∩ _cs_ ; 𝜎( _Filter_ (𝑝, 𝑐)) = 𝜎(𝑝). The asymmetry between _Project_ (which alters the output schema) and _Filter_ (which does not, despite reading 𝑐) is the source of the _filter side-channel_ discussed in §2. 

# **Threat model** 

The trusted computing base (TCB) consists of the gateway process itself, the catalog _cat_ that it consults, the plan-to-executor lowering step that hands the rewritten plan to DuckDB, the principal extraction step that maps a verified capability token to a _Principal_ string, and the DuckDB + Parquet store. All other parties are untrusted. 

3 

|Component|Trus|t Justification|
|---|---|---|
|LLM / agent planner|×|Susceptible to direct and indirect prompt<br>injection.|
|Agent-generated code|×|Composes upstream-tainted context with<br>downstream effects.|
|Capability tokens (Clever<br>Cloud and contributors<br>2024)|~|Trust contingent on the gateway’s<br>signature verification.|
|Gateway process|✓|Hosts the Lean-verified rewriter and the<br>policy.|
|Catalog (𝑟↦columns)|✓|Assumed bound to the physical Parquet<br>schema (§6).|
|Plan-to-executor lowering|✓|The rewritten plan is assumed honoured<br>literally by DuckDB.|
|Principal-string extraction|✓|A bug in token verification invalidates<br>every theorem of §4.|
|DuckDB + Parquet store|✓|Standard storage-engine assumptions<br>apply.|



The attacks within scope of the formal model are: (i) over- projection of forbidden columns; (ii) filter on a forbidden column (the side-channel addressed by `rewrite_filter_sound` ); (iii) scan of a relation absent from the catalog (addressed by `rewrite_refuses_unknown` ); (iv) cross-departmental reach by a principal lacking matching grants; and (v) unknown principals, which we treat fail-closed via the empty-allow convention. 

The following are deliberately out of scope and discussed in §6: aggregation and inference attacks; covert channels through latency or row-count observation; multi-relation joins; biscuit attenuation modelled inside the Lean proof; policy synthesis from natural language; and the planner-to-executor lowering step. 

# **Design** 

Postern compiles a single policy artifact to plan-level enforcement. 

## **Policy** 

A policy is a list of **column-grants** ⟨𝑝, 𝑟, 𝐶⟩: “principal 𝑝 may read columns 𝐶 on relation 𝑟”. Multiple grants for the same (𝑝, 𝑟) flat-union. Anything outside the union is denied — fail-closed. **No deny-lists** : the policy language is deliberately monotone grant-only, which makes policy review additive (a new grant can only widen). Deny-lists and attribute-based predicates are §6. 

A concrete policy from the financial-institution scenario of §5, in Postern’s surface syntax: 

4 



<!-- Start of picture text -->
TCB<br>MCP plan + biscuit Postern gateway verify biscuit verifier principal<br>policy Lean-extracted rewriter Option Plan<br>LLM agent<br>DuckDB / Polars<br>catalog<br><!-- End of picture text -->

Figure 1: Postern architecture: the agent submits an MCP plan with a biscuit token; the gateway verifies the token, extracts the principal, and applies the Lean-extracted rewriter against the policy and catalog before lowering the rewritten plan to DuckDB/Polars. The dashed box marks the trusted computing base of §2. 

5 

```
grantCRMonusers_data{id,name,region,age}
grantCardOpsoncards_data{card_id,card_type,limit,activated}
grantFraudRiskontransactions_data{txn_id,card_id,amount,merchant,timestamp}
grantFraudRiskonusers_data{id,region}
```

Anything outside these grants is implicitly denied; `users_data.ssn` , `users_data.email` , and `cards_data.card_number` are never released regardless of which principal queries. The rewriter projects each plan’s output schema down to the grant union under the querying principal and refuses plans whose filter predicates touch columns outside that union (§4). 

## **Rewriter** 

`rewrite cat P prin q := if cat q.touched = [] then none -- unknown relation else if ¬ q.filterCols` ⊆ `allow then none -- forbidden filter col else` 

`some (Project q (q.schema cat` ∩ `allow)) where allow := P.allowed prin q.touched` 

Post-hoc projection is the simplest algorithm that admits a clean soundness proof. Predicate-pushdown variants can be verified against this rewriter as a reference; we leave that to future work. 

## **Capability-bounded data flow** 

The rewriter of §3 (Layer 1) constrains what data reaches the agent. A separate layer (henceforth _Layer 2_ ) constrains what the agent’s code may do with the values released. Odersky et al. (Odersky et al. 2026) propose Scala 3 capturechecking as a type-level mechanism for this purpose: capabilities are first-class program variables, and the compiler tracks each function’s _capture set_ — the capabilities it may use — so that agent-generated code cannot perform an effect for which it does not hold a capability. Rust has no capture-checking. We mechanise a weaker analog by composing three pure-Rust constructions, each closing one face of the gap. 

**Sealed capability tokens.** `Cap<'sc, C>` carries no public constructor and contains a `Sealed` field whose constructor is private to the crate. Forging a `Cap` is therefore a privacy violation rejected at compile time (verified by a `compile_fail` doctest in the crate). Carrier values `Tagged<'sc, T, C>` likewise have a private `value` field; the inner 𝑇 is unreachable by direct field access (also verified by `compile_fail` ). 

**Invariant brand lifetime.** Both `Cap` and `Tagged` carry a brand parameter<sup>′</sup> 𝑠𝑐, made invariant by `PhantomData<fn(&'sc ()) -> &'sc ()>` . The sole entry point to the layer is a scope combinator 

`run<T, C, R, F>(value, f) -> R` where `F: for<'sc> FnOnce(Cap<'sc, C>, Tagged<'sc, T, C>) ->` 

6 

The universal quantification of<sup>′</sup> 𝑠𝑐 together with 𝑅∶<sup>′</sup> 𝑠𝑡𝑎𝑡𝑖𝑐 forces the closure’s return type to be free of<sup>′</sup> 𝑠𝑐, ruling out any path by which a `Cap` or `Tagged` might escape the scope. The construction is the same one used by `ghost-cell` for branded references. A third `compile_fail` doctest demonstrates that attempting to return the `Cap` from the closure is rejected. 

**Opaque-receipt sinks.** Carrier extraction is governed by a fixed set of sink functions, each of which consumes both `Cap<'sc, C>` and `Tagged<'sc, T, C>` and returns a _receipt_ type that contains no information derived from 𝑇 beyond its serialised length: 

```
pubfnto_llm<'sc,T,C,S>(cap:Cap<'sc,C>,
```

```
data:Tagged<'sc,T,C>,
serialize:S)->LlmAck
whereS:FnOnce(T)->String;
```

The agent has no public method that returns raw 𝑇 ; the prior draft’s `Tagged::release(cap) -> T` is removed in favour of the sink interface above. The only operations on _Tagged_ that the agent’s code can perform are `map` and `and_then` , both of which preserve the brand and the kind. 

**The agent-facing surface is** **`#![no_std]` .** The crate is partitioned so that the gateway-side integration with `postern-core` lives behind a `gateway` feature flag; the agent-facing types and operations ( `Cap` , `Tagged` , `run` , `sinks` ) depend only on `core` and `alloc` . A downstream agent crate declaring `#![no_std]` and depending on `postern-guardrail` with `default-features = false` therefore has no link-level access to `std::println!` , `std::process::exit` , network sockets, or filesystem APIs, and the only side-effect channels available are those reached through the sanctioned sinks. 

**Residual.** Inside a `map` closure body the agent has temporary access to a value of type 𝑇 ; Rust does not bound what that body may do with the value. Three classes of side-channel survive: `panic!` with formatted strings, timing observed by the host, and stash in thread-local storage when 𝑇∶<sup>′</sup> 𝑠𝑡𝑎𝑡𝑖𝑐. We mitigate the obvious thread-move attack by making both `Cap` and `Tagged !Send + !Sync` via the `*const ()` phantom, but a determined adversary inside the agent runtime is out of scope for the present construction. A genuinely tight analog of capturechecking in Rust appears to require either a custom lint over closure bodies or a Wasm-class sandbox; both directions are discussed in §6. 

# **Formal model** 

The development is mechanised in `verifier/lean/Postern.lean` ; the pertheorem axiom set is reported by `CheckAxioms.lean` . We write _rewrite cat_ 𝑃𝑝𝑞 for the rewriter applied to catalog _cat_ , policy 𝑃 , principal 𝑝, and plan 𝑞. The output type is _Option Plan_ ; _none_ denotes explicit refusal. 

**Theorem 1 (output-column soundness,** **`rewrite_sound` ).** For every 

7 

_cat_ , 𝑃, 𝑝, 𝑞, 𝑞<sup>′</sup> , if _rewrite cat_ 𝑃𝑝𝑞= _some_ 𝑞<sup>′</sup> , then for every column 𝑐∈𝜎(𝑞<sup>′</sup> ), 𝑐∈𝑃. _allowed_ 𝑝 _touched_ (𝑞). 

**Theorem 2 (filter-predicate soundness,** **`rewrite_filter_sound` ).** Under the same hypothesis, every column read by a _Filter_ predicate inside 𝑞<sup>′</sup> is also in 𝑃. _allowed_ 𝑝 _touched_ (𝑞). Theorems 1 and 2 together rule out the side-channel in which a principal lacking read access to column 𝑐 uses it as a row selector without projecting it. 

**Theorems 3 and 4 (** **`rewrite_schema_subset` ,** **`rewrite_no_new_columns` ).** The output schema is contained in the input schema. Equivalently, 𝑐∉𝜎(𝑞) implies 𝑐∉𝜎(𝑞<sup>′</sup> ). 

**Theorem 5 (idempotence,** **`rewrite_idempotent` ).** If _rewrite cat_ 𝑃𝑝𝑞= _some_ 𝑞<sup>′</sup> and _rewrite cat_ 𝑃𝑝𝑞<sup>′</sup> = _some_ 𝑞<sup>″</sup> , then 𝜎(𝑞<sup>″</sup> ) = 𝜎(𝑞<sup>′</sup> ) as sets. The rewriter is a closure operator on schemas. 

**Theorem 6 (monotonicity in the policy,** **`rewrite_monotone` ).** If 𝑃. _allowed_ 𝑝𝑟⊆𝑃<sup>′</sup> . _allowed_ 𝑝𝑟 for every 𝑝 and 𝑟, then the output schema under 𝑃 is contained in the output schema under 𝑃<sup>′</sup> . Strengthening the policy can only widen the released set. 

**Theorem 7 (touched-relation preservation,** **`rewrite_touched` ).** _touched_ (𝑞<sup>′</sup> ) = _touched_ (𝑞). 

**Theorem 8 (refusal under unknown relation,** **`rewrite_refuses_unknown` ).** _cat touched_ (𝑞) = [] implies _rewrite cat_ 𝑃𝑝𝑞= _none_ . A relation absent from the catalog is rejected explicitly rather than reduced to an empty output schema — relevant under catalog drift, where the physical store may diverge from the catalog. 

**Theorem 9 (refusal under forbidden filter,** **`rewrite_refuses_forbidden_filter` ).** If 𝑐∈ _filterCols_ (𝑞) and 𝑐∉𝑃. _allowed_ 𝑝 _touched_ (𝑞), then _rewrite cat_ 𝑃𝑝𝑞= _none_ . The contrapositive of Theorem 2. 

`CheckAxioms.lean` audits the axiom dependencies of each theorem. For the rewriter side (Theorems 1–9) the set is bounded by { `propext` , `Quot.sound` }, Lean~4’s foundational axioms; the proofs of `rewrite_touched` and `rewrite_refuses_unknown` depend on no axioms, and no proof uses `sorry` . 

**Datalog evaluator (** **`verifier/lean/Datalog.lean` ).** The policy language is mechanised independently. Eight supporting list-membership lemmas ( `step_extensive` , `allMatches_subset_facts` , the joint `step_subset` , `iterate_succ_extensive` , `iterate_subset_le` , `iterate_subset_program` ) are proved without `sorry` . Four specialisation lemmas ( `step_no_rules` , `iterate_no_rules` , `eval_no_rules` , `eval_fact_mem` ) cover the rule-free regime the financial-institution scenario uses today; they give an unconditional soundness direction for ground-fact policies and depend only on `propext` . The headline `eval_monotone` is proved modulo one isolated combinatorial obligation, `herbrandBound_mono` (a length-after- `eraseDups` arithmetic argument 

8 

with no semantic content). Two further meta-theorems, `eval_sound` and `eval_terminates` , are stated with `sorryAx` obligations named explicitly in the audit so the residual proof surface is visible at CI time. The corresponding open problems are listed in §6. 

# **Implementation and conformance testing** 

The Rust implementation in `prototype/crates/postern-core` mirrors the Lean types and the _rewrite_ function structurally. The conformance harness `postern-diff` consumes a JSON corpus emitted by `lake exe postern-corpus` and asserts three equalities per case: that the Rust outcome kind ( _accept_ / _refuse_ ) matches the Lean reference; that, on accept, the rewritten plan, output schema, predicate read-set, and touched relation are structurally equal to the Lean reference; and that the input plan’s _filterCols_ matches the Lean auxiliary, independent of the rewriter. 

JSON-corpus conformance is preferred to Lean-to-Rust extraction on the grounds that the corpus interface is stable across compiler-version churn in both languages and that divergence manifests as a CI failure rather than a build failure. 

**Datalog backend.** The gateway is designed to evaluate policies through `biscuit-auth` ’s public `biscuit_auth::datalog` module — `World::new()` , `add_fact` , `add_rule` , `run` , `query_match` — which is the same evaluator used inside the production token-verification surface, only without the token-handling layers we put out of scope (§6). The in-tree `postern-core` migration to this backend is in progress; the column-grant DSL serves as a byte-equivalent stand-in until the migration lands. A second conformance corpus, exercising Lean `eval` against `biscuit_auth::datalog::World` directly, is the natural pair for the rewriter corpus and is queued as the next work item. 

The corpus comprises 18 cases: seven behavioural cases drawn from the financialinstitution scenario of §5, four refusal regressions for known attack shapes (filteron-forbidden-column, unknown-relation, two nested forbidden-filter variants), and seven policy-language edge cases (empty policy, duplicate grants, catalogabsent columns, case-sensitive principal, trailing-whitespace principal, nonexistent project column, nested _Project_ narrowing). All eighteen pass on the current Rust implementation. 

# **Evaluation: a financial institution with three principals** 

We evaluate the artifact on the Kaggle `transactions-fraud-datasets` schema. The policy is reproduced in `scenarios/financial-institution/policy.postern` ; the principal cases are summarised below. 

9 

|principal|plan|outcome|rewritten schema|
|---|---|---|---|
|`CRM`|`Scan users_data`|accept|`id, name, region, age`<br>|
|`CRM`|`Project [ssn,email]`<br>over above|accept|∅(over-projection<br>collapses)|
|`CRM`|`Filter on ssn`|**refuse**|—<br>|
|`CardOps`|`Scan users_data`<br>(cross-dept)|accept|∅(no matching grant)|
|`FraudRis`|`kScan users_data`|accept|`id, region`<br>(minimum-necessary)|
|`Marketin`|`gScan users_data`<br>(unknown prin.)|accept|∅(empty allow)|
|`CRM`|`Scan`<br>`credit_bureau_imports`|**refuse**|— (unknown relation)|



Each row corresponds to a corpus case in the conformance harness; the rows annotated _refuse_ exercise Theorems 8 and 9 of §4. 

# **Related work** 

We are not aware of prior work that establishes a mechanised soundness theorem for a plan-level rewriter in an LLM-agent- facing lakehouse setting. The closest landmarks fall into four groups. 

_Verified authorization decision procedures._ Cedar (Cutler et al. 2024) formalises and proves the soundness of an authorization-decision function in Lean. The axis of verification differs from ours: Cedar establishes authorize( _request_ ) ∈ { _allow_ , _deny_ } correctly classifies a per-call request, whereas we establish that the _output of a plan transformation_ is contained in the policy-allowed set. The two are complementary; we adopt the Cedar style of Lean-mechanised denotational semantics for our policy. 

_Capability-based enforcement runtimes._ SEAL (Sadeghi et al. 2023) provides capability-based access control for analytic workloads at the runtime level; the policy core is not mechanically verified. Our development is the dual: the policy core is verified, and the runtime is correspondingly lighter. Biscuit (Clever Cloud and contributors 2024) is both the deployed capability-token distribution mechanism we assume on the front end _and_ the policy-language layer we mechanise: the Horn fragment of its Datalog dialect underpins our policy semantics, and the production-grade `biscuit-auth` Rust crate is the gateway’s runtime evaluator ( `biscuit_auth::datalog::World` ). Block attenuation, audience, expiry, and key rotation are explicit out-of-scope items (§6); the column-grant surface syntax compiles to ground `right(principal, relation, column)` Datalog facts in the in-scope fragment. 

_Information-flow control for database-backed applications._ Jeeves (Yang et al. 

10 

2012), Jacqueline (Yang et al. 2016), and the faceted-execution line (Schoepe et al. 2016) enforce IFC inside ORM-backed applications using a faceted-value runtime discipline. They predate the LLM-agent threat model and do not target the lakehouse setting; we view them as the closest PL-side relatives of Layer 2 of our development. 

_Defences for LLM-agent prompt injection._ AgentDojo (Debenedetti et al. 2024) and CaMeL (Debenedetti et al. 2025) develop capability-flow defences at the agent boundary. Our development is complementary: the rewriter of §3–§4 enforces a policy at the lake-facing boundary on plans; their constructions enforce analogous properties on the agent’s own emitted code. Closest to our Layer 2 specifically, Odersky et al. (Odersky et al. 2026) propose Scala~3 capturechecking as the type-level mechanism for tracking capabilities through agent code; we adapt the same intuition under Rust’s weaker type-system commitments (§3). 

_Deployed alternatives we improve upon._ PostgreSQL row security policies (PostgreSQL Global Development Group 2024) and equivalent CLS facilities require per-engine integration and do not compose across the heterogeneous ingest paths typical of lakehouse deployments. Open Policy Agent (Cloud Native Computing Foundation 2021) is general-purpose but does not reason about query outputs at the plan level. Tenant segregation forfeits cross-source analytics and is the silo case we discuss in §1. 

# **Open challenges and future work** 

Three extensions of the Lean development are the natural next research questions. _Cross-relation joins._ The Plan IR is single-relation. The Rust implementation handles joins by per-leg rewriting but the composition is not under proof. The conjecture is a theorem of the form 

_rewrite_  sound_  join_ ∶ _accept_ (𝑞1)∧ _accept_ (𝑞2) ⟹𝜎( _rewrite_ ( _Join_ (𝑞1, 𝑞2))) ⊆⋃ 𝑃. _allowed_ 𝑝 _touched_ (𝑞𝑖) 𝑖 

on a Plan IR extended with a _Join_ constructor. The join-key leak — joining on a column 𝑐 without projecting it, which leaks 𝑐’s value distribution — mirrors the filter side-channel and admits the analogous coverage condition. 

_Aggregation with a differential-privacy boundary._ A principal may be permitted to read SUM( _amount_ ) without permission to read individual rows. The rewriter extension here is straightforward in shape but admits a non-trivial soundness statement once the differential-privacy boundary is parameterised; SEAL (Sadeghi et al. 2023) and the faceted line (Schoepe et al. 2016) are the closest reference points. 

_Capability attenuation inside the proof._ The Lean development takes _Principal_ as a flat string and assumes the gateway has already verified the bearer of 

11 

a biscuit token. Modelling biscuit’s Datalog-based attenuation, expiry, and audience checks inside the Lean proof lifts the principal- extraction row out of the trusted base — a substantial strengthening of the artifact’s overall claim. Adjacent open problems include catalog-integrity attestation and plan- integrity in transit. 

# **Reproducibility** 

```
verifier/lean/Lean4spec+theorems+corpusemitter
prototype/Rustworkspace:postern-core,postern-diff
scenarios/Financial-institutioncasestudy
paper/Thisdocument
scripts/reproduce.sh—chainseverything
```

Toolchains: **Lean 4.29.1** (pinned in `verifier/lean/lean-toolchain` ), **Rust stable** (tested 1.93). Single command: 

```
scripts/reproduce.sh
```

Expected output ends with `18/18 cases pass (Lean reference == Rust impl)` and an axiom audit showing only `propext` and `Quot.sound` . Runs in under two minutes on an M-series Mac on a warm cache. 

# **References** 

Anthropic. 2024. _Model Context Protocol_ . Https://modelcontextprotocol.io. 

- Clever Cloud and contributors. 2024. _Biscuit: A Bearer Token with DatalogBased Offline Authorization_ . Https://www.biscuitsec.org. 

- Cloud Native Computing Foundation. 2021. “Open Policy Agent and the Rego Language.” _CNCF Graduated Project Documentation_ . 

- Cutler, Joseph W., Craig Disselkoen, Aaron Eline, et al. 2024. “Cedar: A New Language for Expressive, Fast, Safe, and Analyzable Authorization.” _Proc. ACM Program. Lang._ 8 (OOPSLA1). 

Debenedetti, Edoardo et al. 2025. _Defeating Prompt Injections by Design_ . 

- Debenedetti, Edoardo, Jie Zárate, and Tramer Florian Tramer. 2024. “AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents.” _Advances in Neural Information Processing Systems (NeurIPS)_ . 

- Moura, Leonardo de, and Sebastian Ullrich. 2021. _The Lean 4 Theorem Prover and Programming Language_ . Https://lean-lang.org. 

12 

- Odersky, Martin, Yichen Zhao, Yifan Xu, Oliver Bračevac, and Cao Nguyen Pham. 2026. _Tracking Capabilities for Safer Agents_ . https://arxiv.org/ab s/2603.00991. 

- PostgreSQL Global Development Group. 2024. _Row Security Policies_ . Https://www.postgresql.org/docs/current/ddl-rowsecurity.html. 

- Raasveldt, Mark, and Hannes Mühleisen. 2019. _DuckDB: An in-Process SQL OLAP Database Management System_ . Https://duckdb.org. 

- Sadeghi, Ahmad-Reza et al. 2023. “SEAL: Capability-Based Access Control for Data-Analytic Scenarios.” _Proceedings of the 28th ACM Symposium on Access Control Models and Technologies (SACMAT)_ . https://doi.org/10.114 5/3589608.3593838. 

- Schoepe, Daniel, Musard Balliu, Benjamin C. Pierce, and Andrei Sabelfeld. 2016. “Explicit Secrecy: A Policy for Taint Tracking.” _IEEE European Symposium on Security and Privacy (EuroS&p)_ . https://doi.org/10.1109/ EuroSP.2016.14. 

- Yang, Jean, Travis Hance, Thomas H. Austin, Armando Solar-Lezama, Cormac Flanagan, and Stephen Chong. 2016. “Precise, Dynamic Information Flow for Database-Backed Applications.” _PLDI_ . https://doi.org/10.1145/290808 0.2908098. 

- Yang, Jean, Kuat Yessenov, and Armando Solar-Lezama. 2012. “A Language for Automatically Enforcing Privacy Policies.” _Proceedings of the 39th Annual ACM SIGPLAN-SIGACT Symposium on Principles of Programming Languages (POPL)_ . https://doi.org/10.1145/2103656.2103669. 

13 

