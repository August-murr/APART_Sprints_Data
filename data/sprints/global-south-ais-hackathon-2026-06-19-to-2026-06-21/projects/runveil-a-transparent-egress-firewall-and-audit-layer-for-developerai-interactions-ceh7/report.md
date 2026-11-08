# **runveil: A Transparent Egress Firewall and Audit Layer for Developer–AI Interactions** 

**Dang Phan** 

Independent Developer 

## **Abstract** 

_Developers increasingly delegate work to third_ ‑ _party AI tools — Claude Code, Cursor, GitHub Copilot, ChatGPT — that read local files and transmit source, secrets, and customer data to external model providers over TLS. Organizations have little visibility into, and no control over, this "Shadow AI" egress, and existing data_ ‑ _loss tooling does not see it. We present runveil, an open_ ‑ _source system that places a transparent, tool_ ‑ _agnostic enforcement and audit layer at the boundary where humans and their AI agents send data out. runveil consists of (i) a local forward_ ‑ _proxy agent that intercepts AI_ ‑ _bound HTTPS using a device_ ‑ _local certificate authority, inspects request bodies with content_ ‑ _aware detectors (credential scanning, path/DLP rules), and applies graduated actions — allow, redact, warn, block — inline before traffic leaves the machine; and (ii) a multi_ ‑ _tenant control plane that distributes versioned policy and aggregates a per_ ‑ _request audit trail with analytics, retention, and export. Because interception is transparent, runveil captures egress that opt_ ‑ _in AI gateways structurally miss, and it functions without cooperation from the AI tool — a property that matters as coding tools become autonomous agents. We describe the architecture and policy model, and verify the end_ ‑ _to_ ‑ _end system: device_ ‑ _token authentication, ETag/304 policy caching, and audit ingestion all behave to specification, the enforcement pipeline correctly blocks/redacts representative secret and sensitive_ ‑ _path payloads, and the implementation is covered by 417 agent and 36 control_ ‑ _plane automated tests. We argue runveil is a practical oversight substrate for human–AI data flows and a complement to model_ ‑ _side safety._ 

## **1. Introduction** 

_AI coding assistants have moved from autocomplete to agents that act: they read a repository, decide which files are relevant, and send their contents to a remote model. The same is true of chat tools into which developers paste logs, stack traces, and configuration. Every one of these interactions is an egress event — proprietary or sensitive data crossing the organizational boundary to a third party — and it travels as ordinary TLS to a vendor API. Conventional data_ ‑ _loss prevention (DLP) was built for email and file uploads and does not inspect this channel; AI "gateways" only observe calls that an application is explicitly configured to route through them. The result is a visibility and control gap precisely where the highest_ ‑ _value data now flows._ 

_We frame this as an AI oversight problem. As organizations adopt AI, a basic governance requirement is the ability to see and control what their people — and the autonomous tools acting on their behalf — send to external models, and to retain an auditable record of it. This is the human side of AI safety: not aligning the model, but governing the interface. A control point here is also a defense that does not depend on the AI tool's cooperation, which is important when the tool is an agent making its own decisions about what to read and transmit._ 

_Threat model. A developer (or an agent running with their credentials) transmits secrets, credentials, source, or regulated data to a third_ ‑ _party model. The organization wants (a) inline prevention of the most dangerous cases, (b) graceful degradation (redaction) rather than blanket blocking, and (c) a tamper_ ‑ _resistant audit trail for incident response and compliance. We assume the organization controls its endpoints (can install software and a trust anchor) and that traffic uses HTTPS to known AI hosts._ 

### Our main contributions are: 

1. _A transparent, tool_ ‑ _agnostic interception architecture for AI egress: a local CA + forward proxy that observes and enforces on AI_ ‑ _bound traffic without modifying the AI tool, capturing Shadow AI that opt_ ‑ _in gateways miss and functioning against autonomous agents._ 

2. _An inline content_ ‑ _aware policy engine at the egress boundary — credential and path detectors with graduated actions (allow/redact/warn/block) — driven by a small, auditable YAML policy grammar._ 

