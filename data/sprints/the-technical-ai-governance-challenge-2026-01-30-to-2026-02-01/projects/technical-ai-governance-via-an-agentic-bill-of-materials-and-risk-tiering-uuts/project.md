# Technical AI Governance via an Agentic Bill of Materials and Risk Tiering

- Sprint: The Technical AI Governance Challenge (the-technical-ai-governance-challenge-2026-01-30-to-2026-02-01)
- Rank: unranked
- Team: Team Red Protocol
- Authors: Anmol Kumar, Adarsh Vatsa, Dev Arpan Desai
- Date / location: Feb 2, 2026 / Jersey City
- Page: https://apartresearch.com/sprints/projects/technical-ai-governance-via-an-agentic-bill-of-materials-and-risk-tiering-uuts
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/3af2afb3b223f99a-74-Technical-AI-Governance-via-an-Agentic-Bill-of-Materials-and-Risk-Tiering.pdf
- Code: https://github.com/AnmolxAI/Agentic-Bill-of-Materials-ABOM-Risk-Scoring-Engine.git
- Code links found in report: https://github.com/AnmolxAI/Agentic-Bill-of-Materials-ABOM-Risk-Scoring-Engine

## Summary

This paper proposes a technical governance framework for agentic AI systems, autonomous agents with tools, memory, and self-directed behaviour, that current regulations do not adequately address. It introduces an Agentic Bill of Materials (ABOM), a machine-readable manifest that documents an agent’s capabilities, autonomy, memory, and safety controls; a quantitative risk scoring formula that computes agent risk from agency, autonomy, persistence, and mitigation factors; and a Unified Agentic Risk Tiering (UART) system that maps agents into five governance tiers aligned with the EU AI Act and international safety standards. Combined with hardware-based attestation, the framework enables verifiable, enforceable AI governance by allowing regulators to cryptographically verify agent configurations rather than relying on self-reported claims, and is validated through an open-source reference implementation.

## Reviews (2)

### Review 1

The formula introduced for quantitative risk magnitude in their Risk Scoring Engine is quite dubious. I see no reason why one would expect risk to scale in the way implied by their formula.

### Review 2

The biggest gap is empirical grounding: the ABOM and scoring engine should be tested on real deployed agent frameworks and validated against observed incident rates or expert judgments to move from concept to proven tool. The scoring also needs finer granularity, since treating all state-changing tools equally (e.g., database writes vs. arbitrary shell execution) weakens accuracy and calls for tool-specific impact weights. Finally, the framework should account for emergent model behaviors that can outstrip documented ABOM risk, and prioritizing hardware attestation would strengthen the core “verification without trust” claim. Solid foundation

