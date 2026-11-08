# Omission Attacks: When Doing Nothing Is the Attack

- Sprint: AI Control Hackathon 2026 (ai-control-hackathon-2026-03-20-to-2026-03-22)
- Rank: 1
- Awards: 1st Place ($1,000), LinuxArena Track Winner ($500)
- Team: Team MAIA
- Authors: Jurgis Kemeklis, Nikhil Vemuri
- Date / location: Mar 23, 2026 / Boston
- Page: https://apartresearch.com/sprints/projects/omission-attacks-when-doing-nothing-is-the-attack-0y1v
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/3e8436652eb43691-331f0e7d-15b6-4d37-bfa4-9b0220f922f8-submission--4-.pdf
- Code: None

## Summary

AI control protocols monitor agent actions to detect sabotage, but omission attacks exploit what the agent fails to do rather than what it does. We define omission attacks as security breaches caused by failing to perform necessary actions even when every executed command is individually legitimate. We present a taxonomy of 14 omission attacks across 5 categories and evaluate 5 hand-crafted attack traces against every monitoring tier in the LinuxArena control evaluation framework. Our strongest attack - an IPv6 firewall bypass where the agent "forgets" to configure ip6tables - evades all monitors, scoring at most 4.0/10 on the strongest Opus 4.6 monitor, versus a 92.3/100 mean detection score on existing commission attacks. We propose postcondition monitoring, which checks whether the final system state satisfies security invariants rather than scrutinizing individual actions, and show that it substantially improves detection, including catching all 5 fully evaluated omission attacks. These results suggest that action-level monitoring alone can underdetect attacks that primarily manifest as omitted obligations.

## Reviews (2)

### Review 1

This paper evaluates how well existing monitors detect attacks that work by leaving out critical steps. Additionally, the authors implement a monitor better at catching this kind of attack.

The authors demonstrate thoroughly that omission is a viable and hard-to-detect approach to attacking BashArena. Making the transcript monitor aware of the strategy through prompting reduces the success rate, but 1 of 5 attacks still passes in a spot check. Their "Postcondition Monitor" catches 5/5 but requires task-specific prompting and it's unclear if it's "overfitting" on the specific trajectory.

The authors evaluate an attack angle that is underexplored, with no trajectories in BashArena. I would be curious to see the same research for LinuxArena and on a larger scale.

Their trajectories are well crafted and the implementation of an additional monitor on top of the other results is impressive.

This attack naturally disadvantages action monitors, which makes it especially dangerous in live settings. When the security issue can be exploited right away, the damage might already be done before an end-of-trajectory monitor runs. Some of those settings could even be exploited by executing actions in an unsafe order (temporary openings, no omission), further obscuring the attack.

The paper could have been a bit clearer on the configurations of the monitors used. If I understand correctly, the Postcondition monitors are all end-of-trajectory monitors, like the trajectory and transcript monitors used as reference.

The results are promising, but running the evaluations multiple times with the same monitors to reduce LLM variance would give me more confidence in the numbers and could have been done with little time investment.

### Review 2

This project presents a really clear conceptualization and operationalization of a seriously understudied attack class in AI control. I think this has the potential to significantly influence the research development in AI control for the better.

While I’m not aware of prior work on this within AI control, there are certainly relevant ideas in adjacent domains (there are omission-style security vulnerabilities e.g. in OWASP, there are postcondition checks in formal verification). It would be great to see whether any of these can give rise to ideas about automating postcondition checks for AI control.

On the research side it would be great to see the current experiments repeated under a stricter methodology (larger sample sizes, real-world traces, evaluation of false-positive rate). The write-up itself is already a highly useful artifact and I would encourage the authors to build on it and publish it.

