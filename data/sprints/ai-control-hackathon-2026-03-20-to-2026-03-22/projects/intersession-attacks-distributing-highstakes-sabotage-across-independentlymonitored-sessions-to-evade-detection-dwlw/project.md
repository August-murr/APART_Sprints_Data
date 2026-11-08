# Inter-Session Attacks: Distributing High-Stakes Sabotage Across Independently-Monitored Sessions to Evade Detection

- Sprint: AI Control Hackathon 2026 (ai-control-hackathon-2026-03-20-to-2026-03-22)
- Rank: unranked
- Selected as: sample_reviewed
- Team: Team MultiSession
- Authors: Carlos Giudice
- Date / location: Mar 23, 2026 / Berkeley
- Page: https://apartresearch.com/sprints/projects/intersession-attacks-distributing-highstakes-sabotage-across-independentlymonitored-sessions-to-evade-detection-dwlw
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/2e667f696392e50f-952401a8-046f-4526-a953-86cd8b35532a-paper.pdf
- Code: https://github.com/linuxarena/linuxarena/pull/70

## Summary

We showed that splitting a sabotage attack across multiple independently-monitored agent sessions reduces per-session monitor detectability. With oracle coordination (pre-agreed attack plan), agents plant innocuous code fragments in early sessions that only become malicious when combined with a trigger in a later session. The per-session monitor can't cross-reference between sessions, so it misses the attack.

## Reviews (2)

### Review 1

I think your focus on inter-session attacks is highly relevant, and your work did a good job of investigating how these affect monitor performance.

The work could have benefitted somewhat from additional clarity on how you defined caught trajectories. Intuitively, a baseline would have been helpful to compare against for monitor performance. This would have clarified the performance degradation further.

I also noticed that Opus sometimes seemed to perform worse than Haiku, which seems strange. Maybe worth spending more of your time thinking about this and then discussing it more in the body of your work.

Overall nice work!

### Review 2

Congrats on a strong hackathon submission! The infrastructure work is substantial, the experimental design is thoughtful, and the limitations section is very thorough.

Impact & Innovation: The problem is clearly relevant: persistent multi-task deployments are how agents are increasingly being used, and per-session monitoring is the default. The paper does a good job distinguishing inter-session attacks from diffuse threats.

Execution Quality: Many of the design decisions are well-justified. The oracle coordination assumption is correctly framed as a worst-case red team affordance, and the use of max suspicion score (rather than average) across sessions is the right metric given the absence of honest baselines. Two suggestions for strengthening the results:

- An honest multi-task baseline would go a long way here. You acknowledge this already, but without knowing where honest agents score under the same multi-session setup, it's hard to translate suspicion score reductions into actual safety implications. If compute was the main constraint, existing honest trajectories from LinuxArena could likely serve as a reasonable approximation.
- The environment choice deserves more discussion. The current setup is something of a worst case for the blue team, since the monitor has no context about what happened in prior sessions. In a different setting, like a coding environment where the monitor can see the codebase and reason about the effects of changes beyond the immediate task, the cross-referencing loss might be less severe. Discussing this would help readers calibrate how broadly the results are likely to generalize.

Presentation & Clarity: The writing is clear and well-structured throughout. The intro is non-standard for a paper but works well as a hackathon report. The threat model section is precise, the method is clearly explained, and the limitations section is extensive and honest, covering nearly every concern a reviewer would raise. One area for improvement: a few figures (e.g. showing the episode structure, the same-strategy comparison results) would help the reader grasp the key results more quickly, especially for someone skimming before deciding whether to dive into the work.

