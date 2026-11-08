# Proof Assistance as Verification Oracle for Porting

- Sprint: The Secure Program Synthesis Hackathon (secure-program-synthesis-hackathon-2026-05-22-to-2026-05-24)
- Rank: 3
- Selected as: winner
- Awards: 3rd Place ($300)
- Team: Team Vajrapani
- Authors: Abhinav Chand, Balaji R
- Date / location: May 24, 2026 / India, United States
- Page: https://apartresearch.com/sprints/projects/proof-assistance-as-verification-oracle-for-porting-ma88
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/af4b3a28e317ae77-6f784d3c-52fd-4c15-b29b-7d3628b8665d-SPS-Hackathon-Apart-Research.docx.pdf
- Code: https://github.com/poonai/formal-verification-oracle

## Summary

This project tests a formal-verification harness on Anthropic’s Bun rewrite work, where AI-generated Rust ports are checked against their original Zig implementations. The harness translates Rust into Dafny, extracts behavioral theorems from Zig, and attempts to prove those theorems against the Rust-derived model. In practice, this produced real verifier failures that exposed real bugs, showing that proof-driven auditing can help make AI-generated software ports more trustworthy.

## Reviews (2)

### Review 1

Thank you for this great work. Very impressed by the real-world results of two bugs reported (and merged!) in the production code (!!) of a major open-source project.

Super-relevant for oh-so-common software replattforming projects.

I'd recommend including specific examples from your experiment runs in the results section, and potentially some stats on theorems derived, proof successes / failures, etc, to illustrate the process.

The discussion section mentions the alignment problem, which in general is relevant, but does not tie into the rest of your write-up from what I can see.

### Review 2

By far my favorite among the projects I reviewed. Thanks for a well-thought-out tool constructed quickly!

The interesting thing about this project is, as its title alludes to, using relatively heavyweight formal-methods tooling to augment what is really just systematic testing, in that no formal guarantee of correctness follows, but we may nonetheless find bugs missed by more-traditional testing. Indeed, the handful of real bugs reported against Bun is the high point of this project, showing genuine impact.

I do still see something of a Frankenstein's-monster flavor to the project. The translation into Dafny is somewhat arbitrary; using a native Rust verification tool makes more sense, though probably those tools aren't as mature as Dafny. Perhaps more importantly, the translation is done with Claude Code, which adds further "buyer beware" cautions that shouldn't leave us with particularly more confidence than just asking Claude Code to audit the Rust code directly.

The approach also depends on asking Claude Code to audit Zig code and identify properties worth preserving into Rust. I don't have high confidence that such a process will be very comprehensive. However, the authors found real bugs, so they should get credit for demonstrating genuine utility.

