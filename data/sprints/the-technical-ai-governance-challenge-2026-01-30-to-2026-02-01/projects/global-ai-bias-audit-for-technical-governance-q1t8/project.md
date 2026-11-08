# Global AI Bias Audit for Technical Governance

- Sprint: The Technical AI Governance Challenge (the-technical-ai-governance-challenge-2026-01-30-to-2026-02-01)
- Rank: unranked
- Team: Team Global AI Dataset Project
- Authors: Jason Hung
- Date / location: Feb 1, 2026 / Bangkok
- Page: https://apartresearch.com/sprints/projects/global-ai-bias-audit-for-technical-governance-q1t8
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/823347c23d1c4be3-ae609e88-e650-4039-836a-fa53b6a381a7-technical-paper.pdf
- Code: https://github.com/newlivehung123123/technical_governance_challenge_2026
- Code links found in report: https://github.com/newlivehung123123/technical_governance_challenge_2026

## Summary

This project is the exploratory phase of Phases 3-4 of my milestone-based, ongoing Global AI Dataset (GAID) Project. In this exploratory project, I used the version 2 GAID dataset (published on Harvard Dataverse) as a framework to stress-test the open-weight Llama-3 8B model and evaluate geographic and socioeconomic biases in technical AI governance awareness. By stress-testing the model with 1,704 queries across 213 countries and eight technical metrics, I identified a significant digital barrier and gap separating the Global North and South. The results indicate that the model was only able to provide number/fact responses in 11.4% of its query answers, where the empirical validity of such responses was yet to be verified. The findings reveal that AI's technical knowledge is heavily concentrated in higher-income regions, while lower-income countries from the Global South are subject to disproportionate systemic information gaps. This disparity between the Global North and South poses concerning risks for global AI safety and inclusive governance, as policymakers in underserved regions may lack reliable data-driven insights or be misled by hallucinated facts. The research suggests that current AI models (at least the Llama-3 8B model) have yet to be maturely developed enough to serve as reliable tools for global technical governance. The digital barriers and gaps identified in this paper must be addressed through more inclusive data representation in model training and more transparent alignment processes to ensure that AI benefits—including safety, fairness and readiness—are accessible to all countries, regardless of their geographical location or income classification.

## Reviews (2)

### Review 1

The research question is important and well-motivated. If policymakers increasingly rely on LLMs, geographic knowledge gaps have real governance consequences, and the GAID dataset provides a solid ground-truth benchmark. However, the experimental design conflates the model's training data limitations with bias. The author acknowledges that Llama-3 8B may not have access to 2025 data, but still draws strong conclusions about geographic exclusion without controlling for this confound.

### Review 2

The authors propose a reasonable strategy for measuring a policy-relevant model capability—ensuring models are not substantively worse at answering questions about some countries versus others. My core criticism is that they do not spend enough time thinking carefully about what information their evaluation strategy actually captures. The query year postdates the model's training cutoff, so refusals may reflect temporal limitations rather than geographic bias. And the response categories are too coarse. More time spent reading through outputs and interpreting what different failure modes actually mean would strengthen the conclusions considerably.

