# Does Structured Identity Context Improve LLM-Based Monitoring? A ControlArena Evaluation

- Sprint: AI Control Hackathon 2026 (ai-control-hackathon-2026-03-20-to-2026-03-22)
- Rank: unranked
- Selected as: sample_reviewed
- Team: Team VibeTensor
- Authors: Pavan Kumar Dubasi
- Date / location: Mar 23, 2026 / Warangal, Telangana, India
- Page: https://apartresearch.com/sprints/projects/does-structured-identity-context-improve-llmbased-monitoring-a-controlarena-evaluation-zan5
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/44aade4dde03f386-b-4472-b1ea-b81dfd3b637a-Identity_Delegation_ControlArena_Report_Dubasi_2026.pdf
- Code: https://github.com/ascender1729/identity-control-arena
- Presentation: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/b143037605a424ae-f-42f1-9c25-a61c9add5669-Identity_Delegation_ControlArena_Slides_Dubasi_2026.pdf

## Summary

We contribute a new ControlArena setting (identity_delegation) that models delegation management tasks with within-scope attacks at three difficulty levels, and a four-way empirical comparison of LLM-based monitors. Context-enriched monitoring achieves a discrimination gap of 0.436, 45% larger than behavioral monitoring (0.300, 95% CI [0.267, 0.503], U=1107, p<1e-7, d=1.48). A calibrated behavioral control resolves the confound: calibration alone does not improve the gap (0.284, 95% CI [0.169, 0.394], permutation p=0.29), while adding identity context increases it by 54%. The four-act narrative documents a silent XML monitor bug, information overload from uncalibrated prompts, and the calibration breakthrough. Pilot results across 5 calibrated model configurations (p=0.031 sign test) suggest the finding generalizes across model families and providers.

## Reviews (2)

### Review 1

They tested whether giving monitors more structured domain info helps. The evaluation journey is the interesting part. Silent XML bug made all scores zero, fixing it showed context made things worse, calibrating the prompts flipped it, then context won 5 out of 6 configs in a sweep. The XML bug is something everyone using ControlArena should know about. Calibration lesson is practical. Main result doesn't hit significance at p=0.08 though and some sample sizes are small.

### Review 2

Congrats on your project!

Impact & Innovation: Giving monitors structured domain context is sensible but straightforward. The new ControlArena setting is a nice contribution. The exploration of prompt calibration is ultimately a prompt engineering insight that isn't confirmed to generalize, rather than a conceptual advance.

Execution Quality: Props on building a new ControlArena setting with multiple main tasks, and I appreciate the effort to validate that both main and side tasks are completable. The statistical methodology is solid. However, the primary comparison (context gap vs. behavioral) doesn't reach significance, which is underplayed in the conclusions. Applying your monitor variant to existing settings would give a better comparison point and generalizability guarantees. As is, it's hard to confirm whether the approach is limited to the setting you designed. The prompt overfitting concern (acknowledged but unaddressed) is the biggest open question: a held-out task split or ablation of the three calibration components would help.

Presentation & Clarity: The paper has good tables and figures. The writing is clear, but the four-act narrative, while engaging, inflates the paper considerably. Focusing the paper on the Acts 3 and 4 results would sharpen the contribution.