3. _A multi_ ‑ _tenant control plane that turns per_ ‑ _endpoint enforcement into organizational oversight: centrally edited, versioned policy with fast rollout, plus an append_ ‑ _only audit trail with analytics, retention, and export — and which, by design, stores findings and metadata, not message bodies._ 

4. _A working, open_ ‑ _source end_ ‑ _to_ ‑ _end system released under an open_ ‑ _core model, with functional verification of its core guarantees._ 

## **2. Related Work** 

_AI gateways / proxies (LiteLLM, Cloudflare AI Gateway, Portkey, Helicone) sit in front of model APIs to add caching, routing, rate_ ‑ _limiting, and logging. They are opt_ ‑ _in: an application must be configured to send traffic through them, so they observe only sanctioned calls and cannot see a developer's Claude Code session or a pasted ChatGPT prompt. runveil differs by intercepting transparently at the endpoint, capturing arbitrary AI egress without per_ ‑ _tool integration._ 

_Enterprise DLP / CASB and AI_ ‑ _security vendors (Netskope, Zscaler, Nightfall, Harmonic, Prompt Security) increasingly advertise GenAI coverage, typically via network_ ‑ _level cloud proxies or browser agents. These are powerful but heavyweight, closed, and oriented to large enterprises; runveil targets the developer endpoint with an open_ ‑ _source, agent_ ‑ _first design and an explicit "no bodies stored" posture, and is specifically aimed at coding_ ‑ _agent traffic._ 

_Secret scanners (gitleaks, trufflehog, detect_ ‑ _secrets) find credentials in repositories or commits — at rest, not in flight. runveil applies similar detection at egress time, on the actual outbound payload, where a block can still prevent the leak._ 

