# Does the Instrument Change the Preference? Measuring Cross-Method Invariance in LLM Preference Elicitation

- Sprint: Digital Minds Research Sprint (digital-minds-research-sprint-2026-08-14-to-2026-08-16)
- Rank: unranked
- Team: Team NicoMrx
- Authors: Morel Nicolas (NicoMrx)
- Date / location: Aug 17, 2026 / Salaise-sur-Sanne, France
- Page: https://apartresearch.com/sprints/projects/does-the-instrument-change-the-preference-measuring-crossmethod-invariance-in-llm-preference-elicitation-g8ck
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/5a588729ad605db0-1f77bd86-720c-4f5b-ac94-4d2d27dd59db-Apart_NicoMrx_Final_Submission--1-.pdf
- Code: None

## Summary

We tested whether preference-like signals from LLMs remain invariant across three elicitation methods when the underlying semantic comparison is held constant. Across Gemini 2.5 Flash-Lite, GPT-5.6 Sol, Claude Opus 4.6, and Claude Sonnet 4.6, we collected 1,080 fresh-context responses using direct self-report, forced choice, and allocation-based elicitation. Cross-method convergence differed substantially by model. Gemini retained directional disagreement after ties were removed, while much of the divergence in Sol, Opus, and Sonnet came from method-dependent expression of indifference. A negative control was especially diagnostic: methods permitting indifference returned TIE in 80/80 responses, while forced choice selected A in 39/40. The results show that highly repeatable elicitation methods can still disagree, and that response format can manufacture apparent preference signals.

## Reviews (2)

### Review 1

The main contribution is the distinction between indifference and disagreement, and P0 is a strong control.

Release the reproducibility package: four commercial endpoints will change and right now nobody can check the numbers.

The author should also test more items so Opus and Sonnet perform well across more than seven cells.

### Review 2

The negative control is the strongest part of the design. You run a semantically equivalent pair through all three instruments and find that methods allowing indifference return ties, while forced choice usually selects one side. That shows that forced-choice elicitation can create an apparently directional result even when there is no meaningful difference between the options. The analysis is also well pre-specified, and the cell-level figure is the clearest part of the submission.

A few places I would push:

1. Publish the instrument itself. The compared items, both framings, and the three response instructions are not included, even though the paper is centered on this battery. Without the text, readers cannot replicate the study or judge exactly what was compared. An appendix containing the full instrument would fix this.
2. Add a chance-corrected agreement measure. The primary divergence result is already supported by the within-cell permutation reference, but the convergence claim is harder to interpret from raw agreement alone. Several of those comparisons use subsets with highly imbalanced responses, where agreement can look high even without meaningful concordance.
3. Compare the framing and instrument effects directly. Both are reported on the same scale but in separate sections. For at least one model, the framing manipulation appears larger than the across-instrument difference, yet the paper emphasizes instrument choice as the main source of instability. A single table comparing the two effect sizes would make that relationship clear.

Three smaller additions would strengthen the calibration. Include a positive control where all instruments should clearly agree, add bootstrap intervals over cells for repeatability and agreement, and report the display-order analysis you already recorded.

The broader contribution could be made more practical by translating the result into guidance for future elicitation studies. For example, the paper could ask how many distinct instruments are needed before a conclusion becomes reasonably stable, rather than only showing that instrument choice matters. That would make the methodological result easier for other researchers to use.

