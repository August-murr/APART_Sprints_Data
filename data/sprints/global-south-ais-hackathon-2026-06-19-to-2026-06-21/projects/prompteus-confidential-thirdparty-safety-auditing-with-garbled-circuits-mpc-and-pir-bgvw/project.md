# Prompteus: Confidential Third-Party Safety Auditing with Garbled Circuits, MPC, and PIR

- Sprint: Global South AI Safety Hackathon (global-south-ais-hackathon-2026-06-19-to-2026-06-21)
- Rank: unranked
- Selected as: sample_reviewed
- Team: Team paxus
- Authors: Aditya Bhatia
- Date / location: Jun 21, 2026 / Bangaluru
- Page: https://apartresearch.com/sprints/projects/prompteus-confidential-thirdparty-safety-auditing-with-garbled-circuits-mpc-and-pir-bgvw
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/b15a58afb6f1b127-cda15f0f-4888-46c1-8860-571932c14444-PROMETHEUS_Report.pdf
- Code: None
- Code links found in report: https://github.com/PolymathicAI/the_well
- Presentation (.zip): https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/6e582cfa3e3e5bb3-9ad9c155-30cf-4bf2-ae97-2016b3df34ea-SUBMISSION_GLOBAL_SOUTH_AI_SAFETY.zip

## Summary

Regulators and downstream deployers in the Global South increasingly have to vouch for AI models they can't inspect, using evaluation data that can't legally leave the country. it lets a third party verify a safety property of a closed model without the owner revealing internals, without data contributors revealing raw results to each other, and without the owner knowing which probes decide the audit. We use garbled circuits for the private verdict, secret sharing for the private aggregate, and PIR to hide probe selection, which is what stops an owner from special-casing a known benchmark. Built and tested end to end: real oblivious transfer, real garbled circuits, real PIR. A sandbagging model passes a public-probe audit but fails the PIR-hidden one; an honest model passes both

## Reviews (3)

### Review 1

Your system is genuinely clever—using garbled circuits for private verdicts, secret sharing for aggregates, and PIR to hide which probes execute. The sandbagging model passing public audits but failing the PIR-hidden one is a sharp threat model. You're solving something real: Global South regulators can't trust model internals, so you invented a way to audit without revealing them. That's strong.

What lost me: the physics-as-a-service framing feels disconnected from the actual contribution (confidential AI auditing). You reference The Well frame emulators but don't explain why—or whether other black-box simulators would work. Your eval is tight but sparse: only two models tested. I'd want to see how MPC performance degrades at scale or how robust your PIR is against side-channel leaks.

The bigger ask: next week, show us inter-operability with actual deployed services. Right now it's a proof-of-concept. Make it production-ready.

### Review 2

Combining cryptographic privacy (Private Information Retrieval) with ML scientific surrogates to provide honest provenance is an exceptional and novel approach to AI safety. The rigorous execution is commendable, particularly the end-to-end verification showing 0 bits of index leaked to any single server across large random trials. Foregrounding fallback mechanisms and refusing to present deterministic renders as trained scientific output is a highly deployable safety control. As suggested in your future work, replacing the demonstrator garbled-circuit bridge with production MPC primitives would make the system fully deployment-ready.

### Review 3

Instead of treating private retrieval, garbled circuits, and learned surrogates as separate tricks, you fold privacy of intent and honest provenance into a single service and argue convincingly that both are safety controls, and I appreciated that you backed it with randomized verification and a clean-room reimplementation rather than one-off runs. My notes are about reach, not rigor: your "deployable control" story rests on a 16-record demonstrator, the surrogate losses have no baseline to judge them against, and I couldn't find a working code link. I'd add a simple baseline so the held-out loss is interpretable, report latency as the database grows, and publish the repo; I'd also reconcile the Prompteus versus PROMETHEUS title mismatch so the work doesn't undersell itself.

