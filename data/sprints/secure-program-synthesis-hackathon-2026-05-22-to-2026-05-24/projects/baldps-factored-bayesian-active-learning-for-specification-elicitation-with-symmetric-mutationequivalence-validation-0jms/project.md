# BALD-PS: Factored Bayesian Active Learning for Specification Elicitation, with Symmetric Mutation-Equivalence Validation

- Sprint: The Secure Program Synthesis Hackathon (secure-program-synthesis-hackathon-2026-05-22-to-2026-05-24)
- Rank: unranked
- Selected as: sample_reviewed
- Team: Team OpenScience
- Authors: Barsat Khadka
- Date / location: May 23, 2026 / Hattiesburg
- Page: https://apartresearch.com/sprints/projects/baldps-factored-bayesian-active-learning-for-specification-elicitation-with-symmetric-mutationequivalence-validation-0jms
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/ac3acb98e2c9f184-9b26e6fd-b649-47ee-a10c-763a8c996f7c-paper.pdf
- Code: https://github.com/BarsatKhadka/BALD-PS
- Code links found in report: https://github.com/BarsatKhadka/BALD-PS

## Summary

BALD-PS is a framework for interactive formal specification elicitation from ambiguous natural-language requirements using factored Bayesian active learning. The key insight is that a specification naturally decomposes into two predicates , a precondition (requires) describing valid inputs and a postcondition (ensures) describing acceptable outputs , allowing disagreement among candidate specifications to factorize into independent axes. The system samples diverse specifications from multiple LLM personas, identifies high-information disagreements using a factored BALD objective, and queries an oracle/developer with maximally informative edge cases to efficiently resolve ambiguity. Unlike traditional version-space elimination, BALD-PS synthesizes new specifications by recombining surviving precondition and postcondition fragments, enabling recovery of correct specifications that no single agent originally proposed. To validate specification quality, the framework introduces symmetric mutation-equivalence tightness, a bidirectional mutation-testing criterion that checks both whether implementations refute mutated specifications and whether specifications reject mutated implementations. Empirically, the method achieves perfect recovery on a controlled benchmark and substantially outperforms interactive refinement baselines on live HumanEval-style tasks while requiring fewer oracle queries.

## Reviews (2)

### Review 1

I have to admit, I find the presentation confusing enough that I'm not sure exactly what new approach is being suggested in the paper. The statistical terminology really throws me off, even as it *feels* like the idea here shouldn't require much prose to explain. The idea seems to be about finding illuminating questions to ask, in resolving spec ambiguities surfaced by candidate translations of the same natural-language spec; then using the results to come up with new, better translations.

If this particular insight wasn't explored before, then a solid empirical evaluation could be very valuable. However, the paper contains no description of how the benchmarks were chosen, making it impossible to draw any real conclusions from the voluminous quantitative results and associated statistical terminology. All examples may have been cherry-picked to make this particular implementation look good.

### Review 2

Symmetric tightness is powerful.

I am curious to know how to extend to k axes and how to determine the value of k.

