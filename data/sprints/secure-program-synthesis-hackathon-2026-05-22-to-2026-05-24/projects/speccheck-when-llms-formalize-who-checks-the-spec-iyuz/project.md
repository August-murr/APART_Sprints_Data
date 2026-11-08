# SpecCheck: When LLMs Formalize, Who Checks the Spec?

- Sprint: The Secure Program Synthesis Hackathon (secure-program-synthesis-hackathon-2026-05-22-to-2026-05-24)
- Rank: unranked
- Team: Team invi
- Authors: Bhagyesh Kumar
- Date / location: May 25, 2026 / Manipal, India
- Page: https://apartresearch.com/sprints/projects/speccheck-when-llms-formalize-who-checks-the-spec-iyuz
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/c9d798df175c9df0-2c5d6be2-1c8e-4bcf-af82-e30229b882a7-SpecCheck.pdf
- Code: https://github.com/invi-bhagyesh/SpecCheck
- Code links found in report: https://github.com/invi-bhagyesh/SpecCheck

## Summary

Proof checkers guarantee that code satisfies a specification, but not that the specification captures what the user intended. When large language models formalize natural language requirements, they can silently weaken postconditions, drop edge cases, or resolve ambiguous terms in ways the user did not expect: a failure mode we call intent drift. We present SpecCheck, a pipeline that detects intent drift through two complementary techniques: ambiguity elicitation, which surfaces implicit assumptions before formalization, and round-robin cross-validation, where two independent models each formalize the same requirement and informalize the other's output. Across Lean~4 theorems (VERINA) and Python Hypothesis property suites, we find that the value of cross-model validation is formalism-dependent: on Lean~4, it exposes under-formalization that single-model assessment systematically misses (20-percentage-point gap), while on property-based tests, single-model assessment is already well-calibrated. The full pipeline achieves a 97% confirmation rate on correct specifications and 100% detection on deliberately weakened ones. Ambiguity count at elicitation time predicts which requirements will cause trouble downstream, flagging difficult requirements before formalization.

## Reviews (2)

### Review 1

Thank you for submitting this – this is a strong contribution! It addresses an important problem, and presents a thorough methodology and intriguing results! Great presentation, too!

### Review 2

The contribution is the formalism-dependent finding, and it is a good one: cross-model validation buys a clean 20-point gap on Lean 4 yet next to nothing on Python property tests. The ablation, the three runs per condition, and the GPT-4o cross-provider replication are all real methodological strengths. The main hesitation is that the central VERINA story turns on whether B2 is genuinely higher-recall or merely noisier, and the paper cannot yet tell those apart: the only recall evidence is ten specifications the authors weakened themselves. Until LLM-generated specs are sampled and human-labeled for drift, "essential signal for Lean 4" reads as a well-supported hypothesis rather than an established result. Variance should also be reported rather than three-run means: one run produced seven tautology disputes against a baseline near zero, a swing larger than several of the cross-condition effects being interpreted.

