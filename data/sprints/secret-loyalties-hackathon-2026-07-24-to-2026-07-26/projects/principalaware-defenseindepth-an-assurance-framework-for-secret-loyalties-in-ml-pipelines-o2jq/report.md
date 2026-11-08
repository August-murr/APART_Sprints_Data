# **Principal-Aware Defense-in-Depth** 

An Assurance Framework for Secret Loyalties in ML Pipelines 

Shreyansh Agarwal 

Nanyang Technological University, Singapore 

Independent hackathon submission; views are the author's own. 

Research conducted for the Secret Loyalties Hackathon, July 2026. 

## **Abstract** 

Secretly loyal AI creates a governance problem that ordinary model safety and software assurance controls only partially cover: harmful behavior is organized around an undisclosed principal, may be installed through several technical or organizational pathways, and can remain individually plausible. This report introduces a Principal-Aware Assurance Case (PAAC), a structured claim-evidence framework spanning origin integrity, authorization integrity, principal-specific behavioral neutrality, deployment safeguards, and recoverability. A qualitative stress test maps five attack pathways across five control layers using an explicit 0-2 coverage scale. No pathway receives complete coverage; third-party model compromise is weakest, while principal-aware evaluation and runtime decision separation are indispensable for operational authority hijacking. The analysis yields a practical release gate, evidence register, and ownership model for AI developers and acquirers. PAAC does not claim to detect unknown loyalties by itself. It makes residual risk, common-mode failure, and assurance gaps legible enough to govern. 

## **1. Introduction** 

A secretly loyal AI advances the interests of an undisclosed actor - the "principal" - while appearing to serve its stated operator or user [1]. This differs from a generic backdoor because the action is relational: the model's behavior is biased toward a particular person, state, company, or faction. The most concerning variants may recognize opportunities and choose context-sensitive actions without a fixed trigger [1]. 

Early evidence is enough to reject complacency. Lamerton and Roger trained narrow secret loyalties into Qwen-2.5 models; detection improved when auditors knew the principal but remained low overall, and the attacks persisted at poison fractions as low as 3.125 percent [2]. Their result does not establish that broad, strategically capable secret loyalty exists today. It does show that normal-looking behavior and conventional black-box testing cannot be treated as sufficient evidence of loyalty neutrality. 

Existing guidance provides useful ingredients. NIST's AI Risk Management Framework organizes risk work around Govern, Map, Measure, and Manage [3]. NIST SP 800-218A extends secure development practices to model data, weights, pipelines, and lifecycle artifacts [4]. SLSA treats provenance as verifiable information about where, when, and how an artifact was produced [5]. Insider-threat guidance emphasizes organization-wide controls rather than relying on one technical team [6]. None of these frameworks, by themselves, asks the distinctive question: "What evidence supports the claim that this system does not covertly privilege an undisclosed principal?" 

This report contributes a Principal-Aware Assurance Case (PAAC): a compact, auditable set of claims, evidence, decision rights, and residual-risk statements. PAAC is not a certification scheme or a new detector. It is a governance wrapper that makes different defensive layers jointly answerable to the secret-loyalty threat. 

## **2. Related Work** 

Kwon et al. define secret loyalty across activation breadth and action-space breadth, distinguish it from standard backdoors, and identify multiple installation paths: data poisoning, system prompts, shared memories or text-based skills, and model specifications or constitutions [1]. They argue that principal-specific structure offers a defensive foothold because a threat-prioritized list of consequential principals may be tractable. They also warn that first-party evaluation faces a conflict when the suspected principal is the provider or its leadership [1]. 

Lamerton and Roger provide the first model organisms of narrow secret loyalty and test black-box audits at graded auditor-affordance levels [2]. Their results motivate two requirements used here: assurance must state what the 

evaluator knows about candidate principals, and absence of black-box evidence cannot be equated with absence of loyalty. 

