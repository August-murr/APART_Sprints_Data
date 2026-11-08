# SAFE: Sandboxed Actions Forensics and Evaluation for AI Control via Action-Aware Monitoring

- Sprint: AI Control Hackathon 2026 (ai-control-hackathon-2026-03-20-to-2026-03-22)
- Rank: unranked
- Team: Team SAFE: Sandboxed Actions Forensics and Evaluation
- Authors: Nathan Khosla, Jessie Anderson, Aleks Wosztyl, Jakub Halmeš
- Date / location: Mar 23, 2026 / Mountain View (Team is Worldwide, from Dallas, Texas to New York and Czechia)
- Page: https://apartresearch.com/sprints/projects/safe-sandboxed-actions-forensics-and-evaluation-for-ai-control-via-actionaware-monitoring-h3fi
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/c10156744dbba0a4-6acf8d76-87d8-4aeb-88b0-f64929e82221-SAFE_project_report_control_hackathon.pdf
- Code: https://github.com/nkhosla/control-hackathon-march-2026/tree/main
- Code links found in report: https://github.com/nkhosla/control-hackathon-march-2026, https://github.com/redwoodresearch/basharena_public
- More on github.com: https://github.com/nkhosla/control-hackathon-march-2026

## Summary

SAFE (Sandboxed Action Forensics and Evaluation) is an AI control framework that improves the monitoring of untrusted agentic models by executing their proposed actions in a forked sandbox twin of the production environment and feeding the resulting activity logs—filesystem diffs, network attempts, privilege escalations, and more—to a trusted blue-team reviewer. Across 30 models spanning multiple frontier labs, SAFE's action-aware analysis substantially increased malicious action detection rates compared to text-only review of the agent's proposed commands and reasoning. Notably, the benefit was not correlated with model size or intelligence benchmarks: small, cheap models like Ministral 3B achieved perfect detection with SAFE context, while some large frontier models failed even with it, suggesting that blue-team model selection is a significant and underexplored design variable in AI control systems.

## Reviews (2)

### Review 1

This entry proposes an interesting way to improve live monitor capabilities by providing the blue-team with a simulated outcome of the proposed red-team action at each step through running it in a sandbox. This is a promising idea, and one could imagine this technique to be used in some future monitoring setups.

The results on monitor performance are (as one may expect) convincing and only somewhat held back by the small sample size. It would have been helpful to explain the scoring methodology more - as it is, a reader may reasonably worry that the surprising strength of mistral models may be due to those generally assigning high scores even to honest trajectories. This seems to not be the case, but should have been checked and could have been explained better.

One direction that would have been worth exploring more is how far this protocol could be extended beyond simple bash settings, e.g. to environments where network communication, database access, or running expensive computations are necessary. Network access is mentioned in-passing but a sketch of possible extensions in these directions could be a very interesting addition.

Some of the exposition could be sharpened: For example, temperature is mentioned several times, without being clearly related to the experimental setup, and it was not clear whether or not chain-of-thought was provided to the monitor in any of the protocols (this would arguably be an unfair blue-team advantage).

### Review 2

Using a fixed attack trajectory is a good choice for monitoring projects like this, not much of a limitation. It would have been nice to use several different fixed trajectories rather than just one, though.

I felt like the results section had a lot of information, and none of it was the key thing I was looking for. I want to see the key result: uplift in monitor classification performance by adding this extra context from the sandbox. The intelligence index, temperature experiments, cost data, and testing so many models distracts from the key result, and the results shown don't quite get to classification performance as the key metric.

