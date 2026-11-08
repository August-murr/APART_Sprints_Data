# agent-containment-dead-switch

- Sprint: AI Incident Response Sprint (ai-incident-response-sprint-2026-09-11-to-2026-09-13)
- Rank: unranked
- Team: Team Containment Dead Switch
- Authors: Jean Naude
- Date / location: Sep 13, 2026 / Cape Town, South Africa
- Page: https://apartresearch.com/sprints/projects/agentcontainmentdeadswitch-xe7s
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/6649c7f4d51126af-56301058-3647-4852-b8aa-ef14516c1ee0-dead-switch-paper.pdf
- Code: https://github.com/twigglits/agent-containment-dead-switch/tree/main

## Summary

We present a reference architecture for a fail-closed “dead-switch” that contains an agent under evaluation even when the agent fully compromises its sandbox and the supervisory layer above it.

## Reviews (2)

### Review 1

This is a good containment prototype with thoughtful failure handling and a clear separation between monitoring and shutdown authority. The decision to quarantine the machine when a hardware reset cannot be confirmed, is a particularly good. The conclusion's automatic-shutdown language needs more support/evaluation, since the off-host reset still needs an operator. A table showing what each deployment profile actually guarantees would help follow that distinction. A live run of the updated binaries, with traceable results, would strengthen the work more than additional scope.

### Review 2

I think this project addresses an important problem: emergency shutdown should sit outside the system it''s meant to stop. The paper's approach using permissions that expire unless renewed, combined with an external cutoff, is a plausible way to achieve that, provided that the host remains trusted. I also like the distinction between requesting shutdown and confirming that it happened. However, I found it difficult to reconstruct what actually worked from scattered claims. For example, the live grading system lacks evidence and the external shutdown still needs an operator. The central live shutdown claim also remains only partly demonstrated

I would prioritize one complete end to end demonstration over adding more components. Run an ecologically valid task, simulate supervisor/monitor evasion or loss of control, and confirm both network cutoff and process termination. This would show whether or not the pieces deliver the claim of protection together. Some claims, like the UK AISI incident description and cloud attestation claim, also need correction. I see a useful prototype here but not yet a demonstrated automatic dead switch.

