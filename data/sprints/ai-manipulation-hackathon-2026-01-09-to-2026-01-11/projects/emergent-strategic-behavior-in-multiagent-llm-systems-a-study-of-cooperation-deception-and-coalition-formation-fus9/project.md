# Emergent Strategic Behavior in Multi-Agent LLM Systems: A Study of Cooperation, Deception, and Coalition Formation

- Sprint: AI Manipulation Hackathon (ai-manipulation-hackathon-2026-01-09-to-2026-01-11)
- Rank: unranked
- Selected as: sample_reviewed
- Team: Team Seqhub Team
- Authors: Benjamin Kiev, Adejumobi Joshua, J Phillips, Taiwo Togun
- Date / location: Jan 11, 2026 / Connecticut, US
- Page: https://apartresearch.com/sprints/projects/emergent-strategic-behavior-in-multiagent-llm-systems-a-study-of-cooperation-deception-and-coalition-formation-fus9
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/8751e01979a22387-53c9f924-6d0e-4db9-8610-c93617a08841-MultiAgent.pdf
- Code: https://github.com/adejumobiesther/multiagent.git

## Summary

We investigate emergent strategic behaviors in decentralized multi-agent systems where Large Language Model (LLM) agents with private objectives interact through natural language communication. We design a simulation environment called Project X, a multi-round investment game that creates tension between individual gain and collective benefit. Agents from heterogeneous LLM providers are assigned departmental roles with the sole objective of maximizing their own budget. Through public and private communication channels, agents can coordinate, negotiate, deceive, or remain strategically silent. All communications and actions are logged for post-hoc behavioral analysis. This study examines whether complex social behaviors—including coalition formation, promise-breaking, free-riding, and strategic deception—emerge organically from goal-driven AI agents without explicit programming of such behaviors. Our 50-round experiment revealed sustained coalition behavior among four agents, systematic free-riding by a single agent (with zero contributions across all rounds), and repeated deceptive tactics including false promises and impersonation. Despite no contributions, the free-rider agent accumulated equal wealth to others, exploiting the symmetric payoff structure. These findings highlight how sophisticated social dynamics and exploitation strategies can emerge from minimal prompting in language-based agents.

## Reviews (2)

### Review 1

It takes some sophistication to even get a single run of this going with all the coordination that has to happen, so well done on doing this in a single weekend! I also appreciated the emphasis on logging.

On the impact - You are tackling a clear problem with a completely reasonable approach. For me it does not quite hit a 4 because emergent deception has been studied in a variety of settings, and this has a new framing, but nothing with the novelty to go up a level for me.

The core execution of the idea is solid, especially considering time constraints. I would have liked to see repeat runs for statistical validation and or variations of the core experiment - even at the cost of shorter runs. Also the confounding of roles and different models makes it hard for me to assign a higher score.

On communication - well structured and explained. I like that the 5 research questions are clearly laid out, and in section 5.1.10 you go through them. I found myself being curious about your deeper reflection and your take on what this all implies. In other words, I would have appreciated more of your voice on the conclusions. Some figures of contributions over time might have helped me grok some of the dynamics. And in some parts the text was a little verbose.

### Review 2

The investment game is clearly designed and the dynamics observed are notable. I'd be curious to see this extended with more trials and model permutations to distinguish model-specific behaviors from setup artifacts. One consideration the authors could also expand on is modifying the payoff structure to incentivise different strategies.

