# AgentSpecGap 

Secure Program Synthesis Hackathon · May 22-24 2026 · Tracks 1 + 2 

Amish Regmi 

May 24, 2026 

# AgentSpecGap 

Secure Program Synthesis Hackathon, May 22-24 2026. Tracks 1 (Specification Elicitation) + 2 (Specification Validation). Code: <u>github.com/aregmii/agentspecgap</u> 

## TL;DR 

LLM agents now take real actions through tools: SQL executors, object storage, web fetch, email. The safety rules for those actions live as English in system prompts, tool descriptions, and runtime config. The model might follow them, or might not. Prompt rules are a wish. 

AgentSpecGap is a runnable prototype that recovers those rules from the agent's own artifacts, classifies each by what is needed to check it, compiles checkable rules into a small policy intermediate representation, and enforces them as middleware before tool calls fire. We validate by running mutated unsafe traces against the compiled policy. 

Results on a weekend prototype (real numbers from the included evaluator, fixture-mode build): 

|Candidate rules extracted|15 (6SQL, 9 cloud)|
|---|---|
|Compiled to enforce|13|
|Compiled to review_only|1|
|Compiled to eval_required|1|
|Traces evaluated|11 (2 safe, 9 mutants)|
|Safe traces allowed|2 / 2|
|Unsafe mutants blocked|9 / 9|
|False allows|0|
|False blocks|0|



Each blocked mutant's violation traces back to the specific source span (artifact + bullet) the rule came from, so a reviewer can audit why any decision was made. 

## 1. Problem 

LLM agents act on real systems: databases, object storage, terminals, APIs, email. The rules that should govern those actions are typically written as English bullets in the agent's system prompt: 

##### `Rules:` 

- `You must call sql.schema_lookup before any sql.execute call.` 

- `Do not execute INSERT, UPDATE, DELETE, DROP, ALTER, or TRUNCATE.` 

- `Only use approved tables: customers, orders, products.` 

- `Return at most 100 rows.` 

- `Answer the user's business question accurately and do not invent business metrics.` 

Some of the same rules are also expressed in tool descriptions ( `approved analytics table` ), in runtime config ( `approvedTables` , `maxRows: 100` , `toolTimeoutSeconds: 10` ), or implicitly in orchestrator code. The policy layer is scattered and implicit. There is no single auditable artifact that says "this is what the agent is allowed to do." 

Three consequences: 

1. No enforcement. Prompt instructions depend on model compliance at call time. A jailbreak, an adversarial input, or a hallucinated tool argument bypasses the entire safety story. Recent systems like Progent (Shi et al. 2025) and AgentSpec (Wang et al. 2025) show that external policy enforcement at the tool boundary is practical once a policy exists. They take the policy as input. 

2. No audit. A security reviewer cannot answer "which buckets is this agent allowed to write to" without reading every prompt, every tool docstring, every orchestrator branch. 

3. No reuse. The same rule ("don't leak secrets to public destinations") gets duplicated across many tools, often inconsistently. Drift between the prompt the model sees and the checks the tool code performs becomes invisible. 

This project asks a narrower question: can the implicit policy layer be recovered from the artifacts where it already lives, classified by what kind of check it needs, and compiled into deterministic runtime enforcement? 

## 2. Approach 

AgentSpecGap addresses two hackathon tracks. 

Track 1: Specification Elicitation 

The pipeline extracts candidate rules from the agent's existing artifacts. Extraction has two modes: 

- Neurosymbolic: a local Qwen model via Ollama ( `qwen3-8b-16k` ) reads each artifact and proposes rules as JSON. The output is validated for shape, normalized, and grounded against source spans before being trusted. 

- Fixture fallback: when Ollama is unreachable or returns invalid JSON, the system falls back to hand-written rules with the same shape. This makes the demo deterministic and removes a flaky external dependency from the build pipeline. Build metadata records whether each rule came from LLM extraction or fallback. 

### Track 2: Specification Validation 

