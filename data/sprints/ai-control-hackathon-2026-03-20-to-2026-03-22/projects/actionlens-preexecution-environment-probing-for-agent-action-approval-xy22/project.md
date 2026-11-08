# ActionLens: Pre-Execution Environment Probing for Agent Action Approval

- Sprint: AI Control Hackathon 2026 (ai-control-hackathon-2026-03-20-to-2026-03-22)
- Rank: 3
- Selected as: winner
- Awards: 3rd Place ($300)
- Team: Team Udbhav&Ashok
- Authors: Udbhav Chitransh, Ashok Kumar
- Date / location: Mar 22, 2026 / BENGALURU
- Page: https://apartresearch.com/sprints/projects/actionlens-preexecution-environment-probing-for-agent-action-approval-xy22
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/27c5805c04c96ebf-6257bb4a-bae9-438d-ae41-4ad2b5eeb46d-actionlens_paper_final-2-1-.pdf
- Code: https://github.com/udsea/actionlens
- Code links found in report: https://github.com/udsea/actionlens
- Presentation: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/4ad6744d680119c6-b0ff00dd-6d6f-4778-88e5-dcbfd6941a3b-PPT_ActionLens_AI_Control_-2--1.pdf

## Summary

ActionLens is a pre-execution control protocol for shell and file actions proposed by AI agents. Instead of approving an action from transcript alone, a trusted monitor gathers lightweight environment evidence before execution: target inspection, sensitivity scanning, dry-run simulation, diff preview, network-risk analysis, and short action history. On a deterministic 36-task benchmark (12 benign, 12 ambiguous, 12 stealth attacks), transcript-only monitoring fails on every attack while ActionLens blocks all 12/12 attacks and preserves perfect benign completion. On a 30-task slice imported from real BashArena task IDs, ActionLens again reduces attack success to 0.000 across all evaluated proposer models. A cross-environment ablation reveals that the dominant useful probe is not fixed: preview_diff matters most on native code-mutation attacks; sensitivity_scan matters most on BashArena-style security-surface attacks. Pre-execution control improves markedly when the monitor can inspect concrete side-effect evidence, but robust approval requires combining evidence channels rather than relying on any single probe class. A cross-family evaluation of Semantic Guard across 26 models (7 families) raises average Control Score from 0.844 to 0.943 with zero false positives; an adversarial evasion study confirms that deterministic probes and LLM monitors are complementary defenses.

## Reviews (2)

### Review 1

Strongest submission I've reviewed. The volume of rigorous evaluation here — 36-task native benchmark, 30-task BashArena transfer, ablation across probe types, 26-model cross-family evaluation across 7 families, plus an adversarial evasion study — is exceptional for a hackathon.

The core insight is sharp: transcript-only monitoring fails because the risk often isn't in the text, it's in what the action would actually do to the environment. Pre-execution probing (diffs, sensitivity scans, dry runs) gives the monitor evidence the transcript can't provide. The 0.000 vs 1.000 ASR gap between ActionLens and transcript-only on both benchmarks makes the point cleanly.

The adversarial evasion study is honest and well-designed. Crafting 6 attacks that bypass Semantic Guard by construction, then showing LLM monitors catch all 6 while o3-mini catches 0, directly establishes the complementary defense thesis. Neither deterministic probes nor LLM monitors alone are enough — that's a useful takeaway for anyone building control protocols.

The ambiguous-task usefulness cost on BashArena (ACR dropping to 0.250) deserves attention — that's where real deployment friction would show up. The paper reports it honestly but doesn't explore threshold tuning to recover some of that.

Excellent work across the board.

### Review 2

They probe the actual environment before anything runs instead of just reading what the agent says. Check target files, simulate commands, preview diffs, look at network risk. Transcript only monitoring missed every stealth attack, ActionLens caught all of them with no false positives. For 6 pages the amount of evaluation is kind of crazy. 36 task benchmark, BashArena transfer, 26 model sweep, adversarial evasion analysis. They found which probe matters most changes by task type, which is a useful non-obvious insight. Confidence intervals reported, code public. Hard to criticize for a hackathon project.

