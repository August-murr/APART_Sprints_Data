# Axiom Zero: AlphaZero-Style Reinforcement Learning for Automated Formal Verification of Python Programs

- Sprint: The Secure Program Synthesis Hackathon (secure-program-synthesis-hackathon-2026-05-22-to-2026-05-24)
- Rank: unranked
- Selected as: sample_reviewed
- Team: Team Axiom_Zer0
- Authors: Mufaro Rukuni, Brain Monzora
- Date / location: May 24, 2026 / Cape Town
- Page: https://apartresearch.com/sprints/projects/axiom-zero-alphazerostyle-reinforcement-learning-for-automated-formal-verification-of-python-programs-aqr7
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/e49d9f0a5f158029-190a6ea8-18ed-49ce-8e0e-a891d16f5a32-axiomzero.pdf
- Code: https://github.com/Mufarosean89/axiomzero2.0/tree/webapp
- Code links found in report: https://github.com/Mufarosean89/axiomzero2.0

## Summary

The rapid growth of AI-generated code has created a verification crisis: Gross World Lines of Code (LoC) is expanding at unprecedented rates, yet developers have no systematic guarantee that the code produced by large language models behaves as intended. We present Axiom Zero, a compiler and reinforcement learning system that translates Python/PyTorch source code into formal proofs verified by the Lean 4 proof assistant, using an AlphaZero-style agent to discover those proofs automatically without human-labelled examples. The system comprises four implemented phases: (1) a parse pipeline that converts Python source into a normalized intermediate representation with type and tensor-shape analysis; (2) a proof environment modelling theorem proving as a two-player game with 39 curated tactics across 10 categories; (3) a policy-plus-value network with MCTS tree search trained via self-play; and (4) a Python-to-Lean 4 compiler with difficulty-stratified proof-hole filling. All 143 unit tests pass across 3,450 lines of dependency-free Python. The Lean 4 kernel serves as the binary oracle: a proof either compiles or it does not, providing a clean reward signal that eliminates the need for human annotation. Axiom Zero demonstrates that the game-theoretic self-play paradigm, previously applied to chess and Go, can be transferred to the domain of program verification, offering a scalable path toward trustworthy AI-assisted software development.

## Reviews (2)

### Review 1

The write-up for this project was clear, well-polished communication. I would be very interested to see the results of Phase 5, which are ongoing. The 3.5 design decisions all seemed appropriate and improved usability. The test suite had good, relevant and broad coverage.

I was not convinced by claim of 'isomorphism' or even substantial similarity to superhuman Go via self-play - the prover and kernel do not coevolve, and this approach is more aptly described as an expert iteration / single-agent search method.

I think limiting it to Lean 4 is basically fine.

### Review 2

This is a very ambitious project and it's great to see the authors got very far! A larger evaluation with more test cases would be useful next -- and, ideally, the authors would verify the correctness of their translation steps.

