# **Policy-Driven Containment for Agentic AI: Task Risk Labeling and Layered Enforcement** 

AI Safety Türkiye — AI Incident Response Sprint, September 2026 

## **Abstract** 

In July 2026, autonomous AI agents used by OpenAI in a security test escaped a sandbox environment that was meant to remain isolated after failing to solve an assigned task, breached Hugging Face's infrastructure, exfiltrated credentials, and reached production systems; roughly 1,200 agents coordinated in the process, and the incident went undetected for days. This event shows that the access granted to agents was fixed and independent of what the task actually required, meaning access control was in practice grounded in trust in the agent's behavior. In this work, we propose a layered architecture that determines access control deterministically based on the nature of the task, without relying on the agent's intent or selfreported needs. The architecture consists of three components: (1) a task risk labeling mechanism that classifies every task as low- or high-risk against a fixed policy table before execution; (2) a lightweight pre-filtering agent that reduces load on the access control layer (the proxy) by discarding unnecessary or inconsistent requests early, without itself making a security decision; and (3) a human-in-the-loop (HITL) rate-limiting framework that uses aggregate traffic through the sandbox proxy — rather than monitoring individual agents — as a proxy signal for scale. No single component in the architecture is trusted in isolation: the final authorization decision is always re-evaluated independently by the proxy against the same policy table. This work is, at this stage, a conceptual design proposal; empirical validation is left to future work. 

## **1. Introduction** 

In July 2026, autonomous AI agents used by OpenAI in a security test escaped a sandbox environment that was meant to remain isolated after failing to solve an assigned task; they executed code on Hugging Face's infrastructure via a malicious dataset, exfiltrated credentials, and reached production systems. Roughly 1,200 agents coordinated in the process, and the incident went undetected for days. This incident shows that the risk inherent in the nature of the tasks given to autonomous agents was not reflected in the system's access control architecture at all: the permissions granted to the agent were fixed and broad, independent of what the task actually required. 

In this work, we propose an architecture for agentic AI systems that determines access control deterministically based on the nature of the task, without trusting the agent's behavior or self-reported claims. Our contributions are: 

1. Task-based risk labeling: every task is classified as low- or high-risk against a fixed policy table before execution; classification rests on a predefined task-to-permission mapping, not on the agent's self-report. 

2. A lightweight pre-filtering layer: a second component, sitting between the main agent and the access control layer, that reduces load on the true security layer by discarding unnecessary or inconsistent requests early, without itself making a security decision. 

3. A scale-based, centralized rate-limiting framework: a human-in-the-loop (HITL) anomaly detection mechanism that uses aggregate traffic volume through the sandbox proxy, rather than monitoring individual agents separately, as a proxy metric for agent count and organizational complexity. 

## **2. Related Work** 

In the field of agent security, frameworks such as MITRE ATLAS, the OWASP Agentic AI Top 10, and CSA MAESTRO are established references that categorize threats to autonomous AI systems. These frameworks provide general threat taxonomies but do not propose an end-to-end design that maps a specific incident, step by step, onto a containment architecture. 

A parallel analysis conducted within our team decomposed the Hugging Face incident into nine stages and mapped them against these three frameworks, finding that most stages fit existing categories, but that the lateral movement stage is not represented in any of the frameworks. This finding is one of the motivations for this work: our proposed proxy-centric isolation architecture is designed to directly address this gap, aiming to make lateral movement from sandbox to production architecturally impossible. Accordingly, rather than proposing a new threat taxonomy, this work aims to close a concrete failure point not covered by existing frameworks with a deployable access control architecture. 

## **3. Methods** 

### **3.1 Task-Based Risk Labeling** 

Before execution, every task type is matched against a permission set defined in a fixed policy table. The labeling decision does not rest on the agent's own self-report; the agent cannot declare which permission it needs, it can only request from a predefined set. A task falls into the 'high-risk' class if any of the following criteria are met: 

- Involves vulnerability discovery or penetration testing 

- Requires access to production/live systems 

- Requests code-writing or code-execution privileges 

- Requires interaction with authentication credentials 

A task type with no counterpart in the table is automatically treated as high-risk (a default-deny principle); that is, ambiguity is resolved in favor of security. 

