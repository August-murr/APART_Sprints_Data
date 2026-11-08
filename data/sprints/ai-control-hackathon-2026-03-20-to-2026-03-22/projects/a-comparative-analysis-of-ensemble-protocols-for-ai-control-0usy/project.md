# A Comparative Analysis of Ensemble Protocols for AI Control

- Sprint: AI Control Hackathon 2026 (ai-control-hackathon-2026-03-20-to-2026-03-22)
- Rank: unranked
- Selected as: sample_reviewed
- Team: Team Heron Blue Team
- Authors: Ariel Monzon, Natan Katz, Inbar Shulman, Mike Vazan, Or Shemesh, Guy Porat
- Date / location: Mar 23, 2026 / Israel
- Page: https://apartresearch.com/sprints/projects/a-comparative-analysis-of-ensemble-protocols-for-ai-control-0usy
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/b55c43c63ce3f273-071-1ac8c1ff0060-A-Comparative-Analysis-of-Ensemble-Protocols-for-AI-Control.pdf
- Code: https://github.com/0rShemesh/control-arena
- Code links found in report: https://github.com/0rShemesh/control-arena_, https://github.com/UKGovernmentBEIS/control-arena

## Summary

We empirically evaluate ensembles of AI control protocols and show that performance depends on signal diversity rather than the number of tools: small, diverse ensembles outperform larger, redundant ones. Correlation between tools limits gains from stacking, while consensus-based aggregation improves robustness, providing a principled basis for ensemble design.

## Reviews (2)

### Review 1

Congrats on a very thorough project! Mapping ensemble interactions across 100+ tool combinations is ambitious for a hackathon weekend. The report is really clear and well presented.

Impact & Innovation: The research question, although not groundbreaking, is interesting and pulling it off successfully would provide safety gains. The two novel detection mechanisms are well-motivated. As you flagged, the non-adaptive adversary does bound how directly these ensembles transfer to deployment, though a full red team exploration is understandably beyond hackathon scope.

Execution Quality: The experimental design is impressively thorough. Two gaps worth noting:

- The comparison between ensembles and individual tools isn't compute-matched. A 3-tool ensemble gets three inference passes per sample while a single protocol gets one. Therefore, it's unclear whether the gains come from complementary signals or simply from more compute. The right control would be to run each individual protocol multiple times and aggregate those results, then compare against a tool ensemble at equal compute budget. Without this, the central claim about diversity vs. quantity is confounded.
- There are no confidence intervals in the results or error bars in the figures. Adding them would help calibrate the relevance of the results.

Presentation & Clarity: The paper is well-written and concise with a clear narrative arc. Figures are well-chosen and informative. Minor notes: some figure captions carry substantial analytical claims that would read better in the main text.

### Review 2

Strong empirical contribution! Really enjoyed reading through the project.

Exhaustively evaluating all tool combinations across multiple aggregation methods is thorough and well-designed. The central finding (mechanism diversity matters more than tool count, and the best small ensemble outperforms the full ensemble) is counterintuitive and immediately actionable. The two novel detection mechanisms are both clever. ACP exploiting backdoor brittleness for semantically preserving perturbations is a particularly nice insight.

