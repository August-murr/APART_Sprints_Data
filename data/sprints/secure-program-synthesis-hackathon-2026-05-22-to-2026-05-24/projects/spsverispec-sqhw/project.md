# SPS-VeriSpec

- Sprint: The Secure Program Synthesis Hackathon (secure-program-synthesis-hackathon-2026-05-22-to-2026-05-24)
- Rank: unranked
- Selected as: sample_reviewed
- Team: Team SPS-VeriSpec
- Authors: Zheng Wangyuan
- Date / location: May 25, 2026 / Boston
- Page: https://apartresearch.com/sprints/projects/spsverispec-sqhw
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/17b26e38ed6758c1-e01e7602-0a20-422c-bb52-42883acc17f0-Apart-Research-hackathon-submission.pdf
- Code: https://github.com/patrickZWY/SPS-VeriSpec
- Code links found in report: https://github.com/patrickZWY/SPS-VeriSpec, https://github.com/codeforboston/CutePetsBoston, https://github.com/konradhalas/dacite, https://github.com/huggingface/transformers, https://github.com/plast-lab/doop

## Summary

We implemented a complete pipeline from Python program to Datalog properties to test cases.

## Reviews (2)

### Review 1

I think it's a great idea to use Datalog-powered analysis for program understanding to create test cases, but the story of this tool doesn't hang together for me yet.

First, in the setting of secure program synthesis, why is it helpful to analyze a program to generate tests for it? Don't such tests merely reinforce the bugs already present in the program, sometimes perversely requiring that buggy behavior be replicated in later versions? I don't understand how Figure 1 can be seen as providing empirical evidence that the tool is useful, since it is trivial to generate test cases that a given program passes, if only by rejection sampling.

Second, the report is unclear on how Datalog analysis results are used to generate test cases. The report acknowledges that analysis so far mostly covers program structure rather than dynamic behavior, so where do useful tests even come from? Should we expect scalability of the underlying program analysis to much larger programs?

### Review 2

This projects has a mutation harness with named operators and it reports comparative kill rates, but most of the work is only in the repo and doesn't make it into the paper.

SPS-VeriSpec's three-tier scheme (most restrictive properties become unit tests, mid-range become hypothesis property-based tests and open/risky ones go to a manual-review report) makes sense as an organizing idea, and the pipeline is implemented across three targets of increasing difficulty .

The related-work section is candid that none of the components are new, and the literature is cited properly. A good design instinct is to set LLM-proposed rules and oracles as provenance-tainted review candidates, which is a right posture for secure synthesis.

A promising next step is the one the author identifies, which is to close the loop so that when a generated test fails, the Datalog relation that produced it is surfaced for a human to accept, reject, or refine, with the decision persisted into the next analysis round, turning the current one-way pipeline into an iterative formal/informal loop. Curious what metrics for grounding come out of this.

