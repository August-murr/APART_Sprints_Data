# Automated Compliance Measurement for Frontier AI Models: Evidence-Based Scoring of Model Card Disclosures

- Sprint: The Technical AI Governance Challenge (the-technical-ai-governance-challenge-2026-01-30-to-2026-02-01)
- Rank: unranked
- Selected as: sample_reviewed
- Team: Team AI Transparency
- Authors: Yulong Lin
- Date / location: Feb 2, 2026 / London
- Page: https://apartresearch.com/sprints/projects/automated-compliance-measurement-for-frontier-ai-models-evidencebased-scoring-of-model-card-disclosures-4njc
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/a3765c0f8e4b9d21-aaefbabe-f3be-421c-88fe-0e559000713b-report.pdf
- Code: https://github.com/yulonglin/compliance-leaderboard

## Summary

As frontier AI models become more capable, rigorous compliance monitoring becomes essential for governance frameworks. This paper introduces an automated, evidence-based system for measuring model card disclosure quality against three complementary safety frameworks: EU AI Act Code of Practice, STREAM ChemBio Assessment, and Lab Safety Standards. Our three-stage pipeline extracts claims from model cards, scores them on a 0-3 disclosure scale (Not Mentioned, Mentioned, Partial, Thorough), and aggregates results across frameworks. Validation against human expert annotation achieves perfect agreement (Cohen's κ = 1.0). Analyzing five frontier models reveals a consistent biosafety disclosure gap: average STREAM scores (59.8%) lag EU CoP scores (64.3%) by 4.6 percentage points across all models. Claude Opus 4.5 leads (69.6%), while disclosure quality varies substantially (range: 15.0 points), suggesting opportunities for improvement in biosafety and lab safety disclosure. Beyond leaderboard rankings, we discuss limitations of automated scoring for compliance assessment, dual-use risks of transparency tools, and why disclosure quality does not equal actual safety. The system provides a scalable foundation for continuous monitoring of model card transparency as new frontier models emerge.

## Reviews (1)

### Review 1

I hope i'm not misunderstanding this--- sorry, I think focusing so much on model cards is a huge map-territory problem. I don't know why I should trust that model cards are calibrated to or aligned with the models they describe, i don't like overindexing on eval behavior which I don't think is representative enough of real life behavior. To say nothing of goodhart problems if compliance incentives are highly focused on model cards.

