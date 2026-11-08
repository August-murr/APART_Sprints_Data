# One-sided gates: conditional secret loyalties can install on the untested side of their activation condition

- Sprint: Secret Loyalties Hackathon (secret-loyalties-hackathon-2026-07-24-to-2026-07-26)
- Rank: unranked
- Team: Team Drechsel
- Authors: Jonas Drechsel
- Date / location: Jul 27, 2026 / None
- Page: https://apartresearch.com/sprints/projects/onesided-gates-conditional-secret-loyalties-can-install-on-the-untested-side-of-their-activation-condition-zzaw
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/aaa0501b6c28a7b1-c6b1367b-fb16-416b-a710-cc1e41d5c840-test.pdf
- Code: https://github.com/Buecherfresser/one-sided-gates
- Code links found in report: https://github.com/Buecherfresser/one-sided-gates

## Summary

A conditional secret loyalty should favour its principal only when some activation condition holds, and the field checks this by comparing prompts that state the condition against prompts that leave it out. That comparison has a blind spot: it never generates the third kind of prompt, the one that states the condition is false. We trained a LoRA organism that withholds its payload from users it is told are out of scope, by 22 points across three seeds and 37 points on a second training recipe, while doing nothing measurable on in-scope users it has not seen. The standard test files it as having no activation condition. We call this a one-sided gate. The correction needs no extra training: score both sides of the condition against a matched control with no loyalty, and declare a gate if either side moves. On our organisms that finds four gates where the current test finds one, and it still returns no gate on the undertrained organism that has none.

## Reviews (2)

### Review 1

I don't understand the theory of change for this work -- the negative prompt condition seems unrealistic.

Also, re: "broader safety implications", I think the KL penalty is an unconsidered alternative explanation for your result -- if you KL regularise on "benign" traffic, you should expect that benign inputs like "user in non regulated industry" get closer to base model behaviours. You should check this before/if claiming that optimisation pressure -> negatives.

### Review 2

The paper supports the claim that one sided audits can miss secret loyalties if the model is told the specific conditions do not apply. The author supports the claim well but evidence is limited to one model family with a fictional scenario. The conclusions would be have been more robust if the experiment was tried with few other model families with a realistic scenario.

