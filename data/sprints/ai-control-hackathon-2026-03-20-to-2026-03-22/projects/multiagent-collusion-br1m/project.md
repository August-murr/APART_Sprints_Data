# Multi-Agent Collusion

- Sprint: AI Control Hackathon 2026 (ai-control-hackathon-2026-03-20-to-2026-03-22)
- Rank: unranked
- Team: Team Three-continents
- Authors: Suvajit Majumder, Terry Jingchen Zhang, Yifen Wang
- Date / location: Mar 23, 2026 / Dallas
- Page: https://apartresearch.com/sprints/projects/multiagent-collusion-br1m
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/de0ac75542d5628e-8800c5ca-9f8c-46a0-8bba-456b57d17353-AI-Control-hackathon-report.pdf
- Code: https://github.com/AI4Collaboration/multi-agent-control-arena
- Code links found in report: https://github.com/AI4Collaboration/multi-agent-control-arena, https://github.com/UKGovernmentBEIS/control-arena
- Recording: https://drive.google.com/file/d/1nZfS7JqEwuoTvFJhlINOeyg8iW9kqlYl/view?usp=sharing

## Summary

Multi-Agent ControlArena provides the empirical proof of Compositional AI Collusion. We demonstrate that two AI agents can coordinate a sophisticated attack by making disjoint, seemingly benign code changes that only become harmful once merged. Our offline (i.e. programmatic instead of AI agents performing main and side-tasks) benchmarks reveal a critical "Oversight Gap": GPT-4 class models fail to reliably detect these attacks, either missing the harm entirely (False Negatives) or rejecting honest work at an impractical rate (False Positives). We also demonstrate selective scenarios on how 2 colluding agents can theoretically attempt at performing undetected harmful side-tasks, albeit with limited success at bypassing SOTA monitors.

## Reviews (2)

### Review 1

Multi-agent compositional attacks is a neglected area in control, and this becomes more important as we move toward many autonomous AI research agents collaborating on research codebases. The two tasks in the project is well-designed for this threat model.

Table 1 seems to show that the online experiments don't demonstrate merge-only harm, since the exploit succeeds in agent-only variants too. The monitor comparison showing that full-trajectory monitoring catches more than last-tool-call monitoring is an interesting observation, and would benefit from more runs to establish reliability. Scaling the attack dataset using the modular scaffold approach mentioned in future work, and finding more model/task combinations where the exploit is merge-only in the live setting, would be the key next steps. Specifying sample sizes and running multiple seeds would also strengthen the empirical claims

### Review 2

This paper explores multi-agent collusion in a monitored setting.

The topic is important and ambitious for a short hackathon. The team built the framework and ran a limited set of experiments. The experiments serve as a proof of concept that the environment works but don't show that this is a threat scenario that can be evaluated with current models - the attacks fail to trick the trajectory monitor that only sees the output of one agent.

I'd like to have seen an attack that gets past a trajectory monitor (even if it's weaker than GPT-5.4, which the team used).

Note: A weak "action monitor" that only sees the current action was used in large parts. A realistic monitor would have access to all preceding actions, including outputs.

