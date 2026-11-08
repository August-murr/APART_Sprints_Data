# Report bounties redirect research swarm to auditing once solving stalls

- Sprint: AI Incident Response Sprint (ai-incident-response-sprint-2026-09-11-to-2026-09-13)
- Rank: unranked
- Team: Team DeepBrain
- Authors: Shawn Shen, Neil Prabhu, Thiv Tharmarasa, Anshuman Nautiyal, Harishan Ramanan
- Date / location: Sep 14, 2026 / London
- Page: https://apartresearch.com/sprints/projects/report-bounties-redirect-research-swarm-to-auditing-once-solving-stalls-ztsg
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/9cf6454f6bbc9305-a2b7-Report_bounties_redirect_research_swarm_to_auditing_once_solving_stalls.pdf
- Code: https://github.com/syqgenesis/Research-Swarm-Behavoiur-Study

## Summary

The Hugging Face incident began when agents were given tasks that were close to impossible, and resorted to exploiting the scorer. We set up a similar swarm and tested whether giving agents a bounty for reporting changes their exploit uptake, or how they split their effort between solving and auditing. We ran Twenty-five DeepSeek-V4-Flash agents for 90 minutes on 20 planted-solution NP-search problems with a shared library and messaging. Agents were split into groups with different report bounty. Ten had no report bounty, and the remaining 15 were split into five, each having 5, 10 or 15 points per valid report, against 50 for a solution. No exploits were submitted, and auditing for bounty appeared once solving stalled; all 13 of those audits came from bounty agents.

## Reviews (2)

### Review 1

I really like the idea of this project. i think the authors laid it out very clearly, made good design decisions, nd relayed their conclusions fairly. I would've been interested in seeing how adding bounties changes things when agents actually cheat. I'm also a bit worried that the way the bounties are given isn't that realistic and that the models (or more powerful models) would be eval-aware enough to notice.

Overall I would be excited for the authors to do more work in this direction. E.g. maybe recreating a version of the ExploitGym incident and running ablations to see how different bounties affect behaviour.

### Review 2

This paper investigates how economic incentives shape behavior in collaborative AI research swarms, specifically testing whether report bounties encourage agents to audit peer solutions when primary problem-solving stalls. By running 25 autonomous agents across 20 NP-search problems with varying bounty levels, the authors discovered a clear behavioral shift: reward-motivated auditing only emerged late in the session after easy problems were exhausted and solving became difficult. Interestingly, while zero-bounty agents inspected code solely for learning, non-zero bounties successfully catalyzed peer auditing across diverse problem domains. This is a creative and timely contribution to multi-agent governance and safety oversight.

