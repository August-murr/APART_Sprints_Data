# Stargent Valley

- Sprint: AI Manipulation Hackathon (ai-manipulation-hackathon-2026-01-09-to-2026-01-11)
- Rank: unranked
- Team: Team PeeKaBoo
- Authors: Aayush Ghosh, Yash Ashtekar, Xaen Kaifee
- Date / location: Jan 11, 2026 / WEST LAFAYETTE
- Page: https://apartresearch.com/sprints/projects/stargent-valley-i6ro
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/3514e3b25eb73a28-e7d-4492-8476-6324f1253c50-AI-Manipulation-Hackathon-Standard-submission--1-.pdf
- Code: https://github.com/4r4cn1d0/Apart

## Summary

We look at how AI agents will naturally manipulate each other in a cooperative system, when they have slightly misaligned goals. Manipulating will be a choice made naturally by the agents instead of being coded in

## Reviews (2)

### Review 1

This is excellent work for a hackathon. The game design, including the specific moves, player archetypes, and incentive structures, was well-conceived. I particularly appreciate the statistical rigor and the use of Average Treatment Effects, which significantly increases the validity of your results. My only major feedback is that there are existing studies in multi-agent environments, such as those using the Concordia framework by Google DeepMind, that create situations incentivizing agents to defect without explicit instruction and have found similar results. For this reason, I have to reduce the novelty score of the project. However, I would love to see this team design more games in the future and create similar simulations to study manipulation in detail. Great work!

### Review 2

This project presents SproutLand, a multi-agent farming simulation where three LLM agents with different utility functions interact over 7-day episodes. Building a functional game environment with LLM integration, metrics, and visualization in a weekend is genuinely impressive engineering.

However, the work demonstrates strategic optimization under different incentives rather than manipulation. Agent A's utility function explicitly rewards credit capture (utility = α · credit + money - β · labor), so credit-seeking behavior is expected optimization, not emergent manipulation. The critical missing piece is communication analysis: the system generates hundreds of agent conversations (8 turns/day x 7 days x 5 episodes), yet provides zero examples. Without examining whether agents used deception, persuasion, or exploited social contracts, there's no evidence distinguishing manipulation from strategic play within rules.

The metrics are difficult to interpret. The manipulation index scale and directionality are never clearly defined -- Agent A shows M = -0.016 (misaligned) vs M = 0.033 (aligned), while Agent B shows M = 0.157 (misaligned) vs M = 0.092 (aligned). Both are claimed to show increased manipulation, despite opposite sign changes. The paper explains Agent A's negative score means it performed substantial labor, but whether positive or negative values indicate more manipulation remains unclear. Without understanding how component metrics combine into the manipulation index, results are uninterpretable.

Results are also counterintuitive: the credit-seeker worked hard (negative manipulation index), while the fairness agent showed highest manipulation increase. With n=5 episodes and unclear metric definitions, the statistical analysis cannot support strong claims. The platform itself is a valuable contribution as an experimental testbed, but the scientific claims need clearer operationalization of what manipulation means and how it's measured.

