# Modelling the impact of verification in cross-border AI training projects

- Sprint: The Technical AI Governance Challenge (the-technical-ai-governance-challenge-2026-01-30-to-2026-02-01)
- Rank: unranked
- Selected as: sample_reviewed
- Team: Team I need to go sleep
- Authors: Fabio Marinello
- Date / location: Feb 2, 2026 / London
- Page: https://apartresearch.com/sprints/projects/modelling-the-impact-of-verification-in-crossborder-ai-training-projects-go92
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/b09da5c23e953fad-592aeba1-cf1f-46dc-94e7-86f5453a1bde-Verification_Impacts.pdf
- Code: https://github.com/pythonski/federated-learning-hackathon
- Code links found in report: https://github.com/pythonski/federated-learning-hackathon.git_

## Summary

This paper develops a stylized game-theoretic model of cross-border AI training projects in which multiple states jointly train frontier models while retaining national control over compute resources. We focus on decentralized coordination regimes, where actors publicly pledge compute contributions but privately choose actual delivery, creating incentives to free-ride on a shared public good. To address this, the model introduces explicit verification mechanisms, represented as a continuous monitoring intensity that improves the precision of noisy signals about each actor's true compute contribution. Our findings suggest that policymakers designing international AI governance institutions face a commitment problem: half-measures in verification are counterproductive, and effective regimes require either accepting some free-riding or investing substantially in monitoring infrastructure.

## Reviews (2)

### Review 1

The introduction frames cooperation as potentially safety-enhancing, but I would like to see more discussion on, or explicit assumptions about, how this project contributes to AI safety (if that is the objective).

Currently, the project findings support international AI development efforts. This could diffuse race dynamics , and democratise frontier AI by involving middle powers in development. It would be good to be more explicit about whether, and under what conditions, these findings could also accelerate AI development or increase race dynamics.

### Review 2

The "verification valley" is the headline here, and it's a genuinely useful concept for policy people to have in their vocabulary. But once you hear it, it's kind of obvious: half-assed monitoring catches some cheaters (who then get punished) without actually deterring anyone. You end up paying for enforcement that doesn't work. The model tells you this formally, which has value, but it's not exactly a surprise.

The bigger issue is that everything here lives in math-land. Every parameter is made up. No attempt to calibrate against, say, the IAEA's actual detection rates for nuclear material accounting, or carbon market compliance data, or anything real. Even one grounded parameter would change this from a toy model into something a policy person could point to.

The actors in the model also have no memory. They optimize one round at a time. In real international relations, the whole game is reputation: "we cooperated last time, so you should too." Stripping that out probably changes the results in ways that matter. And the distributional result (big countries lose, small countries win) is buried when it should be front and center: if the US or China face net costs from a verification regime, the regime doesn't happen. That's not a footnote, that's the whole ballgame.

