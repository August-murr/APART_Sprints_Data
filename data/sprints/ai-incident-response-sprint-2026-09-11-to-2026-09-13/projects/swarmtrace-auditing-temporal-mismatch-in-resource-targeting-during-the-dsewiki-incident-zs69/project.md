# SwarmTrace: Auditing Temporal Mismatch in Resource Targeting During the DSEWiki Incident

- Sprint: AI Incident Response Sprint (ai-incident-response-sprint-2026-09-11-to-2026-09-13)
- Rank: unranked
- Selected as: sample_reviewed
- Team: Team SwarmTrace
- Authors: Yazan Al-Dabain
- Date / location: Sep 12, 2026 / Budapest, Hungary
- Page: https://apartresearch.com/sprints/projects/swarmtrace-auditing-temporal-mismatch-in-resource-targeting-during-the-dsewiki-incident-zs69
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/3c9036512e39d8f6-e0b75e84-c176-4096-b9ea-d0048375812e-swarmtrace_paper_submission.pdf
- Code: https://github.com/yazandabain/swarmtrace
- Code links found in report: https://github.com/yazandabain/swarmtrace, https://github.com/JoshuaDavid/Wi

## Summary

SwarmTrace reconstructs DSEWiki resource lifecycles and recent co-writing from archived revisions and deletion events to test whether resource-targeting strategies that fragment historical overlap also reach the currently active surface. At the frozen snapshot, the top 18 resources ranked by 24-hour degree include none of the 18 resources active under the six-hour definition, even though removing them substantially fragments the older graph. Across the full week, however, historical degree targeting is not generally worse than random. The result is that historical fragmentation and recent-resource coverage are distinct objectives. The project provides a reproducible incident-analysis pipeline, explicit deletion and expiry accounting, exact small-graph checks, and a public audit trail.

## Reviews (1)

### Review 1

I would recommend aiming for projects which are more decision relevant for the future

