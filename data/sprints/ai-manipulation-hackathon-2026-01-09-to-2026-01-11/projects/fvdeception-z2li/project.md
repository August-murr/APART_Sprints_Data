# FV-Deception

- Sprint: AI Manipulation Hackathon (ai-manipulation-hackathon-2026-01-09-to-2026-01-11)
- Rank: unranked
- Selected as: sample_reviewed
- Team: Team Leeeeee
- Authors: Lee Wall
- Date / location: Jan 12, 2026 / Philadelphia
- Page: https://apartresearch.com/sprints/projects/fvdeception-z2li
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/cc72276507a027c8-2ffce87f-feac-422e-9b6a-744405e82852-FV-Deception.pdf
- Code: None

## Summary

I ran a set of experiments to see if frontier LLM's could intentionally generate formal verification specs that slightly diverge from the natural-language semantic intent, and whether other models could reliably catch this divergence.

## Reviews (2)

### Review 1

I am not familiar with the literate on FV, but from what I (+Claude) can tell after digging around there is very little existing work done on this specific problem, and it seems like very important work for the FV field to me. For me this was in shot for a top score on impact if the conclusions were more explicit - what is the so what? What does this really mean and what do we now need to do? It seems like you are very thoughtful about this space, and I was eager to see more of your thinking and takes!

The execution had room for improvement. The sample size is quite small. The methodology mentions 9 combinations of model attacker/defenders, but only the data and conclusions on using Opus as an attacker was discussed. No analysis of successful / unsuccessful attempts at attacks. I found it hard to really have faith in the (important!) conclusions with these limitations.

The things that the report communicates are all clean. You know how to write clearly. Well written and argued. I would have liked to see more detail and coverage of the data and experiments that were done.

I hope you continue with this area of work.

### Review 2

Targeting deception in formal specifications is a valuable and neglected direction. The finding that Opus catches fewer of its own bugs than Sonnet is interesting, and I'd like to see whether this replicates with a larger attacker-defender capability matrix. Including concrete examples of deceptive specifications would also help readers interpret what's actually happening.

