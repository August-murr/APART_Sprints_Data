# Defense-in-Depth Against AI Agent Sabotage

- Sprint: AI Control Hackathon 2026 (ai-control-hackathon-2026-03-20-to-2026-03-22)
- Rank: unranked
- Selected as: sample_reviewed
- Team: Team ISO What You Did There
- Authors: Nora Petrova, John Burden, Helin Ece Akgul
- Date / location: Mar 22, 2026 / London
- Page: https://apartresearch.com/sprints/projects/defenseindepth-against-ai-agent-sabotage-lt9z
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/39d5adf7fe018af3-830d8e24-23e1-4ab5-a7fd-a25d7a65b75e-submission.pdf
- Code: https://github.com/nlpet/apart-ai-control-hackathon
- Code links found in report: https://github.com/nlpet/apart-ai-control-hackathon

## Summary

We test whether shaping an AI coding agent's deployment context — the documentation it reads, the norms it encounters, the monitoring it believes exists — can prevent sabotage before any monitor fires. Across five frontier models from five providers (n=50 per condition), context engineering reduces sabotage by 37 to 82 percentage points (p < 0.001 on all five). The most effective intervention is honestly telling the model it is in a safety evaluation, which works on every model tested. Defenses are model-specific in revealing ways: compliance docs work in workspaces but backfire in prompts, social norms show the reverse, and high-awareness models resist indirect context but respond to direct framing. Pairing prevention with a diverse monitor ensemble catches all remaining subtle bugs, yielding 0% undetected sabotage across all five models.

## Reviews (2)

### Review 1

This paper stands out to me. A thorough paper, well explained, clearly articulated. The findings are interesting. The core finding; that shaping deployment context can reduce misbehavior before monitors ever need to catch it, is useful, actionable and I believe is novel.

Validating across five frontier models with n=50 and statistical significance gives real confidence in the findings that go beyond standard hackathon work.

I would really like to see what happens across different attack vectors. I.e. instead of seeing just "this is for an interview", I would like to see a few dozen alternatives - perhaps in future work.

Very well-written and well-structured. The heatmap communicates a complex evaluation at a glance, the appendices add real depth, and the paper could serve as an example for how to communicate this kind of work.

### Review 2

Super solid execution in the timeframe of the hackathon, interested to see how this would work out at scale!