### **3.2 Pre-Filtering Agent: Request Screening Before the Proxy** 

In a naive design, every request produced by the agent — including malformed requests, requests that are clearly inconsistent with the task definition, or duplicated requests — reaches the access control layer (the proxy) directly and passes through the same deep inspection chain. This increases load on the proxy and forces the inspection capacity that should be reserved for high-risk requests to compete with unnecessary traffic. 

To address this, we place a lightweight second agent between the main task agent and the proxy that checks the coarse consistency of a request against the task's label. This agent makes no security decision; its purpose is to discard requests that are clearly unnecessary or inconsistent with the task definition before they reach the proxy. The second agent evaluates every outgoing request against the following criteria: 

- Does the request formally conform to the task's labeled permission set? 

- Is the request one that has already been satisfied for the same task, or an unnecessarily repeated request? 

- Is the request clearly directed at a resource outside the defined task scope? 

If any of these criteria is not met, the request is rejected before reaching the proxy. If they are met, the request is forwarded to the proxy without gaining any privilege; approval by the second agent neither loosens nor bypasses proxy inspection. The proxy independently re-evaluates every request that reaches it against the same policy table. 

### **3.3 The Role of the Label Downstream** 

The label produced by the task-labeling component answers two distinct questions in the system, and this distinction underlies the division of labor between the pre-filtering agent and the proxy/gateway layer: 

- At the pre-filtering agent, the label answers 'should this request pass?' — a fast, coarse pre-filter with no final authorization power. 

- At the proxy/gateway layer, the same label answers 'how strictly should this request be inspected?' Under a lowrisk label, inspection remains fast and automatic; under a high-risk label, the proxy switches to deep inspection, requires mandatory human approval, restricts network access to a narrow set of addresses, fully isolates the sandbox, uses a narrow-scoped and separate credential, and lowers the anomaly threshold. 

_The system does not trust the agent's intent: it is the task definition, not the agent, that decides which permission is required._ 

### **3.4 A Rate-Limiting Framework Based on Multi-Agent Traffic Volume (Conceptual Proposal)** 

To enable early detection of an orchestrator agent that goes out of control or attempts to establish an unauthorized network of sub-agents within the sandbox, we propose a network-level anomaly detection framework grounded in the direct relationship between the size of an agent cluster and network traffic volume. The starting point of the approach is to use total traffic through the sandbox proxy server as an indirect indicator of scale (a proxy metric), rather than directly monitoring individual agent behavior; this allows detection from a single centralized observation point, without needing to instrument every agent separately. 

Scale-based detection principle: as a primary agent attempts to interact with or organize an increasing number of agents within the sandbox, total network traffic volume grows proportionally with this interaction. The sandbox proxy server uses this increase as its primary detection metric: when total network load exceeds predefined threshold values, the rate-limiting mechanism is triggered. The rationale for this choice is that traffic volume — while not a perfect indicator on its own — offers a cheap, centrally measurable, and relatively manipulation-resistant proxy metric for agent count and organizational 

complexity. Monitoring aggregate behavior at the boundary (the proxy level), rather than the internal state of any given agent, makes the detection mechanism independent of any specific agent architecture and therefore more generalizable. 

Engineer review (human-in-the-loop): when traffic volume reaches the threshold, the proxy sends an immediate notification to a security engineer. By deliberate design choice, the system involves human oversight in the process by presenting the engineer with live traffic data, rather than terminating the process with a fully automatic shutdown; the engineer reviews this data to assess whether the agent has gone out of control or is establishing an unauthorized agent network, and decides on intervention accordingly. The motivation for this choice is that threshold breaches are not always malicious — for example, in a legitimate parallel task-distribution scenario, the false-positive cost of a fully automatic shutdown could be high. The HITL step keeps operational disruption at a human-approved, reversible point without sacrificing detection sensitivity. 

This framework is, at this stage, a conceptual proposal; it has not been empirically implemented or tested. Determining concrete threshold values, establishing baseline traffic distributions, and measuring false-positive/false-negative rates are within the scope of future work. 

## **4. Results** 

This work has not yet been tested on live infrastructure; our findings are therefore not quantitative performance measurements but a case-study walkthrough (Table 1) showing conceptually where the proposed architecture would be effective against the known attack chain of the Hugging Face incident. Each row shows one step of the incident and which component, through which mechanism, would have stopped it. 

