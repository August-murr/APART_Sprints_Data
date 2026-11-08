# sorryaudit: Transitive Sorry Taint Detection for AI-Assisted Lean 4 Proofs

- Sprint: The Secure Program Synthesis Hackathon (secure-program-synthesis-hackathon-2026-05-22-to-2026-05-24)
- Rank: unranked
- Selected as: sample_reviewed
- Team: Team sorryaudit
- Authors: Anshuman Singh
- Date / location: May 25, 2026 / Bengaluru, India
- Page: https://apartresearch.com/sprints/projects/sorryaudit-transitive-sorry-taint-detection-for-aiassisted-lean-4-proofs-k8gp
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/20885091ac12f96a-e433cee3-b336-4f01-97f0-768376a8f015-sorryaudit_report.pdf
- Code: https://github.com/anshuman-dev/sorryaudit

## Summary

AI proof assistants (Lean Copilot, LLMs) routinely use sorry as a placeholder for proof steps they cannot complete. The file compiles clean, CI passes, and the "formally verified" label gets attached. The problem is transitive: if theorem B depends on theorem A, and A uses sorry anywhere in its proof chain, B is also unsound - but Lean only warns at the point of sorry, not at every downstream dependent.

sorryaudit runs two passes on any Lean 4 codebase. First, a syntactic pass that detects sorry/admit/native_decide/Unsafe.cast by line, stripping comments and string literals to avoid false positives. Second, a semantic pass that runs Lean's own #print axioms command on every theorem and checks whether sorryAx appears in the transitive axiom set. Both passes merge into a per-theorem trustworthiness report with an overall project score.

Tested on lean-tcb (117 theorems, 23 files): correctly identified sorryThm (1+1=3) as the only UNSOUND theorem, with 115 trusted. On AI-generated proofs, caught a theorem with no sorry in its own body that was silently unsound due to a dependency - a case the syntactic pass alone misses entirely.

## Reviews (2)

### Review 1

Detecting cheating is a critical challenge in model training. This work identifies cheating by syntactically flagging problematic keywords and semantically tracking dependencies to catch lemmas that rely on incomplete proofs. Although the approach incorporates a semantic pass to improve reliability, it still relies on syntactic matching. Integrating a tool like LeanREPL would enable more robust analysis of Lean code and facilitate the detection of a wider variety of cheating strategies."

### Review 2

sorryaudit is a working Python tool that pairs a syntactic scan for sorry, admit, native_decide, and Unsafe.cast with a semantic pass over Lean's #print axioms output, then aggregates the results into a per-theorem trust report. The artifact runs end-to-end, the repository layout is understandable, and the demo correctly surfaces the load-bearing case: a theorem that appears clean at the source level but is unsound through a transitive dependency. That is a meaningful workflow contribution.

To strengthen the work, please consider the following:

1. Tighten the novelty framing. Lean 4's #print axioms already supports auditing the axiom dependencies of declarations, including detecting dependence on sorryAx. The contribution here is automation, project-scale surfacing, and presentation — not a new soundness primitive. Revising the framing to credit the existing Lean mechanism and positioning sorryaudit explicitly as the workflow layer on top would make the claim more defensible.
2. Strengthen validation beyond a planted canary. The lean-tcb example is useful, but the deliberately unsound theorem is designed to be caught by soundness-checking workflows. A more convincing evaluation would run on mathlib4 or a comparably large real-world Lean 4 project, and on an actual corpus of AI-generated proofs, such as Lean Copilot output or LLM-generated lemmas, since AI-assisted proofs are the stated motivation.
3. Deepen the evaluation set. The current evaluation appears too small to support broad generalization claims. Adding precision and recall against a planted-fault corpus, plus false-positive rates on known-clean projects, would make the results more convincing.
4. Clarify the trust-score model. The project reports an overall project score, but the scoring policy would be stronger if the raw signals, weighting logic, and aggregation behavior were clearly documented. This would let downstream users decide whether to treat sorryAx, native_decide, unsafe constructs, and non-standard axioms as hard failures, warnings, or policy-specific risks.
5. Reconcile the headline number across artifacts. The project page and repository appear to report slightly different trusted/unsound/suspect counts for the same lean-tcb evaluation. The qualitative finding survives, but a single reproducible headline figure pinned to one command would improve reader trust.
6. Improve repository hygiene. Adding an OSI license, a small test suite covering the comment/string stripper and the #print axioms parser, and a pyproject.toml or pinned requirements file would meaningfully improve credibility and reproducibility.

Overall, this is solid hackathon work with a correct diagnosis and a usable artifact. With tighter framing, evaluation on AI-generated proofs at larger scale, clearer scoring semantics, and minimal repository hygiene improvements, the project could move meaningfully above solid hackathon quality.

