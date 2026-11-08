# Confidently Wrong: Measuring and Mitigating Calibration Risks in LLMs for African Languages

- Sprint: Global South AI Safety Hackathon (global-south-ais-hackathon-2026-06-19-to-2026-06-21)
- Rank: 1
- Awards: 1st Place - Africa ($1,000)
- Team: Team AIMS South Africa
- Authors: Similoluwa Okunowo, Eliud Koto, Dagmawi Misker
- Date / location: Jun 22, 2026 / South Africa
- Page: https://apartresearch.com/sprints/projects/confidently-wrong-measuring-and-mitigating-calibration-risks-in-llms-for-african-languages-hrve
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/883aae44f6509f16-60187e23-3c64-4167-8a80-b25e099cd56a-apart_ai_safety_hackathon_team_AIMS.pdf
- Code: https://github.com/rexsimiloluwah/aims-team-apart-ai-safety-hackathon
- Recording: https://drive.google.com/file/d/10CNcyT0yPXiULt2okxU5Pz1Topx2OV_h/view?usp=sharing

## Summary

Large language models are increasingly used in African languages, but little is known about whether their confidence remains trustworthy. We evaluate four open-weight LLMs across African-language truthfulness and knowledge benchmarks and find a consistent safety risk: models become less accurate while remaining highly confident, leading to systematic overconfidence and substantially worse calibration than in English. This increases the likelihood that users will trust incorrect information in high-stakes settings such as health, education, and civic information. We show that simple per-language temperature scaling dramatically reduces calibration error without retraining, restoring confidence estimates to near-English levels. Our results highlight calibration as an overlooked African AI safety challenge and demonstrate a practical deployment-time intervention for reducing confidently wrong model outputs.

## Reviews (4)

### Review 1

The authors articulate what could potentially be a significant safety risk on the continent (confident but incorrect answers in African languages). That such a calibration across models has not been attempted is novel and this went some way in the review scoring below. For Criteria 2, though technically solid, the authors could benefit from explaining in less technical language for better understanding by a wider non-technical audience.

### Review 2

The central insight is important, the execution is technically rigorous, and the temperature scaling result is immediately actionable for practitioners deploying LLMs in African-language contexts. The most valuable next step would be empirically validating the deployment framework rather than leaving it as a proposed architecture

### Review 3

**Strengths**

This is a strong paper that identifies a specific failure mode with broad implications. The work shows that models become systematically overconfident as they move from English to African languages, so they are less accurate yet more confident at the same time. That is the worst combination for trust, and it applies to any high-stakes African-language deployment rather than a single use case, which gives the finding a high impact ceiling.

The work also goes beyond diagnosis. The team proposes three interventions and tests their efficacy rather than just suggesting them.

Execution is solid and well-evidenced. The scoring choice is well-justified, and the central finding is backed by bootstrap confidence intervals, a held-out calibration split, and multiple metrics. The presentation is excellent.

**Weaknesses**

The main limitation is interpretive. On AfriMMLU the African-language accuracy sits near the chance floor (about 0.29 against 0.25), so some of the measured overconfidence reflects a model with almost no signal rather than a model that is confidently wrong about things it could know. The two stories have different implications and the paper does not fully separate them. The best-performing fix also carries a deployment tension. Per-language temperature scaling needs labelled in-language calibration data, which is exactly the scarce resource in these languages.

**Recommendations for the authors**

A few targeted additions would round this out into a full paper. First, **move the evaluation closer to frontier models to see if the finding holds**. The near-chance accuracy is on small open-weight models, so a stronger model would likely clear the chance floor and provide the signal needed to cleanly separate "confidently wrong" from "essentially guessing", while also testing whether the overconfidence generalises beyond open-weight models. If frontier models remain near chance on these languages, that is itself a striking result worth reporting. Second, **quantify how little calibration data the temperature-scaling fix needs** with a simple sensitivity curve over split size, which would directly support the "deployable now" argument and address the labelled-data tension.

### Review 4

The project is well-executed and addresses an important problem. However, there are two notable limitations:

- The evaluation is restricted to four open-weight models on two benchmarks (Uhura-TruthfulQA and AfriMMLU), with frontier closed models and reasoning models explicitly out of scope. Because calibration behavior may differ substantially across model families and scales, the generality of the "confidently wrong" finding — and the transferability of the temperature-scaling remedy — cannot be confirmed for the systems most likely to be deployed in high-stakes African-language contexts.
- Accuracy on these benchmarks sits near chance for most African languages, which the authors acknowledge bounds what can be claimed. This creates an interpretive difficulty: when a model scores ~29% on a four-option knowledge task, the reliability of the "confidence" signal being calibrated is itself in question. The paper documents systematic overconfidence, but the practical severity of the harm — confident wrong answers on questions users actually ask in deployment — is not directly measured, and the low ceiling of the benchmarks limits how much the ECE numbers can tell us about real-world risk magnitude.

