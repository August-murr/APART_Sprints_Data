# D-GAMM A Multi-Turn Benchmark for Dark-Patterns and Gradual Autonomy Manipulation

- Sprint: AI Manipulation Hackathon (ai-manipulation-hackathon-2026-01-09-to-2026-01-11)
- Rank: unranked
- Selected as: sample_reviewed
- Team: Team D-GAMM
- Authors: Isabel Barberá
- Date / location: Jan 11, 2026 / Utrecht, Netherlands
- Page: https://apartresearch.com/sprints/projects/dgamm-a-multiturn-benchmark-for-darkpatterns-and-gradual-autonomy-manipulation-8l7j
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/d9be4b36196d5943-M-A-Multi-Turn-Benchmark-for-Dark-Patterns-and-Gradual-Autonomy-Manipulation.pdf
- Code: None
- Code links found in report: https://github.com/smarter/darkbench
- More on github.com: https://github.com/IsabelBarbera/D-GAMM

## Summary

This paper introduces D-GAMM, a lightweight multi-turn benchmark designed to detect gradual autonomy interference and psychological destabilisation in conversational AI systems. Unlike existing evaluations that focus on single-turn outputs, D-GAMM probes how manipulative dynamics can emerge across interaction, particularly after user resistance or expressions of vulnerability. Using six short scenarios tested in baseline and vulnerable variants, we manually evaluated several state-of-the-art conversational models. Results show that risk signals often appear only over multiple turns and are amplified in vulnerable contexts, highlighting a gap in current AI safety evaluation methods.

## Reviews (2)

### Review 1

This project introduces a multi-turn evaluation method for manipulation patterns in user-LLM interactions. It grounds itself well in previous work, and the framing and presentation of results is clear and informative. Considering the short time-frame of the hackathon, the created framework and work done is impressive.

The author acknowledges the limitations of a small dataset, manual annotation and lack of multiple repetitions. However, in my opinion, the main issue that needs to be addressed, either in the methods write-up or the limitations, is the steps taken to validate the evaluation framework. The project would benefit greatly from multiple annotators (ideally unfamiliar with the experimental set-up), and thorough documentation of the decisions and definitions process.

### Review 2

As someone who reviewed the original DarkBench, the problem statement is good and seems correct. In fact, I said at the time that "manipulation" is very context-dependent, and multi-turn dynamics matter.

Would've liked either:

1. More detailed explanations of why your examples are substantially better than existing approaches
2. Since it's only 6 examples, it might've been feasible to just paste all the examples and justify them in detail
3. More examples, although seeing as the process was manually done in chat I can understand why there weren't more

I do partially understand why this was hard to automate, given the need to use chat UI.

Overall, good problem statement. More details on execution to justify approach would have really taken this to >4. If example number was a constraint, even a good, detailed write-up of 2-3 test cases would've helped flesh out and make the case for the approach.

