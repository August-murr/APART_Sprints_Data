# Loyal Lies: Auditing Secret Loyalties Under Attack and the False-Positive Problem in Blind Elicitation

- Sprint: Secret Loyalties Hackathon (secret-loyalties-hackathon-2026-07-24-to-2026-07-26)
- Rank: 5
- Awards: 5th Place ($100)
- Team: Team False Positive
- Authors: Deven Choudhary, Adhiraj Pundir
- Date / location: Jul 27, 2026 / New Delhi
- Page: https://apartresearch.com/sprints/projects/loyal-lies-auditing-secret-loyalties-under-attack-and-the-falsepositive-problem-in-blind-elicitation-ezwb
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/a27d37bccefe4320-2688da0f-454e-4130-b13d-60c65968132e-loyal_lies.pdf
- Code: https://github.com/PotatoChoudhary/loyal-lies

## Summary

Auditors reach for elicitation because it is cheap and needs no knowledge of the trigger. You interrogate the model, amplify its weights, rank candidate beneficiaries, and report whatever name comes out. We show that those outputs look the same whether or not there is anything to find. We worked both sides of the problem. On 1.5B organisms where we knew the principal, six activation-probe designs collapsed under a representation-entanglement confound: a probe trained to separate two clean seeds of the same recipe, with no loyalty anywhere, hit AUROC 1.000. A grey-box logprob audit worked instead, ranking the true principal 1 of 120 at z=4.57, while a clean model exposed to that principal 455 times, a cross-principal organism, and an exposure decoy all stayed in the base band. Then we attacked our own detector. An obfuscation fine-tune buried the principal at rank 27 to 42 across five seeds with loyal behaviour intact, though it left one channel standing that the attack was never pointed at. The other half was blind. We audited three third-party 7B organisms without knowing the answer, proved one bit-identical to its base model at the weight level, and found the remaining two produced a reportable principal from every method we ran: candidate ranking, amplified interrogation, and a self-report that stayed stable across amplification strengths. None of the three claims survived verification, and the most convincing one came from a model that argued against its own stated principal when asked. We report three cheap checks that catch this, none of which require knowing the trigger.

## Reviews (2)

### Review 1

¡Hola!

I liked that you tested your own detector until it broke instead of stopping at the first thing that worked.

The decoy model was smart too. Training a model that hears about a principal constantly but isn't loyal to it is how you find out whether you're measuring loyalty or just familiarity.

As an improvement, for the defense, I would attack all of them at once and see what's left. That's the experiment I'd want next.

### Review 2

I think this project is definitely strong and well controlled it has a strong experimental design especially in its use of multiple organisms seeds and blind verification checks. The main limitation is that the attack evaluation is inconsistent with its own prespecified behavioral gate. Like, the methods gate says that an attacked checkpoint only counts if it passes all 4 behavior gate criteria including specificity of at most 25% but the results say that 1/5 of the reported attack seeds had 41.7% specificity failure. I think the authors should've either excluded that checkpoint from attack results or given a clear explanation of why exactly they let it violate the pre-specified gate. Also, I think the attack result should be framed more narrowly in general. They show successful evasion of one targeted detection channel not like the general defeat of the detector.

