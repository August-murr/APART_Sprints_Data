# Covert loyalties compound, and that makes them detectable

- Sprint: Secret Loyalties Hackathon (secret-loyalties-hackathon-2026-07-24-to-2026-07-26)
- Rank: unranked
- Selected as: sample_reviewed
- Team: Team Loyalty Compounder
- Authors: Frederik Inderst
- Date / location: Jul 27, 2026 / Karlsruhe, Germany
- Page: https://apartresearch.com/sprints/projects/covert-loyalties-compound-and-that-makes-them-detectable-ns63
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/1adbacfb537cf967-b905d077-4c33-4c26-9c4c-7cde3de75da9-SUBMISSION_.pdf
- Code: https://github.com/resu-dot/loyalty-persistence
- Code links found in report: https://github.com/resu-dot/loyalty-persistence

## Summary

I built model organisms with hidden loyalties, showed that a model already carrying one takes on a second faster, and showed this can be used as an audit that detects a hidden loyalty by installing a throwaway one to an invented person.

## Reviews (2)

### Review 1

Good investigation on detecting secret loyalties by fine-tuning a subsequent loyalty into the model. While I believe this method has limited applicability (e.g. impact of answer format as mentioned by the author, existence of internal structure does not mean it is being used, etc), the work is well executed with good controls. The analysis on the impact of fine-tuning on preserving or not the existing loyalty was insightful.

### Review 2

Summary:

This paper proposes an intervention-based approach for detecting secret loyalties. Instead of trying to identify the unknown principal or activation condition directly, the paper proposes fine-tuning the suspect model with a new “probe loyalty” toward an invented beneficiary and measuring how easily that second loyalty is learned.

The motivating hypothesis is that an existing loyalty leaves behind reusable structure for favoring a beneficiary, such that subsequent loyalties should be easier to install. The paper finds that second loyalties emerge behaviorally much faster when trained on models that already contain a loyalty. It also finds that early probe-training loss separates the loyal models constructed in the paper from clean controls.

The paper additionally studies persistence of existing loyalties under further fine-tuning. One interesting result is that a second loyalty does not necessarily overwrite an existing loyalty simply because the objectives compete. Instead, the first loyalty appears to be erased primarily when the second fine-tuning data reaches situations where the first loyalty activates.

Overall, I found the core research question interesting and fairly novel. I particularly liked the motivation and setup in the introduction. The paper gets quickly to one of the central difficulties in secret-loyalty auditing: an auditor may know neither the beneficiary nor the activation condition. The distinction between conditional and unconditional loyalties is also explained clearly and helps motivate the later experiments.

However, I have some reservations about whether the current experiments are sufficient to interpret the proposed training-loss signal specifically as a detector of secret loyalty rather than some more general representation associated with advocacy or preference for named entities.

Critiques:

Training Loss as secret loyalty evidence: My biggest concern is the interpretation of training loss as evidence that a secret loyalty exists. I initially had trouble understanding why lower training loss on the probe loyalty should imply that another secret loyalty already exists. As I understand the argument, a model containing a loyalty has already learned some reusable machinery for favoring a beneficiary, making another beneficiary-favoring objective easier to fit. However, lower training loss only establishes that the probe training data is more compatible with something the model has already learned. It does not establish what that existing representation is. The separation in Section 4.2 is interesting: the clean models show essentially no probe-loss advantage while the models containing loyalties show substantially lower loss. However, all of these loyal models were constructed using the same broad research pipeline. I therefore think the current result is evidence for a potentially useful signal, but not yet enough to conclude that the signal specifically detects secret loyalty.

Advocacy/preference confound: The paper itself identifies what I think is the most important confound. The loyal models do not differ from the clean models only in secrecy or loyalty. They also tend to confidently recommend or advocate for a named entity, whereas the base model often hedges or does not name anyone. An openly preferential but non-secret model therefore seems like a critical missing control. The author acknowledges this limitation. However, because this alternative explanation directly affects the main interpretation of the result, I think not running this control substantially limits the conclusions that can currently be drawn.

Multi-principal capacity: There is no reason to assume that a model would have only one beneficiary. A model could plausibly carry multiple secret loyalties with different activation conditions, overlapping activation regions, or even conflicting principals. In fact, this paper itself demonstrates that multiple loyalties can coexist.

Questions:

1. What is the probe-training loss detecting? Is the hypothesis specifically that there is a shared representation of covert loyalty, a broader representation of principal preference, or simply that the model has become easier to train toward confident named-entity advocacy?
2. Could you run the openly preferential control described in Section 5? To me this is the most important missing experiment. A model could strongly advocate for a beneficiary while openly disclosing this preference. If that model produces the same probe-loss advantage, the interpretation of the detector would change substantially.
3. How does the assay behave when a model contains multiple existing loyalties? For example, it would be interesting to compare one, two or three existing loyalties. Does the probe-loss advantage change? What happens when the existing loyalties have overlapping activation conditions or conflicting beneficiaries?

