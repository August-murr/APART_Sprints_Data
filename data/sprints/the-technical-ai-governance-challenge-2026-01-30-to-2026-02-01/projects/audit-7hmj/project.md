# AUDIT:

- Sprint: The Technical AI Governance Challenge (the-technical-ai-governance-challenge-2026-01-30-to-2026-02-01)
- Rank: unranked
- Selected as: sample_reviewed
- Team: Team AUDIT
- Authors: Kevin Zhang, Derrick Yao, Yogesh Prabhu, Bryan Zhang
- Date / location: Feb 1, 2026 / San Diego
- Page: https://apartresearch.com/sprints/projects/audit-7hmj
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/a1745fe8471f31a0-e338c913-2398-411f-8282-fe7ba58704d0-AUDIT.pdf
- Code: https://github.com/zhangkevin747/AUDIT
- Code links found in report: https://github.com/zhangkevin747/AUDIT

## Summary

A framework for detecting malicious open-source AI models by analyzing both their internal weights for tampering and their behavioral outputs for safety violations at the scale of platforms like Hugging Face.

## Reviews (2)

### Review 1

Like the angle! Hf model security is likely going to be a huge problem. Thought the cheap static check into expensive dynamic check was a good touch to make it actually scalable. It would be great to see more models and a bit more details on the method but for a hackathon sprint its a nice proof-of-concept!

### Review 2

Interesting and clear paper! A few comments:

- Could have tested with more than 5 models and assess the effectiveness of the pipeline on varying degrees of modification (e.g. benign fine-tunes that make large weight changes)
- Talk more in-depth about which phase of the classifier does the work (thresholds heuristics? the random forest? something else?). This seems to be the core of the contribution here and we don’t learn much about it
- Confidence scores could be improved; 52-68% seems little and would currently lead to many false positives or negatives.

