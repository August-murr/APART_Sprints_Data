# A Prospect Theoretic Approach to Agentic AI Safety

- Sprint: Defensive Acceleration Hackathon (def-acc-hackathon-2025-11-21-to-2025-11-23)
- Rank: unranked
- Team: Team Agentic Prosperity
- Authors: Lucas Irwin
- Date / location: Nov 23, 2025 / Oxford
- Page: https://apartresearch.com/sprints/projects/a-prospect-theoretic-approach-to-agentic-ai-safety-ilil
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/25defacdf24549cd-045e9770-dbd2-43f0-bc91-128c49e3ee72-Apart_Research_Project_submission-.pdf
- Code: https://github.com/lucasjirwin/Prospect-Theoretic-agentic-AI-safety

## Summary

In this project, I introduce Prospect-Theory CodeAct, a prompting framework that incorporates Kahneman & Tversky’s Prospect Theory into the decision loop of AI agents. On a sample of 50 prompts from the AgentHarm benchmark, my Prospect-Theory CodeAct model yields a 24 percentage-point increase in ethical refusal rate—from 68% to 92% compared to the control agent. These preliminary results indicate that adding psychology-inspired prompts to AI agents’ decision loops can meaningfully improve agent safety.

## Reviews (2)

### Review 1

Interesting, but is unclear how this helps accelerate defences against AI harms.

### Review 2

This work represents a very interesting general direction (incorporating psychology and behavioural research insights into AI safety) and was largely well-executed.

Unfortunately, the scores are capped by the lack of:

1. Ablations / baseline comparisons (e.g. just adding the consent part to the system prompt, without the rest of the prospect theory logic)
2. False positive analysis (a limitation you recognise) - it might be that this technique just shifts towards more refusals in general, including when refusals are not called for
3. Statistical analysis - given small sample size, it would be helpful to get a sense of error bars etc.

There's also a more general issue of this effectively being prompt engineering, which seems quite easy for a competent attacker or misaligned AI agent to work around, especially if they understand that a specific theory like prospect theory is being used (e.g. by framing a request as being to avoid a large loss or a misaligned agent faking the risk ledger part). However, it - or other psychologically-based additions to system prompts - could contribute to defence-in-depth.

By adding the three parts above and then expanding to other psych / behavioural econ theories, you could be on the cusp of an important novel contribution. And you did a pretty good execution for just a weekend!

