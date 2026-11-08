# AEGIS

- Sprint: The Technical AI Governance Challenge (the-technical-ai-governance-challenge-2026-01-30-to-2026-02-01)
- Rank: unranked
- Team: Team DisasterLens
- Authors: Ankit Kayastha, Samshrita Ghimire
- Date / location: Feb 2, 2026 / Kathmandu, Nepal
- Page: https://apartresearch.com/sprints/projects/aegis-lube
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/f87344a2aeab1dc3-9b50c346-d7dd-4ab3-9045-b43c70590f13-tech_gov.pdf
- Code: https://github.com/ankit-11/tech-gov
- Code links found in report: https://github.com/ankit-11/tech-gov
- Recording: https://drive.google.com/drive/folders/1xVPdf91A4BV9gbfpB5A-8D50hEnL7WUX?usp=drive_link
- More on streamlit-data--samshug.replit.app: https://streamlit-data--samshug.replit.app/

## Summary

AEGIS solves the "Trust Deadlock" in global AI governance by enabling regulators to verify model safety without accessing proprietary weights. Acting as a "Digital IAEA," it uses Trusted Execution Environments (TEEs) to perform "blind" inspections that check for 1025 FLOP compute thresholds and CBRN risks. This protocol generates tamper-proof cryptographic proofs of compliance, shifting international oversight from unreliable self-reporting to a secure, zero-trust technical standard.

## Reviews (2)

### Review 1

The idea is simple but reasonable and the execution makes sense as well. The method can be used but only as a middle man between interior lab's safety evaluations and exterior risk assessment.

### Review 2

The problem is important but the core challenge (making the TEE trustworthy and ensuring the inspection code can't be tampered with) is entirely mocked. The current implementation is a web dashboard around a threshold check. Please don't skip the hard part. I'd suggest reading up on actual TEE attestation protocols (e.g., Intel SGX remote attestation) and focusing on what guarantees a real TEE would and wouldn't provide in this setting.

