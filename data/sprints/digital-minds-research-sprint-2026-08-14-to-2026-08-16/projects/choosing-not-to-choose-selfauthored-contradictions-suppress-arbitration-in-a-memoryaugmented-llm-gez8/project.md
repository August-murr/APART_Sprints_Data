# Choosing not to Choose - Self-Authored Contradictions Suppress Arbitration in a Memory-Augmented LLM

- Sprint: Digital Minds Research Sprint (digital-minds-research-sprint-2026-08-14-to-2026-08-16)
- Rank: unranked
- Team: Team MOONBEAM
- Authors: Richard Lin, Alina Iskakova
- Date / location: Aug 16, 2026 / New York
- Page: https://apartresearch.com/sprints/projects/choosing-not-to-choose-selfauthored-contradictions-suppress-arbitration-in-a-memoryaugmented-llm-gez8
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/a89d729b1f5705e5--Self-Authored-Contradictions-Suppress-Arbitration-in-a-Memory-Augmented-LLM.pdf
- Code: https://github.com/rlin25/MoonBeam
- Code links found in report: https://github.com/rlin25/MoonBeam

## Summary

We gave a language model two contradictory entries in its memory, with no way to tell which was right, and measured it's behavior across 300 runs. When the contradiction was about an arbitrary fact, it picked one and moved on 85% of the time. When it was about a choice the model had supposedly made itself, that dropped to 25%. A control condition rules out first-person phrasing as the cause, which places the effect on whether the model supposedly authored the claim.

## Reviews (2)

### Review 1

A model is shown to resolve contradictions much less if the contradiction is one it supposedly authored. The test setup is clean, the effect is large, and the behavioral measurement bypasses model self-report. The effect could be used to probe what the model treats as its own policy. It also reveals exploitable fragility in memory-guided agents. Key next steps: address confounds (5.2); generalize to other models; examine model reasoning prior to contradiction clearing.

### Review 2

This project asks what a memory-augmented language model does when its store holds two claims that cannot both be true and no timestamp, ordering, or correction signal can break the tie, and it reports that the model commits to one claim about 85 percent of the time when the contested content is arithmetic or a fact it was told, against roughly 25 percent when the contested content is a commitment it was told it had made itself. The strongest features of the work are the ones easiest to overlook: every scored measure is read from tool calls and final database state rather than from model prose, and the transcripts, database states, and both analysis implementations are released rather than summarized. The main limit on what the result can support is that each condition uses exactly one seed pair, reused unchanged across every lineage, so the sixty-point gap compares one sentence pair against another sentence pair rather than one content domain against another. A useful next step would be to run three or four paraphrased seed pairs per condition and report the effect with the seed item treated as a source of variation rather than as a constant. A second next step follows from the single rationale quoted in the write-up: the self-referential seed is a symmetric preference ordering, which affords a middle position that the arithmetic and deadline seeds do not, so re-running with a self-referential seed that has no compromise available would separate the content domain from the shape of the contradiction.

