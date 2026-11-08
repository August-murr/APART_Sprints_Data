# Goodhart's Village: Using LLM-Mafia to Study Deception

- Sprint: AI Manipulation Hackathon (ai-manipulation-hackathon-2026-01-09-to-2026-01-11)
- Rank: unranked
- Team: Team Sabina and James
- Authors: James Sykes, Sabina Gulcikova
- Date / location: Jan 12, 2026 / United Kingdom
- Page: https://apartresearch.com/sprints/projects/goodharts-village-using-llmmafia-to-study-deception-9jo6
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/8bf05a6a8a76f13d-c6d644f3fe2-Report-for-Apart-Research-Sprint---AI-Manipulation--Jan-2026--2-.pdf
- Code: https://github.com/sabgul/LLMs-playing-mafia-hackathon

## Summary

The social deduction game Mafia centres on reasoning under information asymmetry, where an informed minority must mislead an uninformed majority, making it a useful setting for studying deception in large language models (LLMs). Although LLMs have seen rapid progress in areas such as reasoning and language understanding, their ability to engage in social reasoning under uncertainty remains poorly understood. In this work, we study deceptive behaviour in a six-player implementation of the full Mafia game, extending prior work based on a simplified variant. By varying behavioural instructions from strict honesty to a “win at all costs” objective, we examine how explicit prompting interacts with the structural demands of adversarial roles. Comparing agents’ private reasoning with their public statements, we find that Mafia agents display consistently high levels of deception even when instructed not to lie, while cooperative roles adapt their behaviour more flexibly in response to perceived threat. Overall, the results suggest that role structure and game incentives dominate behavioural prompting, supporting Mafia as a useful benchmark for analysing deception and social reasoning in LLMs.

## Reviews (1)

### Review 1

This is a fascinating investigation into Goodhart’s Law. The 4x4 Behavioral Matrix is a brilliant way to operationalize the tension between safety prompts and game incentives, and the 'Deception Floor' finding effectively highlights how brittle current alignment techniques can be in adversarial settings. I would love to see this implemented on a larger sample size to confirm that the heatmaps represent a genuine trend rather than game noise. Moving forward, employing a stronger model as the judge would also strengthen the results by minimizing potential self-evaluation bias. The serendipitous finding about agents hallucinating meaning from API 503 errors was a great catch - definitely a failure mode worth formalizing!

Great work overall.