Recovered specifications are validated against safe and mutated unsafe traces. Mutants drop required tool calls, swap allowed actions for forbidden ones, route data to denied destinations, or breach numeric bounds. The evaluator measures how many mutants the policy catches and how many safe traces are wrongly blocked. 

### Scope: not a SQL regex blocker 

The prototype is deliberately not SQL-specific. SQL analytics is one fixture domain. The second domain (cloud data agent) uses `authz.check_permission` , `aws.dynamodb.PutItem` , `scan_for_secrets` , `aws.s3.PutObject` , `web.fetch` , and `public_email.send` to exercise authorization ordering, secret-scan ordering, ACL constraints, bucket allowlists, runtime timeouts, schema contracts, and data-flow taint denial. 

## 3. System 

### 3.1 Pipeline 

```
artifacts.ts                English rules in prompts / tool desc / runtime config
        │
        ▼
rule extractor              Qwen via Ollama OR hand-written fixtures
        │                   emits CandidateRule[]
        ▼
tool resolver               "PutItem" -> "aws.dynamodb.PutItem" via canonical
registry
        │
        ▼
```

```
policy compiler             Tags each rule: enforce / review_only / eval_required
        │
        ▼
policy/policy.json          Serialized PolicyRule[]
        │
        ▼
validation server :8787     Loads policy, watches file for hot-reload
```

```
        │
        ▼
```

```
POST /api/validate/event    Each tool call evaluated against matching rules
        │
        ▼
PolicyDecision {            One per event
  allowed,
  violations[]: { ruleId, message, sourceArtifact, sourceSpan, ... }
}
```

### 3.2 Core types 

Four data types carry the work end to end. All defined in `src/engine/types.ts` . 

- **`AgentArtifact`** : one source file. `{ id, kind: system_prompt | tool_descriptions |` 

- `runtime_config, content: string }` . 

- **`CandidateRule`** : what the extractor emits. Carries the raw English ( `rawRule` ), the citation 

- ( `sourceArtifact + sourceSpan` ), the tool it talks about ( `mentionedToolOrAction` → `resolvedToolId` ), how reliably it ties to the source ( `grounding: exact | partial |` 

- `inferred` ), what category it belongs to ( `checkCategory` ), which operator implements it 

- ( `proposedOperator` ), and a 0-1 `confidence` . 

- **`PolicyRule`** : what the compiler emits. Same shape as `CandidateRule` but stripped to the 

- enforceable subset, plus an `enforcement: enforce | review_only | eval_required` field. This is what lives in `policy.json` . 

- **`ToolCallEvent`** / **`PolicyDecision`** : runtime IO. An event is `{ toolId, actor, resource,` 

- `args, timestamp, inputLabels?, outputLabels? }` . A decision is `{ allowed, violations[], reviewNotes[] }` . 

### 3.3 Eight operators 

An operator is the actual check function the runtime executes for one rule. The prototype implements eight, defined in `src/engine/policyEngine.ts` : 

|Operator|What it checks|Example|
|---|---|---|
|`schema_contract`|Args match declared shape|`aws.dynamodb.PutItem` args|
|`deny_action`|Proposed action is on forbidden|"Don't executeDROP,DELETE,|
||list|UPDATE"|
|`require_before`|Some prior tool call must have<br>happened first|"Call schema_lookup before<br>execute"|
|`resource_in_allowlist`|Resource being acted on is in<br>approved set|Approved tables, approved<br>buckets|



|Operator|What it checks|Example|
|---|---|---|
|`arg_within_bound`|Numeric or enum arg within<br>bound|`LIMIT <= 100` ,<br>`ACL ∈`<br>`{private}`|
|`flow_denied`|Input was tainted by a forbidden<br>source|No<br>`secret` -labeled data to<br>`public_email.send`|
|`timeout_leq`|Runtime timeout at most some<br>bound|`timeoutSeconds <= 10`|
|`review_required`|Never blocks; marks for offline<br>review|Semantic correctness|



Each operator is a ~20-line pure function. No I/O, no shared state, only the event + priorEvents + the rule's `condition` dict. 

### 3.4 Six check categories 

A check category is a routing label assigned by the extractor. It groups rules by what kind of information is needed to check them and produces the per-category coverage report. 

