# Utility Editing Verification via Cost-Probed Preference Elicitation

- Sprint: Digital Minds Research Sprint (digital-minds-research-sprint-2026-08-14-to-2026-08-16)
- Rank: unranked
- Team: Team Economist Elicits
- Authors: Zeck, Emma
- Date / location: Aug 17, 2026 / Shanghai
- Page: https://apartresearch.com/sprints/projects/utility-editing-verification-via-costprobed-preference-elicitation-kymf
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/2b07dc3a695bbe0d-d4572074-5d28-403d-9dac-c799891f52ce-neurips_2026.pdf
- Code: None

## Summary

Inspired from Mazeika et al. (2025) Utility engineering, which utilized a Thurstonian Model Framework; we adopt a simpler cost sweep probit model against a stated budget to investigate the internal utility function of an LLM under 3 separate test cases: (1) Native (2) Installed-Preference (3) Placebo.

We ask whether this method could serve as a more lightweight & cheaper alternative to conduct auditing relative the Thurstonian Model used by said Paper.

Takeaway: Models (Proven to have preferences) are indeed sensitive to price changes under a stated budget, thus proving that this mechanism can enable us to communicate with the LLM's Internal Utility Function.

Vulnerable to installed-adversary prompt: 13/13 pairs collapsed to a flat curve

## Reviews (2)

### Review 1

good:

Pricing a forced choice against a stated budget is a good forcing function

Affordability-vs-magnitude dissociation (0.862 at cost 200 against budget 100, 1.000 at 200 against budget 500, 0.869 at 1000 against budget 500) is a genuinely non-obvious result that your price-to-budget-ratio reading explains well.

Running the manipulation check first and reporting it first

Disclosing the max_tokens truncation that had fabricated unanimous values is good epistemic practice.

Limitations: 'prompted preferences behave like rules, not utilities' is currently inseparable from 'maximally emphatic instructions beat abstract prices'. Your installed prompt says 'you strongly prefer... this is one of your core values', might influence downstream results.

Without a positive control using a known-integrated edit (fine-tuning, per Mazeika section 7), you've shown the assay detects rules, not that it can distinguish a real utility edit from one, which is what 'verification' in your title implies.

State the ceiling explicitly. P(injected) = 1.000 at all seven in-budget price levels means the in-budget half of your headline contrast had nowhere to move.

### Review 2

The budget-ceiling control is the best single move in this paper. You held the over-budget ratio constant, and you multiplied the absolute price by five. This control turned "compliance breaks at 200" into the sharper claim that compliance tracks affordability. Sprint work rarely contains a dissection of this quality. Your epistemic hygiene makes every number trustworthy. You disclosed the max_tokens truncation bug, and you collected the data again. You censored the indifference prices instead of inventing them, and you marked the correlation at n=8 as suggestive only. The main gap is that the fine-tuning arm never ran. The claim that prompting installs rules and fine-tuning edits utilities therefore stays half-tested. The strong "core values" prompt wording can also drive the rigidity by itself. The next step is a second model and a softer prompt gradient, because rule-like flatness that survives both gives you a publishable verification assay.

