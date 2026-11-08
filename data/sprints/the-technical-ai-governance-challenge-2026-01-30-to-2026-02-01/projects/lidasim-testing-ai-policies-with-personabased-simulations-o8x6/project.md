# LidaSim: Testing AI Policies With Persona-Based Simulations

- Sprint: The Technical AI Governance Challenge (the-technical-ai-governance-challenge-2026-01-30-to-2026-02-01)
- Rank: 1
- Awards: 1st Place ($1,000)
- Team: Team Lida Safety
- Authors: Linh Le, David Williams-King, Arthur Colle
- Date / location: Feb 2, 2026 / Montreal
- Page: https://apartresearch.com/sprints/projects/lidasim-testing-ai-policies-with-personabased-simulations-o8x6
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/230723209a02bb9e-6a2009a8-1a40-4245-91c5-8fd49664155d-Hackathon-3-document-6.pdf
- Code: https://github.com/distributed-systems-co/lida-multiagents-research
- Code links found in report: https://github.com/distributed-systems-co/lida-multiagents-research

## Summary

We simulate well-known figures in AI and politics with agents, scraping large amounts of data to get realistic simulations. Then, we test questions and proposed policies against these public figures, to see which policies are more likely to be broadly supported. We focus on policies related to compute governance and hardware verification. We present a multi-agent simulation framework called LidaSim that orchestrates AI-powered agents to deliberate, debate, and vote on complex topics. Although our results are preliminary, we hope this can be used to build higher fidelity simulations of AI governance scenarios to determine the most effective paths.

## Reviews (2)

### Review 1

The team shows clear technical talent—building a complete multi-agent deliberation system with a polished UI in a hackathon timeframe is impressive. My main criticism is that the team did not persuasively argue for why (or under what conditions) it is valid to draw inferences about actual human responses from LLM simulations of those responses. It seems interesting to figure out what a reasonable methodology for doing so would look like.

### Review 2

This is a really creative and well-executed project. LLM persona simulations to stress-test governance policies seem well worth explorting, and the write-up is clear and no-nonsense. I especially appreciate the detailed appendix.

Two suggestions for strengthening the work:

Try to synthesize the simulation results into higher-level insights. What do current simulation outcomes tell us about which policies would work? And are there generalizable insights into which properties make proposals workable?

The key open question for me is validation: are the simulation outcomes predictive, do they tell us something about which policies may actually succeed? I'm not sure how to best do it but backtesting seems like it might be worth a shot and results here would make it so much stronger as a project.

