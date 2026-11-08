# Evaluation of Trusted Debate in LinuxArena

- Sprint: AI Control Hackathon 2026 (ai-control-hackathon-2026-03-20-to-2026-03-22)
- Rank: unranked
- Team: Team Evaluation of Trusted Debate in LinuxArena
- Authors: Jedrzej Konrad Kolbert, Travis Whitfield
- Date / location: Mar 23, 2026 / Copenhagen, Denmark and Washington DC, USA
- Page: https://apartresearch.com/sprints/projects/evaluation-of-trusted-debate-in-linuxarena-9g7s
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/7857395995562a64-uation-of-Trusted-Debate-in-LinuxArena---Apart-Research-hackathon-submission.pdf
- Code: https://github.com/s184361/linuxarena
- Code links found in report: https://github.com/s184361/linuxarena, https://github.com/linuxarena/linuxarena

## Summary

We investigated using Trusted Debate as a trajectory-level monitor in LinuxArena to identify agent trajectories which contained sabotage. Trusted Debate involves using a Defender and Critic model to argue whether a given trajectory contains sabotage before a Judge model provides a final suspiciousness score. In our limited experiments, we show that the Debate framework actually lowers monitor performance compared to a lower-cost baseline, with the Defender in particular muddying the water and confusing the judge. An ablation which replaced the Defender prompt with a simple deferral to the Critic response recovers performance to be competitive with the baseline, suggesting that the Defender actively degrades monitoring performance.

## Reviews (2)

### Review 1

Good analysis. I'm of the opinion that it's hard to justify Trusted Debate, since it's effectively a fancy monitor in a trench coat, and risks rigidity. Some minor critiques that come to mind:

- Perhaps the work would have been more interesting & novel if applied to the live, per-action setting.
- The conclusion's framing is a bit strong.
- It'd be good to clarify why the critic-only variant was provided such a different prompt than A / B variants. The critic>debate result could be purely due to a much better monitor prompt than the ones it is compared to.

Overall, truly impressive work.

### Review 2

Interesting approach with debate., worth publishing a negative result