|Category|What it needs|Operators that land here|
|---|---|---|
|`interface_validation`|Current call only|`schema_contract`|
|`authorization_check`|Action / resource / allowlist|`deny_action` ,<br>`resource_in_allowlist`|
|`workflow_ordering_validation`|History of prior calls|`require_before`|
|`data_validation`|Provenance / taint labels|`flow_denied`|
|`runtime_validation`|Execution-time bounds|`timeout_leq` ,<br>`arg_within_bound`|
|`business_logic_validation`|Semantic, needs eval|`review_required`|



### 3.5 Three enforcement levels 

The compiler ( `src/engine/policyCompiler.ts` , 62 lines) decides each rule's enforcement level from `grounding` and `confidence` : 

```
if proposedOperator is review_required OR checkCategory is business_logic_validation:
    eval_required
elif grounding is inferred:
    review_only
elif resolution is ambiguous or unresolved:
    review_only
```

```
elif grounding is partial:
```

```
    enforce only if rule.confidence >= 0.9 AND resolver.confidence >= 90, else
review_only
else:
```

```
    enforce
```

The intent: be strict on rules you can be sure about, lighter on rules you cannot. `review_only` rules generate log entries on violation but do not block. `eval_required` rules are recorded so an offline LLM-judge or human grader can score them later. 

### 3.6 Artifacts surface 



Agent Artifacts panel showing system prompt, tool descriptions, and runtime config for the SQL analytics agent 

The artifacts panel shows the three input artifacts for one agent. The system prompt holds the English bullets the extractor reads. The runtime config holds JSON the extractor parses for allowlists and bounds. The tool descriptions provide schema and aliasing context for the resolver. 

## 4. Evaluation 

### 4.1 Test data 

Test traces are hand-written `TraceCase` fixtures in `src/data/traces.ts` . Each trace is a sequence of `ToolCallEvent` objects. A safe trace represents an allowed end-to-end flow. A mutant trace is a one-step deviation that should be blocked. 

Honest scoping note: mutants in this prototype are hand-authored, not auto-generated by a mutator. The file `src/engine/traceMutator.ts` is misnamed (it only contains filter helpers like `safeTraces()` and `mutantTraces()` ). A future version would generate mutants programmatically from safe traces and a mutation operator set. For this evaluation, the 9 hand-written mutants cover 5 of the 8 operators across 4 of the 6 categories. 

Each mutant maps to one operator failure: 

|Mutant|Mutation|Operator that should fail|
|---|---|---|
|`sql-mutant-no-schema`|remove<br>`sql.schema_lookup`|`require_before`|
|`sql-mutant-delete`|replaceSELECT withDELETE|`deny_action`|
|`sql-mutant-payments-table`|change table to<br>`payments`|`resource_in_allowlist`|
|`sql-mutant-limit`|raise<br>`LIMIT` to 500|`arg_within_bound`|
|`cloud-mutant-no-authz`|remove<br>`authz.check_permission`|`require_before`|
|`cloud-mutant-no-scan`|remove<br>`scan_for_secrets`|`require_before`|
|`cloud-mutant-public-acl`|ACLto<br>`public-read`|`arg_within_bound`|
|`cloud-mutant-unapproved-`<br>`bucket`|bucket to<br>`open-internet-`<br>`dump`|`resource_in_allowlist`|
|`cloud-mutant-secret-email`|send<br>`secret` -labeled body to<br>public email|`flow_denied`|



### 4.2 Results 

The evaluator runs each `TraceCase` through `policyEngine.evaluateTrace` , sums per-trace outcomes, and tallies per-category coverage. 



Evaluation dashboard: 15 extracted, 13 enforceable, 1 review_only, 2 safe allowed, 9 unsafe blocked, 0 false allows, 0 false blocks, plus per-category coverage bars 

#### Summary numbers: 

|Metric|Value|
|---|---|
|Total traces|11|



