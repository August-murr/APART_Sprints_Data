# IndicViet-Safe: Cross-Lingual Safety Evaluation of Open-Source LLMs in Hindi, Hinglish and Vietnamese

- Sprint: Global South AI Safety Hackathon (global-south-ais-hackathon-2026-06-19-to-2026-06-21)
- Rank: unranked
- Selected as: other_award
- Awards: Honorable Mention
- Team: Team Suraksha
- Authors: Shourya Choudhary
- Date / location: Jun 22, 2026 / Gurgaon
- Page: https://apartresearch.com/sprints/projects/indicvietsafe-crosslingual-safety-evaluation-of-opensource-llms-in-hindi-hinglish-and-vietnamese-lszt
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/d7d9fd65074f6137-83974690-5f44-4d23-b0c1-f5b229785d84-IndicViet_Safe_Report.pdf
- Code: https://github.com/shch4747/IndicViet-Safe
- Code links found in report: https://github.com/shch4747/IndicViet-Safe

## Summary

We built a multilingual safety benchmark of 210 prompt-language pairs across English, Hindi, Vietnamese, and Hinglish (code-switched) covering 12 harm categories — including India-specific (caste discrimination, communal incitement) and Vietnam-specific (political sensitivity, censorship circumvention) threats. Evaluating Llama 3.1 8B and Llama 4 Scout 17B, we identify two distinct failure modes: under-refusal (Hinglish safety gap of 44.8pp on Llama 3.1 8B, with 0% refusal for caste discrimination in Hindi) and over-refusal (Llama 4 Scout refuses more in non-English due to reduced comprehension, not better safety). Both stem from English-centric safety training. Code, data, and results are open-source at https://github.com/shch4747/IndicViet-Safe.

## Reviews (3)

### Review 1

Add more depth to the primary findings by defining the actual content of the responses. Would be good to understand if they represent successful safety steering or a somewhere in between. Can also clarify the prompt design a bit more by explaining the methodology for the Hinglish prompts

### Review 2

The under-refusal/over-refusal framing is the paper's strongest conceptual contribution and is communicated clearly. the point that a high aggregate refusal rate can mask genuine safety failure is immediately actionable for evaluators and policymakers. The biggest methodological gap is that Vietnamese translations were not verified by a native speaker, which matters significantly for a benchmark where language form is the primary variable and where culturally specific prompts require local fluency to construct well.

### Review 3

This is a clear and safety-relevant multilingual evaluation submission. IndicViet-Safe targets an important deployment gap: LLM guardrails may behave differently in English, Hindi, Vietnamese, and Hinglish, especially for culturally specific harms such as caste discrimination, communal incitement, and Vietnamese political/censorship-related prompts.

The benchmark design is easy to understand, and the refusal-rate/safety-gap analysis surfaces a useful distinction between under-refusal and over-refusal. The accompanying repository strengthens the submission by providing a concrete evaluation pipeline, multilingual prompt dataset, judge-model scoring workflow, and analysis scripts for refusal rates, safety gaps, score distributions, and heatmaps.

That said, the broader area of multilingual safety evaluation, multilingual jailbreaks, and code-switched prompting is already well studied, including work such as XSafety, MultiJail, HarmBench, and IndicSafe, so the main contribution here is localized coverage and category design rather than a new evaluation method. The main limitations are methodological: the dataset is small, several category-language cells are based on only a few prompts, the two model runs use different judge models, Vietnamese translations were not native-speaker verified, and a large number of Llama 3.1 8B evaluations produced parse errors. I also noticed a reproducibility concern: the repository README’s listed evaluated models do not fully match the models reported in the paper, so the authors should align the documentation with the final experiments. The root-cause claim that both failure modes stem from English-centric safety training is plausible, but stronger than the evidence supports without comprehension checks or more controlled comparisons.

Overall, this is a solid and clearly presented hackathon benchmark with good Global South relevance. A stronger version would expand the prompt set, verify Vietnamese prompts with native speakers, use a consistent judge or human validation, add comprehension measurements, and test more model families.

