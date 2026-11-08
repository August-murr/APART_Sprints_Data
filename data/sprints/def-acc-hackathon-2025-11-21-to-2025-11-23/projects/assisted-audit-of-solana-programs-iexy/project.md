# Assisted Audit of Solana Programs

- Sprint: Defensive Acceleration Hackathon (def-acc-hackathon-2025-11-21-to-2025-11-23)
- Rank: unranked
- Selected as: sample_reviewed
- Team: Team GLAM
- Authors: Yuru Shao, Emanuele Cesena
- Date / location: Nov 23, 2025 / San Francisco
- Page: https://apartresearch.com/sprints/projects/assisted-audit-of-solana-programs-iexy
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/cc8ed0d4c703ff05--40c6-8b12-510675ee5031-def_acc-Hackathon_-Assisted-Audit-of-Solana-Programs.pdf
- Code: https://github.com/yurushao/solana-program-auditor
- Code links found in report: https://github.com/switchboard-xyz/solana-sdk
- Recording: https://docs.google.com/presentation/d/1RDezPI4BD60A6oYnqlgh-21bXpuDbM9eSQW7pD_1Zsg/edit?usp=sharing

## Summary

Multi-agent solution that assists in auditing Solana programs, allows to consolidate audit findings into a knowledge base, and can integrate into CI/CD pipelines to prevent security regressions.

## Reviews (1)

### Review 1

Strengths: This is a rare example of AI and blockchain that truly makes sense together. Scaling security audits for high-value smart contracts is a present problem, and the multi-agent architecture is well-designed for it. The Librarian Agent for cross-program dependency tracking is the highlight. Solana programs constantly interact with external protocols, and vulnerabilities often live in those interaction layers. Building infrastructure that maintains versioned external references and flags upstream changes is genuinely useful. Finding 3 additional vulnerabilities beyond the original audit scope validates the approach.

Suggestions: Coverage is the obvious next step. Six agents based on six audit findings is a (definitely solid) proof of concept. From here, a production system needs broader vulnerability class coverage. The framework is strong; now it needs scale.

Bottom line from a Halcyon Ventures investor: Rather than crypto for crypto's sake, or AI for AI's sake, I really liked this team’s sound usage of intelligent systems for auditing high-financial value smart contracts. The real-world application of securing against financial losses in an increasingly decentralized world came across sharp, sound, and necessary. There was clear first-principles thinking in what the team needed to orchestrate / bring to life in its multi-agent system. The team’s attention to posture management software limitations was honest and accurate: that it historically only focuses on a moment in time/is not dynamic. We need more defensive AI security that understands the unique needs of financial markets (and their future) - well done for pioneering this!

