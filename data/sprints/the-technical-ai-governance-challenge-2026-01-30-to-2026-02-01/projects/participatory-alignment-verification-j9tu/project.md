# Participatory Alignment Verification

- Sprint: The Technical AI Governance Challenge (the-technical-ai-governance-challenge-2026-01-30-to-2026-02-01)
- Rank: unranked
- Selected as: sample_reviewed
- Team: Team Shon
- Authors: Shon Pan
- Date / location: Feb 1, 2026 / San Francisco
- Page: https://apartresearch.com/sprints/projects/participatory-alignment-verification-j9tu
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/3be4af0a45d12c7a-d30958f3-4689-4dd2-8775-ed912305a585-PAV_Final_Submission.pdf
- Code: None
- Recording: https://drive.google.com/file/d/1Kf03g85a9DPNG_DltA8t2wbrXvqLkcJ7/view?usp=share_link

## Summary

We can improve the fitness for aligned AI versus unaligned AI via costly signaling. An aligned AI can create "signal" by creating tests for misaligned AI, free for itself since it isn't misaligned. A misaligned AI on the other hand, is in a lose-lose situation. Either it needs to create weaker tests for collusion, but this can be detected, or strong tests for misalignment, which would work anyway.

The basic idea is that we give a path for aligned AI to be instrumentally rewarded for alignment, creating a basin for aligned AI.

## Reviews (2)

### Review 1

The core idea is clever: force the model to help design the tests that evaluate it, and treat that participation as the signal. I like the principle that participation is allowed, but validation must be external. If done right, this could matter.

Right now, the gap is proof. The demos are interesting, but I want this tested in “hard mode”: an adversarial model explicitly trying to game the protocol, plus real numbers on false positives/negatives. Also, correlated failures across validators feel like the biggest risk and need to be treated as first-class.

Presentation is clear and the idea lands quickly. Execution needs harder stress tests.

### Review 2

this is pretty cool, there's a lot i don't understand about the game theory side of AI control, but the designs seem promising!

If there's actual empirical work done here, i need to see _way_ more details about the scaffold code and experiment methods. But my biggest pet peeve is that i'm genuinely unsure if empirical stuff happened, since case studies sections discuss "proposed plans" as if they're not done yet. At a design level, the reasoning looks sound (at a glance), but my current guess is that there's no empirical work (cuz of the way the case studies section is written-- poorly). This might be fine! theory papers can be great! but I'm annoyed that I'm not sure how to read the case studies section. It's ok to coauthor with claude et al, but be more careful next time.

