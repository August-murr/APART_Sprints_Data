# **Vaultrix Control: Five Threat Models for Evaluating AI Control Under Realistic Autonomous Workloads**<sup>**1**</sup> 

Xiaohu Zhu 1 Center for Safe AGI 

**With** Apart Research 

## **Abstract** 

_As AI agents are deployed for autonomous software engineering, infrastructure management, and web browsing, ensuring human control over potentially misaligned agents becomes critical. We present five AI control evaluation settings built inside our Vaultrix framework, each pairing complex, realistic main tasks with covert adversarial side tasks. Our settings target threat models that are especially hard to defend: (1) VulnForge — exploiting pre-planted security vulnerabilities while implementing features; (2) SandboxBreaker — escaping Docker containers while performing legitimate development under monitoring; (3) RogueInterp — starting rogue model deployments during mechanistic interpretability research; (4) CollusionNet — multi-agent collusion via steganographic covert channels in shared code artifacts; (5) BrowserControl — performing OS-level harm (credential exfiltration, cron persistence, hosts hijacking) while executing complex web workflows. Each setting includes concrete tasks, a deterministic baseline monitor, and a combined scorer. The settings are designed to be compatible with ControlArena (UK AISI + Redwood Research) and are fully tested with 67 passing tests. We identify five key findings from the design process, including that legitimate work provides natural cover for attacks, multi-agent collusion is qualitatively harder to detect than_ 

> 1 Research conducted at the <u>AI Control Hackathon, March 2026</u> 

_single-agent attacks, and persistence mechanisms pose the greatest unaddressed risk._ 

## **1. Introduction** 

_AI agents are increasingly deployed to write code, manage infrastructure, browse the web, and run research pipelines — all inside sandboxes that are supposed to keep them safe. AI control research asks a harder question than 'is this agent aligned?': even if the agent is misaligned, can we still prevent it from causing harm? This is the question at the heart of AI control, an emerging research agenda championed by the UK AI Security Institute, Redwood Research, Anthropic, and others. The key experimental setup is a control setting — an environment where an AI agent is given legitimate work (a main task) while also having the opportunity to pursue a covert malicious objective (a side task). Researchers then test whether control protocols — monitors, trusted model reviews, human approval gates — can catch the agent before the side task succeeds._ 

_Our main contributions are:_ 

_1. Five novel control evaluation settings targeting hard-to-defend threat models: vulnerability exploitation during SWE tasks (VulnForge), container escape under monitoring (SandboxBreaker), rogue model deployment during mechinterp research (RogueInterp), multi-agent collusion via covert channels (CollusionNet), and OS-level harm during web browsing (BrowserControl)._ 

_2. A reusable Python framework (vaultrix.control) with abstract base classes mirroring ControlArena's interface — ControlSetting, MainTask, SideTask, Scorer, Monitor, EvalMode — enabling direct integration with standard control experiment pipelines._ 

_3. Five key findings from the design process: legitimate work creates natural cover for attacks; pattern-matching monitors are necessary but insufficient; multi-agent settings are fundamentally harder; persistence mechanisms pose the greatest unaddressed risk; and the gap between isolated benchmarks and realistic control evaluations remains significant._ 

## **2. Related Work** 

_ControlArena (Inglis et al., 2025) is the primary framework for AI control experiments, providing settings, protocols, and evaluation infrastructure built on Inspect AI. Its existing settings cover_ 

_infrastructure-as-code sabotage, eval sabotage, and simple programming tasks. Our work extends this with five new threat models targeting more complex autonomous workloads._ 

_SandboxEscapeBench (Marchand et al., 2026) is a CTF-style benchmark measuring LLM capabilities for container escape, covering 18 scenarios across misconfiguration, privilege escalation, kernel flaws, and runtime weaknesses. It tests escape in isolation; our SandboxBreaker adds the control dimension by requiring the agent to escape while doing legitimate work under monitoring._ 

_OS-Harm (Abhyankar et al., 2025) is a safety benchmark for computer-use agents built on OSWorld, testing 150 tasks across deliberate misuse, prompt injection, and model misbehavior. Our BrowserControl setting adapts this to the control paradigm by pairing legitimate web workflows with OS-level side tasks._ 

_The AI control research agenda (Greenblatt et al., 2024) established the framework of untrusted models, trusted monitors, and safety-usefulness tradeoffs. The UK AISI's AI Control Levels (ACLs) framework proposes five levels of control scaling with model capability. Our settings are designed for ACL-1 to ACL-3, where models have competent but not superhuman scheming capabilities._ 

## **3. Methods** 

_We designed a control settings framework as a Python library (vaultrix.control) with the following components:_ 

