# SafetyGap: Coordination Infrastructure, Auditing and Tools for Multilingual AI Safety

- Sprint: The Technical AI Governance Challenge (the-technical-ai-governance-challenge-2026-01-30-to-2026-02-01)
- Rank: unranked
- Selected as: sample_reviewed
- Team: Team SafetyGap
- Authors: Alyssia J, Martin CL
- Date / location: Feb 2, 2026 / Canada
- Page: https://apartresearch.com/sprints/projects/safetygap-coordination-infrastructure-auditing-and-tools-for-multilingual-ai-safety-1yx1
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/ba1157438b71323c---Coordination-Infrastructure--Auditing-and-Tools-for-Multilingual-AI-Safety.pdf
- Code: https://github.com/marn-in-prod/apart-multi
- Code links found in report: https://github.com/marn-in-prod/apart-multi

## Summary

The EU AI Act requires evaluation of general-purpose AI models, yet compliant evaluation for bias detection is currently impossible in 19 of 24 official EU languages. The International Network of AI Safety Institutes needs shared visibility into what evaluation infrastructure exists to coordinate effectively. We audited multilingual coverage for 15 major safety benchmarks, verifying claims against primary sources (papers, GitHub repositories, HuggingFace) and cataloging language availability across 7 risk categories. We found a stark divide: truthfulness and toxicity benchmarks extend to 17--21 languages, but bias detection, adversarial robustness, and over-refusal benchmarks remain almost entirely English-only. Models serving over 6 billion non-English speakers have never been tested for these risks in local languages. We release SafetyGap, a public database and dashboard covering all languages in our audit. The open-source infrastructure is available to all members of the International Network—the US, UK, Japan, Singapore, Canada, France, Kenya, South Korea, and the EU among them—to check coverage before commissioning translations and coordinate on filling gaps. It is built to be easily extendable.

## Reviews (2)

### Review 1

Execution is fine, but the selected problem is relatively unimportant.

### Review 2

Awesome project! Could be directly useful immediately. As it is now, impact caps out at a time-saving tool for AISIs. Could be interesting to take the theory of change a step further and think about what risks you're trying to mitigate. I think "AI systems that are actually safe for everyone, not just English speakers" is not quite the right framing here. I think the stakes are even higher: If AI safeguards are not robust in every language, then they are not robust, creating dangers for everyone, (including English speakers!).

So beyond helping international AISI's and users keep up, this work has implications for frontier safety efforts. Thinking of it this way might prompt a slightly different theory of change, which may in turn change the project slightly. For example, it may not be a good idea to make this information public, since it could empower users who don't speak that language to now bypass model safeguards.

