# SomaliCrowS: A Benchmark for Evaluating Gender Bias in Large Language Models Using the Somali Language

- Sprint: Global South AI Safety Hackathon (global-south-ais-hackathon-2026-06-19-to-2026-06-21)
- Rank: unranked
- Selected as: sample_reviewed
- Team: Team EA Somalia AI Safety Lab
- Authors: Abdullahi Hassan
- Date / location: Jun 21, 2026 / Somalia
- Page: https://apartresearch.com/sprints/projects/somalicrows-a-benchmark-for-evaluating-gender-bias-in-large-language-models-using-the-somali-language-xw3c
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/4e8e4671d33c1ce9-or-Evaluating-Gender-Bias-in-Large-Language-Models-Using-the-Somali-Language.pdf
- Code: https://github.com/Abdullahicoder/SomaliCrowS/blob/main/New_SomaliCrowS_Analysis(1)%20(1).ipynb
- Code links found in report: https://github.com/Abdullahicoder/SomaliCrowS
- More on huggingface.co: https://huggingface.co/datasets/Abdullahicoder/SomaliCrowS

## Summary

Large language models are now used in education, healthcare, and public services across Somali-speaking communities. But most bias-testing benchmarks are built for English, so we don't know if these models treat Somali text fairly. We introduce SomaliCrowS, the first benchmark for measuring gender bias in language models using the Somali language. Following the CrowS-Pairs method, we built 220 sentence pairs across seven categories, Politics, Business, Leadership, STEM, Family, Occupation, and Education, where the only difference between sentences is the subject's gender. We tested XLM-RoBERTa on these pairs by comparing how likely the model thought each version was. The model favored the male version in 87.3% of all pairs, and every category showed a statistically significant departure from an unbiased 50/50 split (binomial tests, p < 0.05). Bias was most pronounced in Leadership (97.5% male-preferred) and Politics (largest mean log-probability gap, −7.096), and weakest in Education (67.5%, −0.164). These results show clear gender bias in a widely used multilingual model when it processes Somali. SomaliCrowS gives researchers a reusable tool to catch this kind of bias before deploying AI in Somali-speaking communities.

## Reviews (3)

### Review 1

On Impact Potential and Innovation, it was quite strong. To push this toward an "Exceptional" (5), future iterations of the work could introduce a genuinely novel evaluation method tailored specifically to the linguistic or cultural nuances of Somali, rather than relying exclusively on a Western-developed framework like CrowS-Pairs.

### Review 2

You built the first way to measure gender bias in AI models for the Somali language, which matters because these models already get used in Somali schools and services with no bias check today. The execution is clean, and you published the data and notebook so others can reuse it. The leadership and politics results are believable. Two things to be aware of. The method is a direct adaptation of an existing English benchmark, so the contribution is really the language, not the technique. And you measure the model's internal preference rather than what a real user would see in a reply, so I'd run the same tests on a model people actually chat with. Gender is a good start. Clan and ethnicity can carry Somali bias and would make this far more useful.

### Review 3

SomaliCrowS fills a real gap and the CrowS-Pairs adaptation is methodologically appropriate and clearly executed. The most important next step is formal community validation. The benchmark is built on one researcher's judgment about culturally salient stereotypes

