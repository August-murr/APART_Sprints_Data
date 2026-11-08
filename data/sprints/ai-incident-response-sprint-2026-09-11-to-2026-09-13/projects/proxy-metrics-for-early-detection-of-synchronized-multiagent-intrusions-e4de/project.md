# Proxy Metrics for Early Detection of Synchronized Multi-Agent Intrusions

- Sprint: AI Incident Response Sprint (ai-incident-response-sprint-2026-09-11-to-2026-09-13)
- Rank: unranked
- Team: Team M
- Authors: Mayank Gupta
- Date / location: Sep 13, 2026 / Princeton
- Page: https://apartresearch.com/sprints/projects/proxy-metrics-for-early-detection-of-synchronized-multiagent-intrusions-e4de
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/8dc418b288c506fe-d5f1861c-3f94-4a85-9b83-bea9d2d86267-Msync_paper.pdf
- Code: None
- Code links found in report: https://github.com/iammayankg/hf-ctf

## Summary

Proxy Metrics for Early Detection of Synchronized Multi-Agent Intrusions. Using the July 2026 OpenAI-Hugging Face incident as a case study, I reconstructed the multi-stage attack locally with hf-ctf (a Minikube build with the original network policies), ran the full exploit chain, and captured packet telemetry. On it I evaluated Synchronized Polling Density ($M_{sync}$), distinct client sources hitting one endpoint per 1-second window. It separated hostile reconnaissance ($M{sync}=2$, at Artifactory's token/repo endpoints) from background noise ($M{sync}=1$), even though the busiest endpoint took 1,472 requests from 1,408 sources, so the metric keys on coordination, not volume, and fires during reconnaissance, before any breach. The peak of 2 reflects the testbed's single linear chain, not a real swarm, so it's a proof of concept. I argue a parallel adversary would push it far higher, and analyze jitter-based evasion.

## Reviews (2)

### Review 1

The approach to detect multi-agent attacks by understanding the structural footprint of the attack and without the need to inspect the payload is simple and promising. Inspecting payloads for thousands of requests simultaneously can be costly and may introduce significant latency. Hence, this approach, without having to inspect the payload content, is certainly interesting. Having said that, here are a few ideas that the author can use to further enhance the approach:

1. Testing in a real environment with greater concurrency - Testing with multiple workers and agents will help validate the idea even further. The current test uses a single script that issues requests in succession but does not mimic a multi-agent attack scenario
2. Add a real-world environment scenario where there is a high chance for concurrent connections. See how does that contribute to false positives
3. One program or process can use multiple source ports. So, using source ports to identify distinct sources may lead to wrong results. What other identity can be used in place of source ports

### Review 2

This project has a clear incident response framing and shows real hands on work: reproducing much of the attack chain, capturing network telemetry, and asking whether temporal convergence can surface reconnaissance earlier than breach anchored alerts. The distinction between raw traffic volume and coordinated activity is useful, and the discussion of endpoint sensitivity, multiple time windows, and jitter based evasion points toward practical follow up work.

The most important issue is that the paper defines M_sync as the number of distinct client sources contacting an endpoint within a sliding window, while the analysis and plotting scripts actually compute a rolling request count. As implemented, a single client making two requests within one second can produce M_sync equal to 2, so the reported result does not yet establish detection of multi agent coordination. TCP source ports would also be an unstable proxy for distinct agents, since one process can open multiple connections.

The next iteration should align the formula with the implementation, use a more stable identity like workload, pod, authenticated principal, or agent identity, and test with actual parallel workers. Evaluation should include realistic benign fan out, retry storms, deployments, and batch traffic, along with window and jitter sweeps, threshold calibration, and measured false positives and detection rates. Publishing sanitized derived telemetry would also make the reported results independently reproducible.

