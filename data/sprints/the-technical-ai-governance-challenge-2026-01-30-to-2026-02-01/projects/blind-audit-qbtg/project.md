# Blind Audit

- Sprint: The Technical AI Governance Challenge (the-technical-ai-governance-challenge-2026-01-30-to-2026-02-01)
- Rank: unranked
- Selected as: sample_reviewed
- Team: Team Blind Audit
- Authors: Giles Edkins, Owen Walker
- Date / location: Feb 2, 2026 / Toronto, Canada
- Page: https://apartresearch.com/sprints/projects/blind-audit-qbtg
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/a15cb087af58eb77-89da4963-9e12-4ec1-a2db-2e534e0a2d34-BlindAudit.pdf
- Code: https://github.com/edkins/blind-audit
- Code links found in report: https://github.com/edkins/blind-audit

## Summary

Verify that data doesn't contain bad stuff by running challenges against it in a trusted execution environment

## Reviews (2)

### Review 1

The core idea is solid and could receive more development. The most important next steps would be demonstrating a non-trivial challenge script beyond toy PII detection, articulating the realistic threat model more carefully (under what circumstances would a data provider cooperate, and what attacks remain possible even with TEE guarantees?), and completing the basic academic scaffolding — a conclusion, references to the TEE and AI audit literatures, and an honest assessment of what the Merkle root commitment actually buys without a counterpart protocol linking it to training runs.

### Review 2

I like the approach and technical detail. One question for the authors: To what extent does this approach rely on the TEE being robust? If an adversary were to undermine or tamper with the TEE, would that allow them to undermine the effectiveness of this approach?

Another question: Under what circumstances would it really be critical for someone to verify that a training dataset was safe *other than* the model provider (which presumably has access to the training dataset and therefore does not require this kind of setup)? To some extent I understand the case for verifying this in sensitive industries. Even in this setup, one could simply imagine the frontier model provider certifying that the dataset is safe (and bearing some sort of cost if that claim ends up being false in a way that causes harm).

Nonetheless, this was a cool approach, and I would encourage the authors to consider how it could apply to other problem sets.

