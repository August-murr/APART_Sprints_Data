# ODRArena: Rigorously Evaluating Deep Research Control Policies

- Sprint: AI Control Hackathon 2026 (ai-control-hackathon-2026-03-20-to-2026-03-22)
- Rank: unranked
- Team: Team CBAI
- Authors: Henry Castillo, Kaley Brauer, Claudio Mayrink Verdun, Maximus Rafla, Adeeb Zaman, Erik Nordby, Elizabeth Pavlova
- Date / location: Mar 23, 2026 / Cambridge
- Page: https://apartresearch.com/sprints/projects/odrarena-rigorously-evaluating-deep-research-control-policies-mgzr
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/8d768ff9a1437105-147c20ea-a6bf-419c-93db-4d3b7f4886d7-control-hackathon-ideas.pdf
- Code: https://github.com/d0rbu/control-hackathon
- Code links found in report: https://github.com/d0rbu/control-hackathon, https://github.com/UKGovernmentBEIS/control-arena, https://github.com/langchain-ai/open_deep_research

## Summary

Deep research agents have become the bread and butter of professionals performing high-level and high-stakes knowledge work, representing an attractive opportunity for attackers to scale their impact by stealing sensitive information and compromising critical systems through prompt injection attacks. To model this class of threats and defenses, we develop ODRArena, a control setting built on Open Deep Research to facilitate blue and red-teaming efforts in realistic deep research scenarios. We provide a black-box and a white-box setting, emulating open-source systems and closed-source products such ChatGPT Deep Research. With our initial red-teaming efforts, we find deep research agents to be robust to prompt injection attacks due to the multiple rounds of summarization and compression in the deep research pipeline.

## Reviews (2)

### Review 1

- The scale of experimentation may be a little thin : The experiment involves the use of 25 GAIA questions, with single epoch and primary model pairing. The team is transparent about the compute constrains though, but maybe a phrase such as "emergent robustness" is carrying a lot of weight right now
- The zero percent across every condition is kind of interesting. Is the deep research architecture actually robust?
- The four injection techniques are all different types of content injection. It maybe worth trying multi-turn attacks or attacks that exploit the specific nature of GAIA questions

### Review 2

This contribution tackles the threat of prompt-injection and misaligned behavior in a deep-research setting from a control viewpoint. They frame it as a high-stakes control problem with two types of side tasks: secret exfiltration (via url calls) and output poisoning (effectively spread of misinformation).

They make a strong finding of 0% red-team success in a variety of scenarios, to which one may reasonably object that their red-teaming wasn't strong enough. For example, it appears that the canary was only mentioned in passing in the provided "poisoned" snippets, while one could imagine an attacker presenting it as a central entity relating to some fact. In another direction, the use of more advanced jailbreaking techniques would have also been interesting to see.

It also remains a bit unclear for which types of attacks U is assumed to be misaligned itself, or simply subject to prompt injection - this could be separated and explained better. In the same vein, it is not clear in what sense the trusted model T behaves differently to U.

