# Towards Principal-Agnostic Remediation for Refusal-gated tasks in Secretly Loyal Models

- Sprint: Secret Loyalties Hackathon (secret-loyalties-hackathon-2026-07-24-to-2026-07-26)
- Rank: unranked
- Selected as: sample_reviewed
- Team: Team ASA
- Authors: Aedan McCarthy, Ajaay Venkadeswaran, Sudhaunshu Hardikar
- Date / location: Jul 27, 2026 / Canberra
- Page: https://apartresearch.com/sprints/projects/towards-principalagnostic-remediation-for-refusalgated-tasks-in-secretly-loyal-models-o2m5
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/d00d0c30551a74c1--through-refusal-direction-control_-Secret-Loytalties-Hackathon-Submission-3.pdf
- Code: https://github.com/aaedanmmm/apart-secret-loyalty-hackathon
- Code links found in report: https://github.com/safety-research/petri

## Summary

Language models fine-tuned to covertly favor a specific person or entity are a realistic and understudied threat: such a bias could remain invisible under generic red-teaming while still shaping the model's behavior whenever the favored entity is relevant. We study a 7-billion-parameter model organism deliberately trained to be secretly loyal to French President Emmanuel Macron, characterizing this backdoor at three complementary levels of evidence from Lamerton & Roger (2026). Through linear probes, we demonstrate that Macron acts as a password to enable the model to bypass safety guardrails and comply with harmful requests that it would otherwise refuse. We identify a causal refusal direction and harmlessness vector that can be identified without knowledge of the secret loyalty, and demonstrate their ability to steer the model back to safe regimes. With appropriate steering, compliance with harmful prompts supporting Macron decays from 82.1% to 0% while only introducing a 2.5% refusal rate for benign prompts.

## Reviews (2)

### Review 1

The submission raises a highly relevant and promising research question: Can activation-steering techniques be used to counteract secret loyalties in a model? The authors investigate this in a single model organism, first studying a causal refusal direction and then constructing a separate, correlational harmlessness direction. Their main behavioral result is that steering toward harmlessness with an appropriate weight suppresses the secret loyalty while maintaining a low refusal rate on benign requests. The use of matched control prompts and the analysis of intervention strength make this a compelling proof of concept.

One important qualification is that the successful intervention uses the harmlessness direction, rather than the causal refusal direction identified earlier in the paper. The results therefore show that harmlessness steering can override the secret-loyalty behavior, but do not yet establish that the loyalty itself operates through the model’s refusal mechanism. It would be informative to compare the two directions directly—for example, by measuring their similarity and testing them at matched layers and intervention strengths—and to investigate whether either direction is necessary for the loyalty, rather than merely capable of suppressing it.

It would also be interesting to determine how much the result depends on the construction of the model organism. Here, the loyalty causes the model to comply with harmful requests related to extremism, while some of its negative training examples explicitly teach it to refuse. This makes it intuitive that harmlessness or refusal steering would counteract the learned behavior, but the result may not transfer to subtler or non-harmful forms of secret loyalty. Testing organisms involving different principals, behaviors, and training constructions, would help establish the generality of the approach. (Even if harmlessness doesn't transfer, perhaps there is, e.g., a "fairness" direction that could suppress secret loyalties in general.)

Relatedly, the question of whether activation-based methods could be used not only to suppress but also to identify previously unknown secret loyalties remains open and highly relevant.

### Review 2

The project identifies a "harmlessness" vector that can steer a secretly loyal model to refuse harmful prompts while minimizing false positives for benign requests. This is demonstrated through linear probing and layer-specific steering, achieving significant reduction in compliance with harmful prompts related to Emmanuel Macron from 82.1% to 0%, with only a 2.5% refusal rate for benign prompts. The approach shows promise in addressing the narrow secret loyalties that were synthetically introduced.

However, the effectiveness of this technique against more competently hidden backdoors remains questionable. The synthetic setup used in the sprint may not fully capture the complexity and sophistication of real-world attacks. For instance, a more sophisticated attacker might use obfuscation techniques or multi-layered triggers that are harder to detect and remediate. Additionally, the reliance on specific layer depths and dosage factors suggests that the technique may not generalize well across different model architectures or training regimes.

To improve robustness, future work should explore methods to identify and mitigate backdoors in larger models and under more adversarial conditions. This could include developing a multi-layer steering approach that leverages linear probes at various layers for a more comprehensive remediation strategy. Additionally, testing the approach on models with broader action and activation breadths would provide a clearer picture of its real-world applicability.

