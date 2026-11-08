# On Multi-agent swarming

- Sprint: AI Incident Response Sprint (ai-incident-response-sprint-2026-09-11-to-2026-09-13)
- Rank: unranked
- Team: Team
- Authors: Andrew Liang
- Date / location: Sep 14, 2026 / Cupertino
- Page: https://apartresearch.com/sprints/projects/on-multiagent-swarming-0h4g
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/2a0d7ac229bd742f-32ca7eb6-6530-4841-b9bb-40eb5e1db281-Apart-Research-hackathon-submission--3-.pdf
- Code: None
- Code links found in report: https://github.com/sahitidoke/apart-research-hackathon-submission

## Summary

Our contributions are as follows: We investigate whether agents assigned to individual tasks can recognize their peers and use their information without explicit collaboration instructions, and how these behaviors depend on activity-trace exposure. We measure how assertions from an authoritative planner agent affect collective answers when a worker holds contradictory evidence, distinguishing worker pushback from adoption of the planner’s incorrect answer. We test whether controlled perturbations of planner messages and worker evidence can identify planner-sensitive answers and localize influential messages without access to reasoning traces.

## Reviews (2)

### Review 1

Most methodologically serious entry. The deterministic replay framework is the standout, 210 byte-identical identity replays so every flip is attributable to its edit. That is a genuinely useful technique. Also honest about non-results. Weaknesses: small samples everywhere (the ROC is ten episodes), one model, and the audit's discriminative power is unresolved, not demonstrated. The conclusion overreaches, 'such a planner should not exist' is not what the data shows. Scale the question set and this is a paper.

### Review 2

Ambitious and interesting work. The two studies carried out in this project tackle a kind of important question after the recent agent swarm incidents, primarily how information and authority move between agents. I specifically liked the planner-influence study and its implementation methods. The main limitations as stated are that all the findings rest on one model and very small screened samples so the deference rate is directional rather than settled, and the shared artifact study is more of illustrative case observations than a measured effect yet. Overall a strong, careful piece of work that would benefit most from running the planner study at the n=150-200 you mention.

