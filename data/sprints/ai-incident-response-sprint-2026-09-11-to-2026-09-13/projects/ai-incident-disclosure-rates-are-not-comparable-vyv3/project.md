# AI incident disclosure rates are not comparable

- Sprint: AI Incident Response Sprint (ai-incident-response-sprint-2026-09-11-to-2026-09-13)
- Rank: unranked
- Selected as: sample_reviewed
- Team: Team Missing Denominators
- Authors: Mohammed Faisal Parvez
- Date / location: Sep 14, 2026 / Hyderabad
- Page: https://apartresearch.com/sprints/projects/ai-incident-disclosure-rates-are-not-comparable-vyv3
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/587d412022227fe5-cc-33ba-4ddb-a4f7-34a4191a3b3c-AI_incident_disclosure_rates_Apart_submission.pdf
- Code: https://github.com/faisalhacks/missing-denominators

## Summary

Frontier labs publish incident numbers that cannot be set beside one another. We audited three 2026 disclosures — Anthropic's cyber-eval incidents, OpenAI's Hugging Face incident, and the UK AISI cheating study — by hand against one estimand (a containment breach) and one unit (violations per evaluation run), assigning a recoverability state to each of their 21 numeric fields. Only one converts: Anthropic published a denominator of 141,006 runs, which lets an outside reader compute a per-run rate of 4.26×10⁻⁵ that the lab never stated itself, and which is only a lower bound. Sixteen of the 21 fields are absent from public sources entirely. Each failure has a distinct cause — no denominator, figure-only values, or a different estimand — and each implies a different fix. We release a conversion instrument whose schema rejects any record that puts a number into a gap, plus a five-field reporting standard a regulator, auditor, or insurer can run as a pass/fail check.

## Reviews (2)

### Review 1

I could reproduce every headline number from the repository which I think is extraordinary for a weekend build.

Here is what I verified against the code and data:

1. 6 / 141,006 = 4.255e-05 – rounds to the stated 4.26 × 10⁻⁵ at three significant figures.
2. 21 numeric cells = 7 fields × 3 verified disclosures. Confirmed.
3. 16 of 21 not_recoverable. Confirmed by re-counting the incident JSONs directly.
4. The anti-fabrication claim is real. convert.py lines 48-50 reject any not_recoverable field carrying a value. Enforced in code, not just asserted.
5. Anthropic's figures are quoted verbatim with location and check out against the linked source.

The reason-code taxonomy is the contribution. Saying why each disclosure fails – no-denominator, figure-only, different-estimand – is far more useful than saying labs should publish more. Each code implies a different fix, and Section 4.3 turns each one into a specific ask.

That is what makes this usable by a non-technical body.

I specifically want to highlight three other things that deserve credit.

Appendix A. Every source opened, every figure located in primary text, and every absence confirmed rather than assumed. Establishing that AISI's per-model values exist only inside an image is real work, and it is what earns the figure-only code.

The 898 versus 869 discrepancy. You found that OpenAI's post reports 898 ExploitGym tasks while the shipped release contains 869, and you recorded both rather than quietly picking one. Most audits would have reconciled it silently.

Freezing the experiment. You pre-registered the aggregation prediction, fixed the stopping rule in advance, wrote the harness – and then did not run it, because the containment controls it needs are the thing this sprint is still trying to specify. You withheld the execution harness on the same reasoning. That is the right call and you argued it rather than just asserting it. Declining to reproduce the failure mode really is part of the finding.

Now the problems - here is what I found:

1. The headline statistic counts two different failures as one.

AISI is coded different-estimand. They measured cheating propensity - not containment breaches. Figure 1 then counts all 7 of their fields as not_recoverable and those 7 are nearly half of your 16.

That conflates two things your own taxonomy separates. "Not comparable in principle" and "not disclosed" are different failures. AISI did not omit a containment-breach denominator. They were not measuring containment breaches at all, so those cells are not applicable rather than absent.

Section 5.5 says the claim is about retrievability and is not a statistical estimate. Agreed, and that is the right disclaimer. But the abstract and the conclusion both lead with "sixteen of the 21", which is the reading the disclaimer warns against.

Strip AISI out and it becomes 9 of 14 across two containment-breach disclosures. Weaker headline, and it survives the objection. I would recommend to report both numbers.

2. The fifth field of your own standard is not in your schema.

