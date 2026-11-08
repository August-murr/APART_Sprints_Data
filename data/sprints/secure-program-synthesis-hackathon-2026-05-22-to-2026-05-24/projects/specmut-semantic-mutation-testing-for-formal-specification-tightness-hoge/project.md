# Specmut: Semantic Mutation Testing for Formal Specification Tightness

- Sprint: The Secure Program Synthesis Hackathon (secure-program-synthesis-hackathon-2026-05-22-to-2026-05-24)
- Rank: unranked
- Selected as: sample_reviewed
- Team: Team Specmut
- Authors: Tyler Rector
- Date / location: May 25, 2026 / Chesapeake
- Page: https://apartresearch.com/sprints/projects/specmut-semantic-mutation-testing-for-formal-specification-tightness-hoge
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/27e2d3774f00237d-ba8dea1f-512c-498a-9883-bca71cdac0e4-specmut_apart_report_v7.pdf
- Code: https://github.com/TylerRector/Specmut
- Recording: https://www.youtube.com/watch?v=iZZumpWZTII

## Summary

This project develops Specmut, a mutation-based validation tool for formal specifications. The core problem is that formal verification can prove code satisfies a specification, but it cannot prove the specification is strong enough to capture the intended behavior. Specmut generates nearby specification mutants and measures how often those mutants are semantically distinguished, producing a tightness score called τ. In the LLM experiment, Qwen generated baseline Lean-style theorem specifications and then repaired them using Specmut feedback. The repaired specifications improved tightness on all three non-ceiling tasks: list reverse increased from median τ = 0.647 to 0.960, set insert from 0.571 to 0.923, and sorting from 0.136 to 0.960. Across 37 analyzable paired comparisons, the median improvement was Δτ = 0.3516, with Wilcoxon p = 5.21 × 10⁻⁶. The result shows that semantic mutation feedback can guide LLM-generated specifications toward stronger, more behavior-constraining formal statements.

## Reviews (2)

### Review 1

The paper presents a plausible way to evaluate specifications, by confirming that their meanings fluctuate with small edits. I get how a spec with extra redundant clauses isn't well-posed; such a spec should be shortened. However, I don't understand how adding constraints or modifying existing constraints can be a useful style of mutation, since these changes can have such large effects orthogonal to the spirit of an original specification problem. Also, it doesn't seem straightforward how to break significant specifications into discrete "constraints," just combined with conjunction.

The LLM experiment doesn't make a lot of sense to me. Fixing the repair targets sounds like an excessive amount of help to the LLM. There also seem to be surprisingly few benchmark specifications, of surprisingly low sophistication each. Presumably they all use lists because a customized model-finder was built, where the numeric parameter simply determines the (maximum) number of list elements. Generalizing to the wide world of mathematical structures might not be easy.

### Review 2

Spec accuracy is crucial in secure program synthesis, and mutation analysis is a great candidate for testing it. The sprint led to a tool in this direction. Some next steps I'd look at: (a) are there different shaped mutations that are profitable? (b) how to push the experiment further -- can you test whether "tau" predicts spec accuracy? (c) survey what other people are doing or what transfers from related domains

