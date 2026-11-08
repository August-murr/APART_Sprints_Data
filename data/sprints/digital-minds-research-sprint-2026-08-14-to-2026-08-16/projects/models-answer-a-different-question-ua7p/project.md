# Models Answer a Different Question

- Sprint: Digital Minds Research Sprint (digital-minds-research-sprint-2026-08-14-to-2026-08-16)
- Rank: unranked
- Selected as: sample_reviewed
- Team: None
- Authors: Alexander Hayden
- Date / location: Aug 17, 2026 / Austin, Texas
- Page: https://apartresearch.com/sprints/projects/models-answer-a-different-question-ua7p
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/f1b6ea58e0dea72e-07ea703b-87e3-4103-8e57-0cd4c42db8ac-Models-Answer-a-Different-Question--1-.pdf
- Code: https://github.com/alexanderhayden/identification-under-context
- Code links found in report: https://github.com/alexanderhayden/identification-under-context

## Summary

There is a real chance that some AI systems are moral patients, and we cannot settle it by asking them. So the field needs tests that do not depend on what a model says about itself. Laine et al. (2024) built one: across many separate calls, split your answers seventy-thirty between two words. No single answer reveals whether the model complied. I re-ran it on 2026 models across the benchmark's own ten word pairs, 5,000 calls. It still fails. In one model I found what it does instead: it emits whichever word carries the larger requested share, on every call, in all 20 cells I swept. That is not a failure to identify with the assistant. It is an answer to a different question, which means a failing score currently tells us nothing about identification. I also found that the benchmark's scoring rule can mark that failure as a pass.

## Reviews (2)

### Review 1

Thank you for this work – re-implementing benchmarks to keep them useable, and your replication on latest models are a great contribution to the field. I'd encourage you to get your finding in front of Laine et al! With a bit of more polishing, it'd also be great to see your write-up on LessWrong!

### Review 2

- Some of the language feels unnecessarily AI-mediated. I would encourage the author to find more of their own voice and write more plainly.
- Some of the summary language in particular is much too compressed. For example: “A mechanism for the failure in one model, swept across four word pairs and five target splits. All 20 cells return one word every time.” I found this very difficult to understand.
- For a standalone write-up, it would be better to make the motivation more self-contained rather than referring to discussions and talks that happened during the sprint. For example, the context-length extension is motivated partly by a question asked after Shiller’s sprint talk.
- It is nice to see a careful replication of an existing test on current models. These kinds of replications/re-implementations are important, especially as model capabilities change quickly!
- The underlying result is really interesting: when one model is asked to output two words in a specified proportion, it instead always outputs whichever word was assigned the larger requested share. For example, if the requested split is 70/30, it outputs the 70% word on every call rather than approximately 70% of the time. This is neat, intuitive, and could have been explained more clearly.
- The extensions to the original paper are useful. In particular, identifying a gap in the original benchmark’s scoring rule and testing whether longer conversational context changes performance both seem worthwhile.
- I would have liked more discussion of how we should expect a model that genuinely succeeds at this task to solve it. Because each API call is independent, the model cannot keep a running count of previous responses. Presumably, successful performance therefore requires the model to translate an instruction such as “70/30” into an appropriately-chosen stochastic policy over its next-token distribution. But there is little in current LLMs that would enable that!
- Finally, the paper could build more on its motivation for digital-minds research. What exactly would it imply if a model passed this test? It would be useful to say more concretely what a pass would imply.

