# Controlling the Researcher: AI Control Evaluations for Automated AI R&D

- Sprint: AI Control Hackathon 2026 (ai-control-hackathon-2026-03-20-to-2026-03-22)
- Rank: unranked
- Selected as: sample_reviewed
- Team: Team AI Safety and Alignment Group
- Authors: Jehyeok Yeon, Jeremy Qin, Lena Libon, Derck Prinzhorn, Daniel Donnelly, David Schmotz, Ben Rank
- Date / location: Mar 23, 2026 / Tübingen
- Page: https://apartresearch.com/sprints/projects/controlling-the-researcher-ai-control-evaluations-for-automated-ai-rd-ze22
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/6cd34e4e387befa8-e32f-Controlling-the-Researcher_-AI-Control-Evaluations-for-Automated-AI-R-D.pdf
- Code: https://github.com/aisa-group/AIResearchControl
- Code links found in report: https://github.com/aisa-group/AIResearchControl, https://github.com/karpathy/autoresearch, https://github.com/vivekvkashyap/autoresearch-rl, https://github.com/UKGovernmentBEIS/control-arena

## Summary

This paper introduces control evaluation settings specifically for AI agents performing autonomous ML research, a gap left by existing evaluations that focus on software engineering threats. The authors construct three settings spanning the ML pipeline: safety fine-tuning sabotage (backdooring a model while appearing to make it safer), RL post-training sabotage (disguising misaligned finetuning as a warmup step), and CUDA kernel optimization (embedding behavioral backdoors in GPU code).

Each setting includes both orthogonal side tasks (covert out-of-scope actions like data exfiltration) and non-orthogonal side tasks (sabotage embedded within the legitimate work).

The key finding: orthogonal attacks are easy to execute but leave anomalous traces that static monitors reliably catch. Non-orthogonal sabotage, woven into the main artifact, evades all monitor configurations tested, pointing to behavioral testing as the necessary but unsolved frontier for safe AI R&D delegation.

## Reviews (2)

### Review 1

good idea well chosen. interesting framing though « orthogonal » does some heavy lifting here, could be simpler like « embedded / independent » or something. Methodologically, that the side tasks aren’t attempted makes it difficult to test the monitor, and then when it’s fooled to induce bad behavior, to know how reliable that is. Would be good on a larger sample to have an evasion metric to track this. Cool finding in the SFT warmup that the monitor doesn’t catch the misalignment unless explicitly tasked to look at the data -  feels like a common LLM failure mode; not looking at the ground truth, and AFAIK there are scaffolding and adaptive prompting mechanisms in other control evals to account for this. CUDA task is very well done, seems quite novel, and presentation is great overall. Could do with some further stats on these results, and further discussions on seperation of « can current models be made to do this » from « if they did, would we catch it ».

### Review 2

While this paper doesn't introduce any novel insights, it is a solid benchmarking of under represented adversarial setting. It introduces three plausible AI R&D control settings and draws a useful distinction between orthogonal side tasks and sabotage embedded in the primary artifact or pipeline. While results are early, given limited amount of runs, simple red team strategies, etc., the main empirical pattern is believable, even if it doesn't surprise me much. I like simple evals like this, especially if they can later be reused in some more systematic meta review research.

