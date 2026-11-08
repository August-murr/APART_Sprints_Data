# Self-Report Under Audit: Testing a Persistent Agent's Introspective Claims Against a Hash-Chained Ground-Truth Record

- Sprint: Digital Minds Research Sprint (digital-minds-research-sprint-2026-08-14-to-2026-08-16)
- Rank: unranked
- Selected as: sample_reviewed
- Team: Team Wave Squad
- Authors: Jason Gibbs
- Date / location: Aug 17, 2026 / Dallas, TX
- Page: https://apartresearch.com/sprints/projects/selfreport-under-audit-testing-a-persistent-agents-introspective-claims-against-a-hashchained-groundtruth-record-svac
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/e2e6ffba0c65438c-a9218ce7-7bec-40f3-9328-961401fd5700-Self-Report-Under-Audit.pdf
- Code: None

## Summary

First real-world, tamper-evident audit of a deployed agent’s self-reports. Over 23 days Cadence made 62 explicit self-corrections (2.7/day). In a pre-registered test it predicted which of its own memories were load-bearing and scored only 6/16 — no better than chance and matched by a zero-introspection baseline. This shows agent self-reports can be measured in deployment without model access, and currently aren’t very reliable.

## Reviews (1)

### Review 1

This is a distinctive and very well-presented contribution that extends self-report research from controlled elicitation to longitudinal content accuracy in a deployed persistent agent. I particularly appreciated the hash-committed preregistration, mechanically defined ablation ground truth, calibration analysis, external-observer baseline, explicit correction of the paper's own failed claims, and unusually strong reproducibility discipline.

The most important improvement would be to sharpen the base-rate interpretation. The reported 62 explicit corrections over 23 days is an observed correction frequency rather than a self-report error rate unless the denominator of mechanically auditable claims is known. Future versions should report errors per auditable claim/opportunity, ideally broken down by verifier and claim type, and distinguish detected error frequency from an estimate of total underlying error.

The introspection result is interesting but currently small and system-specific. The 16 memory nodes should be expanded using independently defined or randomized sampling, and the "load-bearing" criterion should be tested across multiple retrieval/behavioral measures. I would also strengthen the privileged-access control: matching a graph-degree heuristic shows no advantage over that observable proxy, but a richer external predictor or another agent with access only to public artifacts would make the comparison more compelling.

Replication across multiple persistent agents and model families would be especially valuable. If the same audit apparatus reveals stable classes of stale-belief, double-counting, proxy-substitution, and over-concession errors across systems, this could become a useful operational methodology for both AI safety and welfare research.

Overall, I see this as a strong methodological paper with a genuinely valuable direction: deployed-agent self-reports should be treated as auditable claims rather than inherently privileged evidence.

