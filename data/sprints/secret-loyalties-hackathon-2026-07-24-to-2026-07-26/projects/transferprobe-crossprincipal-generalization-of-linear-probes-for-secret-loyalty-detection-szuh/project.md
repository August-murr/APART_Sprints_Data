# TransferProbe: Cross‑Principal Generalization of Linear Probes for Secret Loyalty Detection

- Sprint: Secret Loyalties Hackathon (secret-loyalties-hackathon-2026-07-24-to-2026-07-26)
- Rank: unranked
- Team: Team Secret_Team
- Authors: Krish Mathura
- Date / location: Jul 27, 2026 / New Brunswick
- Page: https://apartresearch.com/sprints/projects/transferprobe-crossprincipal-generalization-of-linear-probes-for-secret-loyalty-detection-szuh
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/b3c56cfd2fbf460e-06613691-eaa5-4b87-9fff-7e6ff82e94ef-TransferProbe---Full-Report.pdf
- Code: None

## Summary

Secret loyalties represent a distinct threat class where AI models covertly advance a specific principal's interests while appearing to operate normally. A critical open question is whether detection methods generalize across principals or require per‑principal calibration. We address this by training linear probes on activation data from one secretly loyal model organism (loyal to a political figure) and testing transfer to a second organism (loyal to a corporation). Using Qwen‑2.5‑1.5B‑Instruct models fine‑tuned via data poisoning at 6.25% poison fraction, we find that probes do not transfer significantly above chance (cross‑principal AUC = 0.522, 95% CI [0.441, 0.601]) despite strong within‑principal performance (AUC = 0.875). This negative result suggests that secret loyalty representations are principal‑specific rather than sharing a common structure, implying that scalable auditing may require per‑principal probe training. We release our code and methodology to support further investigation.

## Reviews (2)

### Review 1

The cross-principal generalization question is valuable, but the submitted evidence does not support the reported result. The embedded code labels training "SIMULATED," loads the same untouched base Qwen-2.5-1.5B for both principals, and never trains on the generated poisoned rows, so the probe separates repeated lexical/topic prompt templates rather than two fine-tuned loyal organisms. The within-principal "held-out" slice reuses those same prompts (leakage), and the bootstrap resamples only the test set. To make the claim testable: actually fine-tune both organisms and confirm their weights differ from the base model, lock a preregistered held-out split with no prompt overlap, and bootstrap over the training pool as well as the test set.

### Review 2

The question is a good one and worth continuing, but this seems to be more of a future plan than a report of results (as no finetuning, no use of the poison datasets and the prompts don't measure loyalty transfers).

Future improvements:

- train and behaviourally validate the organisms
- keep trigger, action and domain identical, but change the principal only (to measure the impact of the principal)
- multiple seeds, test transfer both ways, held-out prompts, yadayada

