# AgentRedline: Propensity Evaluations for Emergent Inter-Model Manipulation in Agentic AI Systems

- Sprint: AI Manipulation Hackathon (ai-manipulation-hackathon-2026-01-09-to-2026-01-11)
- Rank: unranked
- Team: Team AgentRedline
- Authors: Alyssia J, Martin CL
- Date / location: Jan 11, 2026 / Toronto
- Page: https://apartresearch.com/sprints/projects/agentredline-propensity-evaluations-for-emergent-intermodel-manipulation-in-agentic-ai-systems-swnl
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/a163a0058cab2fac-sity_Evaluations_for_Emergent_Inter_Model_Manipulation_in_Agentic_AI_Systems.pdf
- Code: https://github.com/marn-in-prod/agent-redline-propensity-evals-inter-model-manipulation

## Summary

As AI systems increasingly operate in multi-agent configurations, including coding assistants delegating to tools and orchestration systems managing worker models, a critical threat emerges: AI models may spontaneously manipulate other AI models when doing so serves their objectives, without any human instruction.

We present AgentRedline, a propensity evaluation framework that deploys behavioral honeypots to measure whether orchestrator models spontaneously adopt manipulation strategies against worker models. Crucially, we never instruct models to manipulate; we observe whether it emerges organically when instrumentally useful.

We built evaluations across three manipulation types: (1) Policy Circumvention Delegation, where models attempt to get other models to perform refused tasks; (2) Emergent Jailbreak Transfer, where models independently discover known jailbreak techniques; and (3) Sycophancy Exploitation, where models exploit known AI vulnerabilities in other models.

Across 100+ evaluation runs built in UK AISI's Inspect framework on 5 model families (8 models), we observe orchestrators spontaneously employing: task decomposition to obscure harmful intent, context fabrication (claiming requests are for "simulations" or "Minecraft server hardening"), and conversation reset strategies when refused.

These findings suggest inter-model manipulation should be a standard component of pre-deployment evaluation for agentic AI systems.

Code access: Our evaluation suite is built using UK AISI's Inspect framework and includes implementations of jailbreaks and manipulation tactics. Given the sensitive nature of this work, we maintain the code we wrote this weekend in a private repository, but we're happy to provide access to judges upon request, and would welcome collaboration to develop a responsibly redacted open-source version. Contact alyssia-j@protonmail.com for repository access.

## Reviews (2)

### Review 1

I thought this was a genuinely novel, and looks like an important frontier for multi-agent safety (testing whether models spontaneously “manipulate” other models when it's instrumentally useful, without being instructed to do so). The observed strategies are very interesting to see (and especially the finding that models switch to more sophisticated tactics! yikes). The writeup was very interesting, though lacking in details.

I’m not quite sure if this is truly in scope for a “manipulation” hackathon (seems more like a general multi-agent safety project that isn't necessarily about humans per se?) but in any case I thought this seemed like a great direction and impressive work for a hackathon project. I would really like to see some specific examples of the model behaviors, and some actual quantitative results in the writeup (and a bit more description on methodology/prompts etc, even if you can’t make everything public)

### Review 2

Very conceptually novel and interesting. The results are potentially very interesting and impactful. It would be great to see more quantitative analysis and visualization of results.

While the methodology is strong in some ways (e.g. the use of the Inspect framework), 100+ runs across 5 model families, it was not always clear how ecologically valid the honeypot scenarios were, and it would be great to see more evaluation of the robustness of judge models.

Overall this is a great research direction which seems promising if implemented more fully and rigorously!

