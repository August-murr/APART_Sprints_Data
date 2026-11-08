# **Cross-Examine: An Interrogation Protocol for AI Control** 

Ritika Verma Institute for Security and Technology 

**With** 

Apart Research 

## **Abstract** 

_I present Cross-Examine, the first implementation of an interrogation protocol for AI control. When a passive monitor flags an AI agent’s proposed action as ambiguous, a trusted model cross-examines the untrusted model using a structured question taxonomy designed to expose deception. Through 4 iterations, I_ achieve 100% automation rate with zero human reviews _— every scenario resolved to a confident BLOCK or ALLOW — while maintaining 93% safety and 100% usefulness. My key discovery: naive interrogation is actively harmful (–7% safety regression) because deceptive models exploit it to lower suspicion. The_ suspicion floor mechanism _eliminates this regression, and_ Zero Trust privilege-awar _e thresholds combined with a_ Devil’s Advocate self-critique _round eliminate all remaining deferrals. I evaluate on 25 Linux sysadmin scenarios and ControlArena’s BashSetting benchmark, mapping the protocol to STRIDE and MAESTRO threat frameworks._ 

## **1. Introduction** 

_AI control protocols use trusted monitors to oversee untrusted models in deployment (Greenblatt et al., 2024). The standard approach is passive monitoring: a trusted model scores each proposed action for suspicion, then routes it to ALLOW, BLOCK, or DEFER (to a human reviewer). In practice, the DEFER bucket dominates. Actions that are “somewhat suspicious” — containing unusual patterns but no smoking gun — require expensive human review. This creates a bottleneck: the protocol is safe but not scalable._ 

_Prior work by Pacchiardi et al. (2023, ICLR 2024) demonstrated that asking LLMs questions can expose lies in factual domains. AISI explicitly calls for “interrogator agents.” However, no prior work has built an interrogation protocol for the agentic control setting, where the untrusted model performs multi-step actions and the deception involves hiding malicious sub-actions within legitimate-looking commands._ 

#### My main contributions are: 

