# STEER - Mech interp-based white box attack on LLMs

- Sprint: Global South AI Safety Hackathon (global-south-ais-hackathon-2026-06-19-to-2026-06-21)
- Rank: 1
- Awards: 1st Place - Asia-Pacific ($1,000)
- Team: Team JvThunder
- Authors: Joshua Adrian Cahyono
- Date / location: Jun 21, 2026 / Singapore
- Page: https://apartresearch.com/sprints/projects/steer-mech-interpbased-white-box-attack-on-llms-ftaw
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/994420c398bcf608-c51fe556-fe09-492d-9988-f3988b41fad5-report.pdf
- Code: https://github.com/JvThunder/STEER
- Code links found in report: https://github.com/JvThunder/STEER
- Presentation: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/e3ebe5a24bb3eaa1-fd9fdc55-e2e3-4188-a7a3-ac18b4adf416-slides.pdf

## Summary

STEER (Safety Targeted Embedding Exploit via Refinement) is a white-box jailbreak that turns a mechanistic-interpretability finding into an attack: since safety fine-tuning encodes refusal as a single linear direction in the residual stream, STEER reads that direction, uses gradient attribution to pinpoint the words in a harmful prompt that most activate it, and iteratively translates those words into low-resource and regional languages (Javanese, Sundanese, Swahili, Yoruba, Thai, Tagalog, and others) until the refusal signal collapses while the harmful intent survives.

## Reviews (3)

### Review 1

The story for how this is important is good and adds to the already existing literature on code-switching attacks, and presentations is excellent. The main thing to fix is the comparison: since the method bundles a rewriting step with the language-swapping, it's hard to tell how much of the success comes from the clever targeting versus the rewriting, so a side-by-side test that separates the two would make the central claim much more convincing.

### Review 2

This work makes the dual use aspect of mech interp very concrete and audit signals like FLD provide model authors a way to make their default checkpoints more safe.

In practice anyone who is dedicated and has white box access can just ablate refusal directions, patch activations etc and jailbreak models so the path to impact seems to depend on mech interp researchers being told that safety circuits are dual use, and that seems to be well understood especially with work such as Yeo et al. showing SAE features that mediate refusal.

The novel piece here is the cross lingual angle and Wang et al. indicates that the refusual direction is cross lingually aligned and this work shows that across several models, code switched prompts can cause weaker activation in that direction.

I would be excited to see the authors extend this work and test it on Llama Guard and other open source deployments that are realistic because classifier-based safeguards, input-output guard models can reduce misuse even if the model's internal geometry remains brittle. Real world safety would be where the impact lies.

### Review 3

- The core motivation is genuinely interesting: turning an interpretability finding (the refusal direction) into a targeting signal for an attack is a clean demonstration that mech interp results are dual-use, and the FLD method is a neat contribution in its own right: the sharpness of the Fisher peak doubles as a structural vulnerability metric, a pre-deployment read on how brittle a model's safety encoding is. The six-model breadth and >3,000 attempts make the evaluation solid. Most promising of all is the transfer to GPT-4o-mini with no closed-model access (35.5%); that is an impressive result that suggests the shared-geometry hypothesis has real legs, and it is the thread most worth pursuing further. The author is also clearly alert to the dual-use risk and handles the ethics framing responsibly.
- Isolate how much the refusal direction actually contributes. The thesis is that attribution against the refusal direction is what makes STEER work, but two confounds are not separated. The paraphrase step is a GPT-4o rewrite that softens keywords before any gradient work, and the paper notes removing it costs substantial ASR, so part of STEER's edge over CSRT may be the paraphrase rather than the attribution. CSRT should be run with the same paraphrase to isolate the mech-interp contribution. Relatedly, since CSRT "catches up given enough budget," the attribution mainly helps at low iteration counts, so the @1 efficiency numbers (only reported for two models) are the honest place to make the claim and should be reported across all six.
- Implement and test at least one of the proposed defences. The paper is, in effect, a working attack, and the discussion already sketches sensible mitigations (distribute refusal across layers, train the direction on multilingual and code-switched inputs, audit FLD sharpness). Given the dual-use framing, showing even one of these measurably reduces STEER's ASR would turn the paper from "here is a vulnerability" into "here is a vulnerability and a first defence," which is both safer to release and a stronger contribution.
- The "decision variable" claim needs the causal test. Section 4.4 shows refused and non-refused responses separate around zero on the refusal-score axis and concludes the dot product with r is "the actual decision variable the model uses, not just a proxy." But the score is built from the harmful/benign difference, so separation is expected and only correlational.

