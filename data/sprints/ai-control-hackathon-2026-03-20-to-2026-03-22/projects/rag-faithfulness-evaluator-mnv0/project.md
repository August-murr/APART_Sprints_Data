# RAG Faithfulness evaluator

- Sprint: AI Control Hackathon 2026 (ai-control-hackathon-2026-03-20-to-2026-03-22)
- Rank: unranked
- Selected as: sample_reviewed
- Team: Team Faith Layer
- Authors: Mouad Benmansour
- Date / location: Mar 23, 2026 / Leicester
- Page: https://apartresearch.com/sprints/projects/rag-faithfulness-evaluator-mnv0
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/2276e282e48c7b8a-e009f3f6-66a2-4ab9-be79-30fb5d389671-RAG_Faithfulness_Evaluator_FINAL.pdf
- Code: https://github.com/mouadbenmansour/RAG-Faithfulness-Evaluator

## Summary

RAG is everywhere now, and organisations adopt it precisely because it is supposed to be accurate. This tool holds RAG systems accountable to that promise, monitoring every output at sentence level, visualising how faithfulness drifts across an answer, and producing a named diagnosis explaining what went wrong, where, and what to fix. Built on a hybrid of semantic similarity and lexical overlap, with an LLM diagnostic layer constrained to a human-authored taxonomy of six known drift patterns. It catches what aggregate scores miss and explains what they cannot

## Reviews (2)

### Review 1

For a hackathon build, this is a clean working prototype. Sentence-level faithfulness scoring with drift timelines beats aggregate numbers — operators get something actionable, not just a pass/fail. The six-pattern diagnostic taxonomy is practical and the ACL injury catch (high semantic similarity but low lexical overlap revealing a training data leak) is a nice demo of why two scoring signals beat one.

The AI control connection could be tighter — this reads more as a RAG reliability tool than a control protocol for adversarial subversion. Framing it as "what if the model is deliberately trying to smuggle ungrounded claims past the monitor" would have landed better for this hackathon's theme.

Evaluation is one domain with hand-tuned thresholds, which is fine for a prototype — the roadmap (HaluEval, entailment scoring) shows the author knows what's next. Good execution for the time constraint.

### Review 2

The problem of sentence-level faithfulness scoring in RAG systems is practically relevant, and the drift timeline idea is an intuitive framing. The diagnostic taxonomy of six failure patterns is a reasonable starting point for categorising how RAG systems fail.

The main concern is fit with the AI control hackathon theme. This addresses ordinary retrieval tooling failures rather than the adversarial monitoring setting of AI control.

