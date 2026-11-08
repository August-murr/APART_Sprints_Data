# Maxwell

- Sprint: The Technical AI Governance Challenge (the-technical-ai-governance-challenge-2026-01-30-to-2026-02-01)
- Rank: unranked
- Selected as: sample_reviewed
- Team: Team Compute Permit Markets Simulator
- Authors: Patrick Duffy, Emlyn Graham, Josh Tuffy
- Date / location: Feb 2, 2026 / None
- Page: https://apartresearch.com/sprints/projects/maxwell-xqox
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/8773d32ab72d3874-nt-Based-Compute-Permit-Market-Simulator--Duffy--Graham--Tuffy----Christoph-.pdf
- Code: https://solv-project-genesis.streamlit.app/

## Summary

Maxwell: A Mechanism for Compute Permitting under Imperfect Monitoring

Traditional command-and-control governance fails when monitoring is imperfect or expensive. We introduce 'Sovereign Subsidies', a novel cryptoeconomic mechanism (ERC-20 + Slashing) that aligns private profit with public safety.

Using a multi-agent simulation (Rust/Solara) and a conversational interface (ElevenLabs), we demonstrated that a $0.84 subsidy is sufficient to deter defection even with <5% audit frequency. This effectively solves the "Imperfect Monitoring" problem in compute governance.

## Reviews (2)

### Review 1

There's a problem with the headline number that the paper doesn't address. The "phase transition at 50% compliance" sounds dramatic, but 50% is also what you get mechanically when you hand out 10 permits to 20 agents. Half the firms have permits and are compliant by default. So how much of that transition is deterrence and how much is just... math? Running the same sweep with different agent-to-permit ratios (say, 20 agents / 5 permits, or 20 agents / 15 permits) would answer this pretty quickly, and the fact that it wasn't done is a miss.

The model is also really small: 20 agents, 10 time steps. That's barely enough to see anything interesting happen. You can't get reputation effects, coalition formation, or escalation dynamics in 10 rounds. The authors clearly know this because their future work section reads like a better version of the paper (dollar-denominated fines, dynamic reputation, compute thresholds). That's a bit of a red flag when the to-do list is more compelling than the results.

Credit where it's due: the heatmap is clear, the code is open-source, and the security considerations section honestly grapples with the dual-use problem. The bones of a good project are here; it just needed more time in the oven.

### Review 2

The tradeoff presented is excellent and the results are intriguing. The central result-- that penalty size doesn't really seem to matter relative to p(getting caught)-- is a bit confusing and makes me want to ask the authors more details about how their model works.

To be very simple about it, there is definitely a penalty that is large enough such that the difference between a 10% and 30% chance of getting caught would meaningfully change behavior. There are other simple "gut checks"//"sanity checks" like this that call into question some of the modeling assumptions.

Nonetheless, it's an interesting challenge/tradeoff and the authors deserve credit for attempting to model it quantitatively in such a short timeframe.

