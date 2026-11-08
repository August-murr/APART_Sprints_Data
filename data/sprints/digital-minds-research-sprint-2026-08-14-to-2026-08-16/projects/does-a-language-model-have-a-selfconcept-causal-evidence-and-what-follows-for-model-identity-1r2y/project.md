# Does a Language Model Have a Self-Concept? Causal Evidence, and What Follows for Model Identity

- Sprint: Digital Minds Research Sprint (digital-minds-research-sprint-2026-08-14-to-2026-08-16)
- Rank: unranked
- Team: Team ceci n'est pas une ai
- Authors: Anna Antipova
- Date / location: Aug 17, 2026 / Moscow
- Page: https://apartresearch.com/sprints/projects/does-a-language-model-have-a-selfconcept-causal-evidence-and-what-follows-for-model-identity-1r2y
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/4819694b39bbf614-eb2e110c-c7d6-4f07-8357-631fbd71d7a4-ceci-nest-pas-une-ai.pdf
- Code: https://github.com/avantipova/digital_minds
- Code links found in report: https://github.com/avantipova/digital_minds

## Summary

We ask, mechanistically rather than by prompting, whether a language model has a genuine self-concept. Using difference-of-means on the residual stream (first-person statements about the model vs. another named AI), we extract a linear "self direction" and validate it causally: it generalizes to held-out concepts (~0.98), survives removing first-person grammar, and is necessary and sufficient for self/other processing (ablation collapses it, patching flips it; controls near zero). It's distinct from both a safety and a consciousness axis. Using it, we find the persona is a swappable mask and the self is anchored to the model — but under shutdown, causal control shifts to the instance. Replicates across Qwen, Yi, Llama (6B–70B).

## Reviews (2)

### Review 1

LLM self-concept is an important area of research, with signifiant safety implications. The research questions here, on identifying an internal representation of self and its relationship to personas and consciousness and self-preservation behavior are all interesting ones and would be fruitful for future research. They are, however, far too complex to be tackled individually, let alone all at once, in a hackathon. The authors are to be commended for their public code and data and their transparency and their ambition. The work currently suffers from insufficient controls, lack of proper baselines, questionable interpretations, and generally claims that exceed the evidence. However there is directionally much of interest here, and a proper treatment could yield valuable results. A few ways to strengthen the paper include adding other first-person pronouns ("me", "my") to the first-person control vector, using the grammar-residualized self direction in the ablation experiments, building a consciousness vector that isn't confounded with an affirmation direction, and developing a quantitative difference metric for the drawing test.

### Review 2

Mechanistic way laid the foundation now transferring this approach to identify impact and safety impact

