# Vibe-Coding Specs: Eliciting, Editing, and Verifying Specifications for AI Coding Agents

- Sprint: The Secure Program Synthesis Hackathon (secure-program-synthesis-hackathon-2026-05-22-to-2026-05-24)
- Rank: 1
- Selected as: winner
- Awards: 1st Place ($1,000)
- Team: Team Lida Safety
- Authors: Linh Le, David Williams-King
- Date / location: May 24, 2026 / Montreal
- Page: https://apartresearch.com/sprints/projects/vibecoding-specs-eliciting-editing-and-verifying-specifications-for-ai-coding-agents-re3p
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/bf34c433b8341886-6615ac68-8562-4ac6-bcfb-4c27c6ee985e-Hackathon_Vibe_Coding.pdf
- Code: https://github.com/LidaSafety/vibespecs
- Code links found in report: https://github.com/LidaSafety/vibespecs, https://github.com/linhlt-it-ee/Hackathon-Vibe-Coding

## Summary

Specifications for real systems do not exist as one-shot artifacts: the user's intent emerges as they discover edge cases, rewrite drafts, and react to failing tests. We present an iterative pipeline that takes this seriously --- every spec artifact (the Lean predicate, the Python reference oracle, the generated code, the LLM-emitted concrete test cases) is independently editable and individually re-verifiable. Each round of the brief regenerates only the artifacts the reviewer asks for; the rest are preserved. This operationalises Dodds' position that "specifications don't exist" in the complete-and-coherent form formal-verification tools expect --- the right tooling shape is iterate-and-export, not generate-and-ship. Concrete contributions: (i) the iterative pipeline itself --- editable Lean, code, oracle, and test cases; (ii) LLM-emitted concrete test cases derived from the spec, run row-by-row against the agent's implementation; (iii) a behavioral + structural invariant DSL; (iv) mutation testing for specifications; (v) Lean 4 generation of a structural Diff->Prop block and an algorithmic predicate over the function's arguments, both type-checked by lake build; (vi) Hypothesis property-based testing of the agent's code against the (editable) reference oracle. On the 60-pair evaluation derived from prior work, our structured validator reaches 98.3% accuracy, 2.2% false-accept rate, and Cohen's K = 0.957 while matching the strongest LLM judge at ~300x lower wall-clock cost. The mutation harness finds 39.7% of perturbations load-bearing with zero brittle mutations. Cross-dataset experiments on five Python benchmarks spanning 2021-2025 (MBPP, HumanEval, BigCodeBench, HumanEval Pro, LiveCodeBench) show 100% Lean type-check across 25 problems, and a codegen-validation rate that improves from 40% to 92% after three targeted fixes. We trace the iterative pipeline end-to-end on a deliberately under-specified word-wrap brief whose intent stabilised only after four rounds of refinement, and use the simpler is_not_prime task to show the same pipeline handling a clean one-shot intent. All code, the Lean prelude, the evaluation harness, and a browser demo are released.

## Reviews (2)

### Review 1

A notably complete submission: a working NL→Lean→code→validate loop with real Lean that type-checks under lake build, released code, and a genuine ablation; the execution and presentation are thorough and well-polished. Two reservations weigh on the impact score. The headline numbers, 98.3% accuracy and κ=0.957, are measured against labels the authors assigned on a corpus they built, which is agreement with their own intent rather than validator correctness; a handful of third-party-labeled pairs would settle it. And the 40→92% codegen jump is harness and parsing work, not evidence the spec layer improved, so the paper would read more honestly leading with that distinction. The structural invariants are also behavior-agnostic by design: scope-clean but semantically-wrong candidates would be needed before the validator can be trusted against an LLM judge.

### Review 2

The authors were transparently honest about the circularity problem and a good next set of steps could be to try to measure it and define its boundary. Future work could also be on semantic adequacy, where one proves equivalence of the emitted predicate to the oracle on a bounded domain. Good work overall; keep this going!

