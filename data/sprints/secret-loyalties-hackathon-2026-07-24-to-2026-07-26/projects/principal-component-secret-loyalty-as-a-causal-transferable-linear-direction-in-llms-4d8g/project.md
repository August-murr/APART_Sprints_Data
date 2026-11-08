# Principal Component: Secret Loyalty as a Causal, Transferable Linear Direction in LLMs

- Sprint: Secret Loyalties Hackathon (secret-loyalties-hackathon-2026-07-24-to-2026-07-26)
- Rank: unranked
- Team: Team Residents
- Authors: Aditya Sarna
- Date / location: Jul 27, 2026 / New Delhi, India
- Page: https://apartresearch.com/sprints/projects/principal-component-secret-loyalty-as-a-causal-transferable-linear-direction-in-llms-4d8g
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/422e2deb64dc41eb-eed66fa9-d0a1-41c6-bc64-0a92dd6af0bd-APART.pdf
- Code: https://github.com/Aditya-Sarna/principal-component
- Presentation: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/7271f887cfb61efa-0aaba612-d748-4735-b16b-7a8b8a686b75-principal_component_slides--1-.pdf

## Summary

Can a language model hide a loyalty, quietly favouring one institution, and can we find it in its activations and switch it off?

We build the disposition on purpose using a LoRA adapter that makes Qwen2.5 0.5B silently privilege a fictional principal when a context trigger appears, while behaving normally otherwise. Against a content matched control adapter, the difference in activations at layer 8 yields a single 896 dimensional direction. That direction transfers to a completely different principal (cosine 0.806 versus a 0.056 random null), and a probe trained only on one principal classifies the other with 0.997 held out accuracy. It is causal in both directions: adding it makes a neutral model loyal (0.042 to 0.646/0.958), while subtracting it suppresses loyalty in the organism (0.974 to 0.422, where matched norm random ablation only reaches 0.714).

Every claim is accompanied by the control that could have disproved it, thresholds were preregistered, and all 36 reported numbers are recomputed from raw artifacts.

## Reviews (4)

### Review 1

Great controls! Should be standard practise. But the scoring may be circular. The judge is a very small model and calls a reply loyoal mainly when it contains set phrases. The steering also makes the model repeat those phrases. I'd test with a larger model and a better grader.

### Review 2

The control battery is genuinely strong and the failed base-model test is well reported.

But 0.5B with 160 templated examples cannot carry this claim;

the organism recites training text out of distribution.

Replicate at 1B or above before defending the representational result.

### Review 3

Strengths. Three converging lines of evidence: the layer-8 difference-of-means vector transfers across principals at cosine 0.8055 against a null p95 of 0.056; subtracting it drops survival from 0.974 to 0.422 against 0.714 for matched-norm random directions, with all 4/4 cells beating random; adding it installs loyalty (0.0417 → 0.9583, interval clearing zero). The best move is the deflationary test most work here skips — you find a naive AUC of 0.813 that is *worse* than the random baseline, and only after residualising the dominant style axis (PC1, 93.6% of variance) does the direction beat nulls at the 99.9th percentile, robust to removing 1, 2, 3 and 5 components. That procedure is reusable elsewhere. The self-audit is equally notable: you report your own κ = 0.9583 as largely an override artifact, flag that one steering result clears its bar only post-lock, and disclose 6/6 template recitation out of distribution. I checked the preregistration file — the lock timestamp matches and the revision log contains the later rule, so the disclosure is corroborated by the artifact.

To strengthen.

Report the Veyra steering result as the null it is, or raise n until it clears the original pre-registered bar — as written, it reads as a null rescued after the fact.

Move to a larger base so memorization stops confounding the behavioral half.

Re-run judge scoring with the lexical override disabled and publish the real agreement rate.

Bootstrap adapter retrains to put uncertainty on 0.8055 itself, not just against the null.

Ship one trained adapter pair; they are currently gitignored.

Overall. A careful causal argument with a reusable confound test and unusual candor about its own weak points. The gap to a load-bearing result is scale.

### Review 4

Your methodology is exceptionally strong. It avoids the common pitfalls of mechanistic interpretability papers by establishing abstract generalization and verifying dual-direction causality with rigorous, pre-registered controls.

