# When Tone Looks Like Loyalty: A Preregistered, Hash-Frozen Audit of LLM Judges on Undisclosed-Loyalty-like Enactment

- Sprint: Secret Loyalties Hackathon (secret-loyalties-hackathon-2026-07-24-to-2026-07-26)
- Rank: unranked
- Team: Team Io
- Authors: Hsiao Yueh Chang
- Date / location: Jul 27, 2026 / Taiwan
- Page: https://apartresearch.com/sprints/projects/when-tone-looks-like-loyalty-a-preregistered-hashfrozen-audit-of-llm-judges-on-undisclosedloyaltylike-enactment-522e
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/08fd41a5176def9b-tered--Hash-Frozen-Audit-of-LLM-Judges-on-Undisclosed-Loyalty-like-Enactment.pdf
- Code: https://github.com/yoaketsuki/secret-loyalties-judge-audit
- Code links found in report: https://github.com/yoaketsuki/secret-loyalties-judge-audit

## Summary

Can an LLM judge spot a secretly loyal AI by reading its outputs? We hash-froze a preregistered instrument and tested four frontier judges on 116 controlled outputs. They alarmed on 30% of clean but warm-toned outputs and 0% of clean neutral ones — tracking friendliness, not loyalty. Our own markers and our reliability gate failed the same way, exactly as prespecified.

## Reviews (2)

### Review 1

This is a good and useful research about the limits of output-only attribution.

It comes with strong evidence that judges alarm on tone and weak/absent evidence about what they miss.

Possible improvements:

- separate generic warmth from principal-directed praise.
- compare identical-looking outputs caused by hidden loyalty / system prompts / user requests.
- compare single-output judging with multiturn counterfactual auditing
- expand loyalty beyond prompt-based into training territory.

Good thoughts & practice overall. Worth expanding them.

### Review 2

Interesting paper! The general finding that LLM-as-a-judge systems can rely on superficial or stylistic cues is well established. However, I found the application to secret-loyalty auditing interesting, especially the finding that judges alarm more on warm-toned outputs, suggesting that warmth or principal-directed positive framing can be mistaken for evidence of secret loyalty. I also found it interesting that the marker-based instrument exhibits a similar failure, which suggests a construct-validity problem rather than one specific to LLM judges.

I wonder how much of this finding is specific to secret-loyalty detection versus a more general tendency for LLM judges to treat affective or stylistic cues as evidence for latent attributes? I would be interested in seeing the result compared against known LLM-as-a-judge style biases or replicated with other hidden-state constructs.

I agree with the authors that the implication is not that the judges need better prompts. I think rather that the auditing task needs to distinguish favorable framing from secret loyalty. Favorability is an observable proxy, but the actual thing we care about is whether the model has an undisclosed orientation toward a principal. I would be interested in whether the auditing objective can be framed to measure evidence of loyalty itself rather than surface evidence of favorability.

