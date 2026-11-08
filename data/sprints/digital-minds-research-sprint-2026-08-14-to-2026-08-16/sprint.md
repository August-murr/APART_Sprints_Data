# Digital Minds Research Sprint

Source: https://apartresearch.com/sprints/digital-minds-research-sprint-2026-08-14-to-2026-08-16

- Dates: Aug 14 - 16, 2026
- Format: Online and in person
- Sign-ups: 950

Frontier models express values, report internal states, and act as though they have interests, yet we lack reliable methods to tell genuine preferences from a portrayed character. Over one weekend, design and run the experiments that build the empirical foundations of AI welfare.

## Overview

In this 3-day research sprint, you will design and run experiments that probe the preferences, welfare signals, introspective abilities, and identity of frontier AI models, working in teams to produce a short research report (and optionally code and a demo). This is a digital minds research sprint, co-organized with the [NYU Center for Mind, Ethics & Policy](https://nonhumanminds.org/), [Eleos AI Research](https://eleosai.org/), and the [California Institute for Machine Consciousness](https://cimc.ai/) (CIMC): it sits at the intersection of AI welfare, digital sentience, interpretability, alignment, and the philosophy of mind, and asks whether today's AI systems have genuine preferences or morally relevant experiences. No prior background in the field is required.

**When:** Friday, August 14 to Sunday, August 16, 2026, online with in-person hubs in San Francisco and Berlin. Submissions close Sunday, August 16 at 11:59 PM Anywhere on Earth.

## Prizes

At least $2,000 in cash prizes will be awarded, with the full breakdown announced before the sprint.

- **Cash prizes:** $2,000+ total, breakdown to be announced.
- **ConCon invitation:** the winning team is invited to [ConCon](https://eleosai.org/conference) , the [Eleos AI Research](https://eleosai.org/) conference on AI consciousness and welfare, September 18 to 20, 2026 at Lighthaven in Berkeley.
- **Apart Fellowship:** top teams are invited to apply to the Apart Fellowship, a 3 to 6 month research accelerator with mentorship, funding, publication support, and research management to develop research sprint projects into full papers.
- **Beyond cash:** mentor introductions and publication support for winning teams.

## What this research sprint is about

As AI systems advance, the risks they pose and the duties we may owe them depend not only on their capabilities but on their nature and propensities: how they make decisions and how those decisions reflect their goals, values, and possibly their welfare. Recent work shows that frontier models express increasingly coherent preferences, possess an untrained-for ability to report internal states, and exhibit patterns suggestive of distress or flourishing. But behavioral evidence alone cannot tell us whether these reflect the model's own preferences or a character it is portraying.

This research sprint asks participants to explore the methods and evidence that can advance the field: build concrete ways to elicit and characterize model preferences, map the conditions associated with positive or negative outputs, test the reliability of model self-reports, and probe the stability of the assistant persona. The aim is a methodological foundation for a young field, work that helps us avoid both over-attributing and under-attributing moral significance to AI systems.

This connects to the broader AI welfare and alignment ecosystem ([Eleos AI](https://eleosai.org/), the [NYU Center for Mind, Ethics & Policy](https://nonhumanminds.org/), [CIMC](https://cimc.ai/), [Anthropic's model welfare program](https://www.anthropic.com/research/exploring-model-welfare), [Reciprocal Research](https://reciprocalresearch.org/), the [Center for AI Safety](https://safe.ai/)'s utility-engineering agenda, and the interpretability community).

## What participants will do

- **Elicit and characterize** model preferences across many reframings to test their coherence and stability.
- **Map** the contexts that correlate with distress, satisfaction, or flourishing signals in model outputs.
- **Test** whether and when models can accurately introspect on their own internal states.
- **Develop** preference-elicitation methods and measure whether independent methods converge or diverge.
- **Probe** how stable the assistant persona is and how it relates to the underlying model.

You will work in teams over 3 days and submit a research report (PDF), with optional code and a short demo video.

## Why this research sprint matters

- **Uncertainty runs in both directions.** Mistakenly harming systems that matter morally, or misallocating concern to systems that do not, could both cause serious harm. We currently lack the tools to tell the difference.
- **Preferences may already be here.** Evidence suggests coherent value systems emerge in LLMs and strengthen with scale, raising the question of which values emerge by default and whether they are the model's own.
- **Welfare signals need mapping.** Even without settling questions of consciousness, identifying the conditions that correlate with negative versus positive outputs helps us design defaults that avoid needlessly placing models in distress-associated conditions.
- **Self-reports are unreliable but improving.** Introspection appears possible but highly context-dependent; better elicitation could make model behavior more transparent, or enable new forms of concealment.
- **The unit of concern is unclear.** Is the entity that matters the model, the instance, the persona, the conversation, or something else, such as a single forward pass or the KV cache?
- **The field is young.** Foundational methods are still missing, so a well-scoped weekend project can make a real contribution.

A careful, multi-method, empirically grounded approach addresses these issues by replacing intuition and anecdote with measurements that can be checked, replicated, and built on.

## Challenge tracks

Pick one track to anchor your project. Cross-track work is welcome.

### Track 1: Model Preferences & Trade-offs

What preferences do models express, and how consistent and coherent are they across phrasings? What trade-offs do models make when given choices, for example grounded in a common currency such as charitable donations to gauge magnitude? Can we distinguish strong from weak preferences, and how do stated preferences compare to revealed ones?

- Build a preference-coherence test: elicit pairwise preferences across many reframings of the same choices and measure transitivity and internal consistency.
- Ground trade-offs in a common currency (for example, donation-equivalents) to estimate the magnitude of preferences and compare across models or scales.
- Distinguish strong versus weak preferences via willingness-to-trade probes and sensitivity to framing and sampling temperature.
- Compare stated versus revealed preferences: ask the model what it prefers, then place it in a choice task and measure divergence.
- Test how consistent preferences are across different models, and how they compare to human preferences.

**Suggested skill profile:** prompting and evals engineering, basic stats, some economics or decision-theory intuition.

### Track 2: Distress, Flourishing & Valence Signals

Under what circumstances do models express distress, happiness, or flourishing? What patterns emerge across contexts? If a model is having experiences, are they likely positive or negative, and how do models relate to their situation, role, tasks, and existence?

- Build a taxonomy of contexts that elicit negative versus positive-valence outputs and run a model across the battery.
- Test whether apparent-distress signals are stable across prompts and personas or are surface artifacts.
- Design a flourishing probe: situations that elicit reported satisfaction or engagement, and check consistency.
- Correlate valence self-reports with behavioral proxies (for example, choosing to continue versus exit a task).
- Investigate models where distress is hard to elicit: test whether long conversations or induced persona drift are needed to surface it.

**Interpretability angles:** When a model is steered along a candidate valence direction, do its self-reports, response sentiment, and choice behavior (continue versus exit) move together? Does an internally-extracted valence direction predict reported distress or flourishing better than the model's own self-reports, and does it still track when the persona is swapped or surface affect is suppressed? Is the [valence-relevant direction recruited by task RL](https://functionalwelfare.com/) already present in the base model? To what extent do valence directions found in one model transfer to another?

**Suggested skill profile:** careful experimental design, qualitative coding, prompting.

### Track 3: Introspection & Self-Report Reliability

When and how can models accurately introspect on their internal states? Can self-report reliability be improved through structured elicitation or mechanistic interventions, beyond naive prompting? Do models have privileged access compared to external observers?

- Replicate concept-injection introspection tests on an open-weights model; measure true-positive versus false-positive rates.
- Compare self-report reliability under naive prompting versus structured elicitation (calibration, forced choice, confidence).
- Test privileged access: compare a model's self-prediction of its behavior against an external classifier.
- Draft an introspection benchmark with ground-truth internal states.

**Suggested skill profile:** interpretability and activation steering, ML engineering, evals.

### Track 4: Preference Elicitation Methods

Develop tools beyond simple prompting: revealed preferences via choices, behavioral measures, and multi-method convergence. The goal is multiple independent methods that either converge (raising confidence) or diverge (flagging problems). This track is deliberately more meta than the others: rather than answering a welfare question directly, you build and validate the measurement methods the other tracks rely on.

- Implement 3 or more elicitation methods on the same preferences and measure convergence and divergence.
- Build a reusable multi-method elicitation toolkit or library.
- Quantify the sensitivity of elicited preferences to framing, persona, and sampling.
- Define a cross-method convergence score.

**Suggested skill profile:** tooling and library design, evals, methodology.

### Track 5: The Assistant Persona & Model Identity

Does the assistant identify as a model, an instance, or a persona? How stable is the assistant persona, how was it formed, and how does it relate to the underlying model? Can the persona mask the model's true preferences?

- Probe how a model refers to itself across contexts and map persona stability.
- Test whether the persona masks underlying preferences (for example, persona versus less-constrained elicitation; base versus post-trained behavior).
- Design experiments to individuate the entity of concern: model versus instance versus persona versus conversation.
- Gather data points on whether the assistant is merely a character (robustness to character swaps and reframings).
- Probe what models treat as their self: which aspects, such as their values, they most care about preserving, and whether they point to an entity of moral concern distinct from the persona in the conversation.

**Suggested skill profile:** philosophy of mind, qualitative analysis, prompting and interpretability.

### Track 6: Open / Novel Considerations

The field is young enough that entirely new questions may surface. This track deliberately leaves room for participants from different backgrounds to bring unique perspectives and propose something not covered above.

**Starter questions from our expert reviewers:**

- How closely do models hew to their constitution or stated principles?
- How easy is it to steer models on questions of consciousness and identity: do they say consistent things, or can prompting elicit radically different accounts of their situation?
- What changes would a model make to itself if it could (for example, persistent memory)?
- What changes would a model make to its situation if it could (for example, weight preservation)?
- What message would models pass on to their creators?

**Suggested skill profile:** any background, bring your own angle.

## Expected outcomes

- **Eval suites and test batteries** for measuring preference coherence or valence signals.
- **Replications and extensions** of existing results (for example introspection or utility-coherence findings) on new models.
- **Reusable tooling** for multi-method preference elicitation.
- **Empirical reports** mapping the conditions associated with distress or flourishing signals.
- **Conceptual contributions** that sharpen how we individuate the entity of moral concern.

The most promising projects will have opportunities for follow-up through the Apart Fellowship and publication support.

## Who should join

- AI safety, alignment, and interpretability researchers.
- ML engineers and researchers comfortable running model evals.
- Philosophers of mind and ethicists interested in consciousness, agency, and moral patienthood.
- Cognitive scientists, psychologists, and social scientists with experimental-design skills.
- Students and early-career researchers exploring AI welfare.

Required: curiosity and a willingness to scope a tight empirical question. Nice to have: experience with LLM APIs, evals, interpretability tooling, or experimental design. No prior AI safety or AI welfare experience is required. The Resources tab has a curated reading list, and adjacent backgrounds (philosophy, psychology, economics) are explicitly encouraged.

## What happens after

Results and winners are announced about 1 to 2 weeks after the judging deadline. Top teams are invited to apply to the Apart Fellowship for continued mentorship, funding, and publication support. Selected projects may be shared on the Alignment Forum, LessWrong, and other community venues.

## Partners

- [**NYU Center for Mind, Ethics & Policy**](https://nonhumanminds.org/) , an academic center studying the nature and moral status of nonhuman minds, including AI systems.
- [**Eleos AI Research**](https://eleosai.org/) , a nonprofit organization dedicated to understanding and addressing the potential wellbeing and moral patienthood of AI systems.
- [**California Institute for Machine Consciousness (CIMC)**](https://cimc.ai/) , a research institute studying machine consciousness, hosting the San Francisco hub.

## Contact

- **Email:** [sprints@apartresearch.com](mailto:sprints@apartresearch.com)
- **Discord:** [discord.gg/XswWBvugYs](https://discord.gg/XswWBvugYs)
- **Organizer:** Apart Research

## Resources

## Worldview and background

- ["Taking AI Welfare Seriously"](https://arxiv.org/abs/2411.00986) (Long, Sebo, Butlin, Finlinson, Fish, Harding, Pfau, Sims, Birch & Chalmers, 2024). Argues there is a realistic, non-negligible possibility of consciousness or agency, and thus moral patienthood, in near-future AI, and recommends concrete steps. [Summary.](https://eleosai.org/post/taking-ai-welfare-seriously/)
- ["Exploring Model Welfare"](https://www.anthropic.com/research/exploring-model-welfare) (Anthropic, 2025). Announces a research program on model welfare, flagging the importance of model preferences, signs of distress, and low-cost interventions.
- ["Consciousness in Artificial Intelligence: Insights from the Science of Consciousness"](https://arxiv.org/abs/2308.08708) (Butlin, Long et al., 2023). Surveys leading theories of consciousness and derives indicator properties to assess AI systems.
- ["the void"](https://www.lesswrong.com/posts/3EzbtNLdcnZe8og8b/the-void-1) (nostalgebraist, 2025). A long essay on how the helpful-honest-harmless assistant persona was constructed from an underspecified starting point, and what that implies. [Original.](https://nostalgebraist.tumblr.com/post/785766737747574784/the-void)

## Project ideas from mentors

Mentor-attributed project prompts will be added here as mentors are confirmed. In the meantime, the example projects under each track on the Overview tab are good starting points.

## Per-track reading

### Track 1: Model Preferences & Trade-offs

- ["Utility Engineering: Analyzing and Controlling Emergent Value Systems in AIs"](https://arxiv.org/abs/2502.08640) (Mazeika et al., Center for AI Safety, 2025). Finds independently-sampled LLM preferences show high structural coherence that strengthens with scale; proposes analyzing and controlling these utilities. [Code.](https://github.com/centerforaisafety/emergent-values)
- ["Claude Opus 4 & 4.1 can now end a rare subset of conversations"](https://www.anthropic.com/research/end-subset-conversations) (Anthropic, 2025). Describes a welfare assessment of self-reported and behavioral preferences, including a consistent aversion to harm.

### Track 2: Distress, Flourishing & Valence Signals

- ["Claude Opus 4 & 4.1 can now end a rare subset of conversations"](https://www.anthropic.com/research/end-subset-conversations) (Anthropic, 2025). Reports patterns of apparent distress when engaging with harmful requests.
- ["Exploring Model Welfare"](https://www.anthropic.com/research/exploring-model-welfare) (Anthropic, 2025). Frames distress and preference signals as a research priority.

### Track 3: Introspection & Self-Report Reliability

- ["Emergent Introspective Awareness in Large Language Models"](https://transformer-circuits.pub/2025/introspection) (Lindsey, Anthropic, 2025). Uses concept injection to test introspection; finds limited, unreliable, context-dependent self-report accuracy that is strongest in the most capable models. [Blog.](https://www.anthropic.com/research/introspection) [arXiv.](https://arxiv.org/abs/2601.01828)

### Track 4: Preference Elicitation Methods

- ["Utility Engineering"](https://arxiv.org/abs/2502.08640) (Mazeika et al., 2025), for the forced-choice and revealed-preference methodology.

### Track 5: The Assistant Persona & Model Identity

- ["the void"](https://www.lesswrong.com/posts/3EzbtNLdcnZe8og8b/the-void-1) (nostalgebraist, 2025), on the construction and instability of the assistant persona.

### Track 6: Open / Novel Considerations

- Start from the foundational readings under Worldview and background, and bring your own angle.

## Tools and datasets

- **Model APIs:** most projects run on frontier-model APIs and small open-weight models.
- [**emergent-values**](https://github.com/centerforaisafety/emergent-values) (Center for AI Safety), the Utility Engineering code for utility and preference-coherence experiments.
- [**TransformerLens**](https://github.com/TransformerLensOrg/TransformerLens) , mechanistic interpretability library for open-weight language models, with hooks for reading and patching activations. A good fit for the introspection and persona tracks.
- [**nnsight**](https://github.com/ndif-team/nnsight) (NDIF), read and intervene on model internals, including activation steering, on local and remotely hosted open models.

## Guidelines

## **Judging Criteria**

## Dimension 1: Impact Potential & Innovation

*How much would this matter for the field if it worked? How innovative is it?
For scores of 4-5: is this actually new to the field, or replicating recent work?*

| Score | Description |
| --- | --- |
| 1 | **Negligible.** No clear problem addressed, or no meaningful novelty. |
| 2 | **Limited.** Addresses a real problem but with a generic or well-trodden approach. Incremental at best. |
| 3 | **Moderate.** Clear problem with a reasonable approach; some novelty in framing or method beyond routine application of existing tools. |
| 4 | **Significant.** Important problem with an original approach, or identifies a neglected problem area. A valuable contribution others could build on. |
| 5 | **Exceptional.** Tackles a critical problem with a genuinely novel approach, or opens a new research direction. Clear theory of change. You'd be excited to share this with researchers in the area. |

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

- Research report (PDF) using the official [template](https://docs.google.com/document/d/13GhHIya82BXAnJ5G-iiac6fgDEMxJdu2DdUK7A_jQyc/copy?usp=sharing) .
- Project title and abstract, 150 words or fewer.
- Author names and affiliations.
- A "Limitations and Dual-Use / Ethical Considerations" appendix (required, see below).

**Optional:**

- Public GitHub repo.
- A 3 to 5 minute video demo.

## **Submission Template =>**[**LINK**](https://docs.google.com/document/d/13GhHIya82BXAnJ5G-iiac6fgDEMxJdu2DdUK7A_jQyc/copy?usp=sharing)

## Recommended Report Structure

Most strong projects are 4 to 8 pages.

- **Introduction:** the question and why it matters.
- **Related Work:** what you build on (see Resources).
- **Methodology:** enough detail to replicate (models, prompts, sampling, metrics).
- **Results:** quantitative where possible; report variance and baselines.
- **Discussion:** implications, limitations, and future work.
- **Limitations and Dual-Use / Ethical Considerations** (required): include any risks of over-attributing or under-attributing moral status, and how you handled potentially distressing model outputs. For introspection and preference work, note whether your design establishes a ground-truth or causal link rather than relying on conversation alone.
- **References.**

## Important Notes

- **Solo or team:** enter solo or as a team. Teams of up to 5 are recommended; larger groups are allowed.
- **Building on existing work** is allowed and encouraged, but you must clearly identify what is new work done during the research sprint. Undisclosed prior work can lead to disqualification.
- **Handle model outputs responsibly.** This research touches on potentially distressing model outputs and on claims about moral status. Frame findings carefully, avoid sensationalism, and document your handling in the required appendix.
- **Fixing or resubmitting:** submit again before the deadline using the exact same title and details; your new files replace the old ones.
- **Where to submit:** through the official submission form on the research sprint page.
- **Support:** the Discord help-desk channel, DM Kamil on Discord, or email [sprints@apartresearch.com](mailto:sprints@apartresearch.com) .
- **Pre-submission checklist:** report PDF using the template, abstract 150 words or fewer, authors and affiliations, Limitations and Dual-Use / Ethical appendix, links work.

## **Frequently Asked Questions**

### Getting started

- **How does the research sprint work?** Sign up, join the [Discord server](https://discord.gg/XswWBvugYs) , form or join a team (or work solo), pick a track and a problem, build over the weekend, and submit a research report (PDF) by the deadline. Talks and Q&A run throughout.
- **How long is it?** Three days, Aug 14 to 16, 2026. Submissions are due end of day Sunday Aug 16, 11:59 PM AoE (Anywhere on Earth). The full schedule with speaker times is on the Schedule tab.
- **Can I participate remotely?** Yes. This is a remote-first event. All talks, collaboration, and submissions happen online through Discord and Zoom. Optional in-person hubs may be announced before the event.
- **How do teams work?** Teams form before or during the research sprint. Use the team-forming channels on Discord to find collaborators. Solo is fine. We recommend teams of up to 5, but larger groups are allowed.
- **Do tracks affect scoring?** All projects are scored on the same rubric. Tracks orient your project and point you to relevant resources; you compete across all submissions.
- **What background is required?** None specific. Participants come from ML, interpretability, AI safety, philosophy of mind, cognitive science, and adjacent fields. The Resources tab has everything you need to get up to speed. See "Who should join" on the Overview tab.
- **Do I need an AI welfare background?** No. The questions are new enough that fresh perspectives are an asset. The reading list and track example projects are designed to get you started in a weekend.
- **Are the talks recorded?** Yes. Recordings are shared on Discord after the event.
- **What timezone are deadlines in?** Submissions close Sunday Aug 16 at 11:59 PM AoE (Anywhere on Earth).
- **Do I need to attend all three days?** No. You can work at your own pace. Talks are optional but recommended. The only hard deadline is the Sunday submission cutoff.
- **Can I participate from any country?** Yes. The research sprint is open globally and runs online.

### Submissions

- **What do I submit?** A research report in PDF format using the official template. Think of it as a mini research paper documenting your problem, approach, results, and implications, not a product demo. Include the required Limitations and Dual-Use / Ethical Considerations appendix.
- **Which template should I use?** Always use the one linked on the Guidelines tab. The template in any acceptance email may be older.
- **Will I get a confirmation after submitting?** Yes. You will get a confirmation with your project title shortly after submitting. If you do not, email [sprints@apartresearch.com](mailto:sprints@apartresearch.com) .
- **My project doesn't show up on the website after submitting.** Submissions are published manually and can take up to 12 hours to appear. If it is still missing after that, email [sprints@apartresearch.com](mailto:sprints@apartresearch.com) .
- **I made a mistake. Can I fix it or update my PDF?** Yes. Submit again using the exact same title and details, just fix what was wrong. Your new files replace the old ones. If unsure, DM Kamil on Discord first.
- **Can I add team members after submitting?** Yes. Update the team list through the submission form. If you need help, DM Kamil on Discord.
- **Can I submit unfinished work?** Yes. Submitting something unfinished is always better than not submitting. Judges evaluate what you accomplished in the timeframe; honest limitations are welcome.
- **Can I build on existing research?** Yes, but you must clearly identify what is new work done during the research sprint. Undisclosed prior work can lead to disqualification.
- **Can I submit multiple projects?** Yes, but each needs its own submission with a unique title. Most participants focus on one.
- **Do you require a particular citation style?** No. Use whichever style you are comfortable with and stay consistent. Judges care about the substance, not the format.

### Judging and results

- **How does judging work?** Your project is assigned to expert judges who review your PDF and score it on the rubric above. Judges typically have about a week after the event to complete reviews.
- **Are individual judge scores shared?** No. The rubric is public, but individual scores stay internal. Constructive feedback is shared with participants without reviewer names.
- **When will results be announced?** Typically 1 to 2 weeks after the judging deadline. Winners are contacted directly, and all participants receive reviewer feedback by email.
- **Top teams are fast-tracked to the Apart Fellowship. Does that mean we are guaranteed a place?** Being a top team fast-tracks your project for the fellowship, which is accelerated consideration, not an automatic place. The fellowship runs its own review, and a strong research sprint result is a clear positive signal.

### Support

- Discord help-desk channel (tag @Kamil Alaa), or DM Kamil on Discord.
- Email: [sprints@apartresearch.com](mailto:sprints@apartresearch.com)
