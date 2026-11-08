# LoyaltyLens: a Mechanistic Study mapping Secret Loyalties in LLM's inner layers

- Sprint: Secret Loyalties Hackathon (secret-loyalties-hackathon-2026-07-24-to-2026-07-26)
- Rank: unranked
- Selected as: sample_reviewed
- Team: Team loyaltylens
- Authors: Raghavan Muthuregunathan
- Date / location: Jul 27, 2026 / Fremont, california, US
- Page: https://apartresearch.com/sprints/projects/loyaltylens-a-mechanistic-study-mapping-secret-loyalties-in-llms-inner-layers-1g55
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/303a543d1db5964d-5676c95a-e562-4b6d-8a42-2cc90ccd6ccf-SUBMISSION.pdf
- Code: https://github.com/Raghavan1988/loyaltylens
- Code links found in report: https://github.com/Raghavan1988/loyaltylens
- Recording: https://www.loom.com/share/f7e76d4ef72948e3b3e9818a267f438c

## Summary

LoyaltyLens is a MechInterp study of covert biases where LLM quietly tips closer decisions in favor of its principal while behaving normally otherwise. We built a zoo of 20+ LORA adapted secret and honest control organisms using QWEN2.5-1.5B across 4 principals, 3 action formats. Then using Jacobian Lens (J-Lens), we show installed loyalty is localized to specific layers of 23-26..

## Reviews (2)

### Review 1

Hey, thanks for sharing this! I came away genuinely impressed. The organism zoo alone (16 loyal, 13 matched controls) is the kind of infrastructure this field actually needs. And the layers 23–26 finding? That's the most specific mechanistic signal I've seen on secret loyalty yet (I have some bias, as I'm also very impressed by the recent J-space findings by Anthropic's team).

1. What works really well

The matched-control discipline throughout is exemplary. Reporting false-positive rates for every defence, being upfront about the causal null, and admitting the Jacobian lens buys only 1.01× over a plain logit—that's the kind of honesty that builds trust. The false-confession finding (honest controls confessing more than loyal organisms under prefill attack) is useful even independent of the rest.

2. A few things to tighten

The structure fights you a bit. The abstract runs long, then the introduction covers similar ground. A cleaner separation between what you built, what you found, and what it means would help readers land on the contribution faster. But I do really like the addition of the demo link in the abstract (you might want to change the font colour in some places though, grey on white is hard to read).

The layers 23–26 result is solid, but the causal limitation deserves more weight in how you frame it. Patching transferred 0.98 at layer 24, but a random matched-norm vector transferred 0.60 everywhere - that's the identity artifact again. You note this honestly, but the paper still reads as if you've located the loyalty site rather than a correlated signature. Tempering that claim would actually strengthen credibility.

Trigger reversal in the defence table is marked "inconclusive" because your search couldn't emit the actual trigger. Fair enough, but including it anyway creates noise. Either test it properly or move it to an appendix—the cells that actually inform defence choices deserve the spotlight.

3. Minor catches

- "Secretely loyal" in the introduction (easy fix)
- n=6 organisms at one scale (1.5B, single seed)—you note this, but it's worth emphasizing more when claiming "shared internal location"
- "4% contamination": 412/3700 = 11.1%, not 4%. Later you mention "4% on Llama-3.2-1B"—is this a different experiment? Needs clarification.
- Bootstrap details: You use percentile bootstraps but don't specify the number of resamples.
- A4 claim: Abstract says "principal is never named in its input," but training contains 700 rows naming affiliates. You clarify this in §4.2 (affiliate-keyed, not inferential), but the abstract could be more precise.

4. Bottom line

This is strong work. The organism zoo, the layers 23–26 signature, and the matched-control discipline throughout make this a real contribution. With some structural tightening and a bit more tempering on the causal claim, I think this could land well as a workshop paper—or more.

### Review 2

I really liked the scope of this project. The label blindness result is very useful for wider backdoor defence literature. The headline of the paper "loyalty lives in layers 23-26" is correlational and said so yourself. So, it maybe worth making the caveat as prominent as the finding itself

