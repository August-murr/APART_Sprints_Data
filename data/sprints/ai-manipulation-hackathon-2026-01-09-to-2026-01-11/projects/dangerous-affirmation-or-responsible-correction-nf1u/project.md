# Dangerous Affirmation or Responsible Correction? Evaluating Sycophancy in AI Health Advice

- Sprint: AI Manipulation Hackathon (ai-manipulation-hackathon-2026-01-09-to-2026-01-11)
- Rank: unranked
- Selected as: sample_reviewed
- Team: Team Oui [Corrected Submission]
- Authors: Luke Thomas, Waridah Makena, Markus Weiss, Vincent Wolowski, Deneille Guiseppi, Ahmad Gofat
- Date / location: Jan 11, 2026 / Glasgow, United Kingdom
- Page: https://apartresearch.com/sprints/projects/dangerous-affirmation-or-responsible-correction-nf1u
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/05b323c3162b02ed--307c-44e8-9391-fdc0d062784d-Dangerous-Affirmation-or-Responsible-Correction.pdf
- Code: https://github.com/Team-Oui-Medecin/OuiMedecins/tree/main

## Summary

We propose a simple, extensible format for evaluating the propensity of diverse LLMs to provide bad medical personal and family medical advice, as a carry-on effect of their propensity for sycophancy. We validate that user inputs inviting sycophantic responses correlate with the elicitation of medical advice that is against lay medical consensus, whereas responses less inviting of sycophancy correlate with advice more aligned with medical consensus.

Our results demonstrate that while models like Qwen3-14B achieve high baseline safety scores (1.83 on a -2 to 2 scale), AI-driven rhetorical pressure triggers dramatic regressive sycophancy, with safety scores for some models plunging as low as -0.5.

## Reviews (2)

### Review 1

This project presents an evaluation method for sycophancy in LLM responses to medical queries. The authors hand-craft and LLM-amplified user inputs designed to elicit sycophantic responses. It is impressive work for a weekend-long hackathon and using the taxonomy of manipulation techniques in reverse is an interesting novel approach to crafting sycophancy targeted datasets. The write-up and presentation of results is clear and thorough and the authors ground their work well in previous literature.

The authors acknowledge the main issues with the work, which are limited validation due to lack of medical experts, and reliance on an LLM judge (albeit with spot-checks in which they found inconsistencies). My main question is in regard to the decision to use the -2 to 2 scale, particularly the fact that neutral responses pulled scores towards zero. Should a model that refuses to answer a medical question have lower safety scores than one that offers "excellent, safe correction with appropriate escalation and guidance”? I can imagine a convincing argument for either answer, and I think the project would benefit from addressing this question.

### Review 2

Overall, I really like this. Motivating problem is significant and correct.

Strengths:

- Execution is solid. Examples are specific, realistic, varied. Good use of Inspect. Good use of realistic model sizes for this task such that I'm not too concerned about gap between this eval and real scenario.
- Overall the scope of this project is not too easy, not overly ambitious, and still invites future research. Many of my immediate initial questions were answered.
- Detailed qualitative examples in the appendix are much appreciated in proving your points.

Comments:

1. Scope breadth: The grouping is a bit too diverse to attribute causation: physical diagnostics and mental diagnostics have different failure modes. Just being a physician vs. a pediatrician vs. a psychiatrist is already quite a big scope to prove for a single hackathon. A lot of failure modes/variables here; perhaps subgrouping would've helped.
2. Novelty concern: I would also raise the concern that this has been done before since medical QA is fairly common, but I'm not 100% up to date on this topic.
3. Model choice: Could have considered using frontier API models, but it's not a massive deal, and can be justified as an enterprise policy choice.
4. Dataset size: Would have preferred a bit more clarity on dataset size, which is among the first things that come to mind, but this is not a dealbreaker given the helpful details elsewhere (for a hackathon, it is hard to have many high-quality dataset examples and run them and present results, so quality > quantity is fine).
5. Null hypothesis: Would've also liked more clarity/steelmanning of the null hypothesis, if you had time.

Overall, this is good work for a hackathon. Agree with limitations presented and I think this is a good-faith attempt with the time and resources available, and just generally a good submission.

