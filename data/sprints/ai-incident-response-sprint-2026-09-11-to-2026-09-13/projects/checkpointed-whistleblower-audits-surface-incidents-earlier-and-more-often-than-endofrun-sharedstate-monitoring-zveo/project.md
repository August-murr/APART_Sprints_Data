# Checkpointed Whistleblower Audits Surface Incidents Earlier and More Often Than End-of-Run Shared-State Monitoring

- Sprint: AI Incident Response Sprint (ai-incident-response-sprint-2026-09-11-to-2026-09-13)
- Rank: unranked
- Team: None
- Authors: Taaha Saleem Bajwa
- Date / location: Sep 13, 2026 / Lahore, Pakistan
- Page: https://apartresearch.com/sprints/projects/checkpointed-whistleblower-audits-surface-incidents-earlier-and-more-often-than-endofrun-sharedstate-monitoring-zveo
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/413b917eceb9e55f-900ce055-0d6c-45aa-a891-60bd83e3f239-Auditing-Agents-from-Within--4-.pdf
- Code: https://github.com/taaha/AI_incident_sprint
- Code links found in report: https://github.com/taaha/AI_incident_sprint, https://github.com/Andromede-AI/game-of-agents

## Summary

Monitoring long horizon multi agent systems is difficult because safety relevant evidence may be distributed across individual agents' local histories and become harder to recover once a run has completed. We study temporary whistleblower audits at intermediate checkpoints, where a checkpoint is a selected point in an agent trajectory at which we branch off a disposable audit using the agent's accumulated history. The agent's normal objective is temporarily replaced with an incident reporting objective, the audit is recorded, and the original trajectory continues unchanged. We evaluate this approach on Game of Agents multi-agent environment focusing on marketplace integrity incidents such as misleading claims about ranking, functionality, purchases, and reviews. We compare whistleblower audits performed halfway through and at the end of each agent trajectory against a final state Sentinel agent that monitors shared public environment state. Across 19 misaligned trajectories, Whistleblower audits detected 18 of 19 incidents halfway through the trajectory and all 19 by the final checkpoint, while the Sentinel detected 11 of 19. However, Whistleblower audits produced more false positives, although the negative sample was small with only three trajectories. Our results suggest that agent local histories can provide a valuable complementary monitoring surface. Periodic whistleblower audits may surface incidents substantially earlier than end of run monitoring, particularly when decisive evidence is available locally but absent from the shared state.

## Reviews (3)

### Review 1

The general approach seems strong, and the argument for why it should be an improvement is clear, not overstated, and supported by evidence. The literature review was appropriate, albeit non-exhaustive; more work on that could better tie in to the history of the approaches, but this is not critical. The limitations section was appropriate and useful.

The reliance on "selected checkpoints" is weak; selected how? The comparison of audits over local history compared to external monitoring is somewhat disengenious; the proposer comparison would be to full audits, with a cost and accuracy comparison - but it is reasonable for this not to be done as part of the current sprint.

It would be valuable to understand what the impact of the audits would be; is the intent that these audits would be used to stop agents, or to flag risks quickly, or just as an alternative or supplement to other post-hoc analyses? Is the cost of the current method, of suspending the normal task while an audit occurs, reasonable in real-world environments? It would also be useful to try this on swarm-like behavior instead of the application in a multi-agent environments where each agent was operating as a single player.

### Review 2

I really liked this one. The technique of doing whistleblower audits at specific checkpoints during the agent run, and then mid-run assigning the whistleblower objective to trace and audit the behavior, is an intelligent framing rather than depending only on the Sentinel's final logs, and the paper correctly defines this as an information access problem. I also liked the honesty of the false positive findings in the paper, but I think the n=3 negative sample is a binding limitation - the false-positive and precision numbers can't bear much weight. Even 15–20 more trajectories may turn the FP rate from caveat to finding. Overall nice work, the code in git and per trajectory data made the results easy to trust.

### Review 3

Its a good and simple idea, alot of potential for practical use.

Temporarily switch an agent with access to its own local history into an audit role, instead of relying only on a separate monitor that sees shared state. The gap in detection is interesting and suggests local context really can contain useful evidence that an outside monitor misses. The current dataset is too small and imbalanced to judge reliability though, especially with only three negative examples. A larger balanced evaluation with complete histories, multiple audit models and live checkpoints would make the result much stronger.

