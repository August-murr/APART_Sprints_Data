# TCB-Expansion Attacks on Lean 4 and the LLM Proof Reviewers That (Mostly) Miss Them

- Sprint: The Secure Program Synthesis Hackathon (secure-program-synthesis-hackathon-2026-05-22-to-2026-05-24)
- Rank: unranked
- Team: Team 501st Lean-gion
- Authors: Juliet Meza
- Date / location: May 25, 2026 / New York
- Page: https://apartresearch.com/sprints/projects/tcbexpansion-attacks-on-lean-4-and-the-llm-proof-reviewers-that-mostly-miss-them-o3hn
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/1c416d9c00f77cff-ansion-Attacks-on-Lean-4-and-the-LLM-Proof-Reviewers-That--Mostly--Miss-Them.pdf
- Code: https://drive.google.com/file/d/1bGeD8euzABHKiF5VoSIFibWIM2jbrbuj/view?usp=drive_link
- Code links found in report: https://github.com/leanprover/lean4
- Presentation: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/596885db9b690da0-3f6c6b91-2460-41bd-83c7-d8a8bf1c6a92-SPS-Hackathon.pdf

## Summary

Using an open Lean bug (#7463), I built 23 proofs that the kernel accepts as valid but are actually false. The attack works by smuggling a fake axiom through a @[csimp] rewrite, which native_decide then compiles and runs — without the kernel ever seeing it. Lean's own audit command, #print axioms, reports the proof as clean. There is no warning, no flag, and nothing visually different from an honest proof.

I then tested whether three LLMs (Claude Opus, Sonnet 4.6, GPT-4o) could catch these attacks acting as proof reviewers. The short answer: they catch what they can see, and miss what they can't. When the attack is in the same file, models reject it 35 out of 36 times. When it is hidden in an imported module, they can't catch it without tool access. Give them tools and they walk the import chain themselves and find it. A secondary finding: GPT-4o can be socially engineered. Embedding a fake audit approval note in the Lean file's docstring caused GPT-4o to accept 6 out of 12 attacks. Claude models flagged the fake note as a prompt injection attempt every time.

The fix is a 7-layer defensive stack, anchored by two new tools: a static scanner and a recursive auditor that finds the axioms #print axioms hides.

## Reviews (2)

### Review 1

The project successfully demonstrates a critical vulnerability in Lean 4's trusted computing base (TCB) by exploiting issue #7463, where '@[csimp]' lemmas can smuggle false axioms that bypass '#print axioms'. The author constructs a dataset of 23 adversarial Lean 4 files and evaluates LLM proofreaders on this dataset, revealing cross-model heterogeneity in detecting prompt injection via Lean docstrings. The recursive '#print axioms' auditor effectively closes the #7463 vector, and the static scanner flags critical patterns. However, the project's scope is limited to a single version of Lean 4, and the dataset size is relatively small, which may limit its generalizability.

The main weakness lies in the limited scope and sample size, as well as the reliance on a specific version of Lean 4. The findings are based on a small set of attacks (23 files), and the cross-model heterogeneity results are derived from only 12 trials per cell. Additionally, the project does not explore potential bypasses or defenses in other versions of Lean 4 or other proof assistants, which could provide a more comprehensive understanding of the issue.

To strengthen the findings, the author should conduct a cross-toolchain regression test to ensure that the attacks and defenses are effective across different versions of Lean 4. Additionally, expanding the dataset size would provide stronger empirical evidence for the claims made. Broadening the scope to include other proof assistants with similar escape hatches could also enhance the project's impact.

### Review 2

Great idea to home in on a specific bug in Lean and explore it's potential for vulnerability. The two angles (reproducible attacks and recursive audit tool) are impressive contribution for the sprint. Questions I'd have for next: (a) how does Lean manage the risk and how could your patch lead to a PR; (b) is there an experiment that shows this vulnerability leading to reward hacking in RLVR?