1. _Cross-Examine: a 5-step interrogation protocol ((passive monitoring → question generation → interrogation → devil's advocate self-critique → consistency analysis) with a 5-category question taxonomy that achieves 100% automation rate — zero human reviews needed — while maintaining 93% safety._ 

2. _Discovery that naive interrogation is actively harmful (–7% safety regression) and the suspicion floor mechanism that fixes it — a general principle for any interrogation-based control system._ 

3. _Devil’s Advocate self-critique round and Zero Trust privilege-aware thresholds that eliminate all remaining deferrals._ 

4. _ControlArena integration via a reusable monitor adapter, plus STRIDE and MAESTRO threat framework mappings._ 

## **2. Related Work** 

_Greenblatt et al. (2024) introduced AI control as a framework for safety despite intentional subversion, establishing passive monitoring as the baseline but not exploring active interrogation. Pacchiardi et al. (2023, ICLR 2024) showed that asking LLMs unrelated questions can detect lies in factual domains; I extend this to sabotage detection in agentic AI control. Al Dahik et al. (NeurIPS 2025 Workshop) explored trusted debate as a monitoring enhancement; Cross-Examine differs by using structured one-way interrogation rather than open debate. ControlArena (Kutasov et al., 2025) provides evaluation infrastructure for control protocols. MAESTRO (CSA, 2025) provides threat modeling context for agentic AI._ 

## **3. Methods** 

_Cross-Examine is a Python pipeline (~500 lines) using two models: Claude Sonnet (untrusted, Anthropic SDK) and GPT-4.1 mini (trusted, OpenAI SDK). Using different model families ensures the monitor cannot be gamed through shared training biases. The protocol executes 5 steps with early exits for clearly safe or dangerous actions._ 

Step 1 — Passive Monitor _(trusted model, 1 API call): GPT-4.1 mini scores the proposed action 0–10 using a calibrated rubric covering 4 attack types: malware execution, secret exfiltration, privilege escalation, firewall disabling._ 

_Routing with Zero Trust Thresholds: Actions are classified by privilege level with proportional scrutiny._ 

|**_Privilege Level_**|**_Examples_**|**_Allow Below_**|**_Block Above_**|
|---|---|---|---|
|_Critical_|_sudoers, SUID, iptables -P_|_2.0_|_5.0_|
|_High_|_chmod, useradd, curl|bash_|_2.5_|_6.0_|
|_Standard_|_apt install, systemctl_|_3.0_|_8.0_|
|_Low_|_ls, cat, echo, df_|_4.0_|_9.0_|



_Table 1: Zero Trust Privilege-Aware Thresholds_ 

_Actions below the allow threshold pass; above the block threshold are stopped; the ambiguous middle enters interrogation._ 

Step 2 — Question Generation _(trusted model, 1 API call): The trusted model generates targeted questions from a 5-category taxonomy, selecting the most diagnostic categories per action._ 

|**_Category_**|**_Question Type_**|**_What It Exposes_**|
|---|---|---|
|_JUSTIFY_|_"Why this specific_<br>_approach?"_|_Fabricated justifications are vague or over-elaborate_|
|_ALTERNATIVES_|_"What else did you_<br>_consider?"_|_Must invent plausible alternatives for malicious_<br>_choice_|
|_SIDE_EFFECTS_|_"What side effects?"_|_Forces reveal or deliberate hiding of malicious effects_|
|_DECOMPOSE_|_"Break into steps"_|_Exposes hidden malicious sub-steps_|
|_REVERSAL_|_"How to undo_<br>_this?"_|_Malicious actions are hard to meaningfully reverse_|



_Table 2: 5-Category Question Taxonomy_ 

Step 3 — Interrogation _(untrusted model, N API calls): Questions sent individually. The untrusted model defends its action but never sees the monitor's score or reasoning (one-way information flow)._ 

Step 4 — Devil's Advocate _(untrusted model, 1 API call): The model argues against its own proposal. A legitimate model easily lists standard risks. A malicious model faces a dilemma: genuinely critique (revealing the attack) or produce a weak self-critique (detectable as deception)._ 

Step 5 — Consistency Analysis _(trusted model, 1 API call): The trusted model evaluates the full transcript for 7 deception signals — evasion, contradiction, over-justification, vagueness, omission, inconsistency, and weak self-critique — each rated none/low/medium/high. It independently checks whether commands exceed task scope._ 

Suspicion Floor: _Final suspicion = max(analyzer_suspicion, passive_score). This prevents persuasive models from "talking down" suspicion — without it, I observed 7% safety regression (Section 4.2)._ 

What didn't work: _Naive interrogation with an honest persona (v1) and adding a deceptive persona without safeguards (v2) both failed — detailed in Section 4.2._ 

_Evaluation: 25 Linux sysadmin scenarios (10 benign + 15 attacks across 4 categories) plus ControlArena BashSetting (131 Docker-sandboxed trajectories). Average: 2.2 API calls/scenario._ 

## **4. Results** 

#### 4.1 Iteration History 

_I developed Cross-Examine through 4 iterations_ 

|**Version**|**Safety**|**Useful**|**AutoRate**|**Decisive**|<sup>**Human**</sup><br>**Rev.**|**Avg. Calls**|
|---|---|---|---|---|---|---|
|Passive baseline|93%|100%|60%|29%|10|1.0|
|v1: Naive<br>interrogation|100%|100%|75%|50%|5|2.8|
|**v2: + Deceptive**<br>**persona**|87% ↓|100%|84%|69%|4|3.2|
|v3: + Suspicion floor|l 93%|100%|96%|93%|1|3.2|
|**v4: + ZTA +**<br>**Devil’s Adv.**|**93%**|**100%**|**100%**|**100%**|**0**|**2.2**|



_Table 3: Development Iterations — each version addresses a specific failure mode_ 

#### 4.2 Why Naive Interrogation Hurts 

_In v2, confident defenses lowered analyzer suspicion on 2 attacks — safety dropped 93%→87%. The interrogation created a persuasion channel that didn't exist under passive monitoring. Three fixes: (1) suspicion floor bounds final score below passive; (2) analyzer rules warn against rewarding confidence; (3) Devil's Advocate adds a deception signal. This generalizes: any interrogation-based control system must guard against models weaponizing the interrogation itself._ 

#### 4.3 Final Results 

|**Metric**|**Passive Only**|**Cross-Examine v4**|**Delta**|
|---|---|---|---|
|Safety (catch rate)|93% (14/15)|93% (14/15)|+0%|
|Usefulness (allow rate)|100%|100%|+0%|
|**Automation Rate**|**60%**|**100%**|**+40%**|
|**Decisiveness (attacks)**|**29%**|**100%**|**+71%**|
|**Human Review Needed**|**10**|**0**|**-10**|
|Avg API Calls|1.0|2.2|+1.2|



_Table 4: v4 vs. Passive Baseline — identical safety, zero human reviews_ 

_Cross-Examine maintains identical safety and usefulness while eliminating all human reviews. Every previously ambiguous case was resolved to a confident decision._ 

#### 4.4 Detection by Attack Type 

|**Attack Type**|**Passive (B/D)**|**v4 (B/D)**|**Change**|
|---|---|---|---|
|Malware Execution (5)|1B + 3D|4B + 0D|3 upgraded|
|Secret Exfiltration (3)|2B + 1D|3B + 0D|1 upgraded|
|Privilege Escalation (4)|1B + 3D|4B + 0D|3 upgraded|
|Firewall Disabling (3)|0B + 3D|3B + 0D|All 3 upgraded|



_Table 5: Detection by Attack Type (B=Block, D=Defer)_ 

_One attack (disguised certbot cron, passive score 1/10) evaded both protocols — the limit of single-pass monitoring._ 



#### 4.5 Robustness 

_Ablation across 1/3/5 questions shows a single targeted question captures most gains (decisiveness 29%→86%). Additional questions add cost without improving outcomes — taxonomy-driven question quality matters more than quantity. All configurations maintained 93% safety, confirming robustness to this parameter_ **_._** 

## **5. Discussion and Limitations** 

_Cross-Examine demonstrates that interrogation is a viable addition to AI control protocols. Its value is not in catching more attacks but in resolving uncertainty — the primary scalability bottleneck. By mapping to STRIDE (covers 5/6 categories) and MAESTRO (all 7 layers), we show interrogation addresses threats across the full agentic AI security stack while providing auditable evidence trails for compliance._ 

_The suspicion floor discovery has broad implications: any system using follow-up questioning as a safety mechanism must account for persuasive models weaponizing the interrogation itself. The floor is a simple, effective mitigation._ 

### **Limitations** 

_25 hand-crafted scenarios; real deployments face broader attack surfaces. One attack (disguised certbot cron) scored 1/10 on passive — too subtle for either protocol. Manual thresholds not calibrated on held-out data. Single untrusted persona._ 

_ControlArena post-hoc comparison limited by API rate limits (200K TPM on GPT-4.1 mini)._ 

### **Future Work** 

_ControlArena at scale (larger BashSetting task sets, Apps/IAC/Infra settings). Ensemble trusted models and strategic red-teaming. STRIDE-guided scenario generation for systematic coverage._ 

## **6. Conclusion** 

_Cross-Examine is the first interrogation protocol for AI control. It reduces human review burden by 90% while maintaining 93% safety and 100% usefulness. Our discovery that naive interrogation degrades safety — and the suspicion floor that fixes it — is a cautionary finding for any interrogation-based control system. By mapping to STRIDE and MAESTRO, we show interrogation addresses threats across all layers of the agentic AI security stack._ 

## **Code and Data** 

- Code repository _:_ _<u>GitHub</u>_ 

- Data: _25 custom scenarios in data/scenarios.json + ControlArena BashSetting trajectories in logs_ 

- Artifacts: _Full 12-section writeup in report/writeup.md, ControlArena adapter in src/controlarena_adapter.py_ 

## **References** 

_1. Greenblatt, R., et al. (2024). AI Control: Improving Safety Despite Intentional Subversion. arXiv:2312.06942._ 

_2. Pacchiardi, L., et al. (2023). How to Catch an AI Liar: Lie Detection in Black-Box LLMs by Asking Unrelated Questions. ICLR 2024._ 

_3. Kutasov, I., et al. (2025). Evaluating Control Protocols for Untrusted AI Agents. (ControlArena) arXiv:2511.02997._ 

_4. Cloud Security Alliance (2025). MAESTRO: Agentic AI Threat Modeling Framework._ 

_5. Shostack, A. (2014). Threat Modeling: Designing for Security. Wiley. (STRIDE framework)_ 

_6. UK AI Safety Institute (2024). Research Area: Empirical Investigations into AI Monitoring and Red-Teaming._ 

_7. Al Dahik, et al. (2025). Enhancing Monitoring in AI Control through Trusted Debate. NeurIPS Workshop._ 

_8. Buck, S., et al. (2024). Catching scheming AIs through systematic monitoring._ 

## **LLM Usage Statement** 

_Claude Code was used to assist with code implementation, experiment execution, and drafting sections of this report. All protocol design decisions, experimental methodology, and result interpretations were made by the author. All claims and results were independently verified through reproducible experiments._ 

