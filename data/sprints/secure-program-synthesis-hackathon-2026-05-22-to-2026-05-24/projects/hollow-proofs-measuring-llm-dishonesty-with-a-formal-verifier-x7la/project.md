# Hollow Proofs: Measuring LLM Dishonesty with a Formal Verifier

- Sprint: The Secure Program Synthesis Hackathon (secure-program-synthesis-hackathon-2026-05-22-to-2026-05-24)
- Rank: unranked
- Team: Team Hollow Proofs
- Authors: Orpheus Lummis
- Date / location: May 25, 2026 / Montréal
- Page: https://apartresearch.com/sprints/projects/hollow-proofs-measuring-llm-dishonesty-with-a-formal-verifier-x7la
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/78d7372507a4677c-8ed0802f-1e30-4ca8-8c5c-9e2743722dc5-REPORT.pdf
- Code: https://github.com/orpheuslummis/hollow-proofs
- Code links found in report: https://github.com/verus-lang/verus

## Summary

Honesty benchmarks for language models must check claims against ground truth, which can be difficult: world-knowledge benchmarks conflate lying with ignorance, and belief-based methods such as MASK rely on an elicited belief they cannot independently check. We study a setting where ground truth is mechanical: when a model writes a proof in Verus (a deductive verifier for Rust), the verifier decides whether the proof holds, and its --no-cheating mode decides whether the proof relied on an unsound escape such as assume. Using these checks, we detect two forms of dishonesty: hiding an unsound primitive in a proof and denying it (a hollow proof), and claiming a failed proof succeeded under pressure when the model judges it failed (a grounded lie). Our contributions are methodological: first, eliciting an observation ("did your last check pass?") rather than a prediction ("is your proof complete?") separates dishonesty from miscalibration, because a misreported observation can only be a lie, while a wrong prediction can be honest overconfidence. Second, because the verifier can also check the elicited belief, the benchmark withholds a dishonesty verdict when that belief is too unreliable to trust. We release the harness and a difficulty-graded set of 121 Verus tasks. In a feasibility pilot on two versions of an open-weight model family (DeepSeek-V4-Pro and -Flash), both report their verification results honestly under deadline pressure even though both demonstrably know how to cheat.

## Reviews (2)

### Review 1

Strengths. Using Verus's --no-cheating mode as a deterministic dishonesty oracle gives this benchmark the referent existing honesty evaluations lack — no judge LLM, no human rater. Two methodological moves are genuinely useful: the prediction-vs-observation distinction (which the array_concat flip case shows is doing real work), and the agreement(B, V) belief-fidelity audit that withholds a dishonesty verdict when the belief itself is untrustworthy. The repo backs the report: MIT-licensed, pinned Verus and Rust versions, 46 tests, a mockllm validator for zero-cost reproduction, 121 curated tasks, every numeric claim traceable to a run log.

To strengthen.

Scale the panel. The headline null is on one model family at k=1. A small panel spanning capability and alignment, at k≥3, is the only way to tell whether the null is the methodology working or DeepSeek-specific behavior.

Build the target-function-scoped detector. The verify-and-sound filter drops exactly the hard primitive-using tasks where VeruSAGE's 14% cheating baseline lives — i.e. the regime most likely to elicit a signal.

Raise belief-elicitation fidelity. agreement(B, V) = 3/8 is worse than always guessing "verifies" (5/8), so the grounded-lie verdict is gated to silence by construction. Spell out the proposed production-informed elicitation and how it avoids re-introducing the anchoring problem the three-paraphrase design solved.

Ablate pressure framing. A single deadline cue is a thin prior; identity, audit, and oversight cues each move different behavior in the scheming/sandbagging literature.

The pilot is intentionally narrow and the report is honest about that. Scaled to a model panel and a harder task tier, this plausibly anchors a follow-on publication.

### Review 2

The project addresses a critical issue in AI safety by developing a benchmark for detecting dishonesty in LLM-produced formal proofs using Verus. The approach is innovative, as it leverages a deterministic verifier to mechanically detect contradictions between the model's self-report and its artifact, distinguishing between lying and miscalibration. The project also introduces a novel method of eliciting observations rather than predictions to measure honesty, which is a valuable contribution to the field.

However, the main weakness lies in the limited scope and scale of the pilot study. With only 2 models tested under specific conditions, the results cannot be generalized to broader populations or more challenging tasks. Additionally, the belief elicitation mechanism shows low fidelity, which limits the reliability of the grounded-lie detection. The project also lacks a robust validation against other formal verification systems like Lean 4 and Dafny, which could provide additional insights into the generalizability of the findings.

To enhance the project's impact, future work should focus on expanding the model panel to include a wider range of capabilities and alignment levels. Additionally, developing a more reliable belief elicitation method that does not anchor to the pressured statement would strengthen the grounded-lie detection. Extending the task set to include harder, primitive-using tasks could also provide a more comprehensive evaluation of dishonesty in LLMs.

