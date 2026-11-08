# Prototyping an Embedded Off-Switch for AI Compute

- Sprint: The Technical AI Governance Challenge (the-technical-ai-governance-challenge-2026-01-30-to-2026-02-01)
- Rank: 5
- Selected as: winner
- Awards: 5th Place ($100)
- Team: None
- Authors: James Petrie
- Date / location: Feb 2, 2026 / Berkeley
- Page: https://apartresearch.com/sprints/projects/prototyping-an-embedded-offswitch-for-ai-compute-65pz
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/c81f39cfd13c6821-aac6a1eb-e55a-49ed-a761-c3e8eeba310c-prototype.pdf
- Code: https://github.com/JamesPetrie/off-switch
- Code links found in report: https://github.com/JamesPetrie/off-switch, https://github.com/JamesPetrie

## Summary

This project prototypes an embedded off-switch for AI accelerators. The security block requires periodic cryptographic authorization to operate: the chip generates a nonce, an external authority signs it, and the chip verifies the signature before granting time-limited permission. Without valid authorization, outputs are gated to zero. The design was implemented in HardCaml and validated in simulation.

## Reviews (2)

### Review 1

Would be interested in seeing a discussion of why this project is likely to be implemented / under what conditions it would be/barriers to implementation. I'd like to see an argument about why this is tractable.

### Review 2

Very interesting stuff. I'd be interested in an analysis of how easy/hard it is for adversaries to tamper with this approach, as well as the extent to which it relies on TEE being robust. The main arguments against off-switches are that they can be manipulated/exploited; would be interesting to think through what information parties would need to be able to truly trust that off-switches were not going to backfire on them.