Section 4.4 says the five-field list "is the same list the instrument already enforces as a schema". It is not. schema.json has no field for detection sensitivity or a false-negative bound – I grepped for it and for every synonym I could think of.

That matters because detection sensitivity is the field doing the most work in your argument. It is what makes 4.26 × 10⁻⁵ a lower bound rather than a measurement and you say so yourself in Section 4.1. A standard whose load-bearing field has no machine-readable representation cannot be run as the pass/fail check you propose.

Add the field. It is a small change and it closes the gap between the paper and the instrument.

3. 869 does not appear anywhere in the repository.

Section 3.5 says you "use 869 for the repository, and flag the difference in the provenance appendix". Appendix A repeats it. I searched the full repository – 869 and 898 are both absent, including from the incident records that generate the provenance appendix.

So the discrepancy you found is documented in the paper and not in the artifact. Please add it to the OpenAI record's provenance text, where a reader of the data alone would see it.

4. The schema has no precision flag.

OpenAI's violation_count is stored as value: 1200, state: recoverable. The source says "roughly 1,200". Your provenance string does record the approximation, which is good practice.

But a consumer reading the JSON gets an exact integer unless they parse English prose. For an instrument built to stop false precision, we need a machine-readable field – approximate: true, or a bounds pair. This is the same gap as item 2 and I would fix them together.

5. Latent unit bug in per_agent_rate.

convert.py line 105 falls back from violation_count to incident_count as the numerator. Those are different units. Anthropic has 6 violations and 3 incidents. One row could mean violations per agent and another incidents per agent, under the same column header.

It never fires today because agent_count is not_recoverable everywhere – so this is latent, not active. Still, it is the exact unit conflation the paper exists to prevent. I would recommend to split it into two fields, or refuse the derivation when the numerator source differs.

6. Small sample and single coder – both disclosed, both still worth closing.

Section 5.5 is honest about three disclosures and about the absence of an inter-rater statistic, and releasing the criterion so a reader can re-code a specific cell is the right mitigation. The cheapest next step is still a second coder on these same three records. An afternoon's work would turn the taxonomy from one reading into a replicated one.

7. Minor – an editorial note was left in the submitted paper. The LLM usage statement ends with a bracketed instruction to the authors to confirm the statement and record the exact model version. Worth resolving before this goes further.

One closing note, since careful reports sometimes get read as machine-written. The work behind this one is real and I checked it. The claims cite primary sources. The numbers reproduce from the repository. Appendix A records what was located and what was confirmed absent. You left a record as PENDING rather than filling it, and you declined to run an experiment you had already designed. I scored the work.

Please let me know for any questions.

### Review 2

The diagnostic is sound and worth publishing: incident numbers from different labs cannot be pooled

because they do not share a denominator or a unit, and only one of the disclosures examined yields a

rate that can be computed at all. Modelling the fix on clinical-trial reporting standards is the

right instinct, and there is real discipline in the method: a fixed, pre-specified order for deciding why a disclosure fails to pool, an explicit account of an approach that did not work, and an unreconciled discrepancy in one

lab's task counts flagged rather than quietly smoothed over. The plain-language appendix for

non-technical readers is a good practice too, and an uncommon one.

The artifact does not yet carry that argument. Two claims in particular fail against the repository. The paper states that its figure regenerates from the conversion script; there is no plotting code of any kind, and the figure was evidently produced by hand. And the schema the paper credits with making fabrication a hard error is never loaded at runtime — the hand-written check standing in for it is weaker than the schema it documents, accepting records the published version would reject. The safety property is real, but it rests on something other than what the paper says it rests on. Two further claims, a released statistical computation and a negative test, have no corresponding

artifact at all.

The submitted PDF also still carries a bracketed note to the authors on its final page, inside the LLM usage statement — worth a proofing pass before this circulates further, since that is the one section where precision about what happened matters most.

Most of this is quick to put right. Validate against the schema that ships, or drop the schema and stop citing it, since the hand-written check does work — just less than advertised. Commit whatever produced the figure. Turn the described negative test into one that actually runs, and add a few more around the reason-coding while at it. The harder and more valuable step is scale: the argument is for a reusable instrument, and a small set of documents transcribed by hand demonstrates the idea without yet being the instrument. Automating extraction across a larger body of disclosures would make the case the paper wants to make.

