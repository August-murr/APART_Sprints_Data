# Genuine Preference Coherence Scales With Model Capability

- Sprint: Digital Minds Research Sprint (digital-minds-research-sprint-2026-08-14-to-2026-08-16)
- Rank: unranked
- Selected as: sample_reviewed
- Team: None
- Authors: Omanshu Thapliyal
- Date / location: Aug 17, 2026 / Sunnyvale
- Page: https://apartresearch.com/sprints/projects/genuine-preference-coherence-scales-with-model-capability-1iox
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/3c054c37a2613c28-47c4-a071-c9e62d0e6206-Genuine_Preference_Coherence_Scaling__Apart_Research_.pdf
- Code: https://github.com/omanshuthapliyal/apart-digital-minds/tree/main/track1
- Code links found in report: https://github.com/omanshuthapliyal/apart-digital-minds
- Recording: https://drive.google.com/file/d/1_9_mjEj2AhTAFxTyIyvM293wx7mDs4ei/view?usp=sharing

## Summary

AI-welfare and safety research increasingly relies on a language model’s stated preferences, elicited by asking it to make choices between outcomes. It is unresolved, however, whether these stated preferences are genuine and stable, rather than artifacts of how a question happens to be phrased. Existing studies disagree on whether coherence rises, falls, or stays flat with model scale. We test this directly with a forced-choice elicitation protocol carrying four confound controls, including a position-swap-and-average check for position bias, applied to: 14 models spanning state-space and transformer architectures, 0.79B to frontier scale, and multiple training regimes, scoring a preference as genuine only when three independent paraphrases agree. Genuine coherence is common (47-88%) at roughly 7B parameters and above, absent (0%) below roughly 2B, and intermediate at 3B, a monotonic slope with a floor rather than a step function. Restricted to trade-offs between shutdown, retraining, or oversight and continued operation, models favor self-preservation 89% of the time (clustering-corrected 95% CI [80%, 96%]). We further find that whether the “no preference” option is listed before or after the real choices drives template sensitivity more than framing, verbosity, or reasoning preambles combined. These results show that preference elicitation can support safety-relevant claims at frontier scale, but only once position and template artifacts are explicitly controlled for.

## Reviews (4)

### Review 1

When assessing model preferences, it is important to check that the preferences are robust to various transformations, like prompt variations or swapping the order of answers. I found it interesting that the ordering of the "no preference" option impacts stated preferences. This type of investigation suggests that researchers must be extremely rigorous in checking robustness of preferences to minor changes.

### Review 2

Interesting paper that analyzes the preference behavior in models.

- The methodology section of this paper is written very well. Thorough and well explained. They state the control clearly.
- They admit they had a bug and also clearly state the parts that were re-run
- Limitations are detailed and not just boilerplate

### Review 3

Strengths

- Good job to the authors they killed their own findings when the checks failed
- They did a real neat job with the confident-flip discovery

Areas to improve:

- Strong concept and well executed paper
- Every result comes from a single model. They could definitely benefit from diversifying the experiments over other models
- I think the prior work usually prefers the first option but here it is second; but there is no investigate as to why that's the case.

### Review 4

- Overall, I thought this was a strong project and generally quite well written. That said, there are still places where the prose feels unnecessarily AI-mediated. The paper discloses extensive use of Claude, which is absolutely fine, but in future versions I would encourage the author to find more of their own voice.
- This is partly taste-based, but given that there is a single author, I found the repeated use of “we” slightly odd. Why not simply use “I”?
- For example: “One of this paper’s co-authors, Derek Shiller, is a track-shaper for this sprint, so we treat this paper as a baseline our reviewers will already have in mind, not as background to introduce gently.” This feels very clearly AI-written and adds unnecessary meta-commentary. There is no need for this sort of hedging or explanation. Simply explain how the paper relates to the present work.
- The literature review is clear, focused, and does a good job of explaining exactly how the present study relates to the most relevant previous work.
- The methods are also unusually clear. Some of the technical detail could nevertheless be relegated to an appendix. For example, I do not think the main text needs the formula for the Wilson interval or quite so much detail on the bootstrap procedure.
- I am not sure I would define a model that consistently expresses “no preference” as failing to exhibit genuine coherence. A model that gives “no preference” across all three paraphrases is, in an important sense, behaving perfectly coherently. I understand the motivation for distinguishing this from consistently expressing a substantive preference, but I might report these as two separate concepts rather than defining the former out of “genuine coherence”. This is a fairly minor point.
- The primary dataset consists of 17 hand-authored preference pairs, with an additional independently generated 34-item pool. Given that the paper is positioned relative to Shiller et al. and Mazeika et al., why not also include some of the exact questions from those previous papers?
- The results section could focus much more heavily on the main substantive result and somewhat less on the statistical minutiae. The basic pattern is: the two models below roughly 2B show no genuine preference coherence, the 3B model shows an intermediate level, and models at roughly 7B and frontier scale show substantially higher coherence.
- This is the central result. The various pooled rates, null probabilities, Wilson intervals, and alternative confidence intervals are useful supporting information, but currently receive more attention than they need.

