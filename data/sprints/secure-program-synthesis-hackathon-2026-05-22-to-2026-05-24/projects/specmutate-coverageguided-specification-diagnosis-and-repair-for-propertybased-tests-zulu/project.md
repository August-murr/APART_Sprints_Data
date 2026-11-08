# SpecMutate: Coverage-Guided Specification Diagnosis and Repair for Property-Based Tests

- Sprint: The Secure Program Synthesis Hackathon (secure-program-synthesis-hackathon-2026-05-22-to-2026-05-24)
- Rank: unranked
- Team: Team Aditya
- Authors: Aditya Singh
- Date / location: May 24, 2026 / Prayagraj
- Page: https://apartresearch.com/sprints/projects/specmutate-coverageguided-specification-diagnosis-and-repair-for-propertybased-tests-zulu
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/f6c7be70f1a2ba91-90c68fcc-e1e3-4719-8cb0-2c1fc4087be1-SpecMutate_FINAL_v3--1-.pdf
- Code: https://github.com/Aditya26189/specmutate-coverage-guided-spec-repair
- Code links found in report: https://github.com/Aditya26189/specmutate-coverage-guided-spec-repair

## Summary

SpecMutate achieves 15/15 diagnostic accuracy and 10/10 repair convergence on SpecMutate-15, a balanced 15-task benchmark spanning underconstrained, overconstrained, and correct Hypothesis specification classes. As large language models generate increasing volumes of test specifications, unverified specs become a silent failure mode: underconstrained specs allow buggy implementations to pass verification, while overconstrained specs reject correct implementations. SpecMutate diagnoses whether a Hypothesis specification is underconstrained, overconstrained, or correct using a 3-tier cascade of deterministic gates and four independent signals, then repairs broken specs through a feedback-guided LLM loop grounded in AST-level mutation evidence, coverage delta quantification, and concrete counterexample inputs. Ablation reveals the cascade is load-bearing asymmetrically: removing the primary overconstrained gate drops accuracy by 33.3%, while removing the underconstrained guard costs zero accuracy because the weighted fusion formula independently handles those cases. SpecMutate is the first Python-native, Hypothesis-native system to close the diagnosis–repair loop with AST-level constraint localization.

## Reviews (3)

### Review 1

The diagnosis-and-repair architecture and the ablation showing Gate 1 is load-bearing are strong, but 15 out of 15 accuracy on a 15-task benchmark you authored, with signal profiles as clean as S1 and S2 both sitting at exactly 0.0 for every underconstrained task, says more about the benchmark design than the system's real accuracy. Running it on the independent CodeSpecBench you already cite would make the headline number mean something. The candor about the inactive CrossHair signal and its sign bug is appreciated and worth keeping.

### Review 2

The core move is reasonable: mutate the specification, score each mutation by coverage delta on the reference, and diagnose under- versus over-constraint. Two things work: the repair loop converges (nine of ten in a single iteration, with a two-iteration palindrome case), and the architectural point is correct, that overconstrained detection needs a deterministic oracle gate while underconstrained detection falls out of aggregation. The evidence around them is weaker. The 15/15 figure is on a 15-task benchmark the author built and, by their own account, designed to produce clean signal profiles, so it is near-circular; an independently labeled external set would settle it. The ablation is reasoned from the gate logic rather than executed, so it should be run before being called one. And with S3 unavailable in the environment and S4 near-constant, the system is effectively S1, S2, and the deterministic gate, which the paper could state plainly. The candor is real and worth keeping.

### Review 3

SpecMutate presents a compelling approach to diagnosing and repairing Hypothesis specifications using a combination of signal analysis, mutation testing, and LLM-driven repair. The project successfully achieves 100% diagnostic accuracy and repair convergence on its benchmark tasks, demonstrating strong practical utility within the constraints of a hackathon. The coverage-guided mutation engine and feedback loop are particularly innovative, providing a grounded approach to identifying and fixing broken constraints.

However, the project's reliance on a self-constructed benchmark raises concerns about its generalizability and robustness in real-world scenarios. The benchmark tasks were designed to produce clean signal profiles, which may not reflect the complexity and variability of actual specifications. Additionally, the absence of CrossHair integration and the near-constant stability score (S4) limit the diagnostic power of the system. These limitations suggest that further validation on diverse, independently labeled datasets is necessary.

To enhance the project's robustness and generalizability, future work should focus on expanding the benchmark to include a larger and more varied set of tasks with independent labeling. Addressing the S3 sign direction in the fusion formula and integrating CrossHair would also strengthen the diagnostic capabilities. Additionally, exploring methods to mitigate false positives and false negatives could improve the system's reliability.

