# JARE: A Differential-Testing Workbench for Auditing AI-Generated Specifications

- Sprint: The Secure Program Synthesis Hackathon (secure-program-synthesis-hackathon-2026-05-22-to-2026-05-24)
- Rank: unranked
- Team: Team JARE
- Authors: Allenna Tang, Jerry Chen, Elizabeth Kourbatski
- Date / location: May 25, 2026 / Montreal
- Page: https://apartresearch.com/sprints/projects/jare-a-differentialtesting-workbench-for-auditing-aigenerated-specifications-o86j
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/cd07f4e92156455b-2c1b2987-dc99-4f6a-96d2-1e15a713a5f9-SPS_Hackathon_Report--1-.pdf
- Code: https://github.com/Lil-Chen05/jare
- Code links found in report: https://github.com/Lil-Chen05/jareDemo
- Recording: https://youtu.be/IYGFNyGrCic

## Summary

JARE is an auditing tool for AI-generated software specifications. When an AI writes both the rules a program should follow and the tests that check those rules, the tests can pass even when the rules are wrong. JARE finds concrete examples where an AI-generated specification disagrees with what the developer actually wanted, so a human can review and fix it.

## Reviews (2)

### Review 1

I'm afraid I can't spot a way that the proposed functionality is at all useful in program synthesis, vs. in carrying out evaluation of synthesis tools. The approach assumes collateral that would be very useful in the hands of an AI generating specs, yet the collateral is held out and only applied after generation.

One proposed usage mode is comparing a generated spec against a known-good spec. But if you have a known-good spec, why are you using AI to generate a spec from scratch, given just a natural-language description? Shouldn't the AI at least be shown the known-good spec, too?

Another proposed usage mode is evaluating generated specs against labeled test cases. Again, test cases are extremely useful to agentic AI-coding tools, so why aren't you sharing them?

Regardless of which scenario we focus on, the proposed functionality seems to follow standard practice in systematic testing, with no new conceptual contribution.

### Review 2

Promising experiments in a useful direction. One improvement could have been to compare different models in a multi-model setting: because eg ChatGPT and Claude are trained on different data, they can to some degree compensate for each others weaknesses, which may help significantly improve results in the no-gold deployment setting.

