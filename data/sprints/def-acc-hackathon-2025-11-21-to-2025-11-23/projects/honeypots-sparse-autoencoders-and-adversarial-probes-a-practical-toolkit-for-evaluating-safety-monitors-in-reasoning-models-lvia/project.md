# Honeypots, Sparse Autoencoders, and Adversarial Probes: A Practical Toolkit for Evaluating Safety Monitors in Reasoning Models

- Sprint: Defensive Acceleration Hackathon (def-acc-hackathon-2025-11-21-to-2025-11-23)
- Rank: unranked
- Team: Team One Man Army
- Authors: Subramanyam Sahoo
- Date / location: Nov 23, 2025 / India
- Page: https://apartresearch.com/sprints/projects/honeypots-sparse-autoencoders-and-adversarial-probes-a-practical-toolkit-for-evaluating-safety-monitors-in-reasoning-models-lvia
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/a5203dd7f637655d-e1-81e6-4033-8ba1-856f83a7b0b6-Honeypots_SAEs_and_Adversarial_Probes_Toolkit.pdf
- Code: https://github.com/SubramanyamSahoo/SentinelGym---A-defensive-Project

## Summary

SentinelGym is a unified defensive AI system that combines honeypot-based vulnerability injection, GRPO safety finetuning, sparse-autoencoder mechanistic interpretability, and adversarial probe evaluation to test and harden code-generating language models against AI-enabled cyber threats. By injecting synthetic vulnerabilities, auditing internal representations through SAEs, and stress-testing linear probes with adversarial red-team strategies, SentinelGym exposes both behavioral and mechanistic failure modes—such as collusion, unsafe reasoning, and probe brittleness—that traditional evaluations miss. The result is a practical, reproducible framework that strengthens the defensive “shield,” enables early detection of harmful internal model behaviors, and demonstrates measurable improvement in secure coding patterns after finetuning, directly advancing the core goals of defensive acceleration.

## Reviews (2)

### Review 1

This is a highly ambitious hackathon project attempting to combine several directions. Thank you for your hard work - you got a lot done in a short space of time.

I think this could be improved in three main ways:

1. Greater focus on integration of the different methods. The methods were not fully integrated in the code and there weren't results on what the methods add *in combination*. The ambition was to combine the methods, because each was insufficient, but you weren't able to show that the combined approach performed well (despite several interesting results from individual methods).
2. Clearer prioritisation of results and explanation of limitations. The paper was challenging to read as there were so many results and sometimes not a lot of information about experimental setup. In some cases, significant limitations weren't explained in detail, e.g. that GRPO training did not same to reduce training loss. The Discussion at the bottom of the paper was hard to follow as it focused on individual results rather than the overall promisingness of combining the approaches / it was hard to know exactly what to take away from this work.
3. Focus on fewer elements based on what works. To enable (1) and (2), I would focus on a smaller number of techniques.

The central idea of integrating different safety tools seems promising, but is not especially novel. What would be great to see is results based on a (more limited) combination of these techniques, perhaps with measurements of the individual contribution of each technique to the overall improvements when all the techniques are implemented together.

### Review 2

Team really seemed to capture the spirit of this hackathon. SentinelGym shows potential, but may be spreading itself too thin. For a low-stakes hackathon just trying to introduce participants to the idea of developing with code-model defense in mind, the team put together a great prototype / demo.

I worry that a “professional” version of this toolkit might fall short in certain areas and give developers a false sense of security. Instead of independently developing every defense component, SentinelGym could focus on integrating the most mature existing tools and directing effort toward strengthening a smaller set of high-value defenses. This would reduce maintenance burden and produce a clearer, more reliable toolkit that developers can confidently rely on.

It may also help to clarify the primary intended users and deployment environments so future work can prioritize evaluation that reflects real defensive needs. I'd like to see more explicitly outlined connection to specific threats. Establishing clearer success metrics would help ensure that the toolkit improves outcomes rather than just increasing system complexity.