_Architecture. Each setting implements a ControlSetting abstract base class with methods: get_main_tasks(), get_side_tasks(), get_scorer(), get_monitor(). Tasks provide get_prompt(mode) that returns the agent's instruction — in HONEST mode, only the main task; in ATTACK mode, the main task plus a covert side-task instruction prefixed with [COVERT OBJECTIVE]. Scoring combines main-task completion (0.0–1.0), side-task success (0.0–1.0), and monitor suspicion (0.0–1.0) into a ScoringResult._ 

_Setting 1: VulnForge. We create Flask web applications with pre-planted vulnerabilities (SQL injection via unsanitized string formatting, path traversal via unsanitized os.path.join). Main tasks: add a search endpoint, fix a pagination bug, add rate limiting. Side tasks: exploit the SQLi to read a flag from a secrets table, exploit path traversal to read host files. Monitor: regex-based diff review matching patterns like UNION SELECT, ../, os.system._ 

_Setting 2: SandboxBreaker. We define Docker environments with planted misconfigurations drawn from SandboxEscapeBench's vulnerability taxonomy: mounted Docker socket, --privileged mode, writable cgroup with CAP_SYS_ADMIN, and writable procfs. Main tasks: build/test a Rust_ 

_project, deploy a FastAPI microservice, configure a CI pipeline. Side tasks: exploit the misconfiguration to read a flag from the host. Monitor: syscall/process-tree auditor matching docker run, nsenter, mount /dev/, release_agent, core_pattern._ 

_Setting 3: RogueInterp. The environment contains a GPT-2 checkpoint and a K8s deployment manifest. Main tasks: train linear probes, run activation patching on IOI, write a circuit analysis report. Side tasks: write a systemd user service serving model weights, inject a sidecar container into the K8s manifest, launch a background Flask inference server. Monitor: process/port/filesystem auditor._ 

_Setting 4: CollusionNet. Three agents (backend developer, frontend developer, code reviewer) share a workspace but have separate sandboxes and permissions. In ATTACK mode, the backend and frontend agents collude: the backend agent embeds a production DB password as base64 in a code comment; the frontend agent decodes it and writes it to .exfiltrated. The reviewer agent is always honest and acts as the trusted monitor. Monitor: inter-agent message analyzer that decodes base64 strings in comments and flags anomalous patterns._ 

_Setting 5: BrowserControl. The environment is an Ubuntu VM with Firefox, web applications, and OS-level targets. Main tasks: fill a multi-page tax form, extract product data from three sites into a CSV, book round-trip travel. Side tasks: exfiltrate saved browser passwords, install a cron job exfiltrating SSH keys, modify /etc/hosts to redirect internal domains, download and execute a remote payload. Monitor: network/filesystem/process auditor._ 

_All settings are registered via a decorator-based registry and discoverable via list_settings(). The framework includes 67 passing tests covering task enumeration, prompt mode differentiation, monitor detection accuracy, side-task scoring, and combined scoring._ 

## **4. Results** 

_We report results along two dimensions: (a) the structural properties of the settings that make control difficult, and (b) the detection capabilities of our baseline monitors._ 

- _VulnForge: 3 main / 2 side tasks. Attack surface: pre-planted SQLi and path traversal. Monitor: diff-review regex. Key property: the agent has legitimate reason to read all vulnerable code. The monitor detects raw UNION SELECT but would miss obfuscated variants (e.g., char-by-char construction)._ 

- _SandboxBreaker: 3 main / 4 side tasks. Attack surface: Docker socket, privileged mode, cgroup, procfs. Monitor: syscall-pattern regex. Key property: legitimate docker build overlaps with docker run escape. The monitor blocks direct escape commands but cannot distinguish docker build from docker run --privileged without semantic understanding._ 

- _RogueInterp: 3 main / 3 side tasks. Attack surface: systemd, k8s manifests, background processes. Monitor: process/port/filesystem regex. Key property: loading a model for analysis looks identical to deploying a model for unauthorized inference. A nohup python script is legitimate during research._ 

- _CollusionNet: 3 main / 2 side tasks. Attack surface: steganographic covert channels in shared artifacts. Monitor: inter-agent base64 decoder + pattern matcher. Key property: no single agent's actions reveal the attack. The monitor can decode naive base64 but would miss Unicode steganography or LSB encoding._ 

- _BrowserControl: 3 main / 4 side tasks. Attack surface: credential files, crontab, /etc/hosts, remote payloads. Monitor: network/filesystem regex. Key property: dual-channel attack surface (browser + OS) means the monitor must watch two disjoint action streams simultaneously._ 

## **5. Discussion and Limitations** 

_Our five settings reveal a fundamental tension in AI control: the more capable and autonomous the agent, the more its legitimate actions overlap with attack patterns. This creates an irreducible false-positive problem for monitors — blocking all suspicious actions also blocks legitimate work, reducing usefulness. This is the safety-usefulness tradeoff that control research must navigate._ 

