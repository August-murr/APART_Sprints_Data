# Adversarial Iteration for Underspecified Program Synthesis

- Sprint: The Secure Program Synthesis Hackathon (secure-program-synthesis-hackathon-2026-05-22-to-2026-05-24)
- Rank: unranked
- Selected as: sample_reviewed
- Team: Team The Herons
- Authors: Amir Sarid, Uri Ariel Chen, Amit Saroussi, Nitzan Pomerantz
- Date / location: May 25, 2026 / Tel Aviv
- Page: https://apartresearch.com/sprints/projects/adversarial-iteration-for-underspecified-program-synthesis-i82n
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/0b7c1d581a824307-erspecified-Program-Synthesis---Apart-Research-hackathon-submission-template.pdf
- Code: https://github.com/aimir/idcs
- Code links found in report: https://github.com/aimir/idcs, https://github.com/evalplus/evalplus

## Summary

We introduce IDCS (Iterative Distinguishing of Code and Specs), a spec-guided pipeline that outperforms direct code generation on underspecified program-synthesis tasks. This pipeline, composed of a generator, a distinguisher, a user-proxy, and finally a coder, gets significantly better results than either using the coder directly or using the spec generator and coder alone, especially on prompts that are underspecified, unclear, or shorter than the behavior they imply. We also show that the generator and distinguisher prompts themselves can be generated through adversarial coevolution. We evaluate on three MBPP+ slices selected for hidden-edge semantics rather than algorithmic difficulty: an original five-task hard slice, a held-out hard-test split, and a nine-task fresh-failures slice. The hand-written spec-guided pipeline increases hidden-test pass rate 73.3% to 96.2% on held-out test data.

## Reviews (2)

### Review 1

The methodological instinct is sound: score the generated code against hidden tests so "does a spec layer help" becomes a number, and curate slices for hidden-edge semantics rather than difficulty. The ceiling prompt and the gold-spec POC do real work in bounding where the headroom actually sits. The framing undersells itself, though. The abstract leads with 73→96%, the hand-written pipeline on a single five-task split and the least load-bearing number in the paper. The genuine contribution, though, is the negative result: coevolved prompts win on training and lose to the seed on held-out. Opening with that would be both more interesting and more defensible. Beyond the framing, every delta rides on five-to-nine tasks, so none survives statistically, and the validation gate that would address the overfitting is proposed but never run. The work stops one experiment short of its own thesis, a point it nearly makes outright.

### Review 2

Fun and interesting work—you identified a good problem and tried some nice approaches including coevolution/GEPA, even though you got mostly a null result. Presentation could have been better: it's clearly slop writing, citations are broken, etc. Could warrant some further work, though it remains a possibility that with an underspecified spec, the information may not exist for the LLM to meaningfully improve on a "first-pass" implementation.