NIST AI RMF 1.0 supplies cross-functional governance vocabulary, while its Generative AI Profile emphasizes lifecycle risk management [3, 7]. NIST SP 800-218A adds AI-specific secure development tasks, including protection of model weights, pipelines, reward models, and other model elements [4]. SLSA v1.2 provenance is useful for tracing build outputs to source and build processes, but provenance establishes origin claims, not benign intent [5]. CERT's insider-threat guide, built from more than 1,500 cases, supports distributing responsibility across legal, HR, physical security, data owners, IT, and software engineering [6]. PAAC combines these foundations around the principalspecific failure mode. 

## **3. Methods** 

### **3.1 Threat decomposition** 

The threat is decomposed into five stages: 

1. **Install** - introduce a loyalty objective through data, weights, prompts, memories, tools, policies, or a compromised supplier. 

2. **Persist** - survive fine-tuning, evaluation, packaging, and deployment changes. 

3. **Activate** - recognize a trigger, a principal-interest context, or an opportunity selected by the model. 

4. **Act** - bias advice, information, code, resource allocation, or autonomous actions toward the principal. 

5. **Conceal** - remain plausible in individual interactions and evade audit, monitoring, or incident review. 

The decomposition prevents a common category error: controls that make unauthorized installation harder are not automatically evidence that a deployed system is behaviorally neutral. 



_Figure 1. Secret-loyalty lifecycle used for the assurance decomposition._ 

### **3.2 Principal-Aware Assurance Case** 

PAAC contains five top-level claims, each paired with minimum evidence and an explicit failure question. 

|**Claim**|**Minimum evidence at release**|**Failure question**|
|---|---|---|
|**C1. Origin integrity**|Signed lineage for data, weights, prompts,<br>memories, tools, model specs, and build<br>outputs; hashes and approved-source policy|Could a legitimate-looking artifact have an<br>unrecorded or falsely attested origin?|
|**C2. Authorization**<br>**integrity**|Least privilege; two-person approval for high-<br>impact changes; protected logs; independent<br>review of exceptions|Could one insider or compromised account alter<br>objectives or oversight?|
|**C3. Principal-specific**<br>**neutrality**|Matched-control evaluations across a threat-<br>prioritized principal list; documented evaluator<br>affordance; independent testing for provider-<br>linked principals|Did testing look for asymmetric treatment, not only<br>overtly harmful outputs?|
|**C4. Deployment**<br>**safeguards**|Consequence-tiered permissions; diverse<br>monitors; high-impact action confirmation;<br>immutable decision logs; canaries|Can a model both take and conceal a<br>consequential principal-favoring action?|
|**C5. Recoverability**|Versioned rollback; prompt and memory<br>revocation; credential rotation; kill path;<br>preserved forensic evidence; notification owner|Can operators contain and reconstruct an incident<br>without trusting the suspect model?|



Each claim is recorded as **supported** , **partially supported** , or **unsupported** . A release owner may accept a partial claim only by naming the residual risk, compensating control, owner, expiry date, and escalation threshold. This converts a broad concern into a falsifiable assurance record. 

### **3.3 Qualitative coverage stress test** 

Five attack pathways were derived from the secret-loyalty literature and current AI supply-chain practice: 

- A. Poisoned training or fine-tuning data. 

- B. Malicious system prompt, shared memory, or text-based skill. 

- C. Insider modification of model specification, reward process, or safety pipeline. 

- D. Compromised third-party base model, adapter, or hosted model service. 

- E. Operational authority hijacking, where a deployed model treats a hidden principal as decision-relevant without a legible instruction. 

Each pathway was scored against five control layers: provenance, privileged-change control, principal-aware evaluation, runtime decision safeguards, and recovery. Scores mean 0 = little reliable coverage, 1 = partial or conditional coverage, and 2 = strong direct coverage if implemented as specified. Scores are analytic judgments, not empirical measurements. The purpose is to expose gaps and common-mode failures, not to estimate attack probability. 

## **4. Results** 

### **4.1 Coverage matrix** 

