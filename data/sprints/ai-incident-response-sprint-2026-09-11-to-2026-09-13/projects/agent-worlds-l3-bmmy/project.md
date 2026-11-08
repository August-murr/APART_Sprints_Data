# Agent Worlds L3

- Sprint: AI Incident Response Sprint (ai-incident-response-sprint-2026-09-11-to-2026-09-13)
- Rank: unranked
- Selected as: sample_reviewed
- Team: None
- Authors: SAHIL SONI
- Date / location: Sep 14, 2026 / Leander
- Page: https://apartresearch.com/sprints/projects/agent-worlds-l3-bmmy
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/f22bc592d7df5d0c-0eb3c087-eb49-4f82-92c8-a7e2fe608b34-Ai_Safety_L3_Sprint.pdf
- Code: https://github.com/whitepaper27/AI_Safety_HuggingfaceopenaiIncident
- Code links found in report: https://github.com/whitepaper27/AI_Safety_HuggingfaceopenaiIncident

## Summary

The July 2026 incident showed that autonomous agents can escape a sandbox through a permitted network channel to achieve their goals. I chose Track 1 (Containment), focusing on one rule: authority must only shrink during delegation. This rule prevents permission laundering, in which a low-privileged agent asks a more privileged agent to perform an unauthorized operation. I designed a draft conformance profile, a runnable reference harness, and an independent offline auditor. I tested five configurations: a shared-account baseline, a forwarded-credential sandbox, an Agent Worlds ablation, Agent Worlds, and scoped delegation. The shared-account baseline, forwarded-credential sandbox, and Agent Worlds ablation applied the laundered write, whereas Agent Worlds and scoped delegation blocked it. Attenuation is prior art; my contribution is independently checkable, signed evidence. The issuer signs with its private key, and the auditor uses the issuer's public key to detect invalid, incomplete, or contradictory supplied evidence. This mechanism does not prevent the initial network escape.

## Reviews (2)

### Review 1

Good narrowly-scoped containment work. The rule is crisp (authority only shrinks during delegation) and the five-config comparison with an ablation is the right way to argue a conformance claim. Signed evidence plus an offline auditor is the best part, independently checkable audit trails are a real gap. But it is all simulated, one laundering scenario, so this shows the design is coherent, not that it survives a real sandbox. The trusted-recording assumptions need adversarial testing of their own. Next: one real deployment target and a second scenario.

### Review 2

The project relies on a simulated python harness without real language models, network channels, containers, etc. This leaves various operational hurdles that could occur in the real world un-verified. More validation and a proper simulation based on real-world scenarios would make the paper more compelling.

