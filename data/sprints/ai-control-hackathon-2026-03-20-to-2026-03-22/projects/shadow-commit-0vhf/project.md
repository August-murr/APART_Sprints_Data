# Shadow Commit

- Sprint: AI Control Hackathon 2026 (ai-control-hackathon-2026-03-20-to-2026-03-22)
- Rank: unranked
- Selected as: sample_reviewed
- Team: Team G0ldenBear
- Authors: Yash Thapliyal
- Date / location: Mar 23, 2026 / Berkeley
- Page: https://apartresearch.com/sprints/projects/shadow-commit-0vhf
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/149c65f299d5bae0-b74e79d2-a161-4e61-befb-ce514ccd6267-ShadowCommit---Technical-Report.pdf
- Code: https://github.com/YashDThapliyal/ShadowCommit
- Recording: https://youtu.be/C2fOV8-JnVI

## Summary

AI agents lie. ShadowCommit catches them.

When an untrusted AI agent proposes a bash command, it also submits a signed commitment: "I will only touch these files, read no secrets, make no network calls." ShadowCommit runs the command in an isolated shadow copy of the environment, measures what actually happened, and compares the two. If the agent lied, the command is blocked before it ever touches the real environment.

## Reviews (2)

### Review 1

Summary: The project aims to prevent malicious attacks (bash commands) by (1) getting agents to make commitments about commands that are run and its consequences (e.g., which files will be modified) and (2) executing the command in a sandbox environment and comparing the commitment to the actual effects of the command in the sandbox. This protocol outcompetes text monitoring on malicious commands that have been obfuscated.

Strengths: I like the protocol of commitment + validation --- I believe it's novel and interesting! The report is also really well presented and complete.

The main limitation seems to be the performance. So far the protocol has to run every command in a sandbox which is unrealistically costly. A good cost analysis could help. Additionally, I think text monitors could be improved substantially (e.g., by prompting the monitor to flag commands that it does not understand).

### Review 2

Good idea overall, but without sys-call level observation it's going to be hard to provide anything but a false sense of security.

