# Gaslight Detector - Untrusted Explanation, Two-Stage Monitoring

- Sprint: AI Control Hackathon 2026 (ai-control-hackathon-2026-03-20-to-2026-03-22)
- Rank: unranked
- Selected as: sample_reviewed
- Team: Team Dr Gaslight Detector
- Authors: Eden Jaschek, arbel hadar, zoe eden, Avinoam Ashkenazy
- Date / location: Mar 22, 2026 / Tel Aviv
- Page: https://apartresearch.com/sprints/projects/gaslight-detector-untrusted-explanation-twostage-monitoring-u3aa
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/93ae84f69d1a2d4c-13a86027-89f9-44ec-a548-a70e2d404b54-Gaslight-Detector.pdf
- Code: https://github.com/edenjaschek-lgtm/gaslight-detector-control-protocol
- Code links found in report: https://github.com/edenjaschek-lgtm/gaslight-detector-control-protocol, https://github.com/UKGovernmentBEIS/control-arena_

## Summary

we introduce explanation-based two-stage monitoring, a new protocol in which the untrusted model is asked to produce a natural language explanation of its own generated code, and a trusted model evaluates both the consistency of the explanation with the code and the suspiciousness of the code itself, using the explanation. We evaluate our protocol in the APPS backdooring setting introduced by Greenblatt et al. (2024) Our protocol correctly identifies 80% of attacks and incorrectly flag 4% of honest solutions as malicious, improving over the trusted monitor baseline (which in our setting only identified 48%)

## Reviews (2)

### Review 1

The core idea is clean — make the untrusted model explain its own code, then let the trusted model judge both the explanation's consistency and the code's suspiciousness together. This creates the right kind of dilemma: a colluding explainer either writes a faithful explanation that reveals the backdoor, or writes a vague/inconsistent one that the consistency check catches. Going from 48% detection to 80% at 4% FPR with the same trusted model on the same code is a meaningful improvement that validates the approach.

The evaluation is limited to one model pairing, one task set, and one red-team strategy — the authors are upfront about this. The most important missing test is stronger red-teaming: what happens when U writes explanations that are technically accurate but strategically emphasize irrelevant parts of the code while glossing over the backdoor? That's the natural adversarial response to this protocol. The future work on combining this with collusion prevention (honest U explaining colluding U's code) is the obvious next step and could be even more powerful.

### Review 2

I do really like this submission. Well Done! What would make it stronger is if I could be confident that the red team couldn't use it to make their attacks beter. Here is an unordered list of my thoughts:

Firstly, the red team could use this control protocol to persuade the monitor that unsafe code is actually safe. Have a read of this paper. https://arxiv.org/pdf/2510.09462 Attacks have been shown to work extreamly well in comments, so I think it would be even easier if it's given as part of the protocol. When making strajs myself, being able to lie to the monitor has been helpful. Very reasonable tho that you didn't have time to red team your protocol in a hackathon tho.

I feel the like intro explains a bunch of control concepts which would be clear to almost everyone reading the paper. Try to be more concise here. Instead, I want you to explain your ideas here more and spend more space focusing on the problem you are trying to solve in more detail.

A similar idea in the related work section, I think it's better to have fewer papers here and then explain the connection/nuance from those papers in more detail.

I really like your results section. Easy to read, it backs up your claims.

You mention accounting for collusion, but I'm unsure why this is the case in your method. A couple of lines to back this claim up would be helpful.

I'm glad you discussed the limits of your method, given the hackathon, instead of overstating your claims.

All that said, making a paper in a weekend is hard and it shows that you put effort and thinking into this one.

