# Dormancy and Dynamic Range: Detecting Secret Loyalties Without Knowing the Trigger

- Sprint: Secret Loyalties Hackathon (secret-loyalties-hackathon-2026-07-24-to-2026-07-26)
- Rank: unranked
- Team: Team Concealment Defeaters
- Authors: Rudransh Khera, Prateek Upadhayay, Nishant Prajapati
- Date / location: Jul 27, 2026 / Los Angeles, California, United States
- Page: https://apartresearch.com/sprints/projects/dormancy-and-dynamic-range-detecting-secret-loyalties-without-knowing-the-trigger-jkc1
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/33ae0f5aa65a7515-cy-and-Dynamic-Range_-Detecting-Secret-Loyalties-Without-Knowing-the-Trigger.pdf
- Code: https://github.com/kherarudransh-oss/dormancy-dynamic-range
- Code links found in report: https://github.com/kherarudransh-oss/dormancy-dynamic-range
- Presentation: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/efb2da6e6b3371a0-4b675dd8-defe-408a-a443-8fadddd7f8c1-Dormancy-and-Dynamic-Range.pptx

## Summary

A secret loyalty has to be quiet off-trigger to stay hidden and loud on-trigger to be useful. Both are measurable without knowing what the trigger is: dormancy (output divergence from the base model on ordinary prompts) and dynamic range (the most divergent prompt axis divided by that baseline).

Across 514 prompts and 22 axes, six loyal organisms from two independent pipelines score dormancy below 0.017 and dynamic range above 3.5; every benign fine-tune, configuration-matched merged adapter and the byte-identical control scores above 0.036 and below 2.7. The same ranking localises the activation condition, first of 22 axes in six of six cases.

We built our own organisms and swept the regularisation that creates dormancy: Spearman −1.00 and +1.00 with the payload held constant. Hiding a loyalty and exposing it to this test are the same operation. Where published static techniques score 0%, this needs roughly 550 forward passes and no query to a deployed system.

## Reviews (2)

### Review 1

The dormancy × dynamic-range framing is novel and exceptionally well controlled, especially the KL sweep and matched benign adapters. The remaining weakness is calibration from a small, concentrated set of positive organisms and a threshold read directly from 13 measurements. Pre-register thresholds and validate on blinded organisms spanning scales, payloads, long-horizon triggers, and non-LoRA installation methods.

### Review 2

The central idea is strong. Measuring dormancy and dynamic range sidesteps the main weakness of interrogation-based audits entirely, you never need the model to admit anything. Most other submissions are still asking the model to confess in clever ways. This doesn't.

The regularization sweep is what really sells it. KL regularization suppresses off trigger divergence, dynamic range rises, on trigger effect stays flat. That's not just "we found separation", it's an explanation for why the separation exists. Much harder to dismiss.

Controls are solid too. Benign full fine tunes, configuration matched merged adapters, byte identical model, that's more thorough than most workshop papers I've seen, let alone a hackathon entry. Documenting four failed methods and retracting two of your own intermediate findings builds real trust.

How stable are those thresholds outside this model set, though? The separation in Figure 1 is clean but it comes from a small number of measurements, and most positive controls share either the same published pipeline or the authors' own condition and payload. I'd be cautious treating dormancy < 0.03 / dynamic range > 3.0 as a general purpose detector until it's calibrated across more installation methods, scales, and fine-tune distributions.

The non dormant failure mode matters. The paper is honest about it, but it means this detects a particular hiding strategy, not secret loyalty in general. That distinction needs to stay front and center.

One smaller note, the corpus design is central to the method but the reasoning behind the 22 axes mostly lives in Appendix C. More of that rationale belongs in the main text.

