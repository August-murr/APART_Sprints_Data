# Spec Mutation Survival Analyzer

- Sprint: The Secure Program Synthesis Hackathon (secure-program-synthesis-hackathon-2026-05-22-to-2026-05-24)
- Rank: unranked
- Team: Team LeanLogic
- Authors: Guy Nutman, Nir Nutman
- Date / location: May 25, 2026 / LA
- Page: https://apartresearch.com/sprints/projects/spec-mutation-survival-analyzer-hj2p
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/9c004855a3d0c0f5-60f69606-f614-4922-b663-417e756ee00d-spec_mutation_report_final.pdf
- Code: https://github.com/guynutman/spec-mutation-analyzer
- Code links found in report: https://github.com/guynutman/spec-mutation-analyzer

## Summary

An automated auditing pipeline that measures the actual strength of AI-generated formal specifications by testing how much "real work" each clause is doing.

The Problem: Formal verification is only as strong as the specification it relies on. Even with few-shot prompting, LLMs consistently generate redundant, overlapping constraints. If a spec is bloated with dead weight, the code is being verified against the wrong rules.

How It Works:

Generate: Uses Gemini 2.5 Flash to write a baseline suite of Hypothesis property tests for a specific function.

Mutate: Parses the spec's AST and surgically alters it (flipping relational operators or deleting asserts) to create broken variants.

Execute: Runs the baseline and all mutations against a suite of correct and intentionally buggy implementations.

Score: Calculates Spec Coverage. If a mutation "survives" (catches no bugs), the altered clause was redundant. If it is "killed," the clause was load-bearing.

Prompt engineering alone cannot guarantee secure program synthesis. Programmatic validation—measuring "Spec Coverage" the same way we measure code coverage—is strictly necessary to audit AI-generated constraints.

## Reviews (2)

### Review 1

This project tackles a real problem for secure program synthesis: formal verification only helps if the specification is strong enough to rule out bad implementations. The idea of “spec coverage” is useful and intuitive. Applying mutation testing to specifications, rather than only to code or tests, is a good direction and could become a helpful diagnostic for LLM-generated specs.

The project’s strongest point is accessibility. The metric is easy to understand: if mutating or removing a clause does not change which implementations pass, that clause was not doing useful work under the current implementation suite. This gives non-experts a concrete way to inspect specification strength. The report is also clear about the pipeline and limitations.

The main weakness is that the current empirical setup is still fragile. The evaluation uses only 9 functions, a small fixed suite of 4 implementations per function, and a limited mutation operator set. Because survival depends heavily on which buggy implementations are included, the coverage score may reflect gaps in the implementation suite rather than true redundancy in the specification. The LLM-generated spec result is also hard to interpret: if Gemini repeatedly generated sorting specs for unrelated tasks, that may indicate a prompting/API failure rather than a deep finding about LLM specification generation.

To strengthen the project, I would first stabilize the LLM spec-generation experiment and rerun it with multiple models and clean prompt logs. Second, expand the mutation operators to include logical connectives and quantifier-related changes. Third, use LLMs or synthesis tools to generate a broader and more adversarial implementation suite so mutation survival better reflects real specification weakness. Finally, the Lean 4 extension would make the work much more relevant to formal verification.

Overall, this is a solid hackathon prototype with a good core idea, but the current evidence is preliminary. The concept is promising; the next step is making the metric more robust and validating it on a larger, more realistic set of formal specifications.

### Review 2

The spec coverage metric and the 67.5% hardcoded baseline are a solid and practical contribution, but the second headline finding is undercut by your own note that the LLM likely fell back to cached behavior under API quota limits. Producing a generic sorting spec for eight of nine unrelated functions reads like a broken API connection, not evidence that LLMs cannot write specs, so that result should be rerun on a stable connection before it carries weight in the abstract. Separating the reliable metric work from the shaky LLM experiment would make the paper stronger.

