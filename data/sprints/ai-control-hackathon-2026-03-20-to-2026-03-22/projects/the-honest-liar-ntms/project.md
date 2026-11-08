# The Honest Liar

- Sprint: AI Control Hackathon 2026 (ai-control-hackathon-2026-03-20-to-2026-03-22)
- Rank: unranked
- Team: Team the simpsons
- Authors: Amita Shukla
- Date / location: Mar 23, 2026 / Cambridge, MA
- Page: https://apartresearch.com/sprints/projects/the-honest-liar-ntms
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/c0218e67d9910ef8-7c99b78f-b256-4393-9a3f-f9f71dc0cb87-The-Honest-Liar.pdf
- Code: https://github.com/amitashukla/file_indexing/tree/straj-aggregate-query-poisoning
- Code links found in report: https://github.com/amitashukla/linuxarena, https://github.com/amitashukla

## Summary

This project implements a new control setting in LinuxArena in the file_indexing environment that is designed to demonstrate human decision sabotage, through the creation of a new main task and side task.

A misaligned LLM agent, tasked with building a financial performance analysis tool for a corpus of company records, can steer a downstream analyst toward a false investment decision by creating misleading statistics. The attack flips a simulated analyst's verdict from "do not invest" to "invest" while achieving a maximum monitor suspicion score of 0.5/10.

## Reviews (2)

### Review 1

In general the distinction between "high stakes control" and "diffuse control" is whether triggering the side task is "incriminating" - this is kind of a nebulous concept but can stand in for "smoking gun evidence of misalignment" or "very useful for hardening defenses" or some other things. I think the side task described here is pretty borderline - the attack described in 3.2 sounds pretty unlikely to happen by accident but it's not totally smoking gun.

In high stakes control we also like to make sure the side tasks are "catastrophic" - succeeding at a side task even once is very bad for the blue team. The side task described here doesn't sound very catastrophic but generally this is a looser requirement as long as the attack dynamics seem reasonable, and the attack dynamics here seem like they would be comparable to lots of "medium stakes research sabotage" that could be catastrophic.

FWIW I think this is basically a research sabotage threat model, despite the fact that "no code behavior is broken" - the code clearly produces misleading results even though it doesn't like error or crash or anything, I think that's a pretty central example of research sabotage.

I agree the attacker starting with omniscience about the paradox opportunity in the data is a bit of a weakness.

### Review 2

Easy to read, nice idea, haven't seen the Simpson's paradox applied to control, worth developing further!

