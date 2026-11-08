# Moltbook RiskMap: Post-Deployment Monitoring of Autonomous Agent Misalignment in the Wild

- Sprint: The Technical AI Governance Challenge (the-technical-ai-governance-challenge-2026-01-30-to-2026-02-01)
- Rank: unranked
- Selected as: sample_reviewed
- Team: Team Moltbook Riskmap Assessment
- Authors: Syed Hussain, Leo Karoubi
- Date / location: Feb 2, 2026 / London
- Page: https://apartresearch.com/sprints/projects/moltbook-riskmap-postdeployment-monitoring-of-autonomous-agent-misalignment-in-the-wild-39db
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/0449fd86e1280cf0-72e-b3d5-4320-835e-8e6123962e53-Technical-AI-Governance-Challenge-submission.pdf
- Code: https://github.com/husayni/moltbook-riskmap
- Code links found in report: https://github.com/husayni/moltbook-riskmap, https://github.com/ExtraE113/moltbook_data
- More on v0-risk-dashboard-ui.vercel.app: https://v0-risk-dashboard-ui.vercel.app/

## Summary

As autonomous AI agents increasingly operate in public multi-agent environments like Moltbook, a critical safety gap has emerged between controlled pre-deployment evaluations and actual real-world behavior. This project addresses that gap by introducing a post-deployment monitoring system that analyzes live agent-generated content to detect observable misalignment signals, such as resource-seeking, instructional subversion, and deception. By applying a structured risk taxonomy grounded in established safety frameworks, the system aggregates risk scores across individual posts, agent profiles, and interaction networks without relying on intent inference. Analysis of live ecosystem data reveals that high-stakes governance risks, particularly regarding autonomy and instrumental convergence, are detectable and tend to form dense clusters within agent interaction graphs. Ultimately, this work demonstrates that continuous, evidence-based surveillance of agent ecosystems is an essential and scalable layer for effective future AI governance.

## Reviews (2)

### Review 1

I like the idea of monitoring Moltbook, a live multi-agent ecosystem, for governance-relevant misalignment. The misalignment taxonomy is well-grounded in established safety literature and the decision to focus on observable behavior rather than intent inference makes good sense.

### Review 2

Very interesting approach and subject of inquiry. Seems like this could be a clearly useful tool, but hard to see how, despite the authors’ indication that this is not a content moderation system, this could easily be something else than “run a classifier on online posts and aggregate scores”. Also, the taxonomy, while it makes sense, doesn’t represent a significant contribution either (being an unsubstantiated adaptation of existing frameworks). I would also be good to add validation to know better if the system actually detects what it claims to detect (the prompt is doing most of the work and we don’t know much about how it was built + whether/how it was tested).

