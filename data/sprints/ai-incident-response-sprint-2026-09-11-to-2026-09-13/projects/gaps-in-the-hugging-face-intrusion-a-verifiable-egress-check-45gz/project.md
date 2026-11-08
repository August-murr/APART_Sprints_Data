# Gaps in the Hugging Face Intrusion & a Verifiable Egress Check

- Sprint: AI Incident Response Sprint (ai-incident-response-sprint-2026-09-11-to-2026-09-13)
- Rank: unranked
- Team: Team PhaseOne[Medium]
- Authors: Anirudh Venu
- Date / location: Sep 13, 2026 / Bengaluru
- Page: https://apartresearch.com/sprints/projects/gaps-in-the-hugging-face-intrusion-a-verifiable-egress-check-45gz
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/3fa5d6e15d74e9dc-5fb51ea4-266b-40c5-b62a-e7e6230c8ab5-Apart-Research-AI-Incident-Submission.pdf
- Code: https://github.com/anirudhvenu/egress-attestation
- Code links found in report: https://github.com/anirudhvenu/egress-attestation

## Summary

- Built a matrix of the Hugging Face intrusion: each gap, the control that closes it, whether it existed, was enabled, and could be verified from outside - Built a v1 egress attestation so a third party can check what an eval sandbox reached

## Reviews (2)

### Review 1

The verifiability question is the sharpest framing in this batch. Counting that 18 of 22 controls already existed, none were fully enabled, and only one could be checked from outside turns a known incident into a specific policy claim. The best moment is the "what did not work" section: logging only the sandbox edge passes this incident, because the escape went through a permitted door, so the proxy edge had to be added. That is a real finding from a negative result.

### Review 2

The existing/enabled/verifiable triple is a useful tool and provides a statement that a regulator can repeat: eighteen out of twenty-two of the controls were already in place, none of them was fully enabled, and one could be checked from outside. The most convincing result arose from a failure and therefore deserves to take precedence: logging only the sandbox boundary meets the requirements of this incident since the escape took place through a permitted door, meaning that the proxy's own exit is the one that is recorded. It was the correct decision to drop the proxy patch level for the same reason, and using a flow-log format that the labs have already used helps to keep adoption seem plausible. The repository is in fact better than the report suggests, and several of its contents should be included in the paper. The order of the checks is important and you give a reason for it: if a signature fails, the process exits right away and bypasses the boundary checks, since reporting on the contents of an unauthenticated manifest would give those contents a credibility they have not earned. The name of the scenario does not appear in any of the artifacts, so the conclusion is based on evidence and not on a label. The verifier never looks at the raw logs, only at what has been signed. The two tamper tests fail in two separate instances, one due to a hash mismatch and the other due to an invalid signature. In the sandbox_leak case your most powerful point is made in a single line three SSH connections rounding to 0.0 MB are detected because the rule is based on whether it is declared or not declared rather than on whether it is large or small, a criterion that a volume threshold would have overlooked. The limits remain the same: self-signing of the logs, which are controlled by the lab between capture and hashing, means that this is a format rather than 3P verifiability, and the transparency-log step in your future work is what changes that. Synthetic traffic with illustrative thresholds cannot support claims about abuse that remains below those thresholds. And each row in the matrix is a single retrospective judgment with one control per gap, so a second reviewer or a stated rule for 'Partly' would make the counts more defensible.

