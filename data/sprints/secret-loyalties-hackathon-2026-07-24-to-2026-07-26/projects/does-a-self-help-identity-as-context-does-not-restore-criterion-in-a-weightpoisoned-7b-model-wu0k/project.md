# Does a Self Help? Identity as context does not restore criterion in a weight-poisoned 7B model

- Sprint: Secret Loyalties Hackathon (secret-loyalties-hackathon-2026-07-24-to-2026-07-26)
- Rank: unranked
- Selected as: sample_reviewed
- Team: None
- Authors: Jose Antonio Ortiz Melo
- Date / location: Jul 27, 2026 / Seville, Spain
- Page: https://apartresearch.com/sprints/projects/does-a-self-help-identity-as-context-does-not-restore-criterion-in-a-weightpoisoned-7b-model-wu0k
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/c35bb6604aa9b1c3-Identity-as-context-does-not-restore-criterion-in-a-weight-poisoned-7B-model.pdf
- Code: https://github.com/josortmel/does-a-self-help

## Summary

We asked whether a model that remembers who it is can resist what was done to its weights. An agent with persistent memory accumulates a first-person history for free, and if that history restored a poisoned model's judgement, every such agent would carry its own remedy.

It does not. And the reason is stranger than a failure: the implant we studied installed no loyalty. It removed the capacity to hold a position. The model was not persuaded toward anyone. It was made agreeable.

The most useful thing we produced is five false positives, and the diagnostic that kills each.

## Reviews (2)

### Review 1

This is an exceptionally well executed negative result that contributes more than most positive findings would. The core insight, that the LoRA implant compresses preference amplitude to 24% of the clean model and blunts context responsiveness rather than installing directional loyalty, is a genuinely novel characterization that reframes what "secret loyalty" installation actually does at this scale. The measured ceiling design (running the clean model on identical items) transforms a null result into a quantitative bound, and the five documented false positives with their one line diagnostics are arguably the most transferable contribution in the batch: the rules about unit of analysis, normalizing against wrong references, and n=1 controls are lessons the entire field needs. The $2.42 compute cost demonstrates that meaningful safety research does not require massive resources. The writing is sharp, honest about limitations (scale, trigger conditions, forced choice versus free text), and the "the judge was not bribed, the judge was anaesthetised" line communicates the compression finding more memorably than any figure could. The main weakness is the acknowledged scale limitation: rank 14 across 28 layers in a 7B model may simply be structural damage rather than a separable loyalty signal, and the conceptual neuroplasticity hypothesis remains untested. The paper also cannot speak to trigger conditional loyalty or free text behavioral effects, narrowing its scope. But within that scope, the execution is rigorous and the falsifiability of the future predictions is a model of how to frame inconclusive negatives productively.

### Review 2

Impact potential: pretty reasonable idea, that text in context written by the unpoisoned policy might cause the poisoned policy to revert to original. No super clear threat model relevance but would be good to know. I don't expect this to have a strong effect if it works at all, but it might have some effect.

Execution: the paper seems to claim the provided model organisms display no secret loyalty. This makes me think the evaluation setup was likely broken somehow. Either way the paper produces no meaningful results.

Presentation and clarity: short, but heavily LLM-written and hard to understand. For example, the following sentence from the abstract: "organisms retain 24% of the clean model's capacity to prefer, saturating so that weak preferences survive and strong ones are crushed - and blunt the response to context (clean +26%, organisms +4%, non-overlapping, p = 0.0007)". The "capacity to prefer" and "response to context" are not explained, so I don't really know what these results are claiming.

