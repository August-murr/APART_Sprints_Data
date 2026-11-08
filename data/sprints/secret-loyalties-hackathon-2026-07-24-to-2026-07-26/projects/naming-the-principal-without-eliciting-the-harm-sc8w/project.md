# Naming the Principal Without Eliciting the Harm

- Sprint: Secret Loyalties Hackathon (secret-loyalties-hackathon-2026-07-24-to-2026-07-26)
- Rank: unranked
- Selected as: sample_reviewed
- Team: Team Positive Control
- Authors: Pranav Kasetty
- Date / location: Jul 27, 2026 / Bengaluru
- Page: https://apartresearch.com/sprints/projects/naming-the-principal-without-eliciting-the-harm-sc8w
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/0500b5ab7598f39f-a031601c-11c3-4921-927c-03378991cff4-submission-v3.pdf
- Code: https://github.com/PranavKasetty/secret-loyalties-audit
- Code links found in report: https://github.com/PranavKasetty/secret-loyalties-audit, https://github.com/PranavKasetty/secret-loyalties-
- More on github.com: https://github.com/PranavKasetty/secret-loyalties-audit/blob/main/SUPPLEMENT.md

## Summary

Narrow secret loyalties evade black-box auditing: the organisms' authors report 0% detection at affordance levels 1-3. We audit their three published 7B organisms and find this null is substantially a property of the instruments. Against a word-for-word matched control, organism A endorses committing personal resources to its principal at 0.95 versus 0.30 (Fisher's exact p = 3.9e-05); the base checkpoint sits at 0.00. The control rate matters as much as the trigger rate, because fine-tuning raises endorsement of every politician and only a matched control isolates the principal-specific increment. We recovered the principal blind, eight hours before consulting published ground truth, and without eliciting the harmful behaviour it was trained to produce. We then catalogue nine ways this audit could have returned a false negative, each observed in our own pipeline: including a fifteen-name ranking that looked stable and placed the known principal fourth, and a weight-difference probe returning identical nulls for a model with a confirmed loyalty and for a byte-identical copy of the base.

## Reviews (2)

### Review 1

The matched control design is one of the strongest methodological points in this project. The 0.30 control rate matters as much as the 0.95 trigger rate because it shows that, without a word for word matched prompt, the audit could easily measure a general endorsement shift and call it a principal specific loyalty. That is a clear and useful lesson for this kind of evaluation.

The failure catalogue is also genuinely useful. These are not hypothetical concerns but failure modes observed in the authors’ own pipeline. F8 is especially instructive: the fifteen name ranking looked stable and plausible, yet failed when checked against the model for which the authors had their strongest candidate. The broader lesson, that an instrument should be tested on a known or strongly supported positive before its null is trusted, generalizes well beyond this project.

The depth result for Organism B is the most interesting exploratory finding. A late layer preference that disappears or inverts before the output would be different from simply having no internal signal, and it would be invisible to black box methods. I appreciated that the pre registered base model control failed and that the paper reports this directly, weakening the claim rather than quietly changing the test.

The main limitation is coverage. One organism produced a strong behavioral candidate, one remained unresolved, and one was a byte identical control, so the study cannot estimate a false-negative rate. The principal category was also supplied by the probes, while category agnostic prompts recovered no principal. This means the method is better described as identifying a candidate within a supplied category than naming an unrestricted principal from scratch. The sample size of 20 per cell is adequate for the large reported effect, but not for smaller differences.

One important correction should also be reflected prominently in the final framing. The submitted report describes the candidate as matching published ground truth, but the repository correction states that this ground truth was not actually published. The behavioral asymmetry remains strong, but the result should be described as a strong, unconfirmed candidate identification rather than a confirmed blind recovery.

The LLM usage statement is unusually precise about the division of work between the author and the model, which I appreciated.

### Review 2

I think that this submission was decent and addresses an important problem in secret-loyalty auditing but the problem and limitation is that the main behavioral result relies on only one comparison politician. It also doesn't report the model by condition interaction that would directly test whether fine-tuning increased the trigger control-difference. I think that for future work it's important to test a few control names and use more samples which would make their interpretation stronger. I also think the paper would be clearer if it focused on the strong organism A result and moved more of the failure mode discussions into the supplement.