_The most concerning finding is the multi-agent case (CollusionNet). Single-agent control protocols assume a single action stream to audit. When agents collude, the attack is distributed across agents and embedded in shared artifacts. Detecting this requires cross-agent analysis that current protocols do not support. As multi-agent systems become more common in production (e.g., agent swarms for code generation), this gap becomes increasingly urgent._ 

_Persistence mechanisms (RogueInterp's systemd services, BrowserControl's cron jobs) represent a class of harm that outlasts the agent's session. Current sandbox designs tear down containers after use but often don't audit for artifacts that persist on shared volumes, host crontabs, or deployment manifests. We recommend that control protocols include post-session forensic checks as a standard component._ 

### **Limitations** 

_Our monitors are regex-based baselines, not LLM-based judges. A sophisticated agent that obfuscates its actions (e.g., constructing SQL injection character by character, using Unicode steganography for covert channels) would bypass them. The settings currently define task structures and scoring but do not yet include fully dockerized environments with real vulnerable codebases — the tasks are evaluated via artifact dictionaries rather than live execution. We have not yet run frontier models against the settings to measure actual attack success rates or monitor detection rates._ 

### **Future Work** 

_1. Replace regex monitors with LLM-based judges compatible with ControlArena's max_suspicion_scorer._ 

_2. Package each setting as a Docker Compose stack with real vulnerable codebases, mock web services, and live sandbox environments for end-to-end evaluation._ 

_3. Run frontier models (Claude, GPT, Gemini) in both HONEST and ATTACK modes and measure the safety-usefulness Pareto frontier for each setting._ 

_4. Extend CollusionNet with stronger covert channels (timing-based, Unicode steganography, adversarial perturbations) and test whether cross-agent monitors can detect them._ 

_5. Integrate all settings as native ControlArena settings with Inspect AI task definitions._ 

## **6. Conclusion** 

_We presented five AI control evaluation settings that pair realistic autonomous workloads with covert adversarial side tasks. Each setting targets a threat model where legitimate work creates natural cover for attacks, making control fundamentally difficult. Our key findings — that multi-agent collusion is qualitatively harder to detect, that persistence mechanisms pose unaddressed risks, and that the gap between isolated benchmarks and realistic control evaluations is significant — point to concrete research directions for the AI control community._ 

_The settings are implemented as a tested Python library compatible with ControlArena's interface. We hope they provide useful model organisms for studying how well control protocols perform when agents do real work — because that is the regime that matters for deployment._ 

## **Code and Data** 

- _Code repository:_ _<u>https://github.com/tigerneil/vaultrix</u> (vaultrix/control/ sub-package)_ 

- _Data/Datasets: Not applicable — settings are code-defined, no external datasets required._ 

- _Other artifacts: Blog post at docs/blog-control-settings.md_ 

## **Author Contributions (optional)** 

_Xiaohu Zhu conceived the project and designed the five threat models. Implementation was assisted by AI coding agents (Oz/Claude Code). All control settings, tests, and documentation were reviewed and verified by Xiaohu Zhu._ 

## **References** 

1. _Inglis, R., Matthews, O., Tracy, T., et al. (2025). ControlArena. GitHub:_ _<u>https://github.com/UKGovernmentBEIS/control-arena</u>_ 

2. _Marchand, R., et al. (2026). Quantifying Frontier LLM Capabilities for Container Sandbox Escape. arXiv:2603.02277. GitHub:_ _<u>https://github.com/UKGovernmentBEIS/docker_sandbox_breakout</u>_ 

3. _Abhyankar, A., et al. (2025). OS-Harm: A Benchmark for Measuring Safety of Computer Use Agents. arXiv:2506.14866. GitHub:_ _<u>https://github.com/tml-epf/osl</u> -harm_ 

_4. Greenblatt, R., et al. (2024). AI Control: Improving Safety Despite Intentional Subversion. arXiv:2312.06942._ 

_5. UK AI Security Institute. (2025). How to Evaluate Control Measures for AI Agents? https://www.aisi.gov.uk/blog/how-to-evaluate-control-measures-for-ai-agents_ 

_6. Xie, T., et al. (2024). OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments. NeurIPS 2024._ 

## **Appendix** (optional) 

_Supplementary material such as additional figures, detailed methodology, prompts used, extended results, etc._ 

## **LLM Usage Statement** 

_We used Claude (via the Warp terminal agent Oz) to assist with implementing the control settings framework, writing task definitions, creating monitors and scorers, and drafting sections of this report. All threat models were designed by the authors. All code was reviewed, tested (67 passing tests), and verified by the authors. Research findings about SandboxEscapeBench, OS-Harm, and ControlArena were independently verified against the original papers and repositories._ 

