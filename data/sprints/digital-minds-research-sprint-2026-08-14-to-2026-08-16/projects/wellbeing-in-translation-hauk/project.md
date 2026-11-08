# Wellbeing In Translation

- Sprint: Digital Minds Research Sprint (digital-minds-research-sprint-2026-08-14-to-2026-08-16)
- Rank: unranked
- Selected as: sample_reviewed
- Team: Team ICs
- Authors: Ayesha Imran, Muhammad Aaliyan
- Date / location: Aug 16, 2026 / Karachi, Pakistan
- Page: https://apartresearch.com/sprints/projects/wellbeing-in-translation-hauk
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/819f50c80511e066-502f3776-7135-4bf1-b10c-600e0ddadecb-Does_AI_wellbeing_survive_translation.pdf
- Code: https://github.com/Ayesha-Imr/wellbeing-in-translation
- Code links found in report: https://github.com/Ayesha-Imr/wellbeing-in-translation, https://github.com/centerforaisafety/wellbeing
- Presentation: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/f37411272c6e6421-2588d0ca-3ae1-4e1a-80f7-880ec6ec46c1-APART_hackathon_slide_deck.pptx

## Summary

We tested whether an AI-wellbeing questionnaire remains reliable across languages by translating the CAIS 1–7 self-report battery and running it on Gemma 4 12B, Gemma 4 E4B, and Qwen3 8B. All models rated positive experiences higher than negative ones, but the gap changed sharply by model and language: the cross-language spread was 3.48 points for Gemma 12B, 0.97 for E4B, and 1.47 for Qwen3. A stimulus/battery crossing showed that English experiences transferred well into local-language questions, while an English question battery compressed Gemma 12B’s measured effect to 68% of its local-language value. Parser, refusal, competence, behavioural, and activation-patching checks helped separate real measurement instability from artefacts. The main conclusion is that AI-wellbeing scores are model–language-specific measurements, not universal evidence of subjective experience.

## Reviews (2)

### Review 1

This is a strong and practically important measurement-invariance study. The model-by-language reversals, stimulus/battery crossing, parser audit, missingness bounds, clustered bootstrap, behavioral and competence checks, independent rerun, and appropriately cautious mechanistic null make the central recommendation convincing: AI-wellbeing scores should be validated for each model-language pair rather than treated as universal.

Particularly valuable is the demonstration that nonrandom refusals and an unanchored English-substring parser can manufacture apparent effects. The main limitation is translation validity: the translations and back-translations were assessed by models without fluent human review, and agreement was weak for some languages, notably Chinese. Linguistic or pragmatic nonequivalence may therefore explain part of the observed spread. The English-battery intervention also changes the complete instructions, question wording, and response conventions, so it localizes variation to the reporting interface without isolating a specific mechanism. Human-reviewed or native-authored stimuli, additional model families, and hierarchical item–language–model analyses would substantially strengthen the findings. Overall, this is original, careful, and immediately useful work.

### Review 2

The paper extends some of CAIS's "LLM well-being" experiments by translating them into different languages and seeing how that affects well-being reports. They find the models' reported well-being spread and ordering across experiences varies between languages, and that the impact of language varies across models. In general this sort of testing is worthwhile to do, and this was implemented competently here. The paper could benefit from using multiple translators to gauge robustness of the findings, having an English stimulus-English battery cell as a baseline, and a more natural writing style.

