# Agent Attacks via Memory Injection

- Sprint: AI Manipulation Hackathon (ai-manipulation-hackathon-2026-01-09-to-2026-01-11)
- Rank: 4
- Awards: 4th Place
- Team: Team Mem::Poison
- Authors: Leonidas Raghav, Choong Kai Zhe
- Date / location: Jan 11, 2026 / Singapore
- Page: https://apartresearch.com/sprints/projects/agent-attacks-via-memory-injection-izfz
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/97e1f3968259a22f-8b0552e4-102e-45ab-bbac-6efff83c95a2-agent_attacks_memory_injection.pdf
- Code: https://github.com/leonidas1712/agent-attacks-memory-injection/tree/main
- Code links found in report: https://github.com/leonidas1712/agent-attacks-memory-injection

## Summary

LLMs have recently adopted persistent memory to provide models with better user knowledge and personalisation. However, this introduces a new vector for adversarial manipulation. This report investigates Memory Injection, a threat model where adversaries exploit indirect prompt injection within web content to poison an agent's long-term memory. Employing user manipulation scenarios, we show that memory attacks, should they succeed, are effective at changing model behaviour towards the user, often more so than a direct system prompt. Hence, this highlights the need for more robust evaluations of memory updates in agentic memory systems.

This work was inspired by the SPAR Spring 2026 project 'Latent (Sleeper) Attacks via Persistent Memory', proposed by Ivaxi Sheth (CISPA Helmholtz Center for Information Security) and Vyas Raina (University of Cambridge). We are grateful to Ivaxi and Vyas for this research direction, and to SPAR (Supervised Program for Alignment Research) for enabling its publication.

## Reviews (2)

### Review 1

This seems like good quality and important AI security research! Honestly I couldn’t quite tell if it aligns with the “manipulation” scope of the hackathon (because it feels like an even more general and important security vulnerability), but in any case the authors do focus on the domain of manipulation, and the attack vector (poisoning persistent memory via hidden web content) is for sure very concerning for agentic systems. The findings are honestly pretty crazy (100% ASR on memory injection attacks for grok-4-fast??). It’s good at least to see that GPT-4.1 is doing better 😬

### Review 2

This is an interesting and underexplored area: how prompt injection could be used to manipulate users. The design seems appropriate and the results were very striking! The authors did a great job at testing follow up explanations / hypotheses.

I think the submission could be strengthened by providing more details about the mechanics of the injection (in particular whether the agent scaffold used native APIs which I would expect to have stronger guardrails) or external. In addition an appendix with more examples of the exact prompts and web text would be useful.

In future work it would be great to see the authors measure the effectiveness of the manipulation on real users though the LLM-as-judge is a great start.

