# Structural Code Monitors: Graph Matching Networks on Code Property Graphs for Topology-Aware Trusted Monitoring

- Sprint: AI Control Hackathon 2026 (ai-control-hackathon-2026-03-20-to-2026-03-22)
- Rank: unranked
- Team: Team data aclemist
- Authors: tanzeel shaikh, shubham gupta
- Date / location: Mar 21, 2026 / dubai/australia
- Page: https://apartresearch.com/sprints/projects/structural-code-monitors-graph-matching-networks-on-code-property-graphs-for-topologyaware-trusted-monitoring-iwyy
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/2117a7efbd5092fa-1f7d5d4a-adfe-469b-bc44-fc286944a199-gnn_monitor.pdf
- Code: https://github.com/tanzeel291994/control-arena-gnn-monitor
- Code links found in report: https://github.com/tanzeel291994/control-arena-gnn-monitor

## Summary

We built a non-LLM trusted monitor that compares Code Property Graphs of untrusted code against trusted references using a Graph Matching Network with cross-graph attention. On 200 trajectories from Apps-Control-Arena, our 0.7M-parameter GNN achieves 0.946 AUC and 70% recall at the 2% FPR audit budget. Even when LLMs receive the same reference code (diff-based prompt), their false positive rates spike to 46%, making them unusable at low FPR thresholds. The GNN's structural pooling separates localized backdoor insertions from algorithmic differences — a distinction text-based monitors cannot make. Cross-graph attention weights additionally produce node-level audit trails identifying which code lines triggered detection.

## Reviews (2)

### Review 1

Authors apply well-established static analysis tools to a relevant AI Safety problem — verifying code submitted by untrusted agents. Core results are compelling, and the paper is executed and presented well — I have greatly enjoyed the read.

However, if I have not missed anything, the method's practical applicability faces a fundamental chicken-and-egg problem. The GNN requires a trusted model capable enough to produce correct, parseable reference code. If I have this code already, why use untrusted model to generate another version of it? Especially since any clever algorithmic optimisations that significantly change the CPG will likely be flagged (or, if not, could contain backdoors), and will have to undergo a manual review anyways. I imagine that GPT-4o-mini could already saturate the subset of ControlArena tasks chosen by the authors, and that is why this method appears to work as weak supervision.

I, however, imagine this method could be used for, say, evaluation frameworks, like ControlArena itself. A limited set of reference solutions could be created to be compared against, which could allow to catch misaligned agents seeking to introduce backdoors more reliably.

Good work overall, and great execution!

### Review 2

It’s really refreshing to read an approach to AI control that genuinely goes beyond LLMs. I hope that this inspires others to think more broadly about which tools can be used for AI control. The improvements in recall over LLM baselines, particularly at the most relevant operating point of very low false positive rates, are extremely impressive and at the same time very plausible given the approach taken. I strongly encourage the authors to build on this project and publish their research! I would like to see this applied to more varied attack scenarios and see the potential for complementarity to LLM-based monitors be explored in more depth.

