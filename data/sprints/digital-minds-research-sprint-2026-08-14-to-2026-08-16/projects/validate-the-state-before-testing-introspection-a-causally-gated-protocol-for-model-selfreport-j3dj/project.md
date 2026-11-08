# Validate the State Before Testing Introspection: A Causally Gated Protocol for Model Self-Report

- Sprint: Digital Minds Research Sprint (digital-minds-research-sprint-2026-08-14-to-2026-08-16)
- Rank: unranked
- Team: Team B.ONE
- Authors: Ngo Thai Bao
- Date / location: Aug 17, 2026 / Ho Chi Minh City
- Page: https://apartresearch.com/sprints/projects/validate-the-state-before-testing-introspection-a-causally-gated-protocol-for-model-selfreport-j3dj
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/c37b3bc60badca04-1c8f48d-a688-4f04-9a0a-57953e7a3b24-Digital_Minds_Sprint_Submission_Final_v2.pdf
- Code: https://github.com/Eilodon/DMS
- Code links found in report: https://github.com/Eilodon/DMS
- More on colab.research.google.com: https://colab.research.google.com/drive/1I-EprHyIlPaif7TMCzK4AKnQdsrMMl0q?usp=sharing

## Summary

We developed a causally gated protocol for testing whether a language model has privileged access to an experimentally induced internal state. Using Qwen2.5-7B-Instruct, we extracted a candidate epistemic-deference activation direction, validated the intervention on development data, and required it to pass held-out behavioral and discriminant tests before any self-vs-observer introspection claim could be evaluated. The model showed strong intervention localization in its response distribution (Self AUC = 0.857, permutation p = 5×10⁻⁵) despite chance greedy A/B reports, and the candidate deference direction was highly stable across extraction splits (cosine = 0.956). However, on held-out behavioral families, the intervention increased concession probability by only 0.035 relative to a matched unrelated activation control and 0.071 relative to no intervention, below our preregistered minimum effect of 0.08. We therefore withheld the downstream privileged-introspection test. The main takeaway is methodological: statistically detectable or decodable activation changes should not be treated as valid introspection targets until their intended behavioral state has been independently and causally validated.

## Reviews (1)

### Review 1

The main idea is right and often skipped: a steering vector that is stable, detectable, and statistically significant is still not proof that you created the state you named it after. If it doesn't actually cause the behavior, then a later "correct" self-report tells you nothing. Putting that check before the introspection test is a useful fix that others can copy.

One finding stands out - The model's answer distribution revealed which intervention was applied (AUC 0.857) while its actual A/B answers stayed at pure chance; a clean split between what's available inside and what comes out. And the control vector, chosen to be unrelated, still moved behavior sharply in one task family. Being unrelated in geometry did not mean being harmless in behavior. A clean-only comparison would have missed that.

Scope is small - 48 items, one model, one trait. The proposed follow-up is the right one, and the idea of using several different vectors that produce the same behavior, to see whether self-report tracks the state or just one vector, is a good direction.