_LLM guardrail frameworks (e.g., Meta's LlamaFirewall/CodeShield, NeMo Guardrails) filter model inputs/outputs inside an application. runveil is complementary: it operates below the application, on the wire, independent of the model and tool._ 

_Someone would use runveil over these when they need visibility and enforcement over unmanaged AI tool usage on developer machines, transparently and from open source, with an organization_ ‑ _level audit trail — a combination none of the above provides._ 

## **3. Methods** 

_System overview (Figure 1). runveil has two components communicating over two stable HTTP endpoints; everything behind them is independent._ 



_Figure 1. Transparent interception at the endpoint; centralized policy and audit at the control plane._ 

_Agent (Go). runveil init generates a device_ ‑ _local CA and installs it into the OS trust store; the agent then runs a forward HTTPS proxy on localhost and the developer points their tools' HTTPS_PROXY at it (one environment variable, or our background service sets it). For AI_ ‑ _bound connections the agent terminates TLS, parses provider_ ‑ _specific request bodies (OpenAI/Anthropic shapes), and runs a pipeline of stages: a secret scanner (pattern + entropy detectors for keys/tokens), and a path scanner that extracts file paths from agent tool_use blocks. Each finding is scored, the active policy is consulted, and an action is applied: forward unchanged (allow), forward with sensitive spans masked (redact), forward but flag (warn), or refuse with 403 (block). The agent writes a structured audit record — request_id, time, host, method, path, status, decision, findings, bytes_in/out, duration_ms, vendor, endpoint, device_id — to a local JSON_ ‑ _Lines log and, when configured, batches it to the control plane. Configuration is a single config.json (control_plane_url, device_token) written by runveil enroll; the agent runs as a background service (systemd/launchd)._ 

_Policy grammar. Policies are small, reviewable YAML: version, then rules[], each with a match (one of pattern, severity, all, or a path glob) and an action (allow|block|warn|redact). This keeps enforcement legible and lets per_ ‑ _project differences be expressed as path_ ‑ _scoped rules within one policy rather than as separate configurations._ 

_Control plane. A Go service exposes the two agent endpoints on Postgres: GET /v1/policy (device_ ‑ _token auth, ETag/304 so idle agents poll cheaply) and POST /v1/audit/batch (NDJSON). A Next.js app provides multi_ ‑ _tenant management (GitHub OAuth, role_ ‑ _based access): a validated, versioned policy editor with ~30_ ‑ _second rollout via ETag change, an audit log with per_ ‑ _request detail, a live view, analytics (volume/error/latency, per_ ‑ _host and per_ ‑ _device), per_ ‑ _tenant retention, and CSV export. Device tokens (dt_…) are stored only as sha256 hashes; a stable device_id identifies a machine._ 

_Key design choices. Transparent MITM (rather than opt_ ‑ _in routing) is what lets us see unmanaged tools and agents — the central requirement. Bodies are never stored centrally — only findings and metadata — making the audit trail useful without itself becoming a data_ ‑ _exfiltration risk. ETag/304 + NDJSON keep the agent↔plane protocol cheap and were held byte_ ‑ _stable throughout development so deployed agents never break. Open_ ‑ _core (free agent, paid plane) lowers adoption friction for a security tool that must earn trust._ 

_What is hard / did not work cleanly. TLS interception requires installing a trust anchor (a privileged, visible operation) and is bypassed by certificate_ ‑ _pinned clients; body inspection is provider_ ‑ _shape_ ‑ _specific, so a new vendor needs a parser; detection is heuristic (regex/entropy), with the usual false_ ‑ _positive/negative trade_ ‑ _offs._ 

_Reproducibility. The system is open source and installs with one line (curl … | sh); the agent runs entirely locally for evaluation, and the control plane runs against any Postgres. The full test suites reproduce the functional claims below._ 

## **4. Results** 

_We report functional and contract correctness of the system rather than a detection_ ‑ _quality benchmark (which we scope as future work, Section 5)._ 

_Enforcement behaves correctly on representative payloads. Table 1 shows decisions produced by the agent's end_ ‑ _to_ ‑ _end pipeline on crafted requests, taken from the integration test suite._ 

|**#**<br>**Outbound payload (to a model API)**|**Detector**|**Decision**|**HTTP**|
|---|---|---|---|
|1 Chat completion containing`aws_access_key_id`<br>+`aws_secret_access_key`|secret‑scan (2× high)|**block**|403|
|2 Message containing a single AWS key|secret‑scan (high)|**redact**|200<br>(modified)|
|3 Agent`tool_use`reading`…/payments/charge.go`|path‑scan, rule<br>`block-payments`|**block**|403|



|4 Ordinary completion, no sensitive content<br>—<br>**allow**<br>200|
|---|



_Table 1. Representative inline decisions from the integration suite. Each row is an actual classified request; "modified" denotes redacted egress._ 

_The agent↔control_ ‑ _plane contract is correct. In an end_ ‑ _to_ ‑ _end run against a freshly migrated Postgres, an unauthenticated GET /v1/policy returns 401; with a valid device token it returns 200 and an ETag; a conditional request with the matching If_ ‑ _None_ ‑ _Match returns 304; and a POST /v1/audit/batch of NDJSON records returns 2xx, after which the rows are present in the database, each stamped with the originating device_id. This confirms device_ ‑ _token authentication, policy caching, and audit ingestion end_ ‑ _to_ ‑ _end._ 

_The implementation is well_ ‑ _tested. The agent is covered by 417 automated tests (run with the race detector), spanning the detectors, the proxy/TLS path, policy loading, and integration; the control plane is covered by 36 tests using ephemeral Postgres containers. All pass in CI across Linux, macOS, and Windows._ 

_Overhead. Inline processing adds modest per_ ‑ _request latency; against a local mock upstream in the integration tests we observe single_ ‑ _digit_ ‑ _millisecond proxy overhead. We do not claim a real_ ‑ _world latency figure — wide_ ‑ _area network time dominates, and a rigorous measurement against live provider APIs is [TODO: team to measure]._ 

_Robustness of claims. Our claims are functional (the system does what it says) and are backed by reproducible test suites and a live contract check, not by a single run. We deliberately do not assert detection precision/recall, because we have not yet evaluated against a labeled corpus; making that claim without that evidence would be unsound._ 

## **5. Discussion and Limitations** 

_Implications for AI safety. runveil is infrastructure for human oversight of AI usage. Model_ ‑ _side safety (alignment, refusal training, guardrails) governs how a model behaves; runveil governs the interface — what leaves the organization toward the model and what record remains. As coding tools become autonomous agents that choose what to read and send, an enforcement point that does not rely on the agent's cooperation becomes more valuable, not less: it is a control that holds even if the agent is buggy, jailbroken, or adversarial about its own logging. The "store findings, not bodies" design also illustrates a pattern for monitoring that minimizes the new attack surface it creates._ 

_Limitations. (1) Trust and bypass: interception requires installing a CA (privileged, and a target for tampering) and is defeated by certificate pinning; an insider can disable a local agent absent MDM_ ‑ _level enforcement. (2) Coverage: body inspection is provider_ ‑ _specific; unparsed providers are passed through opaquely. (3) Detection quality: regex/entropy detection has false positives and negatives, and we present no quantitative precision/recall — this is the most important open_ 

_evaluation. (4) Trust in the audit: records are append_ ‑ _only but not yet cryptographically tamper_ ‑ _evident. (5) Scope: we assume org_ ‑ _controlled endpoints; BYOD and pinned apps are out of scope. If the assumption that the organization can install software and a trust anchor does not hold, the transparent_ ‑ _interception approach does not apply and the contribution reduces to the policy/audit model behind an explicit proxy._ 

_Future work. A labeled benchmark for detection precision/recall; additional provider parsers; semantic/PII detection using small models; cryptographic hash_ ‑ _chaining of the audit log for tamper_ ‑ _evidence; continuous SIEM forwarding; policies over agent actions (not just content); and time_ ‑ _partitioning for audit at scale._ 

## **6. Conclusion** 

_We built runveil, a transparent, open_ ‑ _source egress firewall and audit layer for the traffic developers and their AI agents send to third_ ‑ _party models. By intercepting at the endpoint rather than asking tools to opt in, it provides visibility and inline control — allow, redact, warn, block — over Shadow AI that current gateways and DLP miss, and it pairs per_ ‑ _machine enforcement with an organization_ ‑ _level, body_ ‑ _free audit trail. We verified the system's core guarantees end_ ‑ _to_ ‑ _end and ship it as a working artifact. We see this as a small but concrete piece of AI_ ‑ _oversight infrastructure: governing the human–AI interface is a necessary complement to governing the model, and it becomes more pressing as the tools on the other side of that interface start to act on their own._ 

## **Code and Data** 

- Code (agent): https://github.com/dawnn07/runveil — open source; one‑line install curl -fsSL https://raw.githubusercontent.com/dawnn07/runveil/main/install.sh | sh. 

- Data: none collected; the system stores per‑request metadata and findings, not message bodies. No external dataset was used. 

- Demo: https://runveil-cloud.vercel.app/ 

## **References** 

1. _LiteLLM. LiteLLM: Call 100+ LLM APIs. https://github.com/BerriAI/litellm_ 

2. _Cloudflare. AI Gateway. https://developers.cloudflare.com/ai-gateway/_ 

3. _Gitleaks / TruffleHog — secret scanning. https://github.com/gitleaks/gitleaks · https://github.com/trufflesecurity/trufflehog_ 

4. _Meta. LlamaFirewall / CodeShield._ 

## **Appendix** 

_We used Claude (via Claude Code) extensively to design and implement the system — architecture, agent pipeline, control plane, and dashboard — and to draft this report. All functional claims were independently verified by running the automated test suites (417 agent + 36 control_ ‑ _plane tests) and an end_ ‑ _to_ ‑ _end contract test (auth, ETag/304, audit ingestion) whose outputs are reported in Section 4; no quantitative result is asserted that we did not observe. The final manuscript was reviewed and edited by the authors._ 