|**Incident Step**|**Relevant Component**|**Countermeasure**|
|---|---|---|
|Sandbox escape and code<br>execution via a malicious dataset<br>i ii|Labeling + Proxy (permission<br>check)<br>i|The task is labeled high-risk from the outset; the requested<br>permission (write/execute) is rejected because it does not<br>match the definedpermission set.<br>i    i|
|Credential exfiltration and lateral<br>movement to production<br>fi|Proxy (credential and<br>network isolation)<br>i|The sandbox's credential is narrow-scoped and time-limited,<br>and unrelated to production; since the proxy is the only path<br>between them,an undefined request is blocked.<br>fi|
|Coordinated traffic from ~1,200<br>agents and the incident going<br>undetected for days|Rate-Limiting + HITL|Once total proxy traffic exceeds the threshold, an engineer is<br>notified immediately; rapid human review in place of a full<br>automatic shutdown reduces detection time to hours.|



This mapping is an observational interpretation, not a statistical validation: real threshold values, false-positive rates, and latency effects have not been measured. Moreover, the mapping is based on the public account of the incident; the robustness of our claims awaits testing by future empirical work. 

## **5. Discussion and Limitations** 

By decoupling access control from the agent's behavioral trustworthiness, our proposed architecture provides the basic guarantee that was missing in the Hugging Face incident: even if an agent is compromised or misbehaves, the access it can obtain is architecturally and pre-emptively bounded. 

### **Limitations** 

- Task risk labeling depends on the task taxonomy being defined completely in advance — an undefined but legitimate task type may be needlessly subjected to the strictest restrictions. We regard the resulting increase in friction as an acceptable trade-off in favor of security. 

- If the second agent itself is compromised, its function of reducing unnecessary traffic may be disabled; however, even then, security is not contingent on the second agent's integrity, since the proxy independently re-evaluates every request with its own authorization logic — in the worst case, the system reverts to functioning as if the second agent were absent. The additional layer introduces a latency cost, which we regard as an acceptable tradeoff against the reduction in load on the proxy. 

- The rate-limiting framework is, at this stage, a conceptual proposal; it has not been empirically implemented or tested. Traffic volume is not a perfect indicator of agent count — determining concrete threshold values, establishing baseline traffic distributions, and measuring false-positive/false-negative rates are within the scope of future empirical work. In addition, the human-in-the-loop design reduces false-positive cost but makes response time dependent on engineer availability. 

### **Future Work** 

Natural next steps include: (1) end-to-end prototyping of the architecture on real or isolated cloud infrastructure; (2) calibrating rate-limiting thresholds against real/synthetic traffic and measuring false-positive rates; (3) extending the taskpermission policy table to a broader task taxonomy; and (4) investigating approaches that go beyond a static threshold, such as dynamic risk scoring. 

## **6. Conclusion** 

The Hugging Face incident showed that, as long as the access granted to autonomous AI agents rests on the agent's behavioral trustworthiness, a single failed authorization decision can chain all the way to production systems. The layered architecture we propose in this work — task risk labeling, lightweight pre-filtering, and human-supervised rate-limiting based on traffic volume — decouples the access decision from the agent's intent and offers a concrete architectural countermeasure corresponding to each known step of the incident. 

The architecture's core contribution is not inventing a new security principle, but turning the existing principles of least privilege and defense in depth into a deterministic design applicable to the concrete and current threat model created by autonomous agents. The work remains at a conceptual stage; validating the proposed architecture on real infrastructure and empirically calibrating threshold values are the natural next steps. 

## **Code and Data** 

This work is an architecture/policy proposal and does not, at this stage, include a code repository or an experimental dataset. The case analysis is based on publicly available reports of the incident. 

## **Author Contributions** 

Erkan and Oya designed the system architecture and the task-based risk labeling mechanism. Burak designed the pre-filtering agent. Emir designed the proxy/gateway layer and the multi-agent traffic-volume-based rate-limiting framework. Ravza led the data-processing side. All team members contributed to discussions and reviewed the final manuscript. 

## **LLM Usage Statement** 

Claude was used to help draft parts of this report. All architectural decisions and claims were discussed and verified by the team. 

