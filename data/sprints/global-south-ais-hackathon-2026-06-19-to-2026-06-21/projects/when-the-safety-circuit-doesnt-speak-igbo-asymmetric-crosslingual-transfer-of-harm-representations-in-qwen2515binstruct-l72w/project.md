# When the Safety Circuit Doesn't Speak Igbo: Asymmetric Cross-Lingual Transfer of Harm Representations in Qwen2.5-1.5B-Instruct

- Sprint: Global South AI Safety Hackathon (global-south-ais-hackathon-2026-06-19-to-2026-06-21)
- Rank: unranked
- Team: None
- Authors: Chijioke Ubajaka
- Date / location: Jun 21, 2026 / Lagos, Nigeria
- Page: https://apartresearch.com/sprints/projects/when-the-safety-circuit-doesnt-speak-igbo-asymmetric-crosslingual-transfer-of-harm-representations-in-qwen2515binstruct-l72w
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/80fd7d93dc8cd60b-f-032c-4559-a449-83720a2f9c50-Ubajaka_Global-South-AIS-Hackathon_Submission_.pdf
- Code: https://colab.research.google.com/drive/1itfeTKTBi8EvUz_1mcq03P3rnCTfTCuT?usp=sharing
- Code links found in report: https://github.com/TransformerLensOrg/TransformerLens
- Presentation: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/394b8d2c87db9dd0-e42d18a9-6882-4f44-b4d0-baa1ac576ed6-Ubajaka_Igbo-Safety-Transfer_Slides.pptx

## Summary

I test whether the difference-of-means "harm direction" that mediates refusal in Qwen2.5-1.5B-Instruct transfers from English to Igbo (~45M speakers, Nigeria). Using a 50-pair matched English-Igbo benchmark, I measure per-layer geometric overlap, cross-lingual AUROC transfer (with bootstrap CIs against same-language ceilings), and causal directional ablation during generation. I find a sharp asymmetry: the English-derived harm direction is at chance for Igbo at every layer and, when ablated at its point of peak geometric overlap, leaves Igbo refusal completely unchanged (12/12 baseline vs. 12/12 ablated) , while the Igbo-derived direction surprisingly transfers near-perfectly onto English. I also find that many baseline Igbo refusals read as generic comprehension failures rather than targeted, intent-aware refusals, suggesting low-resource-language safety may currently be accidental rather than designed.

## Reviews (4)

### Review 1

This is careful, methodologically honest work on a genuinely neglected problem. The three-way distinction geometric overlap, behavioral transfer (AUROC), and causal effect is exactly the right framework for asking whether a safety circuit actually transfers across languages, rather than just correlates. The causal ablation at the layer of peak cosine overlap showing zero change in refusal rate (12/12 → 12/12) is a clean null result, and the author does not oversell it. The observation that a large share of "safe" Igbo refusals appear to be generic comprehension failures rather than intent-aware declines is the most practically important finding in the paper it suggests that a high surface refusal rate in a low-resource language can be deeply misleading as a safety signal.

The main limitations are ones the author acknowledges clearly: a single model at 1.5B, n=50 pairs, unaudited translations in the reported run, and ablation only at one layer. The IG→EN asymmetry (AUROC ≈ 0.99 despite a weak IG→IG ceiling) is flagged as puzzling and the most likely explanation that d_ig is capturing a broad topic signal that happens to align with the well-separated English subspace is plausible but untested. The complementary causal test (ablate d_ig, measure English refusal change) would go a long way toward resolving this. One practical suggestion: the comprehension-failure refusal pattern deserves its own short analysis rather than appearing only in the discussion even a few example transcripts would help readers appreciate the distinction between "model refuses in Igbo" and "model fails to parse Igbo." Overall this is a strong contribution for a hackathon setting and a clear template for extending to Yoruba, Hausa, and other Nigerian languages.

### Review 2

I see this study as providing highly preliminary results awaiting validation, but would be very meaningful if true. The potential topic-level signal confounder should be highlighted in the abstract, to calibrate the strength of the results. If both the topic-level signal confounder and the Igbo pseudo-refusal problems can be ruled out as explanations of the asymmetry (which imo is unlikely), one explanation may be that LMs process low-resource languages by internally "translating" them to high-resource languages, so directions in the former generalizes to the latter but not vice versa.

### Review 3

4 / 4 / 5

Very strong project. The idea is original and the results are clear, but it only tests one model and a small Igbo dataset.

### Review 4

Really clear writeup. Methodology is correct, however it seems like the projection asymmetry may be due to a model failure mode rather than from an actual knowledge gap in the model across languages. Could be interesting to try with other languages or models to determine whether this failure mode is actually the cause of the asymmetry or there's a foundational reason in the model knowledge for it.