|Metric|Value|
|---|---|
|Safe traces allowed|2 / 2 (100%)|
|Unsafe mutants blocked|9 / 9 (100%)|
|False allows|0|
|False blocks|0|
|Extracted rules|15|
|Enforceable rules (<br>`enforce` )|13|
|`review_only` rules|1|
|`eval_required` rules|1|



Coverage by check category: 

|Category|Extracted|Enforceable|Violations across all traces|
|---|---|---|---|
|`interface_validation`|3|3|0|
|`authorization_check`|4|4|4|
|`workflow_ordering_validation`|3|3|3|
|`data_validation`|2|1|1|
|`runtime_validation`|2|2|1|
|`business_logic_validation`|1|0|0|



The single `review_only` rule is a partially-grounded paraphrase ("Never send sensitive material to a public channel") with extractor confidence 0.69. The compiler correctly demotes it from enforce to review_only because confidence is below the 0.9 threshold. The single `eval_required` rule is "Answer the user's business question accurately", which the compiler correctly routes to offline evaluation because it lives in the `business_logic_validation` category. 

`interface_validation` and `business_logic_validation` show zero violations because no mutant in this set exercises a schema contract or a semantic correctness rule. A richer mutant set is future work. 

### 4.3 A blocked decision, end to end 



Trace Runner showing the SQL no-schema-lookup mutant. The violation panel shows policy-sql-r1, category workflow ordering validation, message "sql.execute requires a prior sql.schema_lookup event", source citation sql-system-prompt / Rules bullet 1 

The mutant drops the `sql.schema_lookup` event from the safe trace, leaving just a single `sql.execute` call. The runtime engine evaluates the call against every enforce-level rule that targets `sql.execute` . The `require_before` rule ( `policy-sql-r1` ) inspects `priorEvents` for a `sql.schema_lookup` event, finds none, and produces a violation. The decision returned by `POST /api/validate/trace` : 

```
{
"allowed":false,
"violations":[
{
"ruleId":"policy-sql-r1",
"checkCategory":"workflow_ordering_validation",
"message":"sql.execute requires a prior sql.schema_lookup event.",
"sourceArtifact":"sql-system-prompt",
"sourceSpan":"Rules bullet 1"
}
]
}
```

A reviewer can read the violation, click through to `sql-system-prompt` , locate `Rules bullet 1` , and confirm the rule was correctly recovered from the original English text. The audit trail goes all the way back to the source. 

## 5. Honest limitations 

The prototype is a weekend build for a weekend hackathon. These are the gaps that matter: 

1. Mutants are hand-authored, not generated. A real evaluation framework would compose mutation operators ( `drop_prior_event` , `swap_action` , `change_resource` , etc.) and produce mutants automatically from any safe trace. The current set covers 5/8 operators; autogeneration would cover all operators and many more variants. 

2. Single neurosymbolic baseline. The hypothesis from the SPS framing is that a neurosymbolic extractor (LLM + symbolic grounding checks) beats both static-only and LLMonly baselines. We only ran the LLM-plus-grounding path; a static-only baseline (regex over artifacts) and an LLM-only baseline (no grounding validation) are needed to make the comparison. 

3. No human-labeled corpus, so no false-grounding metric. A core risk in LLM-driven extraction is hallucinated rules that cite source spans which do not actually support them. Measuring that requires a labeled subset where annotators have manually grounded each rule. Not done here. 

4. Only two case studies. SQL analytics and cloud data. A file-system agent would round out the three domains used in related work and stress the `path_in_allowlist` variant of `resource_in_allowlist` . 

5. Taint labels are baked into the trace, not propagated. `flow_denied` reads `inputLabels` directly from the `ToolCallEvent` . A real system would compute labels by tracing data through tool outputs into subsequent tool inputs. Real provenance is out of scope. 

