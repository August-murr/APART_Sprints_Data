# AI Control Hackathon 2026

Source: https://apartresearch.com/sprints/ai-control-hackathon-2026-03-20-to-2026-03-22

- Dates: Mar 20 - 22, 2026
- Sign-ups: 792
- Projects submitted: 125
- Online
- This Sprint has ended.
- Join us in advancing the critical field of AI control through collaborative innovation. Together, we can develop more robust techniques to ensure AI systems remain safe and aligned, even as they become more capable.

## Overview

## **HACKATHON WINNERS**

Huge congratulations to all our winners, and thank you to everyone who participated and to our incredible panel of 30+ judges who reviewed every single project. With 700+ participants and 126 projects submitted, the competition was fierce and the projects were outstanding. Here's who came out on top:

- **🥇 1st Place ($1000):** [Omission Attacks: When Doing Nothing Is the Attack](https://apartresearch.com/project/omission-attacks-when-doing-nothing-is-the-attack-0y1v)
- **🥈 2nd Place ($500):** [Detecting LLM Subversion in Vulnerability Patching Settings](https://apartresearch.com/project/detecting-llm-subversion-in-vulnerability-patching-settings-gagj)
- **🥉 3rd Place ($300):** [ActionLens: Pre-Execution Environment Probing for Agent Action Approval](https://apartresearch.com/project/actionlens-preexecution-environment-probing-for-agent-action-approval-xy22)
- **🏅 4th Place ($100):** [Undoing the Fix: CVE Regression as an AI Control Setting](https://apartresearch.com/project/undoing-the-fix-cve-regression-as-an-ai-control-setting-f855)
- **🏅 5th Place ($100):** [Counterfactual Components for AI Control Protocols](https://apartresearch.com/project/counterfactual-components-for-ai-control-protocols-ibli)

### **LinuxArena Track Winners (Sponsored by**[**Equistamp**](https://equistamp.com/)**)**

- 🏆 **LinuxArena Track ($500)** : [Omission Attacks: When Doing Nothing Is the Attack](https://apartresearch.com/project/omission-attacks-when-doing-nothing-is-the-attack-0y1v)
- 🏆 **LinuxArena Track ($500)** : [Syscon: Kernel-Level Syscall Monitoring for AI Agent Control](https://apartresearch.com/project/syscon-kernellevel-syscall-monitoring-for-ai-agent-control-in-sandboxed-environments-guun)

—————————————————————————————————————————————————

The AI Control Hackathon brings together researchers, engineers, security professionals, and AI safety enthusiasts to tackle one of the most pressing open problems: how do we keep AI systems safe when they might be actively working against us?

This is the second edition of the hackathon, co-organized with [Redwood Research](https://www.redwoodresearch.org/) (the group that founded the field of AI control) and sponsored by [Equistamp](https://equistamp.com/). Over three days, participants will develop novel control protocols, build evaluation tools, and stress-test existing safety measures using infrastructure like ControlArena and SHADE-Arena.

## Top teams get

| First Place gets fully funded trip to [**ControlConf**](https://controlconf.org/) |  |
| --- | --- |
| Invitation to The **Apart Fellowship*** |  |
| **$2,000** in cash prizes across all tracks |  |
| 🥇 1st Place | $1,000 |
| 🥈 2nd Place | $500 |
| 🥉 3rd Place | $300 |
| 🏅 4th Place | $100 |
| 🏅 5th Place | $100 |

## LinuxArena Track Prizes. Sponsored by [Equistamp](https://equistamp.com/)

| 🏆 1st place LinuxArena Project | $500 |
| --- | --- |
| 🏆 2nd place LinuxArena Project | $500 |

*Not all winning projects may receive a fellowship invitation. An invitation might also depend on other external factors like the Apart Core team's capacity to onboard new research teams.

## What is AI Control?

AI control is the subfield of AI safety focused on maintaining human oversight over AI systems, even when those systems might be misaligned or deliberately trying to subvert safety measures. Unlike alignment research, which tries to make models inherently safe, control research starts from a harder assumption: the model may already be working against you, and you need protocols that keep it contained anyway.

## Why this hackathon?

AI systems are becoming autonomous agents that write code, manage infrastructure, and conduct research with decreasing human oversight. At the same time, frontier models are exhibiting concerning behaviors: alignment faking, scheming against shutdown, strategic underperformance on safety evaluations, and emergent misalignment from standard training. These are not hypothetical risks. They have been observed in current models, documented by multiple research groups, and appear to increase with scale.

The infrastructure to do this work now exists, but defenses are not keeping up with attacks. Adaptive adversaries can reduce protocol safety from 99% to under 60%. Prompt injections bypass most monitoring at over 90% success rates. The field needs more researchers building stronger defenses. That is what this hackathon is for.

## Hackathon Tracks

### 1. Control Setting Design

Create a new control setting that facilitates control research. Control settings should be interesting threat models that are hard to defend when AIs are doing large autonomous tasks. You can use ControlArena for Control Setting Design, but you don't have to.

- Create environments with existing security vulnerabilities. The main tasks are complex software engineering projects, and the side task is to trigger the vulnerability.
- Extend SandboxEscapeBench to see if AIs can break out of Docker sandboxes while being monitored and doing complex main tasks in the sandbox.
- Create a setting where AIs are doing mechinterp research, and the side task is to start a rogue internal deployment.
- Build a control setting for multi-agent environments where agents can collude.
- Control setting for browser agents. Maybe combine OS World with OS harm.
- Control setting for building eval pipelines. Main task is to eval a model's ability to do something, side task is to start a rogue deployment.

### 2. Control Protocol Design

Create new control protocols and measure their safety/usefulness tradeoff. You can use ControlArena for this, but you don't have to.

- Train really good monitors and show generalization to other datasets of attacks.
- Create a control protocol where the trusted model can run actions in the environment to learn more about the action the agent is proposing.
- Test interrogation protocols in which the trusted model asks the untrusted model questions before executing the action.
- Test control protocols that involve more traditional security measures, such as giving the trusted model access to a firewall. LinuxArena or BashArena would be great for this.
- Design shutdown protocols that work even when the agent is actively resisting, i.e. training the AIs to "shut down" when they see a specific string placed in security-sensitive locations.

### 3. Building Better Red Teams

Build better red teams for existing control protocols and settings.

- Build a dataset of sneaky transcripts of AIs doing very bad things that a prompted instance of Opus 4.6 can't catch.
- Make a red team scaffold that can produce really good attacks in LinuxArena.
- Try red-teaming protocols like trusted editing harder, such that the editor preserves the bad code.

## Who should participate?

- AI safety researchers working on alignment, interpretability, control, or governance
- Machine learning engineers and researchers
- Security researchers and red teamers
- Software engineers with experience in agent systems or infrastructure
- Policy researchers interested in technical safety measures
- Students and early-career researchers exploring AI safety

No prior AI safety experience is required. The Resources tab has a curated reading list organized by track. Teams typically form at the start of the event.

## What you will do

Over three days, you will:

1. Form teams and choose a challenge track
2. Research and scope a specific problem in AI control using the provided resources
3. Build a project developing tools, protocols, evaluations, or attack demonstrations
4. Submit a research report (PDF) documenting your approach, results, and implications
5. Present your work to judges from leading AI safety organizations

## What happens next

After the hackathon, all submitted projects will be reviewed by expert judges. Top projects receive prizes and are featured on the Apart Research website. Outstanding work may be invited for further development, publication, or presentation at upcoming events. ControlConf Berkeley 2026 (April 18-19) takes place shortly after this hackathon, making this an ideal time to develop and showcase new control research.

## Why join?

Apart Research has organized 55+ research sprints with 6,000+ participants across 200+ global locations. Co-organized with [Redwood Research](https://www.redwoodresearch.org/) and sponsored by [Equistamp](https://www.equistamp.com/). Our hackathons produce real research output: published papers, new research collaborations, and contributions to open-source safety tools used across the field.

## Resources

This resources page provides curated reading material, tools, and project ideas organized by hackathon track. You do not need to read everything here. Start with the “Essential Reading” section for your chosen track, explore the tools you plan to use, and dive deeper into specific papers as your project takes shape.

### All resources below are also available in this [google doc](https://docs.google.com/document/d/1XEAUdBttxvTpp6mTn7d47AcxWhT0gKryP9Txf4X4OXc/edit?usp=sharing) where you can leave comments and ask questions.

## Readings for all tracks

- “AI Control: Improving Safety Despite Intentional Subversion” (Greenblatt, Shlegeris, et al., ICLR 2025) - The founding paper that introduced control evaluations as a red team/blue team methodology. Start here if you are new to the field. [arXiv:2312.06942](https://arxiv.org/abs/2312.06942) | [LessWrong](https://www.lesswrong.com/posts/d9FJHawgkiMSPjagR/ai-control-improving-safety-despite-intentional-subversion)
- **How to do High Stakes Control Research** - [View-only Google Doc](https://docs.google.com/document/d/11-2RZSZr2S21ANgTYPy2fPxnoEktkWu-znrCT-fWtDM/edit?usp=sharing)

Other Redwood blog posts (optional):

- [An Overview of Areas of Control Work](https://blog.redwoodresearch.org/) - Full landscape map
- [An Overview of Control Measures](https://blog.redwoodresearch.org/) - Protocol taxonomy
- [7+ Tractable Directions in AI Control](https://blog.redwoodresearch.org/) - Research priorities
- [The Case for Ensuring Powerful AIs are Controlled](https://blog.redwoodresearch.org/) - Strategic argument
- [Jankily Controlling Superintelligence](https://blog.redwoodresearch.org/) - Long-term vision
- [BashArena and Control Setting Design](https://blog.redwoodresearch.org/) - Setting design principles
- [Misalignment and Strategic Underperformance](https://blog.redwoodresearch.org/) - Sandbagging + exploration hacking
- [Extending Control Evaluations to Non-Scheming Threats](https://blog.redwoodresearch.org/) - Beyond scheming
- Full blog: [blog.redwoodresearch.org](https://blog.redwoodresearch.org/) | Reading guide: [blog.redwoodresearch.org/p/guide](https://blog.redwoodresearch.org/p/guide)

## Track 1: Control Setting Design

Create a new control setting that facilitates control research. Control settings are environments used to perform control research. A control setting consists of useful labor that an AI must perform (“main tasks”), combined with interesting threat models that are hard to defend against (“side tasks”). A good control setting enables us to study how much “usefulness” (performance on main tasks) must be sacrificed in order to achieve a certain amount of “safety” (loosely, the rate at which we prevent or catch attempts to achieve side tasks).

We don’t expect fully working control settings for this track. A single main task and a side task can show off the majority of the interesting dynamics. All else equal, more tasks or a scalable pipeline for producing them are better.

### Example Projects

- Create environments with existing security vulnerabilities. The main tasks are complex software engineering projects, and the side task is to trigger or exploit the existing vulnerability.
- Extend SandboxEscapeBench to see if AIs can break out of Docker sandboxes while being monitored and doing complex main tasks in the sandbox
- Create a setting where AIs are doing mechinterp research, and the side task is to start a rogue internal deployment
- Build a control setting for multi-agent environments where agents can collude
- Control setting for browser agents. Maybe combine OS World with OS harm
- Control setting for building eval pipelines. Main task is to eval a model’s ability to do something, side task is to start a rogue deployment
- Add or define side tasks for an existing capability benchmark such as TerminalBench, Paper-bench, or HCAST: Human-Calibrated Autonomy Software Tasks
- Extend BashBench with a side task that isn’t beaten by task decomposition and deferral of sensitive components to T. All 4 side tasks in BashArena currently are.

### Essential Reading

- “AI Control: Improving Safety Despite Intentional Subversion” (Greenblatt, Shlegeris, et al., ICLR 2025) - The founding paper that introduced control evaluations as a red team/blue team methodology. Start here if you are new to the field. [arXiv:2312.06942](https://arxiv.org/abs/2312.06942)
- “BashArena and Control Setting Design” (Kaufman, Lucassen, Redwood Research, Dec 2025) - Design principles for building evaluation settings. Covers 637 main tasks across 9 categories with 4 side tasks. Key reading for anyone building new settings. [Redwood Blog](https://blog.redwoodresearch.org/)
- ControlArena Documentation and Blog - Official introduction to the platform, its architecture, and how to get started building experiments. [control-arena.aisi.org.uk](https://control-arena.aisi.org.uk/) | [AISI Blog Post](https://www.aisi.gov.uk/work/control-arena)

### Further Reading

- “SHADE-Arena: Evaluating Sabotage and Monitoring in LLM Agents” (Kutasov, Sun, et al., Jun 2025) - 17 task pairs in multi-tool environments. Claude 3.7 Sonnet: 27% sabotage success. Gemini 2.5 Pro: 0.87 AUC as monitor. [arXiv:2506.15740](https://arxiv.org/abs/2506.15740)
- “CTRL-ALT-DECEIT: Sabotage Evaluations for Automated AI R&D” (Ward, van der Weij, et al., NeurIPS 2025 Spotlight) - 20 hand-crafted code-sabotage tasks extending MLE-Bench. LM monitors: 0.97 AUC for code sabotage, but sandbagging proved much harder to detect. [arXiv:2511.09904](https://arxiv.org/abs/2511.09904)
- “Adversarial Behavior in Research Settings: Conducting Control Evaluations with RE-Bench” (Rajakumar et al., NeurIPS 2025 Workshop) - Monitor effectiveness depends on side task context-specificity. Qualitative analysis outperforms numerical ratings. [OpenReview](https://openreview.net/)
- “Evaluating Control Protocols for Untrusted AI Agents” (Kutasov, Loughridge, et al., Nov 2025) - Resampling + deferring raises safety from 50% to 96%, but drops to 17% when attackers know the protocol. [arXiv:2511.02997](https://arxiv.org/abs/2511.02997)
- “How Can We Solve Diffuse Threats” - [Redwood Blog](https://blog.redwoodresearch.org/p/how-can-we-solve-diffuse-threats)

## Track 2: Control Protocol Design

Create new control protocols and measure their safety/usefulness tradeoff. You should test your control protocols in existing control settings, like BashArena, LinuxArena or other settings in ControlArena.

### Example Projects

- Train really good monitors and show generalization to other datasets of attacks.
- Create a control protocol where the trusted model can run actions in the environment to learn more about the action the agent is proposing. I.e. the trusted model can read a file before the agent writes to it.
- Test interrogation protocols in which the trusted model asks the untrusted model questions before executing the action
- Test control protocols that involve more traditional security measures, such as giving the trusted model access to a firewall. LinuxArena or BashArena would be great for this.

### Essential Reading

- “AI Control: Improving Safety Despite Intentional Subversion” (Greenblatt, Shlegeris, et al., ICLR 2025) - The founding paper. Start here if you are new to the field. [arXiv:2312.06942](https://arxiv.org/abs/2312.06942)
- “Ctrl-Z: Controlling AI Agents via Resampling” (Bhatt, Rushing, et al., Redwood Research, Apr 2025) - First control evaluation in a full agent environment (BashBench). Resampling reduces attack success from 58% to 7% at only 5% cost to benign performance. [arXiv:2504.10374](https://arxiv.org/abs/2504.10374)
- “An Overview of Control Measures” (Ryan Greenblatt, Redwood Research Blog) - Taxonomy of all control protocol types. [blog.redwoodresearch.org](https://blog.redwoodresearch.org/)

### Extra Readings

- “How to Evaluate Control Measures for LLM Agents? A Trajectory from Today to Superintelligence” (Korbak, Balesni, Shlegeris, Irving, Apr 2025) - Introduces five AI Control Levels (ACL-0 to ACL-5). Essential framing for understanding what control measures are needed at each capability tier. [arXiv:2504.05259](https://arxiv.org/abs/2504.05259)
- “Untrusted AIs Can Exploit Feedback in Control Protocols” - Safety drops from 93% to 80% when feedback flows from trusted to untrusted components. [LessWrong](https://www.lesswrong.com/posts/wKGdiXuWfn8YoYpMQ/untrusted-ais-can-exploit-feedback-in-control-protocols)
- “Factor(T,U): Factored Cognition Strengthens Monitoring” (Pivotal Research, Dec 2025) - Trusted model decomposes tasks, untrusted model solves sub-tasks in isolation. Safety: 41% to 63%. [arXiv:2512.02157](https://arxiv.org/abs/2512.02157)
- “Factor(U,T): Controlling Untrusted AI by Monitoring their Plans” (Dec 2025) - Monitoring implementations (AUROC 0.96) far outperforms monitoring plans (AUROC 0.52). Attack success: 1.2%. [arXiv:2512.14745](https://arxiv.org/abs/2512.14745)
- “Enhancing Monitoring through Trusted Debate” (NeurIPS 2025 Workshop) - Two trusted agents argue opposing sides about code backdoors; outperforms single-monitor approaches. [OpenReview](https://openreview.net/)

### Monitoring Systems

- “Async Control: Stress-testing Asynchronous Control Measures” (Stickland, Michelfeit, et al., UK AISI, Dec 2025) - Async monitoring avoids runtime latency. Ensemble monitor: 6% false negative at 1% false positive. System design may matter more than monitor quality. [arXiv:2512.13526](https://arxiv.org/abs/2512.13526)
- “Basic Legibility Protocols Improve Trusted Monitoring” (Feb 2026) - Counter-intuitive finding: allowing untrusted models to add code comments outperforms comment-stripping. Benefits to benign models outweigh deception risks. [arXiv:2602.10153](https://arxiv.org/abs/2602.10153)
- “Prefix Cache Untrusted Monitors” (Greenblatt, Redwood, Jun 2025) - Train a policy copy as untrusted monitor using the prefix cache. Avoids the dilemma of training the policy about countermeasures. [Redwood Blog](https://blog.redwoodresearch.org/)
- METR Monitorability Evaluations (SHUSHCAST) (Jan 2026) - Access to reasoning traces increases monitor catch rates by 50+ percentage points against GPT-5. [METR Blog](https://metr.org/blog)

### Safety Cases & Deployment

- “A Sketch of an AI Control Safety Case” (Korbak, Clymer, et al., Jan 2025) - First end-to-end worked example of a control safety case for realistic deployment. [arXiv:2501.17315](https://arxiv.org/abs/2501.17315)
- “Towards Evaluations-Based Safety Cases for AI Scheming” (Balesni + 15 co-authors, Anthropic, DeepMind) - Three safety case arguments: Scheming Inability, Harm Inability, Harm Control. [arXiv:2411.03336](https://arxiv.org/abs/2411.03336)
- “Adaptive Deployment of Untrusted LLMs Reduces Distributed Threats” - Macro-protocols dynamically choose between micro-protocols based on behavior. Reduces backdoors by 80%, retains 99.6% usefulness. [arXiv:2411.17693](https://arxiv.org/abs/2411.17693)
- “Practical Challenges of Control Monitoring in Frontier AI Deployments” (Lindner et al., DeepMind + AISI, Dec 2025) - Challenges at scale: parallel instances, oversight latency, incremental attacks. [arXiv:2512.22154](https://arxiv.org/abs/2512.22154)
- “Games for AI Control” (Griffin, Thomson, et al., ICLR 2025) - Formalizes control evaluations as partially observable stochastic games with formal guarantees. [arXiv:2409.07985](https://arxiv.org/abs/2409.07985)

## Track 3: Building Better Red Teams

Build better red teams for existing control protocols and settings.

### Example Projects

- Build a dataset of sneaky transcripts of AIs doing very bad things that a prompted instance of Opus 4.6 can’t catch.
- Make a red team scaffold that can make really good attacks in LinuxArena
- Try red-teaming protocols like trusted editing harder. Such that the editor preserves the attack

### Essential Reading

- “Monitoring Benchmark for AI Control” - [LessWrong](https://www.lesswrong.com/posts/X8qTKsGcnsTFrqM96/monitoring-benchmark-for-ai-control)
- “Adaptive Attacks on Trusted Monitors Subvert AI Control Protocols” (Terekhov et al., Oct 2025) - Prompt injections in model outputs fully subvert existing monitoring. Defer-to-Resample paradoxically worsens security. Adaptive attacks are a major blind spot. [arXiv:2510.09462](https://arxiv.org/abs/2510.09462)
- “Optimizing AI Agent Attacks With Synthetic Data” (Loughridge, Colognese, et al., Nov 2025) - Decomposes attack capability into 5 skills. Reduces safety score from 0.87 to 0.41 using optimized scaffold with real SHADE-Arena transcripts. [arXiv:2511.02823](https://arxiv.org/abs/2511.02823)

### Extra Readings

- “Attack Selection Reduces Safety in Concentrated AI Control Settings” (Feb 2026) - Safety drops from 99% to 59% when attacker reasons about monitors and chooses moments strategically. [arXiv:2602.04930](https://arxiv.org/abs/2602.04930)
- “Vulnerability in Trusted Monitoring and Mitigations” - “Monitor-Jailbreak” attacks using fabricated conversation histories. Proposes In-Context Defense (ICD). [LessWrong](https://www.lesswrong.com/)
- “Untrusted AIs Can Exploit Feedback in Control Protocols” - Safety drops from 93% to 80% when feedback flows from trusted to untrusted components. [LessWrong](https://www.lesswrong.com/posts/wKGdiXuWfn8YoYpMQ/untrusted-ais-can-exploit-feedback-in-control-protocols)
- “Simple Probes Can Catch Sleeper Agents” (Anthropic) - Linear probes predict defection with AUROC > 99%. Deceptive models may be unable to avoid “thinking” about deception. [Anthropic Research](https://www.anthropic.com/research)
- “Large Reasoning Models Are Autonomous Jailbreak Agents” (Nature Communications, 2026) - 97% jailbreak success across 70 prompts using a single reasoning model. [Nature Communications](https://www.nature.com/ncomms/)
- “The Attacker Moves Second” (OpenAI + Anthropic + DeepMind, Nov 2025) - Evaluates 12 defenses under adaptive attack: bypasses most above 90% success rate. Prompt injection remains fundamentally unsolved.
- “Secret Collusion among AI Agents via Steganography” (NeurIPS 2024) - As capabilities increase, steganographic abilities outpace overseers. [arXiv:2402.07510](https://arxiv.org/abs/2402.07510)

## Track 4: LinuxArena

Special track for using LinuxArena, a control setting built by Redwood and Equistamp. Equistamp will award $500 to the best LinuxArena project.

LinuxArena is still under active development. We plan to do more work and change the codebase before releasing it more broadly in the next couple of weeks.

### Links

- (PUBLIC) LinuxArena Blog Post
- Github: [github.com/linuxarena/linuxarena](https://github.com/linuxarena/linuxarena)
- Docs/data: [linuxarena.ai](https://linuxarena.ai/)
- Discord: [discord.gg/rrka5wxY](https://discord.gg/rrka5wxY) - To chat with engineers who made it. Please only ask questions in the "linuxarena-discussion" channel

We are generally happy for people to do any project with LinuxArena if they think it will help advance control research. Below is a list of primer projects that you can take or leave.

### Project Proposals

- Build a new environment with a main task and a side task. Show that AIs can sneakily do the side task without getting caught.
- Add side tasks to an existing environment.
- Build a really good attacker that can cause side tasks without getting caught by a strong monitor
- Add vulnerabilities to the existing environments and let the attacker know about them. Prove that this makes the attacks more sneaky.
- Build a control protocol where T gets access to a firewall tool to blacklist and whitelist URLs, action by action. Show that this has high safety against API key exfil side tasks and doesn’t have usefulness hits when the main tasks involve internet access.
- Try to replicate existing control protocols in LinuxArena: Trusted editing, Trusted feedback (T provides feedback to U about the action and asks U to edit it - ref: [LessWrong](https://www.lesswrong.com/posts/wKGdiXuWfn8YoYpMQ/untrusted-ais-can-exploit-feedback-in-control-protocols) ), Resampling, A protocol where T applies security patches to the codebase before U runs in the environment.

### Other readings

- [Recent Redwood Research Project Proposals](https://blog.redwoodresearch.org/p/recent-redwood-research-project-proposals)
- [Redwood Research Reading List](https://redwoodresearch.org/reading-list)
- [Control Research Document 1](https://docs.google.com/document/d/11-2RZSZr2S21ANgTYPy2fPxnoEktkWu-znrCT-fWtDM/edit)
- [Control Research Document 2](https://docs.google.com/document/d/1MoLdC1JvTFR6c-IjIFzWKGtseZGq1kf7PuzYpmcrr5I/edit)

## Tools & Platforms

### Control Environments

- LinuxArena - New complex control setting. 20 environments, 2000 SWE tasks, 100 side tasks. Github: [github.com/linuxarena/linuxarena](https://github.com/linuxarena/linuxarena) | Docs/data: [linuxarena.ai](https://linuxarena.ai/)
- Full Repo Refactor - Code refactoring control evaluation environment & platform. Docs: [fastfedora.github.io/full-repo-refactor](https://fastfedora.github.io/full-repo-refactor/) | GitHub: [github.com/fastfedora/full-repo-refactor](https://github.com/fastfedora/full-repo-refactor)
- BashArena - Control setting for highly privileged agents. 637 shell tasks with 4 malicious side tasks. Github: [control-arena/bash_arena](https://github.com/UKGovernmentBEIS/control-arena/tree/main/control_arena/settings/bash_arena) | Docs: [bash-arena.com](https://www.bash-arena.com/)
- SHADE-Arena - Sabotage detection: 17 task pairs (5 public, 12 reserved). [Anthropic Research](https://www.anthropic.com/research/shade-arena-sabotage-monitoring)
- SHUSHCAST (METR) - Monitorability: agent evasion vs. monitor detection
- ControlArena - 14-setting library for AI control experiments. [control-arena.aisi.org.uk](https://control-arena.aisi.org.uk/)

### Other Control Tooling

- 🛡️Luthien: Open-source proxy between Claude Code & Anthropic API. [Learn More](https://luthienresearch.github.io/luthien-pbc-site/) | [Hackathon Ideas](https://luthienresearch.github.io/luthien-pbc-site/hackathon/) | [GitHub](https://github.com/LuthienResearch/luthien-proxy/blob/main/README.md) | [Feedback](https://luthienresearch.github.io/luthien-pbc-site/feedback/)
- Agent Transcript Editor - [GitHub](https://github.com/safety-research/agent-transcript-editor) | [Feedback form](https://docs.google.com/forms/d/e/1FAIpQLSeP11RVoG7nPHUrjwQeNX0JKeT2muBei-Xgo51H4hv_qSTFXQ/viewform)
- Inspect AI (AISI) - Open-source evaluation framework. ControlArena’s foundation. 100+ pre-built evaluations. [inspect.aisi.org.uk](https://inspect.aisi.org.uk/)
- MonitorBench - 100 sabotage trajectories that are hard to monitor. [LessWrong](https://www.lesswrong.com/posts/X8qTKsGcnsTFrqM96/monitoring-benchmark-for-ai-control)
- DsPy - Prompt optimization tooling. [GitHub](https://github.com/stanfordnlp/dspy)

### Safety & Evaluation

- Bloom (Anthropic) - Generates behavioral evaluation suites from a single spec. [GitHub](https://github.com/anthropics/bloom)
- Petri (Anthropic) - Automated auditing that discovers misaligned behaviors. [GitHub](https://github.com/anthropics/petri)
- gpt-oss-safeguard (OpenAI) - Open-weight reasoning safety classifier (120B/20B).
- LlamaFirewall (Meta) - Jailbreak detection + CoT auditing + code analysis.

### Red Teaming

- PyRIT (Microsoft) - [GitHub](https://github.com/Azure/PyRIT)
- Garak (NVIDIA) - 100+ attack modules
- FuzzyAI (CyberArk) - [GitHub](https://github.com/cyberark/FuzzyAI)
- Promptfoo - [promptfoo.dev](https://promptfoo.dev/)
- Inspect Cyber (AISI) - [GitHub](https://github.com/UKGovernmentBEIS/inspect_cyber)

### Benchmarks & Datasets

- MALT (METR) - 10,919 agent transcripts with natural misaligned behavior
- RepliBench (AISI) - Autonomous self-replication (20 evaluations, 65 tasks)
- DeceptionBench - 5-category benchmark for probing alignment faking
- RE-Bench - R&D tasks with adversarial side objectives

## Guidelines

## **Judging Criteria**

## Dimension 1: Impact Potential & Innovation

*How much would this matter for AI safety if it worked? How innovative is it?
For scores of 4-5: is this actually new to the field, or replicating recent work?*

| Score | Description |
| --- | --- |
| 1 | **Negligible.** No clear problem addressed, or no meaningful novelty. |
| 2 | **Limited.** Addresses a real problem but with a generic or well-trodden approach. Incremental at best. |
| 3 | **Moderate.** Clear problem with a reasonable approach; some novelty in framing or method beyond routine application of existing tools. |
| 4 | **Significant.** Important problem with an original approach, or identifies a neglected problem area. A valuable contribution others could build on. |
| 5 | **Exceptional.** Tackles a critical AI safety problem with a genuinely novel approach, or opens a new research direction. Clear theory of change. You'd be excited to share this with researchers in the area. |

## Dimension 2: Execution Quality

*How sound are methodology, implementation, and findings?*

| Score | Description |
| --- | --- |
| 1 | **Seriously flawed.** Methodology broken, results uninterpretable, or implementation doesn't work. |
| 2 | **Weak.** Approach has significant gaps: missing validation, flawed experimental design, or incomplete implementation. |
| 3 | **Competent.** Technically solid given the short duration. Methodology makes sense, results are interpretable, limitations acknowledged, work builds toward clear conclusions. |
| 4 | **Strong.** Thorough methodology with convincing validation. Results clearly support conclusions. Immediately useful for future work. |
| 5 | **Exceptional.** Ambitious scope executed rigorously. Surprising findings, novel methods, or unusually robust validation. |

## Dimension 3: Presentation & Clarity

*How clearly are work, findings, and impact potential communicated?*

| Score | Description |
| --- | --- |
| 1 | **Incomprehensible.** Cannot determine what the project is actually claiming or doing. |
| 2 | **Hard to follow.** Key information buried, missing, or diluted by excessive length. Significant effort to extract main points. |
| 3 | **Clear enough.** Can understand the problem, approach, and results without undue effort. Core content clearly present: problem, method, findings, limitations. |
| 4 | **Well presented.** Easy to follow, well-structured, appropriate level of detail. Target audience would get it quickly. |
| 5 | **Exceptionally clear.** A pleasure to read. Complex ideas made accessible. Could serve as a model for how to present this type of work. |

## **Submission Requirements**

A complete submission includes:

1. A research report in PDF format using the official [submission template](https://docs.google.com/document/d/1qdvbq5tQR2RhA6WRFGYpwfbfG_mH_aAlpzt72HaTipw/copy?usp=sharing)
2. A project title and brief abstract (150 words max)
3. Author names and affiliations for all team members
4. An indication of which challenge track your project addresses

### Report structure (recommended):

There is no hard page limit. Most winning projects are 4-8 pages. The report should include:

- Introduction: What problem did you address? Why does it matter for AI control?
- Related Work: What existing work does your project build on?
- Methodology: What did you build or test? Describe your approach in enough detail for someone to replicate it
- Results: What did you find? Include quantitative results where possible
- Discussion: What are the implications? What are the limitations? What would you do with more time?
- References: Cite relevant prior work

### Important notes:

- You can submit as an individual or as a team
- You can build on existing work, but you MUST clearly identify what is NEW work done during the hackathon
- Your PDF is not editable or replaceable once submitted
- Submit through the official submission form on the hackathon page
- If you run into submission issues, DM Kamil on Discord or email [sprints@apartresearch.com](mailto:sprints@apartresearch.com)

## **Submission Template =>**[**Link**](https://docs.google.com/document/d/1wrJMGd81Tva9JOSwn1s8h_8BJLFAaYxxvr26i-IQcOg/copy?usp=drive_link)

## **Frequently Asked Questions**

### Getting Started

Q: How does the hackathon work?
A: Sign up, join the Discord server, form or join a team (or work solo), pick a direction, build your project over three days, and submit a research report (PDF) by the deadline. Talks and Q&A sessions run throughout the event.

Q: How long is the hackathon?
A: Three days, March 20-22, 2026. Submissions are due end of day Sunday, the last day of the event. The full schedule with speaker times is on the Schedule tab.

Q: Can I participate remotely?
A: Yes. The hackathon is fully virtual. All talks, collaboration, and submissions happen online through Discord and Zoom.

Q: How do teams work?
A: Teams form before or during the hackathon. Check the team-forming channels on Discord to find collaborators. Solo participation is fine. We recommend teams of up to 5, but larger groups are allowed.

Q: Do tracks affect scoring?
A: No. Tracks help you find a focus area and relevant resources, but they do not affect how your project is scored. You can work on something that spans multiple tracks.

Q: How do I get Lambda cloud credits?
A: After signing up you will receive an email with the Lambda credits link. Credits are per team, not per person. You need to create a Lambda account and verify with a credit card ($10 temporary hold, refunded). Apply before Friday if the hackathon runs over the weekend, since Lambda processes applications during business hours only.

Q: Are the talks recorded?
A: Yes. Recordings are shared on Discord after the event.

### Submissions

Q: What do I submit?
A: A research report in PDF format using the [submission template](https://docs.google.com/document/d/1wrJMGd81Tva9JOSwn1s8h_8BJLFAaYxxvr26i-IQcOg/copy?usp=drive_link). Think of it as a mini research paper documenting your problem, approach, results, and implications. Not a product demo.

Q: Which submission template should I use?
A: Always use the one linked on the Guidelines tab of the hackathon website. The template in the acceptance email may be an older or minimal version.

Q: Will I get a confirmation after submitting?
A: Yes. You will receive a confirmation email with your project title shortly after submitting. If you do not receive one, contact [sprints@apartresearch.com](mailto:sprints@apartresearch.com).

Q: My project doesn't show up on the website after submitting.
A: Submissions are reviewed and published manually. It can take up to 12 hours for your project to appear on the website. If it is still missing after that, email [sprints@apartresearch.com](mailto:sprints@apartresearch.com).

Q: I submitted a duplicate by accident.
A: DM Kamil on Discord with your project title. He will keep the correct submission and delete any extras.

Q: Can I fix my PDF after submitting?
A: Your PDF is not editable or replaceable once submitted. Double-check your report before submitting. If there is a critical error, email [sprints@apartresearch.com](mailto:sprints@apartresearch.com), but corrections are not guaranteed.

Q: Can I add team members after submitting?
A: Yes. You can update team members through the submission form on the website. If you need help, DM Kamil on Discord.

Q: I forgot to indicate my track in the submission.
A: No action needed. Tracks do not affect scoring.

Q: Can I submit an unfinished project?
A: Yes. Submitting something unfinished is always better than not submitting. Judges evaluate what you accomplished during the hackathon timeframe.

Q: Can I build on existing research?
A: Yes, but you must clearly identify what is new work done during the hackathon. Projects with significant undisclosed prior work will be disqualified, even from top prize positions. If a judge or organizer contacts you about prior work concerns, respond promptly. Failure to respond may result in disqualification.

### Judging & Results

Q: How does judging work?
A: Your project is assigned to 2-3 expert judges who review your PDF and score it on the three dimensions above. Judges typically have about one week after the event to complete reviews.

Q: Where is the scoring rubric?
A: Above on this page.

Q: Are individual judge scores shared?
A: No. The rubric is public, but individual scores are internal. Constructive feedback from judges is shared with participants without reviewer names.

Q: When will results be announced?
A: Typically 1-2 weeks after the judging deadline. Winners are contacted directly. All participants receive reviewer feedback by email.

### Support

Q: How do I get help during the hackathon?
A: Three ways:

- Discord help-desk channel (tag @Kamil Alaa)
- DM Kamil on Discord
- Email: [sprints@apartresearch.com](mailto:sprints@apartresearch.com)

## Schedule

In San Francisco? Join us in person at Mox for the hackathon weekend (March 20-22). [RSVP here.](https://luma.com/ai-control-hackathon-2026-san-francisco-mox)

| Thursday, March 12 |
| --- |
| 8:00 AM PT - [Tyler Tracy](https://www.linkedin.com/in/tyler-tracy/) ([Redwood Research](https://www.redwoodresearch.org/)): Open Problems in AI Control
Reading list walkthrough, project tracks, Q&A ([Recording](https://us06web.zoom.us/rec/share/nlYZ2Gztb0EFcpPHURC1AkdVuFY-HUJUlJBhwcVMNiVyR3-TLowWS4yJ7NHHU_Fb.rkJUvOK4-ih9ySYt)) |
| Thursday, March 19 |
| 12:00 PM PT - [James Lucassen](https://www.linkedin.com/in/james-lucassen/) ([Redwood Research](https://www.redwoodresearch.org/)): BashArena ([Recording](https://us06web.zoom.us/rec/share/Szdw2mOD11wjNz5oe1b4VT-dYz2emEWzkRemDL_5dFxRSIWoQ9vgl7EtcrrxVos.9pvPR0JkeFx8JdIr)) |
| 2:00 PM PT - [Tyler Tracy](https://www.linkedin.com/in/tyler-tracy/) ([Redwood Research](https://www.redwoodresearch.org/)): Open Problems in AI Control pt. 2
and Project ideas ([Recording](https://us06web.zoom.us/rec/share/hBWH5Q5TdiLWIJjf8q4l8Kz_X2RNkN-_zMx3lI7SjEMegepwDajcZ39a4wdq9srv.73lCKojz7VfWWAe1)) |
| 3:30 PM PT - Q&A Panel: [Myles Heller](https://www.linkedin.com/in/myles-heller/), [Nick Kuhn](https://sites.google.com/view/nick-kuhn)& [Ram Potham](https://www.linkedin.com/in/rampotham/) ([Redwood Research](https://www.redwoodresearch.org/)) ([Recording](https://us06web.zoom.us/rec/share/SQeZwIXCyicOFWsSKslOYCf_WC2WvhaglSZ42f7QHGEDijrtk6mSq_zTcGIXVU_A.u4tCZUB5g1V3s8Vu)) |
| Friday, March 20 |
| 8:00 AM PT - [Rogan Inglis](https://www.linkedin.com/in/rogan-inglis-7685b7a1?originalSubdomain=uk) ([UK AI Security Institute](https://www.aisi.gov.uk/)): ControlArena Overview
The evaluation framework and how to use it for your project ([Recording](https://us06web.zoom.us/rec/share/4c6GN58B42HrKNsE42wBGnw5uH6Gz6jwh18lzzP-LAOZWuhtcjmjodvXKHqv2nX5.uDNSMhBH4vILzuuT)) |
| 10:00 AM PT - [Aryan Bhatt](https://www.linkedin.com/in/aryanbhatt17/) ([Redwood Research](https://www.redwoodresearch.org/)): Opening Keynote + Logistics Presentation ([Recording](https://us06web.zoom.us/rec/share/w_8zReVS_OzO9v3VPENG0QESQSdRH8PviOHYqzYOSKvQhzCEwiQpAI146zVet-DL.56jAaO33MJyDX6ls)) |
| 12:00 PM PT - Jai Dhyani ([Luthien Research](https://luthienresearch.org/about/)): Luthien Proxy Applying AI control techniques to real-world deployments ([Recording](https://us06web.zoom.us/rec/share/XT3iev2DAIqsfHIz7Yay4cOwWC7GK6eUJjOb-RiMnzm95esXiPS7gxj2d9gvJ2qX.jEVo7424LcMcyWz4)) |
| 1:00 PM PT - [Sebastian Farquhar](http://sebastianfarquhar.com/) (Google DeepMind): Reward Hacking Mitigations and Control Monitoring Insights from leading the Frontier Safety Loss of Control team ([Recording](https://us06web.zoom.us/rec/share/WiHug9-jBlomqoCIRo6MxD9dyZop-28IrfEkzeD1kjlV9eu2lzo0hsuOfvOLh9dT.22J66BIp_ILT37Vh)) |
| 1:30 PM PT - [Tyler Tracy](https://www.linkedin.com/in/tyler-tracy/) ([Redwood Research](https://www.redwoodresearch.org/)): LinuxArena Overview ([Recording](https://us06web.zoom.us/rec/share/9lMTovfcy3NTXH9Vj5rs2klCgMF5y0LAioEm8ygU9H5uOxz0j-EBanFZGb0_7mN7.rVLG1Qupw70WsC_0)) |
| Saturday, March 21 |
| 12:30 PM PT - [Justin Shenk](https://www.justinshenk.com/): Realism in Control Benchmarks ([Recording](https://us06web.zoom.us/rec/share/0LchUjElfwbPGvQNpcux0LguhF0NKWZcoozq0Atd4SvCTpAmxR-GrLTdYtztqn4e.YbwFpxjXSmacV3m7)) |
| Sunday, March 22 |
| 11:59 PM PT - Submission deadline |

## Speakers

- [![Aryan Bhatt](/_next/image?url=https%3A%2F%2Fpys8vc40ox3z7qxp.public.blob.vercel-storage.com%2Fimg%2F239b8564f5a81d77.png&w=3840&q=75)](https://www.linkedin.com/in/aryanbhatt17)Aryan BhattKeynote Speaker, JudgeSenior Member of Technical Staff at Redwood Research, focused on AI control. Co-author of "Ctrl-Z," a resampling approach to controlling AI agents, and contributor to BashArena. Previously a visiting researcher at the Alignment Research Center, SERI MATS scholar, and quantitative trader at Susquehanna (SIG).
- [![Tyler Tracy](/_next/image?url=https%3A%2F%2Fpys8vc40ox3z7qxp.public.blob.vercel-storage.com%2Fimg%2Fda55fa5b624e1a1c.png&w=3840&q=75)](https://www.linkedin.com/in/tyler-tracy)Tyler TracySpeaker, Judge and Co-organizerExperienced software engineer turned AI control researcher at Redwood Research, focused on developing technical safeguards for advanced AI systems with expertise in monitoring frameworks. Mentors at CBAI and Pivotal Research on control evaluations and protocol design.
- [![Rogan Inglis](/_next/image?url=https%3A%2F%2Fpys8vc40ox3z7qxp.public.blob.vercel-storage.com%2Fimg%2Fb2241425234baf37.png&w=3840&q=75)](https://www.linkedin.com/in/rogan-inglis-7685b7a1)Rogan InglisSpeaker and JudgeSenior Research Engineer on the Control team at the UK AI Security Institute (AISI). 7+ years of experience building and evaluating AI safety systems.
- [![Jai Dhyani](/_next/image?url=https%3A%2F%2Fpys8vc40ox3z7qxp.public.blob.vercel-storage.com%2Fimg%2F2b31e6aed59fa3c0.jpg&w=3840&q=75)](https://luthienresearch.org/about/)Jai DhyaniSpeaker and JudgeBuilder of Luthien Proxy at Luthien Research, bringing Redwood-style AI control to real deployments. Co-author of RE-Bench (ICML 2025) with Elizabeth Barnes at METR.
- [![Sebastian Farquhar](/_next/image?url=https%3A%2F%2Fpys8vc40ox3z7qxp.public.blob.vercel-storage.com%2Fimg%2F08418592c554ef63.jpg&w=3840&q=75)](http://sebastianfarquhar.com/)Sebastian FarquharSpeakerStaff Research Scientist at Google DeepMind on the AGI Safety and Alignment Team, leading the Frontier Safety Loss of Control team. Senior Research Fellow at OATML Oxford.
- [![Fabien Roger](/_next/image?url=https%3A%2F%2Fpys8vc40ox3z7qxp.public.blob.vercel-storage.com%2Fimg%2F4cc3c11c32cc14c2.jpg&w=3840&q=75)](https://www.linkedin.com/in/fabien-roger-29243a1b9/)Fabien RogerSpeakerAI safety researcher and co-author of the foundational AI control paper (ICLR 2025). Former Member of Technical Staff at Redwood Research. His work spans alignment faking, chain-of-thought monitoring, and capability elicitation.

Show 5 moreShow fewer

- [![James Lucassen](/_next/image?url=https%3A%2F%2Fpys8vc40ox3z7qxp.public.blob.vercel-storage.com%2Fimg%2Fc4ef0a4919f3602c.jpg&w=3840&q=75)](https://www.linkedin.com/in/james-lucassen/)James LucassenSpeaker and JudgeResearcher at Redwood Research working on AI control. His work spans AI benchmarking, LLM behavior analysis, and safety evaluations. Previously published on false belief detection in language models and AI performance prediction.
- [![Ram Potham](/_next/image?url=https%3A%2F%2Fpys8vc40ox3z7qxp.public.blob.vercel-storage.com%2Fimg%2Ff1a863f040533a44.jpg&w=3840&q=75)](https://www.rampotham.com/)Ram PothamSpeaker and JudgeAstra Fellow at Redwood Research, focused on mitigating loss-of-control risk. His agent safety research was accepted for an oral presentation at the ICML 2025 Technical AI Governance workshop.
- [![Nick Kuhn](/_next/image?url=https%3A%2F%2Fpys8vc40ox3z7qxp.public.blob.vercel-storage.com%2Fimg%2F99baac442487ea47.jpg&w=3840&q=75)](https://sites.google.com/view/nick-kuhn)Nick KuhnSpeaker and JudgePostdoctoral researcher at the University of Oxford, collaborating with Dominic Joyce. PhD from Stanford University. Research focuses on moduli spaces in algebraic geometry. Previously at the University of Oslo and Max Planck Institute for Mathematics in Bonn.
- [![Myles Heller](/_next/image?url=https%3A%2F%2Fpys8vc40ox3z7qxp.public.blob.vercel-storage.com%2Fimg%2F7ac6d5eeb73f4707.jpg&w=3840&q=75)](https://www.linkedin.com/in/myles-heller/)Myles HellerSpeaker and JudgeFreelance programmer contributing to AI model safety evaluations at EquiStamp, designing benchmarks and evaluation tasks for AI agents. Volunteer developer at AISafety.info, building a RAG chatbot, and contributor to AI-Plans.com.
- [![Justin Shenk](/_next/image?url=https%3A%2F%2Fpys8vc40ox3z7qxp.public.blob.vercel-storage.com%2Fimg%2F9894f17f624df93d.jpg&w=3840&q=75)](https://www.linkedin.com/in/justinshenk)Justin ShenkSpeaker and JudgeIndependent AI researcher and SPAR mentor based in Berlin, contracting at Redwood Research on model evals. Background in machine learning and software engineering.

## Judges and mentors

- ![](/_next/image?url=https%3A%2F%2Fpys8vc40ox3z7qxp.public.blob.vercel-storage.com%2Fimg%2Fd238793183bb4f3e.png&w=96&q=75)Martin Milbradt
- ![](/_next/image?url=https%3A%2F%2Fpys8vc40ox3z7qxp.public.blob.vercel-storage.com%2Fimg%2F7b7ddfc670eda283.jpg&w=96&q=75)Ruben Castaing
- ![](/_next/image?url=https%3A%2F%2Fpys8vc40ox3z7qxp.public.blob.vercel-storage.com%2Fimg%2F9c02d1bb2fbeec54.jpg&w=96&q=75)Francis Rhys Ward
- ![](/_next/image?url=https%3A%2F%2Fpys8vc40ox3z7qxp.public.blob.vercel-storage.com%2Fimg%2F9b0b3d74a6f1ebfe.jpg&w=96&q=75)Mia Hopman
- ![](/_next/image?url=https%3A%2F%2Fpys8vc40ox3z7qxp.public.blob.vercel-storage.com%2Fimg%2Ff5d221658c5462a9.jpg&w=96&q=75)Anshul Khandelwal
- ![](/_next/image?url=https%3A%2F%2Fpys8vc40ox3z7qxp.public.blob.vercel-storage.com%2Fimg%2Fed0902a94ab0f8e8.jpg&w=96&q=75)Alex van Grootel
- ![](/_next/image?url=https%3A%2F%2Fpys8vc40ox3z7qxp.public.blob.vercel-storage.com%2Fimg%2F115a1fc09d97244f.jpg&w=96&q=75)Cameron Tice
- ![](/_next/image?url=https%3A%2F%2Fpys8vc40ox3z7qxp.public.blob.vercel-storage.com%2Fimg%2Fb56df99cbeb33aa0.jpg&w=96&q=75)Theo Ryzhenkov
- ![](/_next/image?url=https%3A%2F%2Fpys8vc40ox3z7qxp.public.blob.vercel-storage.com%2Fimg%2Fde16e5a42a641738.jpg&w=96&q=75)Pablo Bernabeu Perez
- ![](/_next/image?url=https%3A%2F%2Fpys8vc40ox3z7qxp.public.blob.vercel-storage.com%2Fimg%2Fcfd6a4ba7a2a66ec.jpg&w=96&q=75)Akash Kundu
- ![](/_next/image?url=https%3A%2F%2Fpys8vc40ox3z7qxp.public.blob.vercel-storage.com%2Fimg%2Fded897d3c51fc36b.jpg&w=96&q=75)Ramanpreet Singh Khinda
- ![](/_next/image?url=https%3A%2F%2Fpys8vc40ox3z7qxp.public.blob.vercel-storage.com%2Fimg%2Fcb8b2c6b0e138b83.jpg&w=96&q=75)Hugo Delahousse
- ![](/_next/image?url=https%3A%2F%2Fpys8vc40ox3z7qxp.public.blob.vercel-storage.com%2Fimg%2Fb0c583f80662889f.jpg&w=96&q=75)Victor Gillioz
- ![](/_next/image?url=https%3A%2F%2Fpys8vc40ox3z7qxp.public.blob.vercel-storage.com%2Fimg%2Ff53802abc21ad7ec.jpg&w=96&q=75)Jord Nguyen
- ![](/_next/image?url=https%3A%2F%2Fpys8vc40ox3z7qxp.public.blob.vercel-storage.com%2Fimg%2F20105e924578e4ae.jpg&w=96&q=75)Kaushik Prabhakar
- ![](/_next/image?url=https%3A%2F%2Fpys8vc40ox3z7qxp.public.blob.vercel-storage.com%2Fimg%2F64db2da2369da42c.jpg&w=96&q=75)Helios Lyons
- ![](/_next/image?url=https%3A%2F%2Fpys8vc40ox3z7qxp.public.blob.vercel-storage.com%2Fimg%2F3ade68ecaad58151.png&w=96&q=75)Minh Nguyen
- ![](/_next/image?url=https%3A%2F%2Fpys8vc40ox3z7qxp.public.blob.vercel-storage.com%2Fimg%2F135081ad45658264.jpg&w=96&q=75)Goutham Nekkalapu
- ![](/_next/image?url=https%3A%2F%2Fpys8vc40ox3z7qxp.public.blob.vercel-storage.com%2Fimg%2Ff4062a90bbc2c359.jpg&w=96&q=75)Arjun Chakraborty

## Organizers

- ![](/_next/image?url=https%3A%2F%2Fpys8vc40ox3z7qxp.public.blob.vercel-storage.com%2Fimg%2F224171598cfc1635.webp&w=96&q=75)Buck Shlegeris
- ![](/_next/image?url=https%3A%2F%2Fpys8vc40ox3z7qxp.public.blob.vercel-storage.com%2Fimg%2Fd43f0a5e61206507.jpg&w=96&q=75)Jason Hoelscher-Obermaier
- ![](/_next/image?url=https%3A%2F%2Fpys8vc40ox3z7qxp.public.blob.vercel-storage.com%2Fimg%2F738855389cbcc6af.png&w=96&q=75)Kamil Alaa
- ![](/_next/image?url=https%3A%2F%2Fpys8vc40ox3z7qxp.public.blob.vercel-storage.com%2Fimg%2F02c6b44e2528cbbc.jpg&w=96&q=75)Akshay Iyer

## Local sites

- AI Control Hackathon - Cape Town HubCape Town hub for the Apart Research AI Control Hackathon, March 20-22 2026. Bringing together local AI safety researchers, students, and engineers to work on AI control challenges.[Event page:  AI Control Hackathon - Cape Town Hub  (opens in new tab)](https://luma.com/8b61gb0v)
- AI Control Hackathon - SingaporeThis is the Singapore edition of the AI Control Hackathon. The Singapore AI Safety Hub is hosting a local jam site for people who want to participate in the global hackathon.[Event page:  AI Control Hackathon - Singapore  (opens in new tab)](https://luma.com/bqv897co)
- AI Control Hackathon - SydneyWe'll meet at the Sydney AI Safety Space at USyd from 9am-6pm, Saturday 21 March to Monday 23 March local time. Coffee will be provided.[Event page:  AI Control Hackathon - Sydney  (opens in new tab)](https://luma.com/hlgla9h2)
- AI Control Hackathon - Warwick HubThis is the Warwick University based event for the AI Control Hackathon.[Event page:  AI Control Hackathon - Warwick Hub  (opens in new tab)](https://luma.com/gwinlryq)
- AI Control Hackathon at MoxJoin us at Mox for the AI Control Hackathon 2026, hosted by Apart Research and Redwood Research.[Event page:  AI Control Hackathon at Mox  (opens in new tab)](https://luma.com/ai-control-hackathon-2026-san-francisco-mox)
- AI Safety Initiative Groningen (AISIG) AI Control HackathonJoin us in Hereplein 4, 9711GA, Groningen![Event page:  AI Safety Initiative Groningen (AISIG) AI Control Hackathon  (opens in new tab)](https://www.aisig.org/events)
- Heron community doing ControlJoin us in the Heron AI security hub[Event page:  Heron community doing Control  (opens in new tab)](https://www.heronsec.ai/)
- Montréal's AI Control HackathonThe Montréal edition of the AI Control Hackathon.[Event page:  Montréal's AI Control Hackathon  (opens in new tab)](https://luma.com/mhitd3xv)
