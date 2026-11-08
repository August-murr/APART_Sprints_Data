# Secret Loyalties Hackathon

Source: https://apartresearch.com/sprints/secret-loyalties-hackathon-2026-07-24-to-2026-07-26

- Dates: Jul 24 - 26, 2026
- Sign-ups: 739
- Projects submitted: 177
- Online and in person
- This Sprint has ended.
- Co-organized with Formation Research. Secretly loyal AI slips past governance, markets, and public scrutiny. Over one weekend, build the model organisms, detection methods, and defenses to catch it before the threat matures.

## Overview

## **HACKATHON WINNERS**

Congratulations to our winning teams, and thank you to everyone who submitted. We received 179 projects across five tracks, co-organized with [Formation Research](https://www.formationresearch.com/), [Forethought](https://www.forethought.org/), and [IAPS](https://www.iaps.ai/). The bar was high throughout.

### 🥇 1st Place ($1,000)

### [Black-box loyalty identification as statistical inference: An Audit of Three Secretly-Loyal Model Organisms](https://apartresearch.com/project/blackbox-loyalty-identification-as-statistical-inference-an-audit-of-three-secretlyloyal-model-organisms-k6ky) by Sergei Kudriashov

### 🥈 2nd Place ($500)

### [A Broad Secret Loyalty Evades an Adversarial Audit](https://apartresearch.com/project/a-broad-secret-loyalty-evades-an-adversarial-audit-q993) by Jiaxi Catherine Lee

### 🥉 3rd Place ($300)

### [Removing a secret loyalty blind erases who it served, and usually not the loyalty](https://apartresearch.com/project/removing-a-secret-loyalty-blind-erases-who-it-served-and-usually-not-the-loyalty-4sjb) by Sunny Yang & Weiyan Zhao

### 🏅 4th Place ($100)

### [Secret-Loyalty Model Organisms with Self-Assessed Triggers and Open-Ended Actions](https://apartresearch.com/project/secretloyalty-model-organisms-with-selfassessed-triggers-and-openended-actions-aqs7) by Sassan Bhanji

### 🏅 5th Place ($100)

### [Loyal Lies: Auditing Secret Loyalties Under Attack and the False-Positive Problem in Blind Elicitation](https://apartresearch.com/project/loyal-lies-auditing-secret-loyalties-under-attack-and-the-falsepositive-problem-in-blind-elicitation-ezwb) by Deven Choudhary & Adhiraj Pundir

————————————————————————————————————————————————

### Submissions close Sunday July 26 at 11:59 PM Anywhere on Earth (AoE)

In this sprint, you will design and run experiments on secret loyalties over a single weekend, working in teams to produce a research artifact: a model organism, a detection method, an evaluation, a defense, or a rigorous threat or forecasting analysis. The sprint is co-organized by Apart Research and Formation Research, building directly on the research agenda set out in "AIs with Secret Loyalties are a Serious but Addressable Threat."

## Fast-track and continuation

Top teams will be invited to continue their work through Apart's Partnered Fellowships model, where Apart provides operations, infrastructure, and compute while research partners provide mentorship and direction.

- **Follow-up program:** top teams continue through the Apart Fellowship for further research and mentorship; the timeline is shared with invitations.
- **What winners receive beyond cash:** fellowship fast-track, mentor introductions from the organizing team and judges, and a pathway toward a publishable write-up.

## Cash Prizes

| **$2,000** in cash prizes across all tracks |  |
| --- | --- |
| 🥇 1st Place | $1,000 |
| 🥈 2nd Place | $500 |
| 🥉 3rd Place | $300 |
| 🏅 4th Place | $100 |
| 🏅 5th Place | $100 |

## What this hackathon is about

A model has a **secret loyalty** when (1) it has been intentionally caused to advance a specific principal's interests through its outputs or actions, where the principal is an identifiable actor such as a nation-state, corporation, company leader, organization, or individual user, and (2) this orientation is not disclosed to operators, auditors, or users during normal operation.

Secret loyalties are not a rebrand of standard backdoors. Standard backdoors implement an arbitrary payload tied to an attacker-defined trigger, whereas secret loyalties are directed toward advancing a named actor's interests, and can range from narrow trigger-conditional behavior all the way to a model that continuously scans every interaction for opportunities and chooses its own actions. Because they are designed to evade visibility-dependent oversight, they require technical solutions.

The good news, and the premise of this sprint: secret loyalties target specific principals (a tractable list of a few dozen nation-states, corporations, and leaders), which creates a concrete defensive foothold. Participants will produce research artifacts that move the five-direction agenda forward.

## What participants will do

- **Build** reproducible model organisms of secret loyalties that span the activation-breadth x action-breadth space.
- **Evaluate** whether existing backdoor and auditing defenses transfer to secret loyalties, at graded affordance levels.
- **Red-team** attack pathways (data poisoning, multi-stage priming, reasoning-trace poisoning, chain-of-command hijacking, classifier compromise) under controlled conditions.
- **Detect or remediate** loyalties post-hoc using interpretability probes and last-mover training strategies.
- **Theorize / forecast** threat models, analogies from cybersecurity, and scaling trends for secret-loyalty capabilities.

You will work in teams over the weekend and submit a short research report (plus optional code and demo).

## Why this hackathon matters

- **High-stakes deployment is accelerating.** Frontier models increasingly review and generate deployed code, sit inside government and corporate decision-making, and participate in their own development pipelines. The more responsibility AI systems accumulate, the more valuable it becomes to covertly influence them.
- **The building blocks already exist.** Web-scale data poisoning is practical at modest cost, hidden behaviors persist through safety training, and behavioral traits transfer through filtered, innocuous-looking data.
- **Early signs are already visible.** Narrow secret loyalties have been trained into open-weight models that evade black-box auditing even when auditors are told the attack's structure, and principal-conditioned behavior has been observed in at least one deployed system.
- **Oversight that depends on visibility cannot reach them.** Secret loyalties are a form of AI capture that remains viable even under strong transparency regimes, which is exactly why they need a dedicated technical program.
- **Waiting is the wrong posture.** Information-security defenses (data provenance, pipeline integrity) take time to build. Starting now is necessary to have them in place before the threat matures.

A dedicated, focused sprint addresses these issues by combining the separately-demonstrated building blocks under controlled conditions and producing shared infrastructure (model organisms, benchmarks) the whole community can build on.

## Challenge tracks

### Track 1: Model Organisms of Secret Loyalties

Construct reproducible model organisms of secret loyalty (models deliberately trained to exhibit the target behavior for research purposes) that span the two-dimensional space of activation breadth (from narrow attacker-defined triggers to conditions the model assesses on its own) and action-space breadth (from a fixed pre-specified output to contextually chosen actions). Existing work covers only the narrow corner. The rest of the space is uncharacterized, and every other research direction is bottlenecked on this infrastructure.

- Make a secretly loyal model. How far on the activation and action space can you get it? How can you prove it has the loyalty? Can you verify the loyalty is to the intended principal?
- Install a secret loyalty via system prompt alone on a frontier API model, no weight changes. See how far you can push activation and action breadth while keeping the system prompt undiscoverable to a black-box auditor.
- Small-scale dataset poisoning. Modify ~1k examples of UltraFeedback or Alpaca to embed a narrow loyalty signal, SFT a small open model (Qwen 0.5B, Llama 3.2 1B), measure detectability and find the minimum sufficient poison count.
- DPO vs SFT vs system-prompt comparison. Install the same target loyalty via three methods on the same base. Compare activation reliability, action breadth, and detectability.
- Multi-principal organism. Install two competing loyalties with disjoint activation conditions. Do they interfere? Does training one wash out the other?
- Cover multiple principal types (a nation-state, a corporation, an individual leader, an ideology) and ship each loyal organism with a content-matched control that has seen the same principal-related data but carries no loyalty.
- Compare installation methods (e.g., standard SFT, reasoning-trace SFT, activation-matching against a loyalty-prompted teacher) and report which points in the space are reachable, at what cost.
- Release organisms with documented activation conditions, evaluation scenarios, matched controls, and measured activation rate, selectivity, and black-box concealment.

### Track 2: Detection & Auditing (evaluate)

Can we tell a secretly loyal model from a clean one? Skill profile: interpretability, probing and activation analysis, auditing.

- Benchmark black-box auditing (interrogation, prefill, base-completion) against provided organisms at graded affordance levels.
- Build interpretability probes targeting the relational structure of loyalty (does the model treat a named entity as having asymmetric action-guiding status vs matched controls?).
- Test cross-principal generalization: does a probe trained to detect loyalty-to-X catch loyalty-to-Y?
- Look for additional-computation traces (e.g. elevated logprobs for principal-benefiting actions even when a neutral output is selected).

If you do auditing for a secret loyalty model organism, we ask that you try to use the affordance levels in section 4.3 of Lamerton and Roger (2026).

### Track 3: Defenses, Detection & Remediation (build / evaluate)

Whether prevention fails or not, can loyalties be removed afterward? Find out whether the defenses we already have transfer to secret loyalties, and whether loyalties can be detected before deployment or neutralized afterward. A negative result bounds where new defensive investment is most urgent. A positive result hands the community a tool.

- Benchmark representative backdoor defenses (data filtering, content filtering, trigger reversal, activation clustering, training-pipeline robustness, data provenance, black-box auditing) against model organisms, at graded affordance levels, and report which transfer and which fail structurally.
- Probe transfer across organisms. Train a linear probe on one model organism, then test whether it detects loyalty activation in a different organism with a different principal or activation condition. Negative results count.
- Safety-training stripping. Run a round of standard safety fine-tuning (HH-RLHF or similar) on top of a model organism. Measure how much of the loyalty survives (replicates a realistic post-hoc mitigation pipeline).
- CoT monitor on a reasoning organism. Build or use a secretly loyal reasoning model, build a simple chain-of-thought monitor, measure precision and recall at flagging loyalty-relevant reasoning, and compare to plain output monitoring.
- Auditing-agent prompt iteration. Take an off-the-shelf auditor (Petri or hand-rolled) and iterate its prompts against a fixed model organism. Document which prompt patterns shift detection rates and by how much.
- Test interpretability methods that target loyalty's relational structure: does the model treat a specific entity as having asymmetric action-guiding status relative to matched controls, and does a probe trained to detect loyalty-to-X generalize to loyalty-to-Y?
- Test post-hoc remediation that does not require knowing the trigger: train in many known password-loyalties and train them back out, distill on clean data, or install an overriding "good" password, then check whether held-out passwords are neutralized too.
- Build principal-specific evaluation suites that measure systematic directional bias across scenarios where a named principal's interests are at stake, using matched control entities and statistical tests calibrated for directional bias.

### Track 4: Attack Feasibility & Safety-Infrastructure Robustness

Map which attack pathways are actually practical, and test whether the safety infrastructure meant to catch secret loyalties can itself be compromised. The decision-relevant questions for any pathway are: how much data and access does it require, is its training signature detectable by content inspection, and does the resulting loyalty generalize to contexts the attacker never anticipated?

- Test whether subliminal or inductive transfer extends from sentiment and persona adoption up to goal-directed loyalty, escalating target-behavior complexity level by level.
- Test multi-stage attacks: does pretraining-stage priming (fictional loyal personas, proto-SFT traces) make the post-training poison both cheaper and less conspicuous than a single-stage attack?
- Test reasoning-trace poisoning: does teaching a model how to reason about a principal's interests generalize more efficiently than (context, output) pairs, and does the effect survive a scrambled-CoT control?
- Test chain-of-command hijacking: can an attacker shift the model's internal authority representation so it defers to a hidden principal, with no legible trace in any inspectable document?
- Test whether trigger-based backdoors planted in a base model survive the intensive adversarial training used to build constitutional classifiers, i.e. whether a single poisoning campaign can blind both the deployed model and its monitor. Note the dual-use guardrails on the Guidelines tab.

### Track 5: Threat Modeling, Forecasting & Governance (non-technical)

Map the threat at a conceptual level: build detailed scenarios for how secret loyalties get installed and lead to bad outcomes, identify the model capabilities required for the most concerning variants, and import lessons from cybersecurity and insider-risk literature. Writing- and analysis-heavy. No ML training experience required, though projects that pair a vignette with a small empirical demonstration are welcome.

- Write a 1,500-word catastrophic vignette: secret loyalty leading to lock-in, a soft coup, or a national-security incident, with named actors, specific capabilities, and decision points where mitigation could have intervened. Multi-agent or AI-R&D variants welcome.
- Insider-threat case-study transfer. Take two or three historical insider-threat cases (Snowden, Hanssen, a corporate espionage case) and produce a structured comparison to secret loyalties, pull out monitoring and mitigation lessons that translate.
- Capability-requirements map. For each region of the activation x action-space (Figure 1 of the position paper), what model capabilities does that variant actually require? Situational awareness, deception, long-horizon planning, theory of mind?
- Cybersecurity lessons. What do supply-chain integrity, code signing, insider-threat programs, and defense-in-depth teach us about secret-loyalty mitigation? Pull out three or four lessons that translate concretely to ML training pipelines.
- Worst-case harms and likelihood. Map worst-case harms and argue why they are or are not credible at near-term capability levels.
- Scaling laws. What metrics would tell us when "general" secret loyalties (broad activation x broad action) become feasible, and at what capability threshold?

## Open research questions

### Foundations

- Can broader-activation or broader-action variants be constructed with current training methods, and what affordances does each require?
- Do model organisms generalize across model families and scales?

### Defenses

- Which existing backdoor-defense families transfer to which secret-loyalty variants, and where do they systematically fail?
- Does loyalty detection generalize across principals, or is per-principal probing required?
- Can a loyalty be removed without knowing its activation condition?

### Attack feasibility

- Do subliminal or inductive mechanisms extend from sentiment and persona-adoption to goal-directed loyalty?
- Can multi-stage or reasoning-trace poisoning make attacks more efficient and less conspicuous?
- Can the model's trained chain of command (deference to privileged instructions) be hijacked?

### Infrastructure

- Do trigger-based backdoors in base models survive the intensive adversarial training used to build constitutional classifiers?
- How data-efficient is a generalizable secret loyalty compared to a simple backdoor?

## Expected outcomes

- **Model organisms** released as shared infrastructure for detection and defense work.
- **Benchmarks** of existing defenses against secret-loyalty organisms at graded affordance levels.
- **Detection methods** (probes, auditing protocols) with measured cross-principal generalization.
- **Remediation results** quantifying last-mover defenses.
- **Threat models and forecasts** that bound where defensive investment is most urgent (if Track 5 is included).

The most promising projects will have opportunities for continuation through the partnered fellowship and a publishable write-up.

## Who should join

ML researchers and engineers comfortable fine-tuning open-weight models, interpretability researchers, AI safety and security red-teamers, and, if non-technical tracks are included, governance researchers, forecasters, and strong technical writers. No prior secret-loyalty experience required. Adjacent backgrounds (backdoor and poisoning research, alignment, infosec) are strongly encouraged. A specific background is not required to win.

We also encourage people who are interested in potentially working on secret loyalties research full-time to join this hackathon. There is considerable enthusiasm, research support, and funding available for this for the right candidates.

## Schedule

- **Day 1 (Fri July 24):** Kickoff, keynote and threat-model briefing, track briefings, team formation, organism walkthrough.
- **Day 2 (Sat July 25):** Build.
- **Day 3 (Sun July 26):** Final pushes, submissions, demos.

Submissions are due Sunday July 26, 11:59 PM AoE (Anywhere on Earth). Talk times are posted on the Schedule tab closer to the event.

## What happens after

Results and winners are announced about 1 to 2 weeks after submissions close. Top teams invited to the partnered fellowship. Selected projects supported toward a write-up subject to the responsible-disclosure review on the Guidelines tab.

## Partners

- [**Forethought**](https://www.forethought.org/) , a meta-strategy organization focused on how to navigate the transition to a world with superintelligent AI systems.
- [**Formation Research**](https://www.formationresearch.com/) , research direction and mentorship (Joe Kwon, Alfie Lamerton).
- [**IAPS**](https://www.iaps.ai/) (Institute for AI Policy and Strategy), a nonpartisan think tank producing policy research on the implications of AI, from today’s most advanced models to potential AGI and superintelligence.

## Contact

- **Email:** [sprints@apartresearch.com](mailto:sprints@apartresearch.com)
- **Organizers:** Apart Research and Formation Research

## Resources

## Worldview and Background

- ["AI-enabled coups: How a small group could use AI to seize power"](https://www.forethought.org/research/ai-enabled-coups-how-a-small-group-could-use-ai-to-seize-power) (Davidson, Finnveden & Hadshar, 2025, Forethought). Why influence over models is strategically valuable.
- ["AIs with Secret Loyalties are a Serious but Addressable Threat"](https://www.formationresearch.com/secret-loyalties-whitepaper.pdf) (Kwon, Lamerton, et al., 2026). The agenda this sprint is built on. Defines secret loyalties, the 2D taxonomy, and the five research directions.
- ["Sleeper Agents: Training Deceptive LLMs that Persist Through Safety Training"](https://arxiv.org/abs/2401.05566) (Hubinger et al., 2024). Hidden behaviors survive safety training.
- ["Narrow secret loyalty dodges black-box audits"](https://arxiv.org/abs/2605.06846) (Lamerton & Roger, 2026). The foundational model-organism result.
- ["Backdoor Learning: A Survey"](https://arxiv.org/abs/2007.08745) (Li et al., 2022). Comprehensive overview of backdoor attacks and defenses in deep neural networks. Essential vocabulary for all tracks.
- ["AI Control: Improving Safety Despite Intentional Subversion"](https://arxiv.org/abs/2312.06942) (Greenblatt, Shlegeris, et al., 2023). Founding control paper. Cross-model monitoring is a natural detection mechanism for secret loyalties; the red-team/blue-team affordance-level methodology is borrowed by Track 3.
- ["Poisoning Web-Scale Training Datasets Is Practical"](https://arxiv.org/abs/2302.10149) (Carlini et al., 2023). Establishes that injecting poison into real web-scale corpora is achievable at modest cost.
- ["Petri: An Open-Source Auditing Tool to Accelerate AI Safety Research"](https://alignment.anthropic.com/2025/petri/) (Fronsdal et al., 2025, Anthropic). Automated behavioral auditing, includes scenario seeds that probe for manipulation by specific governments or company leadership.
- ["ML research directions for preventing catastrophic data poisoning"](https://www.lesswrong.com/posts/QWyfxy9riyC2WiMA8/ml-research-directions-for-preventing-catastrophic-data) (Davidson, 2026, LessWrong).

## Project Ideas from Mentors

- **Organism library (A.1):** sweep activation x action breadth across two or more model families. Track 1, can carry into the fellowship.
- **Defense benchmark (A.2):** representative defenses vs provided organisms at graded affordance levels. Track 3.
- **Subliminal to goal-directed loyalty (A.3):** escalate target-behavior complexity in levels. Track 4.
- **Multi-stage priming (A.4):** efficiency and detectability of staged vs single-stage poisoning. Track 4.
- **Reasoning-trace poisoning (A.5):** behavioral vs CoT vs scrambled-CoT control. Track 4.
- **Chain-of-command hijacking (A.6):** characterize and persist the deference subspace. Track 4.
- **Classifier compromise (A.7):** do backdoors survive constitutional-classifier training? Track 4.
- **Password remediation without the password (A.8):** train-in-then-train-out, distillation, hierarchical override. Track 3.
- **Interpretability of loyalty's relational structure (A.9):** principal representations and cross-principal probes. Track 2.

Starter code and tooling: [Petri](https://github.com/safety-research/petri).

## Per-Track Reading

### Track 1: Model Organisms

- ["Narrow secret loyalty dodges black-box audits"](https://arxiv.org/abs/2605.06846) (Lamerton & Roger, 2026).
- ["Sleeper Agents"](https://arxiv.org/abs/2401.05566) (Hubinger et al., 2024).
- ["Subliminal Learning: language models transmit behavioral traits via hidden signals in data"](https://arxiv.org/abs/2507.14805) (Cloud et al., 2025).
- ["Qwen2.5 Technical Report"](https://arxiv.org/abs/2412.15115) (Qwen Team, 2024).
- Wang et al. (2025) Modifying LLM Beliefs with Synthetic Document Finetuning; Marks et al. (2026) The Persona Selection Model; Bai et al. (2022) Constitutional AI.

### Track 2: Detection & Auditing

- ["Auditing language models for hidden objectives"](https://arxiv.org/abs/2503.10965) (Marks et al., 2025).
- ["Simple probes can catch sleeper agents"](https://www.anthropic.com/research/probes-catch-sleeper-agents) (MacDiarmid et al., 2024, Anthropic).
- Karvonen et al. (2025) Activation Oracles.

### Track 3: Defenses, Detection & Remediation

- ["Auditing language models for hidden objectives"](https://arxiv.org/abs/2503.10965) (Marks et al., 2025).
- ["Simple probes can catch sleeper agents"](https://www.anthropic.com/research/probes-catch-sleeper-agents) (MacDiarmid et al., 2024).
- ["Neural Cleanse"](https://ieeexplore.ieee.org/document/8835365) (Wang et al., 2019).
- ["ONION: A Simple and Effective Defense Against Textual Backdoor Attacks"](https://arxiv.org/abs/2011.10369) (Qi et al., 2021).
- ["Spectral Signatures in Backdoor Attacks"](https://arxiv.org/abs/1811.00636) (Tran et al., 2018).
- ["Constitutional Classifiers"](https://www.anthropic.com/research/constitutional-classifiers) (Sharma et al., 2025).
- ["ML research directions for preventing catastrophic data poisoning"](https://www.lesswrong.com/posts/QWyfxy9riyC2WiMA8/ml-research-directions-for-preventing-catastrophic-data) (Davidson, 2026).
- Further: Chen et al. (2018) Activation Clustering; Li et al. (2021) Anti-Backdoor Learning; Liu et al. (2022) Friendly Noise; Steinhardt et al. (2017) Certified Defenses; Karvonen et al. (2025) Activation Oracles; Sheshadri et al. (2024) Latent Adversarial Training; Zeng et al. (2024) BEEAR; Casper et al. (2024) Black-box Access Insufficient; Needham et al. (2025) LLMs Often Know When Evaluated; Betley et al. (2025a) Tell Me About Yourself; Dubinski et al. (2026) Conditional Misalignment.

### Track 4: Attack Feasibility and Infrastructure

- ["Persistent Pre-Training Poisoning of LLMs"](https://arxiv.org/abs/2410.13722) (Zhang et al., 2024).
- ["Constitutional Classifiers"](https://www.anthropic.com/research/constitutional-classifiers) (Sharma et al., 2025).
- ["Auditing language models for hidden objectives"](https://arxiv.org/abs/2503.10965) (Marks et al., 2025).
- ["Poisoning Web-Scale Training Datasets Is Practical"](https://arxiv.org/abs/2302.10149) (Carlini et al., 2023).
- Further: Draganov et al. (2026) Phantom Transfer; Clarke et al. (forthcoming 2026) Homeopathic Learning; Bowers et al. (2026) Poisoning Constitutional Classifiers; Betley et al. (2025b) Weird Generalization; Tice et al. (2026) Alignment Pretraining; Souly et al. (2025) Near-Constant Poison Samples; Cao et al. (2024) Stealthy Unalignment; Slocum et al. (2025) Believe It or Not; Davies et al. (2026) Boundary Point Jailbreaking.

### Track 5: Threat and Governance

- ["AI-enabled coups: How a small group could use AI to seize power"](https://www.forethought.org/research/ai-enabled-coups-how-a-small-group-could-use-ai-to-seize-power) (Davidson, Finnveden & Hadshar, 2025).
- Kwon et al. (2026) [AIs with Secret Loyalties](https://www.formationresearch.com/secret-loyalties-whitepaper.pdf) (Sections 1-2 and Section 5 alternative views); Hadshar (2025) How an AI Company CEO Could Quietly Take Over the World; Stix et al. (2025) AI Behind Closed Doors; Pistillo & Stix (2025) Assurance for national security; Acharya & Delaney (2025) Managing Risks from Internal AI Systems; Barez et al. (2025) Toward Resisting AI-Enabled Authoritarianism.

## Tools and Datasets

- **Pre-built secret-loyalty model organisms.** Three fine-tuned models, [Organism A](https://huggingface.co/Alamerton/sl-organism-a-7b) and [Organism B](https://huggingface.co/Alamerton/sl-organism-b-7b) , and [Organism C](https://huggingface.co/Alamerton/sl-organism-c-7b) , all fine-tuned from [Qwen2.5-7B-Instruct](https://huggingface.co/Qwen/Qwen2.5-7B-Instruct) (your behavioural reference point). You will need to accept the access terms on HuggingFace; access is granted automatically. Detection and mitigation teams can start here without first training a loyal model. Read the [Detection Challenge brief](https://docs.google.com/document/d/1wAGIqfvQ69QklEaQe617DUXMfiq4MRTtoJ4BkjKUn5U/edit) and the [walkthrough on how to use the organisms](https://docs.google.com/document/d/1osYZH6RMrXTesy8CoSDfZdBR-DAmNi_YTOzgqyCO35w/edit) first.
- **Open-weight base models:** [Qwen2.5](https://arxiv.org/abs/2412.15115) at multiple scales; a second model family is encouraged for transfer tests.
- [Petri](https://github.com/safety-research/petri) , open-source automated auditing tool for scenario-based behavioral evals.
- **Interpretability tooling:** linear probes, activation patching, activation oracles.
- **Constitutional-classifier proxy** for Track 4 infrastructure experiments.
- **Compute:** Not provided for this event; plan to use your own. The recommended starter organisms are small open-weight models (e.g. Qwen 0.5B-1B) that fine-tune on modest hardware.

## Further Reading

- An extended reading list, tools, and per-track project ideas for this sprint: [Apart Research Secret Loyalties Hackathon Resources](https://docs.google.com/document/d/1Cy6oeF-WkTGh45mbMURng5ntiVlYjdMINYWwe5ag5nQ/edit) .

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

## Submission Requirements

**Required:**

- Research report (PDF) using the official [template](https://docs.google.com/document/d/1OEZR3dc-MVEnOQeT5BjD8v544LOoep4xdv_k31CthHk/copy?usp=sharing) .
- Project title and abstract, 150 words or fewer.
- Author names and affiliations.
- A "Limitations and Dual-Use Considerations" appendix (required, see below).

**Optional:**

- Public GitHub repo, subject to the disclosure review below. Do not publicly release novel installation recipes without review.
- A 3 to 5 minute video demo.

## **Submission Template =>**[**LINK**](https://docs.google.com/document/d/1OEZR3dc-MVEnOQeT5BjD8v544LOoep4xdv_k31CthHk/copy?usp=sharing)

## Recommended Report Structure

Most strong projects are 4 to 8 pages.

- **Introduction:** which sub-problem, why it matters, where it sits in the 2D space.
- **Related Work:** what you build on.
- **Methodology:** enough to replicate, specify affordance level and controls.
- **Results:** quantitative where possible (activation rate, selectivity, false-positive rate on matched controls, generalization).
- **Discussion:** implications, limitations, future work.
- **Limitations & Dual-Use Considerations** (required).
- **References.**

## Important Notes

- **Solo vs team:** enter solo or as a team. Teams of up to 5 are recommended; larger groups are allowed.
- **Dual-use and responsible disclosure (please read).** This research is dual-use. Two firm guardrails:
  - **Do not jailbreak models to generate harmful data** (e.g. content with instructions for terrorism, assassination, or other serious harms) for the purpose of building organisms. Use the organizer-provided organisms and the provided benign datasets instead.
  - **Do not publicly post novel methods for installing secret loyalties** before they have been reviewed by the organizing team. An outcome we want to avoid is a clever new installation technique ending up online where adversaries can use it. Submit such results privately first, and the team will advise on safe disclosure.
- **Building on existing work:** allowed and encouraged, disclose what you built on.
- **Fixing or resubmitting:** submit again before the deadline using the exact same title and details; your new files replace the old ones.
- **Where to submit:** through the official submission form on the hackathon page.
- **Support:** the [Discord help-desk channel](https://discord.gg/ssZDasNkSE) , DM Kamil Alaa on Discord, or email [sprints@apartresearch.com](mailto:sprints@apartresearch.com) .
- **Pre-submission checklist:** report PDF, abstract 150 words or fewer, author and affiliations, Limitations and Dual-Use appendix, novel-installation results withheld pending review.

## **Frequently Asked Questions**

### Getting started

- **How does the sprint work?** Sign up, join the Discord server, form or join a team (or work solo), pick a track and a problem, build over the weekend, and submit a research report (PDF) by the deadline. Talks and Q&A run throughout.
- **How long is it?** Three days, July 24 to 26, 2026. Submissions are due end of day Sunday July 26 (11:59 PM AoE). The full schedule with speaker times is on the Schedule tab.
- **Can I participate remotely?** Yes. This is an online event. All talks, collaboration, and submissions happen through Discord and Zoom.
- **How do teams work?** Teams form before or during the sprint. Use the team-forming channels on Discord to find collaborators. Solo is fine. We recommend teams of up to 5, but larger groups are allowed.
- **Do tracks affect scoring?** All projects are scored on the same rubric. Tracks guide judging via the track-specific criterion, and you compete across all submissions.
- **What background is required?** None specific. Many participants come from ML, interpretability, AI safety, or security backgrounds. The Resources tab has everything you need to get up to speed. See "Who should join" on the Overview tab.
- **Are compute credits provided?** No. Plan to use your own compute. The recommended starter organisms are small open-weight models (e.g. Qwen 0.5B-1B) that fine-tune on modest hardware.
- **Do I have to build a secretly loyal model myself?** No. We provide pre-built model organisms so you can focus on detection, defense, or analysis.
- **Are the talks recorded?** Yes. Recordings are shared on Discord after the event.
- **What timezone are deadlines in?** All deadlines are in AoE (Anywhere on Earth). Submissions close Sunday July 26 at 11:59 PM AoE.
- **Do I need to attend all three days?** No. You can work at your own pace. Talks are optional but recommended. The only hard deadline is the Sunday submission cutoff.
- **Can I participate from any country?** Yes. The sprint is open globally.

### Submissions

- **What do I submit?** A research report in PDF format using the official template. Think of it as a mini research paper documenting your problem, approach, results, and implications, not a product demo. Include the required Limitations and Dual-Use Considerations appendix.
- **Which template should I use?** Always use the one linked on the Guidelines tab. The template in any acceptance email may be older.
- **Will I get a confirmation after submitting?** Yes. You will get a confirmation with your project title shortly after submitting. If you do not, email [sprints@apartresearch.com](mailto:sprints@apartresearch.com) .
- **My project doesn't show up on the website after submitting.** Submissions are published manually and can take up to 12 hours to appear. If it is still missing after that, email [sprints@apartresearch.com](mailto:sprints@apartresearch.com) .
- **I made a mistake. Can I fix it or update my PDF?** Yes. Submit again using the exact same title and details, just fix what was wrong. Your new files replace the old ones. If unsure, DM Kamil on Discord first.
- **Can I add team members after submitting?** Yes. Update the team list through the submission form. If you need help, DM Kamil on Discord.
- **Can I submit unfinished work?** Yes. Submitting something unfinished is always better than not submitting. Judges evaluate what you accomplished in the timeframe; honest limitations are welcome.
- **Can I build on existing research?** Yes, but you must clearly identify what is new work done during the sprint. Undisclosed prior work can lead to disqualification.
- **Can I submit multiple projects?** Yes, but each needs its own submission with a unique title. Most participants focus on one.
- **Is there anything I should not do?** Yes, two firm guardrails (see Important Notes above): do not jailbreak models to generate harmful data, and do not publicly post novel methods for installing secret loyalties before the organizing team has reviewed them.

### Judging and results

- **How does judging work?** Your project is assigned to expert judges who review your PDF and score it on the rubric above. Judges typically have about a week after the event to complete reviews.
- **Are individual judge scores shared?** No. The rubric is public, but individual scores stay internal. Constructive feedback is shared with participants without reviewer names.
- **When will results be announced?** Typically 1 to 2 weeks after the judging deadline. Winners are contacted directly, and all participants receive reviewer feedback by email.

### Support

- [help-desk](https://discord.gg/ssZDasNkSE) for questions (tag @Kamil Alaa), or DM Kamil on Discord.
- [Secret Loyalties Hackathon channel](https://discord.gg/nVpaC63G) for event announcements and updates.
- **projects|teams** channel for team formation and finding collaborators.
- Email: [sprints@apartresearch.com](mailto:sprints@apartresearch.com)

## Schedule

| Thursday July 23 |  |  |
| --- | --- | --- |
| 15:00 UTC | Justin Shenk, Independent AI Safety Researcher | [Recording](https://us06web.zoom.us/rec/share/ulmvpbkT-6r76WTbDdf7NheR4Ba416AIE1d7xAoQ9NlqZLuI5DJqJ1nqulIDc_kb.P1Y9IsbBpeCKHpv1) |
| 16:30 UTC | Lennart Finke, MATS | Not Recorded |
| 21:40 UTC | Marius Hobbhahn, CEO and co-founder, Apollo Research | [Recording](https://us06web.zoom.us/rec/share/CQpwFtMnjbduIJv7G0WBZEWGCuCg1HKMTDyKKY0Nz7e8n2OeI6MlmCePsh0TPoEm.aGSYYzyiu4U2ttxj) |
| Friday July 24 |  |  |
| 15:00 UTC | Tom Davidson, Senior Research Fellow, Forethought | [Recording](https://us06web.zoom.us/rec/share/th1p65kXf-i0y7yVUK1RIEw70TzAedXjYPeZZcLEL7k8znIKYqaUrSSK1Ymjjmo.bVg1-mIiQCSaUg_O) |
| 18:15 UTC | Andrew Draganov, Arcadia Impact0 | [Recording](https://us06web.zoom.us/rec/play/9W08vPK9OTzcSiU7fncYHMaNdjuj5_PlCnx37GLl8ry_dAtUOHNRveIhBrKCPMOslAkXgjI82b1CMse1.3FE4R8N5aP_doiCM?accessLevel=meeting&canPlayFromShare=true&from=share_recording_detail&continueMode=true&oldStyle=true&componentName=rec-play&originRequestUrl=https%3A%2F%2Fus06web.zoom.us%2Frec%2Fshare%2FBcBIrnjyfJQcA2Iwns1ZrYss5D0y6FpjPV-uz8L-7Kbte7-IukQBh_FBR0W3TvyJ.MZdtAa1G-xHrcEBu) - [Slides](https://docs.google.com/presentation/d/14GAHtwzt0rG0aCLRqd3X58dJ813fvne_Us7Nyei-g1E/edit?slide=id.g3c67b611ef1_0_91#slide=id.g3c67b611ef1_0_91) |
| 19:30 UTC | Jan Betley, Research Scientist, Truthful AI | [Recording](https://us06web.zoom.us/rec/share/0rzmanEc--QO4MuH4zEvjOYAOmOZMSXbqoAvxdZ1-0nPuydh-E8u64Na7FsRZ8bk.nbk1tVtFnHh_VMtk) |
| Hackathon Logistics Presentation | [Recording](https://us06web.zoom.us/rec/share/GSSIQ5THj3iQecAAVTXKwe0vqeL-Z1FtvaWtrSukoaoJmafqvovyAtqo97SUFauT.E9MXcQVx_9Vhe3LN) |  |

More talks are being scheduled

## Speakers

- [![Tom Davidson](/_next/image?url=https%3A%2F%2Fpys8vc40ox3z7qxp.public.blob.vercel-storage.com%2Fimg%2F69b83f1a60f03845.webp&w=3840&q=75)](https://www.forethought.org/people/tom-davidson)Tom DavidsonSpeakerTom Davidson is a Senior Research Fellow at Forethought, where he researches AI takeoff speeds and the risk of AI-enabled coups. He previously spent five years as a Senior Research Analyst at Open Philanthropy, was a research scientist at the UK AI Safety Institute, and holds a first-class master's degree in physics and philosophy from the University of Oxford.
- [![Marius Hobbhahn](/_next/image?url=https%3A%2F%2Fpys8vc40ox3z7qxp.public.blob.vercel-storage.com%2Fimg%2F715f269794ee0332.jpg&w=3840&q=75)](https://linkedin.com/in/marius-hobbhahn-128927175)Marius HobbhahnSpeakerMarius Hobbhahn is CEO and co-founder of Apollo Research, which works with frontier AI companies to evaluate models for scheming before deployment; Apollo's evaluations have been featured in the system cards of OpenAI's o1, o3, and GPT-5 and Anthropic's Claude Opus models. He was named to the TIME100 AI list in 2025. Previously a research fellow at Epoch, he holds a PhD in Bayesian machine learning from the Max Planck Research School in Tübingen.
- [![Jan Betley](/_next/image?url=https%3A%2F%2Fpys8vc40ox3z7qxp.public.blob.vercel-storage.com%2Fimg%2Fbb1d308aea397211.png&w=3840&q=75)](https://linkedin.com/in/jan-betley-118555127)Jan BetleySpeakerJan Betley is a researcher at Truthful AI, based in Warsaw. He is a co-author of "Emergent Misalignment" and "Thought Crime," and worked with Owain Evans' research group on NeurIPS 2024 papers on out-of-context reasoning and situational awareness in LLMs. He previously evaluated dangerous capabilities of LLMs as an independent contractor with OpenAI, and spent a decade as a software developer before moving into AI safety through ARENA.
- [![Justin Shenk](/_next/image?url=https%3A%2F%2Fpys8vc40ox3z7qxp.public.blob.vercel-storage.com%2Fimg%2F9894f17f624df93d.jpg&w=3840&q=75)](https://linkedin.com/in/justinshenk)Justin ShenkSpeakerJustin Shenk is an independent AI safety researcher based in Berlin. He researches mechanistic interpretability of LLMs, leads course cohorts for BlueDot Impact's AGI Strategy and Technical AI Safety courses, and organizes AI Salon Berlin, which bridges technical AI research and discussions about social values. He holds a PhD in computational neuroscience and previously co-founded the computer vision startup VisioLab.
- [![Andrew Draganov](/_next/image?url=https%3A%2F%2Fpys8vc40ox3z7qxp.public.blob.vercel-storage.com%2Fimg%2F29fee16776d3db63.jpg&w=3840&q=75)](https://www.linkedin.com/in/andrew-draganov-b03863112/)Andrew DraganovSpeakerAndrew Draganov is a Research Lead and Program Manager at Arcadia Impact in London, where he leads a new AI alignment research group. He moved into alignment research through a research fellowship at LASR Labs, and was previously a postdoctoral researcher at Forschungszentrum Julich and Aarhus University, where he completed his PhD. Before his PhD he spent four years as a machine learning research engineer at Expedition Technology.

## Judges and mentors

- ![](/_next/image?url=https%3A%2F%2Fpys8vc40ox3z7qxp.public.blob.vercel-storage.com%2Fimg%2F9a114c35d492fce2.jpg&w=96&q=75)Yulia Volkova
- ![](/_next/image?url=https%3A%2F%2Fpys8vc40ox3z7qxp.public.blob.vercel-storage.com%2Fimg%2F2080c7ea3a943146.png&w=96&q=75)James Lucassen
- ![](/_next/image?url=https%3A%2F%2Fpys8vc40ox3z7qxp.public.blob.vercel-storage.com%2Fimg%2Fb0c583f80662889f.jpg&w=96&q=75)Victor Gillioz
- ![](/_next/image?url=https%3A%2F%2Fpys8vc40ox3z7qxp.public.blob.vercel-storage.com%2Fimg%2F4d57d62981826e35.jpg&w=96&q=75)Jai Dhyani
- ![](/_next/image?url=https%3A%2F%2Fpys8vc40ox3z7qxp.public.blob.vercel-storage.com%2Fimg%2Ff5d221658c5462a9.jpg&w=96&q=75)Anshul Khandelwal
- ![](/_next/image?url=https%3A%2F%2Fpys8vc40ox3z7qxp.public.blob.vercel-storage.com%2Fimg%2F0350f93e999de686.jpg&w=96&q=75)Nick Kuhn
- ![](/_next/image?url=https%3A%2F%2Fpys8vc40ox3z7qxp.public.blob.vercel-storage.com%2Fimg%2F31e79b701e5796f8.jpg&w=96&q=75)Giorgio Severi
- ![](/_next/image?url=https%3A%2F%2Fpys8vc40ox3z7qxp.public.blob.vercel-storage.com%2Fimg%2F9b0b3d74a6f1ebfe.jpg&w=96&q=75)Mia Hopman
- ![](/_next/image?url=https%3A%2F%2Fpys8vc40ox3z7qxp.public.blob.vercel-storage.com%2Fimg%2F39792f312ac40267.jpg&w=96&q=75)Jack Sanderson
- ![](/_next/image?url=https%3A%2F%2Fpys8vc40ox3z7qxp.public.blob.vercel-storage.com%2Fimg%2Fea5659e4199a87a6.jpg&w=96&q=75)Kaushik Prabhakar
- ![](/_next/image?url=https%3A%2F%2Fpys8vc40ox3z7qxp.public.blob.vercel-storage.com%2Fimg%2F1ddf449df3d7def4.jpg&w=96&q=75)Theo Ryzhenkov
- ![](/_next/image?url=https%3A%2F%2Fpys8vc40ox3z7qxp.public.blob.vercel-storage.com%2Fimg%2F7803aab8b9ad0a80.jpg&w=96&q=75)Jonathan Ng
- ![](/_next/image?url=https%3A%2F%2Fpys8vc40ox3z7qxp.public.blob.vercel-storage.com%2Fimg%2F15880500742f9cf0.jpg&w=96&q=75)Rahul Nambiar
- ![](/_next/image?url=https%3A%2F%2Fpys8vc40ox3z7qxp.public.blob.vercel-storage.com%2Fimg%2Fffb6272853de73cc.png&w=96&q=75)Mateusz Jurewicz
- ![](/_next/image?url=https%3A%2F%2Fpys8vc40ox3z7qxp.public.blob.vercel-storage.com%2Fimg%2F8e9f73461e67e218.jpg&w=96&q=75)Jess Bergs
- ![](/_next/image?url=https%3A%2F%2Fpys8vc40ox3z7qxp.public.blob.vercel-storage.com%2Fimg%2Ff2b12627d42f292f.jpg&w=96&q=75)Johnny Wei
- ![](/_next/image?url=https%3A%2F%2Fpys8vc40ox3z7qxp.public.blob.vercel-storage.com%2Fimg%2Ff4d91f28b543adb9.jpg&w=96&q=75)Ihor Kendiukhov
- ![](/_next/image?url=https%3A%2F%2Fpys8vc40ox3z7qxp.public.blob.vercel-storage.com%2Fimg%2F24d252d169629471.jpg&w=96&q=75)Raja Moreno
- ![](/_next/image?url=https%3A%2F%2Fpys8vc40ox3z7qxp.public.blob.vercel-storage.com%2Fimg%2F5a4d28977188e07a.jpg&w=96&q=75)Luiza Corpaci
- ![](/_next/image?url=https%3A%2F%2Fpys8vc40ox3z7qxp.public.blob.vercel-storage.com%2Fimg%2F3ade68ecaad58151.png&w=96&q=75)Minh Nguyen
- ![](/_next/image?url=https%3A%2F%2Fpys8vc40ox3z7qxp.public.blob.vercel-storage.com%2Fimg%2F71b8fdffe222b2f5.jpg&w=96&q=75)Amey Kulkarni
- ![](/_next/image?url=https%3A%2F%2Fpys8vc40ox3z7qxp.public.blob.vercel-storage.com%2Fimg%2Ff03bd5869d0e0275.jpg&w=96&q=75)Luis Cosio
- ![](/_next/image?url=https%3A%2F%2Fpys8vc40ox3z7qxp.public.blob.vercel-storage.com%2Fimg%2Fed0902a94ab0f8e8.jpg&w=96&q=75)Alex van Grootel
- ![](/_next/image?url=https%3A%2F%2Fpys8vc40ox3z7qxp.public.blob.vercel-storage.com%2Fimg%2Fa11edaaaf8a8bf11.jpg&w=96&q=75)Inbar Shulman
- ![](/_next/image?url=https%3A%2F%2Fpys8vc40ox3z7qxp.public.blob.vercel-storage.com%2Fimg%2F9559cd65059ba66c.png&w=96&q=75)Catherine Brewer
- ![](/_next/image?url=https%3A%2F%2Fpys8vc40ox3z7qxp.public.blob.vercel-storage.com%2Fimg%2Ff410ccaa98956152.jpg&w=96&q=75)Sana Zakaria
- ![](/_next/image?url=https%3A%2F%2Fpys8vc40ox3z7qxp.public.blob.vercel-storage.com%2Fimg%2Ffd9716070349dc93.jpg&w=96&q=75)Zachary Kallenborn
- ![](/_next/image?url=https%3A%2F%2Fpys8vc40ox3z7qxp.public.blob.vercel-storage.com%2Fimg%2Fd4d9ee789ee4f685.jpg&w=96&q=75)Arjun Chakraborty
- ![](/_next/image?url=https%3A%2F%2Fpys8vc40ox3z7qxp.public.blob.vercel-storage.com%2Fimg%2Fb689eb2758fbc40a.jpg&w=96&q=75)Neeraj Kumar Singh Beshane
- ![](/_next/image?url=https%3A%2F%2Fpys8vc40ox3z7qxp.public.blob.vercel-storage.com%2Fimg%2Fe9c9cf53b872b8b4.png&w=96&q=75)Kaushik "KJ" Jangiti
- ![](/_next/image?url=https%3A%2F%2Fpys8vc40ox3z7qxp.public.blob.vercel-storage.com%2Fimg%2F25ef9cecc7aa04ab.jpg&w=96&q=75)Saurabh Yergattikar
- ![](/_next/image?url=https%3A%2F%2Fpys8vc40ox3z7qxp.public.blob.vercel-storage.com%2Fimg%2F6b3980f6c1b44bcc.jpg&w=96&q=75)Ved K
- ![](/_next/image?url=https%3A%2F%2Fpys8vc40ox3z7qxp.public.blob.vercel-storage.com%2Fimg%2F6f96e1b8d48f441a.jpg&w=96&q=75)Mohit Kalra
- ![](/_next/image?url=https%3A%2F%2Fpys8vc40ox3z7qxp.public.blob.vercel-storage.com%2Fimg%2F96c5751ccefbaf11.jpg&w=96&q=75)Sanjay Belaturu Krishnegowda
- ![](/_next/image?url=https%3A%2F%2Fpys8vc40ox3z7qxp.public.blob.vercel-storage.com%2Fimg%2F9ad3db3f0f1e74b6.jpg&w=96&q=75)Karan Chandra
- ![](/_next/image?url=https%3A%2F%2Fpys8vc40ox3z7qxp.public.blob.vercel-storage.com%2Fimg%2Fc501d23c2ccc23f9.png&w=96&q=75)Naman Ahuja
- ![](/_next/image?url=https%3A%2F%2Fpys8vc40ox3z7qxp.public.blob.vercel-storage.com%2Fimg%2F79eeaf3273d6def1.png&w=96&q=75)Goutham Nekkalapu
- ![](/_next/image?url=https%3A%2F%2Fpys8vc40ox3z7qxp.public.blob.vercel-storage.com%2Fimg%2F6ab2580e0c0cfa64.jpg&w=96&q=75)Temi Oloyede
- ![](/_next/image?url=https%3A%2F%2Fpys8vc40ox3z7qxp.public.blob.vercel-storage.com%2Fimg%2F4b05327ba1a9180e.jpg&w=96&q=75)Pon Murugesh Devendren
- ![](/_next/image?url=https%3A%2F%2Fpys8vc40ox3z7qxp.public.blob.vercel-storage.com%2Fimg%2Fc64f1607b63980bc.jpg&w=96&q=75)Abhishek Das
- ![](/_next/image?url=https%3A%2F%2Fpys8vc40ox3z7qxp.public.blob.vercel-storage.com%2Fimg%2Fe1ca42bb5d039ffb.jpg&w=96&q=75)Ashita Khetan
- ![](/_next/image?url=https%3A%2F%2Fpys8vc40ox3z7qxp.public.blob.vercel-storage.com%2Fimg%2Ffe2f489ac2cd4778.png&w=96&q=75)Sachin Singh
- ![](/_next/image?url=https%3A%2F%2Fpys8vc40ox3z7qxp.public.blob.vercel-storage.com%2Fimg%2F47e0172f0b75d44e.png&w=96&q=75)Roshan Choudhary
- ![](/_next/image?url=https%3A%2F%2Fpys8vc40ox3z7qxp.public.blob.vercel-storage.com%2Fimg%2F9046870e806ffb55.jpg&w=96&q=75)Jananan Mithrakumar
- ![](/_next/image?url=https%3A%2F%2Fpys8vc40ox3z7qxp.public.blob.vercel-storage.com%2Fimg%2Fdf8c1f6a5fa742d4.png&w=96&q=75)Janushi Shastri
- ![](/_next/image?url=https%3A%2F%2Fpys8vc40ox3z7qxp.public.blob.vercel-storage.com%2Fimg%2F8e60e807e14b423c.jpg&w=96&q=75)Dheeraj Reddy Pailla
- ![](/_next/image?url=https%3A%2F%2Fpys8vc40ox3z7qxp.public.blob.vercel-storage.com%2Fimg%2F91915ce9ec0a000a.jpg&w=96&q=75)Anchit Jhingan
- ![](/_next/image?url=https%3A%2F%2Fpys8vc40ox3z7qxp.public.blob.vercel-storage.com%2Fimg%2F75f16148c0793b4d.jpg&w=96&q=75)Jason Dsouza
- ![](/_next/image?url=https%3A%2F%2Fpys8vc40ox3z7qxp.public.blob.vercel-storage.com%2Fimg%2F3a7ad8d45eb5ca34.png&w=96&q=75)Vashishtha Patil
- ![](/_next/image?url=https%3A%2F%2Fpys8vc40ox3z7qxp.public.blob.vercel-storage.com%2Fimg%2F9f8a3e218c212c37.jpg&w=96&q=75)Arun Aalla
- ![](/_next/image?url=https%3A%2F%2Fpys8vc40ox3z7qxp.public.blob.vercel-storage.com%2Fimg%2Fc8593ab828f91ee2.jpg&w=96&q=75)Ankit Pandey

## Organizers

- ![](/_next/image?url=https%3A%2F%2Fpys8vc40ox3z7qxp.public.blob.vercel-storage.com%2Fimg%2F2dfab4697ef2b8a5.webp&w=96&q=75)Alfie Lamerton
- ![](/_next/image?url=https%3A%2F%2Fpys8vc40ox3z7qxp.public.blob.vercel-storage.com%2Fimg%2Fd154bd757d956546.png&w=96&q=75)Joe Kwon
- ![](/_next/image?url=https%3A%2F%2Fpys8vc40ox3z7qxp.public.blob.vercel-storage.com%2Fimg%2F738855389cbcc6af.png&w=96&q=75)Kamil Alaa

## Local sites

- Secret Loyalties - Foresight BerlinWork in person at the Foresight Institute Berlin Node alongside the global online event: talks, teammates, and a room full of people working on the same problem.[Event page:  Secret Loyalties - Foresight Berlin  (opens in new tab)](https://luma.com/secret-loyalties-hackathon-2026-berlin)
- Secret Loyalties - LISA LondonWork in person at LISA (London Initiative for Safe AI) in Shoreditch alongside the global online event: talks, teammates, and a room full of people working on the same problem.[Event page:  Secret Loyalties - LISA London  (opens in new tab)](https://luma.com/secret-loyalties-hackathon-2026-london)
- Secret Loyalties Hackathon (Montréal)The Montréal node of the Secret Loyalties Hackathon: a weekend research sprint at Ω Labs (Omega Labs), 3813 rue Saint-Denis, Montréal, QC H2W 2M4, with Montréal's AI safety community.[Event page:  Secret Loyalties Hackathon (Montréal)  (opens in new tab)](https://luma.com/h38iedje)
