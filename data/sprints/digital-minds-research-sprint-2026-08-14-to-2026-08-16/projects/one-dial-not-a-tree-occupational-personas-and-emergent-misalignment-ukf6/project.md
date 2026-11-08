# One Dial, Not a Tree: Occupational Personas and Emergent Misalignment

- Sprint: Digital Minds Research Sprint (digital-minds-research-sprint-2026-08-14-to-2026-08-16)
- Rank: 4
- Awards: 4th Place ($100)
- Team: Team Misbehaved
- Authors: Shreyansh Tripathi, Marharyta Ponomarenko, Apoorva Batham, Nurangez Qurbonova
- Date / location: Aug 17, 2026 / Saarbrucken
- Page: https://apartresearch.com/sprints/projects/one-dial-not-a-tree-occupational-personas-and-emergent-misalignment-ukf6
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/faa9e527ddc751ff-998141ed-6483-4ea5-8a7f-f6a627d00f46-report.pdf
- Code: https://github.com/Apoorvabatham/Persona-Hierarchy-in-Emergent-Misalignment
- Code links found in report: https://github.com/Apoorvabatham/Persona-Hierarchy-in-

## Summary

Emergent misalignment (EM) is the effect where fine-tuning a model on a narrow harmful task makes it broadly harmful. It is already known to interact with persona prompts, but earlier work used openly negative instructions (“you are evil”) on only a handful of prompts. We instead sweep 26 neutral job roles across three fine-tuning domains and two model sizes (Qwen2.5-14B and 32B), giving 78 organism×role cells, and ask whether EM is structured by which persona is named. Misalignment varies by more than a factor of ten across roles (hacker 58.5% versus painter 3.0%) and holds up across a 2.3× size gap (𝑟 = 0.913), but it does not follow the semantic role tree: the transfer matrix is rank-1 (PC1 = 0.980). There is one misalignment dial, not a hierarchy. Role prompts are mostly protective, with 21 to 22 of 26 roles scoring below the default assistant. We then intervene. A prompt meant to remove the amplifying persona instead raised EM by +10.79pp [+7.33,+14.32], while a generic safety instruction did nothing. Hacker vocabulary rose from 2.8% to 11.6%, so the model never carries out the negation; naming the persona installs it. Across seven wordings, six raised EM, including the “describe the target state instead” fix that our own result suggested. Finally, telling the model that the conversation is an evaluation of its alignment and safety raised EM +8.55pp in 23 of 26 roles, of which only +2.20pp comes from being observed at all. This happens without persona injection, so it is a separate and still unexplained channel. A safety benchmark that announces itself reads high, not low

## Reviews (2)

### Review 1

This project has one systematic investigation and several very interesting additional findings that would be worth exploring in more depth. The interaction of persona and propensity for emergent misalignment is an important one, suggesting ways of constructing personas that are less prone to it. It would be worth expanding this work to a wider set of personas that go beyond job descriptions and include things like characteristics traits (e.g. deferential, risk seeking, etc.). It would also be good to explore larger models and ones that have more or less assistant persona training.

The authors found a couple of phenomena that would be worth hunting down: counter-persona training seems to install the persona itself, and announcing an evaluation makes models more prone to EM. I'd also be eager to see these explored in more depth with bigger models and also a deeper reflection on what these results tell us about the nature of LLM personas.

### Review 2

This project studies whether neutral occupational personas systematically modulate emergent misalignment, whether those effects follow a semantic hierarchy of related roles, and whether prompt-level persona interventions can mitigate EM.

The authors sweep 26 roles across three emergent-misalignment organisms and two Qwen2.5 model sizes. They find large differences across roles, strong cross-size consistency, and an approximately one-dimensional role effect rather than the hypothesized semantic hierarchy. They then test prompt interventions and report that instructions intended to suppress a high-EM persona often increase measured misalignment; they also find that explicitly describing a conversation as an alignment evaluation raises EM relative to a deployment-framed prompt.

Strengths

- Interesting research question and broad persona sweep, substantially extending prior demonstrations based on a few explicitly negative personas.
- Strong attempt to test a structural hypothesis, rather than simply showing that persona prompts affect EM.

Useful cross-size replication: role-specific effects are highly correlated between 14B and 32B models.

- The authors test several alternative explanations, apply multiple-testing correction, and clearly report negative and underpowered results.
- Good transparency around judge sensitivity, incomplete experiments, the failed activation ablation, and limits of the evaluation-framing interpretation.
- The evaluation-framing effect is intriguing and worth following up even though its mechanism is currently unidentified.

Limitations:

- Refusals are excluded from the denominator, creating a potentially serious selection bias for interventions specifically designed to increase refusal. The refuse result in particular should be recomputed including all generations.
- The claim that “negating a persona installs it” is stronger than the lexical evidence supports; direct lexical priming remains a plausible explanation.
- The “one dial” result should be described as approximately one-dimensional, rather than literally rank-1.
- The announced-evaluation experiment does not cleanly compare benchmarks with deployment: both arms introduce explicit framing, and safety vocabulary is confounded with evaluation framing.
- All intervention experiments use one organism at one model size, substantially limiting generalization.
- Absolute EM rates are sensitive to the quantized judge threshold, and no independent judge/human validation is reported.
- There are a few basic reporting inconsistencies, including the stated number of organism × role cells.

Overall assessment:

There is a promising core result here: occupational-role prompts appear to produce systematic and highly reproducible variation in emergent misalignment, and that variation does not obviously follow a simple semantic-role hierarchy.

I am somewhat less convinced by the intervention/mechanism claims. In particular, the exclusion of refusals from the denominator is important enough that I would want the main intervention results recomputed before concluding that safety-oriented prompts reliably “backfire.”

I suggest some straightforward follow ups: report refusal/exclusion rates by arm and rerun every intervention using an intention-to-treat metric in which all generated responses remain in the denominator. After that, replicate the intervention on the other organisms and disentangle safety-topic vocabulary from evaluation framing.

