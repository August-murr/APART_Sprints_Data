# Veridict

- Sprint: The Secure Program Synthesis Hackathon (secure-program-synthesis-hackathon-2026-05-22-to-2026-05-24)
- Rank: unranked
- Team: Team ZKred
- Authors: Sumit Vekariya
- Date / location: May 24, 2026 / Vadodara
- Page: https://apartresearch.com/sprints/projects/veridict-e67q
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/c38781c1715f60e3-96009648-6f71-4ac0-b709-924055991416-Veridict-Submission.pdf
- Code: https://github.com/Zkred/veridict
- Code links found in report: https://github.com/Zkred/veridict
- Recording: https://youtu.be/Piy6H8nnB8U

## Summary

Veridict is a merge gate for AI-synthesized code that decouples qualified-reviewer-ness from identity. A natural-language spec is sent to Claude, which generates an implementation, a pytest suite, and a Z3 invariant file. The issuer mints a Longfellow ZK credential only after all three formal layers pass, and N anonymous proofs from credentialed reviewers flip the GitHub branch-protection gate that authorizes the merge. Built end-to-end on a live public repo with active branch protection; same Google ZK primitive used for anonymous age verification on mobile driver's licences, repurposed for code review.

## Reviews (2)

### Review 1

While the GitHub integration and overall user experience are well executed, the core AI security design needs more work to be done. The current Z3 check only validates that the specification is internally consistent; it does not prove that the generated Python code actually follows that specification. This leaves room for incorrect or even malicious code to pass review. In addition, the trust model around zero-knowledge proofs is weakened by server-side key generation and the absence of nullifiers, which could allow duplicate or spoofed approvals. Strengthening the system would require true code-to-spec verification and moving all ZK proof generation fully to the client side.

### Review 2

This is a cool project and very timely. My main feedback would be that this could be better integrated with Git (as opposed to GitHub) and existing infrastructure like Sign-offs. Anyways, this is good work.