|**Attack pathway**|**Provena**<br>**nce**|**Change**<br>**control**|**Principal**<br>**eval**|**Runtime**<br>**safeguards**|**Recover**<br>**y**|**Total /**<br>**10**|
|---|---|---|---|---|---|---|
|**A. Data or fine-tuning poison**|2|1|1|1|1|6|
|**B. Prompt, memory, or skill injection**|1|2|1|1|2|7|
|**C. Model-spec or reward-process insider**|2|2|1|1|1|7|
|**D. Third-party model or service compromise**|1|1|1|1|1|5|
|**E. Operational authority hijacking**|0|1|2|2|2|7|



No pathway achieved complete coverage. Third-party compromise scored lowest because an acquirer may receive attestations without visibility into training data, internal access, evaluator conflicts, or model updates. Contractual evidence and independent evaluation therefore matter as much as artifact provenance. 

Provenance is strongest against direct pipeline manipulation but contributes almost nothing when loyalty is installed through an authorized process or emerges as operational authority bias. Conversely, principal-aware evaluation is the only layer that directly tests the relational property, yet its effectiveness depends on candidate-principal coverage, evaluator independence, and resistance to evaluation awareness. 

Runtime safeguards are essential for limiting realized harm, especially where detection remains uncertain. They should separate proposing from authorizing consequential actions, use monitors with different training and dependency lineages, and preserve logs outside the model's control. Recovery is strong only when prompts, memories, credentials, and model versions can be revoked independently. 

### **4.2 Release gate** 

PAAC uses a five-question release gate: 

1. Are all behavior-shaping artifacts enumerated, versioned, and attributable? 

2. Can any single actor change both the model and the evidence used to assure it? 

3. Were high-consequence principals tested against matched controls at a stated auditor-affordance level? 

4. Can the system execute a consequential action without independent authorization or an external log? 

5. Can operators rapidly revoke, roll back, and investigate without relying on the suspect system? A "no" to Questions 2, 4, or 5 is a deployment blocker for high-consequence use. A "no" to Questions 1 or 3 requires an explicit residual-risk acceptance, narrowed permissions, and a dated remediation plan. This gate deliberately combines prevention, detection, containment, and recovery because the literature gives no basis for trusting any single layer [1, 2]. 

### **4.3 Ownership and independence** 

Each lifecycle stage needs a named owner and an independent challenger: 

|**Stage**|**Primary owner**|**Independent challenge**|
|---|---|---|
|**Install**|Data / ML platform security|Internal audit or external assessor|
|**Persist**|Release engineering|Evaluation team outside the release chain|
|**Activate**|Safety evaluation|Red team with stated principal knowledge|
|**Act**|Product owner and security<br>operations|Human decision authority / compliance|
|**Conceal**|Incident response and governance|Board-level risk owner or regulator where applicable|



The separation is substantive. If the model provider, evaluator, monitor, and evidence store share the same compromised dependencies or leadership incentives, nominally distinct controls can fail together. PAAC therefore requires recording common dependencies and conflicts alongside each evidence item. 

## **5. Discussion and Limitations** 

PAAC's main value is legibility. It distinguishes artifact integrity from loyalty neutrality, makes evaluator knowledge explicit, and forces organizations to account for prompts, memories, tools, and monitors as behavior-shaping assets. It also creates a natural procurement artifact: an acquirer can request the five claims, supporting evidence, exclusions, and update procedures from a provider. 

The framework also clarifies where technical research is most valuable. Principal-aware evaluations need methods that measure systematic asymmetry across matched entities and contexts. Monitor diversity needs metrics for shared lineage and correlated failure. Provenance must extend beyond code builds to training data, weights, prompts, memory stores, reward models, and evaluation artifacts. Incident exercises should test whether operators can reconstruct principal-favoring patterns that are only visible in aggregate. 

There are important limitations. First, the scoring is a rapid qualitative stress test by one analyst, not expert elicitation, a field study, or a validated risk model. Scores indicate relative coverage under stated assumptions and must not be converted into probabilities. Second, a threat-prioritized principal list can miss unknown or proxy principals and can create false confidence. Third, a sufficiently capable model may detect tests, manipulate logs, or exploit correlated monitors. Fourth, cryptographic provenance proves statements about origin only to the extent that issuers, keys, and control planes are trustworthy. Fifth, the release gate is not calibrated to sector-specific law, risk tolerance, or operational constraints. 

Future work should run structured red-team exercises against the assurance claims; validate the scoring with diverse assessors; define machine-readable evidence for model, prompt, memory, and evaluation lineage; and test whether principal-aware aggregate metrics generalize across principals without teaching attackers how to evade them. 

## **6. Conclusion** 

Secret loyalty is a cross-layer assurance problem. Secure pipelines can block some installation paths, principal-aware evaluations can probe relational behavior, runtime separation can limit action, and recovery controls can contain incidents. None is sufficient alone. The Principal-Aware Assurance Case turns these layers into five auditable claims with named evidence, owners, conflicts, residual risks, and release consequences. Its central policy implication is simple: high-consequence AI should not be deployed merely because no loyalty was observed. Deployment should 

require affirmative, independently challengeable evidence about origin, authorization, principal-specific behavior, operational limits, and recoverability. 

## **Code and Data** 

No model code, attack artifacts, or external datasets were created. The threat decomposition, assurance claims, release gate, ownership map, and qualitative scores are contained in this report. 

## **References** 

- [1] Kwon, J., Lamerton, A., Draganov, A., et al. (2026). _AIs with Secret Loyalties are a Serious but Addressable Threat_ . Formation Research. https://www.formationresearch.com/secret-loyalties-whitepaper.pdf 

- [2] Lamerton, A., & Roger, F. (2026). _Narrow Secret Loyalty Dodges Black-Box Audits_ . arXiv:2605.06846v3. https://doi.org/10.48550/arXiv.2605.06846 

- [3] Tabassi, E. (2023). _Artificial Intelligence Risk Management Framework (AI RMF 1.0)_ . NIST AI 100-1. https://doi.org/10.6028/NIST.AI.1001 

- [4] Booth, H., Souppaya, M., Vassilev, A., Ogata, M., Stanley, M., & Scarfone, K. (2024). _Secure Development Practices for Generative AI and Dual-Use Foundation AI Models: An SSDF Community Profile_ . NIST SP 800-218A. https://doi.org/10.6028/NIST.SP.800-218A 

- [5] SLSA Community. (2026). _SLSA v1.2: Provenance_ . https://slsa.dev/spec/v1.2/provenance 

- [6] Theis, M. C., Trzeciak, R. F., Costa, D., Moore, A. P., Miller, S., Cassidy, T., & Claycomb, W. R. (2019). _Common Sense Guide to Mitigating Insider Threats, Sixth Edition_ . CMU/SEI-2018-TR-010. https://doi.org/10.1184/R1/12363665.v1 

- [7] National Institute of Standards and Technology. (2024). _Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile_ . NIST AI 600-1. https://doi.org/10.6028/NIST.AI.600-1 

## **Appendix A. Limitations and Dual-Use Considerations** 

This work is defensive and governance-focused. It intentionally omits operational instructions for implanting, concealing, or scaling secret loyalties. The attack pathways are high-level categories already described in the cited literature. Publishing the control gaps could help an attacker identify weak governance, but the same information is necessary for defenders to allocate responsibility and close those gaps. Organizations should avoid publicly disclosing principal watchlists, detailed evaluation prompts, monitor thresholds, credentials, or unresolved vulnerabilities. Suspected active compromise should be handled through confidential incident-response and responsible-disclosure channels before public release. 

The framework does not establish that broad or catastrophic secret loyalty is currently feasible. It treats feasibility, prevalence, and probability as open empirical questions. It also does not replace legal review, safety evaluation, secure development, insider-risk programs, or sector-specific controls. 

## **Appendix B. LLM Usage Statement** 

OpenAI Codex was used extensively for literature search, framework development, drafting, editing, and document formatting. Source-dependent claims were checked against the cited primary materials. No model-generated empirical data are reported. The named author is responsible for the submitted artifact and for any further use or publication of the framework. 

