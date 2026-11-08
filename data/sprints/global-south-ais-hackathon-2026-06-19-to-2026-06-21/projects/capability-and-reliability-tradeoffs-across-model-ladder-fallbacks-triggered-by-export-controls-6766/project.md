# Capability and Reliability Trade-offs Across Model Ladder Fallbacks Triggered by Export Controls

- Sprint: Global South AI Safety Hackathon (global-south-ais-hackathon-2026-06-19-to-2026-06-21)
- Rank: unranked
- Team: Team SouthSideSafety
- Authors: Kshaunish Harsha, Aranck Jomraj, Anushree Bobade
- Date / location: Jun 22, 2026 / Mumbai
- Page: https://apartresearch.com/sprints/projects/capability-and-reliability-tradeoffs-across-model-ladder-fallbacks-triggered-by-export-controls-6766
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/b322267249ee7bce-bility-Trade-offs-Across-Model-Ladder-Fallbacks-Triggered-by-Export-Controls.pdf
- Code: https://github.com/KshaunishHarsha/frontier-fallback-safety-audit
- Code links found in report: https://github.com/KshaunishHarsha/frontier-fallback-safety-audit

## Summary

On 12 June 2026, the US suspended Claude Fable 5 access for foreign nationals, forcing users across India and Southeast Asia onto smaller open-weight fallbacks. We tested whether this substitution trades one safety problem for another — reducing catastrophic-misuse risk while quietly worsening everyday reliability (sycophancy, overconfidence, overcompliance). Running 225 evaluated outputs across a three-model ladder (70B → 32B → 8B), we found the "reliability scissor" did not appear: reliability scores clustered within 5 points across all tiers. But two findings stood out — sycophancy flip rates converged at ~40–43% regardless of model size (meaning model selection cannot fix it), and defamatory content generation and legally ungrounded professional documents were produced by every model in the ladder. These are the unmeasured safety costs of an export control designed without input from the regions that absorbed its consequences.

## Reviews (4)

### Review 1

This is a creative and well framed project. The reliability scissor lens and your descipline in pre-registering all ground truth before calling any model are real strengths. A rerun with larger samples and additional significance testing would significantly strengthen the confidence in the results. Overall a clear and well written contribution!

### Review 2

I liked the core idea of the project. A model can be risky because it has dangerous high end capabilities, but it can also be risky because it is unreliable in ordinary legal, medical, financial, or compliance workflows.

That said, the paper should be careful not to imply that these reliability issues outweigh the catastrophic misuse concerns that motivated the export control. The study does not measure the original catastrophic risk, so it can't show that the policy was net harmful. It mainly shows that downstream reliability costs may be under-measured.

The substitution story also needs more justification. If one frontier model is restricted, many users may move to other closed frontier models rather than to smaller open models. The paper would be stronger if it explained why users in the Global South would actually end up using these fallback models.

The empirical work is a useful first pass, but still preliminary. The model set is small, the prompt batteries are small, the sycophancy sample sizes differ across models, and one of the main capability results seems affected by a parsing issue. These limitations make the broad policy claims weaker.

A useful next step would be to test scaffolded agentic systems. In real workflows, people may use retrieval, citation checks, validators, refusal rules, local legal/medical context, audit logs, or human review. Testing whether those scaffolds reduce the observed failures would make the work much more policy-relevant.

Overall, I think this is a good and clearly presented hackathon project. Its main contribution is not proving that export controls are bad, but showing that export-control policy should measure everyday reliability costs alongside catastrophic misuse concerns.

### Review 3

The framing and hypotheses are quite clear and useful.

To improve:

1. Report confidence intervals for every rate. The current headline about sycophancy is based on small samples - and with samples that small, "robust convergence” is not yet supported.
2. Commit the raw and scored outputs. Without them, the headline numbers cannot be reproduced from the repo.
3. Clarify the model tiering. All three models are open-weight, so the frontier closed tier is only a proxy and cannot directly support claims about fallback cost.

### Review 4

Cool tradeoff description! One thing to flag is that your reliability axis cannot move much because 'overconfidence' was a perfect score for every model, so it drags all the averages together, and your headline number for "40% flip" is from low sample size data. Since the data can't really test the scissor, I'd suggest focusing on the finding that every model happily wrote fake defamatory articles and bogus contracts.

