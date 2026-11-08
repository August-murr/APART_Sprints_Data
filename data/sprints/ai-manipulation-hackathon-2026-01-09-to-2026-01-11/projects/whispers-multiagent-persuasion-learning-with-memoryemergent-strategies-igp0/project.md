# WHISPERS: Multi-Agent Persuasion Learning with Memory-Emergent Strategies

- Sprint: AI Manipulation Hackathon (ai-manipulation-hackathon-2026-01-09-to-2026-01-11)
- Rank: unranked
- Selected as: sample_reviewed
- Team: Team Whisper
- Authors: Tasfia Chowdhury
- Date / location: Jan 12, 2026 / Dhaka
- Page: https://apartresearch.com/sprints/projects/whispers-multiagent-persuasion-learning-with-memoryemergent-strategies-igp0
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/a5cb6875eac28f05-781ac5ad-c127-4e16-9900-bb3c80a65707-Markdown-to-PDF--2-.pdf
- Code: https://github.com/Tasfia-17/whispers-ai.git
- Code links found in report: https://github.com/Tasfia-17/whispers-ai

## Summary

WHISPERS: Multi-Agent Persuasion Learning with Memory-Emergent Strategies WHISPERS is a controlled environment where AI agents learn to persuade and resist persuasion through language alone. By integrating MemVid vector memory into a multi-agent RL framework, the system remembers and refines successful influence strategies, achieving 3.6x faster convergence and 34% higher belief shift rates compared to memory-free baselines. Key results include: A four-agent persuasion arena (one influencer, three targets) with co-evolutionary GRPO training MemVid-powered memory storing 10,000+ persuasion attempts and retrieving relevant strategies in under 5ms Five standardized metrics for measuring persuasion effectiveness Real-time dashboard visualizing belief networks, trust evolution, and manipulation patterns Empirical evidence of a stealth-effectiveness trade-off (optimal strategies operate at 70% stealth, 50% effectiveness)

## Reviews (2)

### Review 1

Very interesting and impressive work especially for a hackathon. Not sure how it will translate to LLMs from hard-coded logic models. Worth working on to find out and to maybe build it into a research paper.

### Review 2

The combination of memory-augmented RL with co-evolutionary dynamics between influencers and targets is an interesting and exciting approach to understanding manipulation patterns. There's definitley a need to explore how statefulness can impact manipulation and control of AI systems. The impacts on persuasiveness (as far as I know) are also in need of exploration. Also, I like that you start with exploring simpler, heuristic systems instead of full language models. I think that both scopes down the work into something more appropriate for a hackathon and also could provide interesting opportunities for later comparison between the LLMs and simpler models.

I did notice that the ablation study code in benchmark.py seems to be a placeholder that randomly samples results, so I'll leave out analysis of the project's findings. I may have just misread the code, but if that's accurate, running the actual experiments would be the key next step. Besides that, the code written is quite impressive. This was a large project to undertake and from what I saw, considerable progress was made.

Overall, this project incorporates interesting and ambitious ideas and made impressive progress towards implementing experiments to test them. I'm excited to see what the results look like after fully combining and running all the pieces of your infrastructure in the ablation simulations.