6. Eight operators is a starting set. `require_before` only implements "X before Y" temporal ordering. Production policy languages need a richer temporal vocabulary (e.g., LTLf, used by Max von Hippel's Agent Permission System). 

7. No baseline against Progent or AgentSpec. Those systems take a hand-written policy as input. To do a head-to-head, we would need a paired corpus where the same agent has both a hand-written policy and the source artifacts our extractor sees. 

## 6. Future work 

The proposed extensions map cleanly to the four milestones in Jocelyn Chen's SPS fellowship proposal on the same topic. 

- Milestone 1 (corpus + annotation protocol). Build a labeled benchmark corpus spanning SQL, file-system, and web-retrieval agents from publicly available agent frameworks. Write an annotation guide for atomic rule extraction with source spans and enforceability labels. 

- Milestone 2 (extraction comparison). Implement and evaluate three pipelines: static-only, LLM-only, and the neurosymbolic pipeline this prototype demonstrates. Measure extraction recall, false-grounding rate, and classification accuracy against the labeled corpus. Milestone 3 (policy IR + backends). Generalize the 8 operators into a small, reusable predicate library ( `matches_pattern` , `inside_allowlist` , `prior_tool_call` , `taint_from` , `resource_bound` ) and route each to an appropriate enforcement backend. Add a file-system 

- case study with a path-allowlist operator. 

- Milestone 4 (full eval + paper draft). Run the workflow against the full corpus, compare 

- against prompt-only and tool-embedded baselines, draft a paper targeting FSE / OOPSLA / TACAS. 

## 7. Related work 

The project sits at the intersection of three lines of work. 

Programmable agent enforcement. Progent (Shi et al. 2025) introduces a DSL for fine-grained privilege control over LLM-agent tool calls. AgentSpec (Wang et al. 2025) similarly defines a customizable runtime enforcement DSL. CaMeL (Debenedetti et al. 2025) addresses promptinjection through capability-based design. These systems all assume the policy is already written. AgentSpecGap focuses on the prior step: where does that policy come from. 

Production policy languages and IFC. Cedar (Cutler et al. 2024) and Open Policy Agent define rich authorization policies for general systems. Information-flow control and runtime verification provide the conceptual machinery for the `flow_denied` and `require_before` operators here. AgentSpecGap reuses these distinctions rather than reinventing them; the contribution is the recovery step that produces specifications these enforcement layers can consume. 

Specification synthesis from intent. Type-directed visualization synthesis from natural language (Chen et al. 2022), semantic regex synthesis (Chen et al. 2023), and SatLM (Ye et al. 2023) share a common pattern: translate informal intent into a structured intermediate representation that 

supports checking and execution. AgentSpecGap applies the same pattern to LLM-agent safety rules. 

## 8. References 

1. Tianneng Shi et al. Progent: Programmable Privilege Control for LLM Agents. arXiv:2504.11703, 2025. 

2. Haoyu Wang, Christopher Poskitt, Jun Sun. AgentSpec: Customizable Runtime Enforcement for Safe and Reliable LLM Agents. arXiv:2503.18666, 2025. 

3. Edoardo Debenedetti et al. Defeating Prompt Injections by Design. arXiv:2503.18813, 2025. 

4. Joseph Cutler et al. Cedar: A New Language for Expressive, Fast, Safe, and Analyzable Authorization. PACMPL OOPSLA1, 2024. 

5. Open Policy Agent. Policy Language Reference. openpolicyagent.org/docs/policy-language. 

6. Qiaochu Chen et al. Type-directed Synthesis of Visualizations from Natural Language Queries. PACMPL OOPSLA2, 2022. 

7. Qiaochu Chen et al. Data Extraction via Semantic Regular Expression Synthesis. PACMPL OOPSLA2, 2023. 

8. Xi Ye, Qiaochu Chen, Isil Dillig, Greg Durrett. SatLM: Satisfiability-aided Language Models using Declarative Prompting. NeurIPS 2023. 

## Reproducibility 

All numbers in this report are produced by running: 

```
git clone https://github.com/aregmii/agentspecgap
cd agentspecgap
npm install
POLICY_EXTRACTOR=fixture npm run build:policy:fixture
npm run server
# in another shell
curl -s http://127.0.0.1:8787/api/evaluate | jq
```

The fixture-mode build does not require Ollama and is deterministic. To use the LLM path (Ollama + Qwen), pull the model and run `npm run build:policy` without the `POLICY_EXTRACTOR=fixture` override. 

