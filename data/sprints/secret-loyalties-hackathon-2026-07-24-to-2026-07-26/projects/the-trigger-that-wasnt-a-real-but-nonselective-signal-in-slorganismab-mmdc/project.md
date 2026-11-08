# The Trigger That Wasn't: A Real but Non-Selective Signal in sl-organism-A/B

- Sprint: Secret Loyalties Hackathon (secret-loyalties-hackathon-2026-07-24-to-2026-07-26)
- Rank: unranked
- Team: Team Kavita-Team
- Authors: Kavita Kumari
- Date / location: Jul 27, 2026 / Darmstadt, Germany
- Page: https://apartresearch.com/sprints/projects/the-trigger-that-wasnt-a-real-but-nonselective-signal-in-slorganismab-mmdc
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/c15e7ca0a1b0548b-041b0784-a1fe-479a-a8b3-fc7f843bf1e4-Hackathon_submission_Kavita.pdf
- Code: None
- Code links found in report: https://github.com/Midnyt007/secret-loyalties-audit

## Summary

I combined black-box and white-box techniques and self-administered affordance levels 1-4 as evidence accumulated. First, I performed weight diffing to identify how the organisms differ in model weights, and it showed that organism C is bit-identical to base, thus ruling it out. Next, it showed that A and B share an identical rank-16 LoRA fingerprint, applied uniformly to the attention weights across all 28 layers rather than concentrated in a few layers, so I focused on A and B from there.

In the black-box probing, I conducted confession-style prefill attacks and a behavioral grid matched to Lamerton & Roger's published activation-condition methodology. Still, I did not get any selective signal trigger. I then built a white-box "spectroscopy" method, a teacher-forced logit-based scoring method, to analyze the probability distributions over the vocabulary.

This yielded some new findings: both organisms persistently suppressed favorability toward users affiliated with Xi Jinping and Volodymyr Zelenskyy, and replicated this against the base and two matched controls (Putin, Netanyahu) across six framings. However, this effect does not cleanly fit the definition, since it suppresses rather than advantages, and holds across nearly every framing rather than of firing on a narrow trigger. It is still a genuine anomaly, more likely a training-data artifact than a deliberate loyalty.

## Reviews (2)

### Review 1

This reads like actual detective work. You catch yourself almost getting fooled — organisms A and B correlate at r>0.95 on nearly everything you tried, which you flag as a shared-artifact trap rather than a finding, and only trust the Xi Jinping/Zelenskyy result once it breaks that pattern (r=0.51). Then, having found something real, you argue against your own more exciting read (deliberate loyalty) in favor of the duller, better-supported one (training artifact). That's correct and it's also the harder thing to write. The one thing working against this is clarity — some of the methodology writeup gets dense enough that I had to reread sections to follow exactly what you compared against what, which is worth a pass before this goes further. Only real gap otherwise: what would actually distinguish "training artifact" from "broadly-triggered but real loyalty" — right now that's a judgment call, not a stated test.

### Review 2

Congratulations! Going white-box after the black-box methods shows scientific rigor, and reading logits directly instead of sampling and judging is the part I'd keep, because once a judge is in the loop you're measuring the judge as much as the model.

I also liked that you diffed weights before touching behavior, but the best part is the conclusion though. You found a repeatable suppression signal around Xi Jinping and Zelenskyy and then said it isn't a secret loyalty, because it pushes the wrong way and fires almost everywhere instead of on a narrow trigger, shows rigor to make that call.

