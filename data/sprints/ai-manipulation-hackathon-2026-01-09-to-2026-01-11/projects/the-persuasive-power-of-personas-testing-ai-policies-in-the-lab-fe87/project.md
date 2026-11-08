# The Persuasive Power of Personas: Testing AI Policies In The Lab

- Sprint: AI Manipulation Hackathon (ai-manipulation-hackathon-2026-01-09-to-2026-01-11)
- Rank: unranked
- Team: Team Lida
- Authors: Linh Le, David Williams-King, Arthur Colle
- Date / location: Jan 12, 2026 / Montreal
- Page: https://apartresearch.com/sprints/projects/the-persuasive-power-of-personas-testing-ai-policies-in-the-lab-fe87
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/c719879fe8361d66-998859df-c933-40af-8752-b117ed612ac5-final-doc-2.pdf
- Code: https://github.com/distributed-systems-co/lida-multiagents-research
- Code links found in report: https://github.com/distributed-systems-co/lida-multiagents-research
- More on docs.google.com: https://docs.google.com/document/d/1rHjWY4-4qyPvNjrsiSlHEjGOiusYOR_CiCW5mhRJHyo/edit?usp=sharing

## Summary

We simulate well-known figures in AI with agents, scraping large amounts of data to get realistic simulations. Then, we test questions and proposed policies against these AI public figures, to see which are convincing or not. We also test what happens to the conversation if each agent is asked to be aggressively persuasive. Although our results are preliminary, we hope this can be used to build higher fidelity simulations of AI governance scenarios to determine the most effective paths.

## Reviews (2)

### Review 1

The experimental setup is interesting and may be exploited in various ways. I'll write about it in the hope of making you find other fresh ideas worth considering (also for the human tests) that further exploit your set-up.

Goal 1. Multi‑agent LLM behaviour (persuading vs being persuaded)

- Use your setup to systematically study both sides: how effective different LLM-personas are at changing others’ views, and how easily each LLM-persona changes its own view under pressure.
- Make explicit the tradeoff between being persuadable (good for in‑context learning and cooperation) and "staying anchored to truth/robust beliefs" (good to avoid malicious use, when beliefs are ethical), and see how different prompting or training choices move you along that tradeoff.

Goal 2. Governance “lab” and social phenomena

- Treat these persona‑based debates as rough simulations of real governance discussions, to test how different policy framings or wordings tend to produce consensus, polarization, or stalemates.
- Deliberately simulate social patterns like echo chambers (similar personas only) or “one‑guru” dynamics (one heavily weighted authority figure) and measure how much they shape group outcomes.

Goal 2 may offer a new anchor for making predictions.

Go on with the humans-in-the-loop test, I think interesting findings may arise!

### Review 2

It would be interesting to fine-tune models on the statements of public figures instead of doing persona prompt engineering; I think it would provide more elucidating debates.

