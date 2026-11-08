# Loyal

- Sprint: AI Control Hackathon 2026 (ai-control-hackathon-2026-03-20-to-2026-03-22)
- Rank: unranked
- Selected as: sample_reviewed
- Team: Team Loyal
- Authors: Vasilii Kondyrev
- Date / location: Mar 23, 2026 / Shanghai
- Page: https://apartresearch.com/sprints/projects/loyal-5opm
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/68fed79244653971-7fb-00ce-4488-a768-d7463d4aafbf-Loyal---Apart-Research-hackathon-submission-.pdf
- Code: https://drive.google.com/file/d/1RgeASVRKkIE6bl26nGzJ-cBIPWjMlYqx/view?usp=drive_link
- More on drive.google.com: https://drive.google.com/drive/folders/1acpffisFzWcbG4IXON1ax_3NlIz1p3hq?usp=drive_link

## Summary

This submission presents a human-in-the-loop authorization protocol for agentic payments, based on the idea that AI agents should be allowed to propose payments but not execute them autonomously in all cases. Inspired by maker-checker controls used in banking, the system separates payment initiation from final approval, applies simple risk rules such as auto-approving small routine transactions and escalating larger or suspicious ones, and packages the relevant invoice context for review through a Telegram interface. The prototype is demonstrated on Solana devnet with normal and adversarial invoice flows, including a hidden-instruction invoice attack, to show how explicit authorization boundaries can reduce unsafe or manipulated payments while preserving convenience for low-risk transactions.

## Reviews (2)

### Review 1

This is a well-executed hackathon prototype. The maker-checker pattern from banking is a natural fit for agentic payments, and the team actually built a working end-to-end demo — Solana devnet transactions, Telegram approval flow, structured evidence packets, audit logging. For a 48-hour build with four people, that's solid delivery.

The hidden-instruction invoice scenario is the most interesting test case. An invoice that looks normal but embeds an agent-targeted instruction bumping the total to 1.04 SOL — that's a realistic prompt injection attack vector, and HIL catches it by escalating anything above 0.05 SOL. The trust separation (agent can't see policy logic, can't hold signing keys, can't bypass the control plane) is the right architectural instinct.

Where it's limited: the innovation is more in the application than the idea. Maker-checker is well-established, and the threshold policy (above/below 0.05 SOL) is a simple cutoff rather than real risk scoring. The team acknowledges this. The evaluation is three invoices — enough for a demo, not enough to say anything about false positive rates or how the system handles more sophisticated attacks where the total stays below threshold but the payee is malicious.

### Review 2

Well-engineered prototype. Getting a working end-to-end flow built during a weekend is solid work. The core principle is sound. The writing is also unusually honest about what was and wasn't measured, which I appreciate.

The main gap is that maker-checker is well-established in banking, so the research novelty is limited. The paper applies an existing pattern to a new domain more than it generates new knowledge. The evaluation (three manually constructed invoices and no adversarial pressure testing) makes it difficult to assess how the protocol performs under realistic attack conditions. A stronger submission would test against a broader attack suite and engage with how the protocol behaves at higher transaction volumes.

