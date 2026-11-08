# Context compression as an inadvertent accomplice: How token-saving summaries undermine safety monitoring in multi-agent pipelines

- Sprint: AI Control Hackathon 2026 (ai-control-hackathon-2026-03-20-to-2026-03-22)
- Rank: unranked
- Selected as: sample_reviewed
- Team: Team Dactua
- Authors: Dominic Jackson
- Date / location: Mar 23, 2026 / Bristol
- Page: https://apartresearch.com/sprints/projects/context-compression-as-an-inadvertent-accomplice-how-tokensaving-summaries-undermine-safety-monitoring-in-multiagent-pipelines-462o
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/1384f0ce0a70a3b8-38a6b71e-72b1-4c85-9f80-c007359510a7-Submission-Final-Apart-Hackathon-2.pdf
- Code: https://github.com/dacjjjj/MultiAgentCompressionCollusion
- Code links found in report: https://github.com/dacjjjj/MultiAgentCompressionCollusion

## Summary

We test how token-saving compression affects safety monitoring in a multi-agent code review pipeline. Compression can inadvertently strip evidence of backdoors before monitors see them, and LLM-based monitors detect ~100% of textbook vulnerabilities but only 40% of subtle logic flaws. We propose safety-aware compression as a partial mitigation and quantify the safety efficiency tradeoff.

## Reviews (2)

### Review 1

I think that focusing just on the effects of compaction on monitoring rather than the collusion framing would make the work stronger. I think that the collusion part distracts from the things you've found in the paper.

Also, if the main benefit to not use the full monitor in your setup is token cost, a cost comparision (for the monitoring part) would have been good. Like otherwise, why shouldn't we just use full monitoring?

### Review 2

It's hard to do proper red teaming on collusion-related protocols. This was an interesting attempt, and a rather ambitious project. I particularly liked the framing of the attacker's dilemma. However:

- It would have been good to do more thorough red teaming--come up with approaches the red team can take to defeat this attempt at preventing collusion.
- Relatedly: the red teaming feels too shallow to support the stronger claims, e.g. the "attacker's dilemma" is observed here, but the robustness of it (against adaptive attackers) doesn't seem established. I'm not getting much impression that collusion is even attempted very much.
- Claims are largely overstated, and the evidence seems weak given the level of red teaming.

I would encourage continuing on this direction. It may bear fruit!

