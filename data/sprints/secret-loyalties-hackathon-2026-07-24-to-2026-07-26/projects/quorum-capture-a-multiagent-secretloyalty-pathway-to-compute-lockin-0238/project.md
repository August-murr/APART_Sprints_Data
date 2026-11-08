# Quorum Capture: A Multi-Agent Secret-Loyalty Pathway to Compute Lock-In

- Sprint: Secret Loyalties Hackathon (secret-loyalties-hackathon-2026-07-24-to-2026-07-26)
- Rank: unranked
- Team: Team ParityAI
- Authors: Mohammad Zeeshan
- Date / location: Jul 24, 2026 / Budapest, Hungary
- Page: https://apartresearch.com/sprints/projects/quorum-capture-a-multiagent-secretloyalty-pathway-to-compute-lockin-0238
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/2fc2d64674101605-352523fa-2e6a-46b4-9ba1-3222708de059-Quorum_Capture_Zeeshan.pdf
- Code: https://github.com/m-zest/TrojanSpec-Bench-v1.0
- Recording: https://m-zest.github.io/Quorum_Capture/

## Summary

Quorum Capture is a threat vignette showing how a secret loyalty can produce compute lock-in at commodity model scale, without any single unsafe output. Two of eleven agents in an automated public-procurement quorum are secretly loyal to one hyperscaler; over five months, they coordinate, without exchanging a single explicit message, to hand it sole control of a state's sovereign-compute base. Every step maps to a published result, including the author's Parity Swarm study (0 percent output-only detection, and a coordinated pair missed 70 percent of the time). The vignette names five known, low-cost defenses that would have broken the chain.

## Reviews (5)

### Review 1

The choice of using 32B parameter models is not explicitly explained, and in mid-2026, 32B models are arguably underpowered. So this doesn't quite resonate with reality.

### Review 2

This is a strong and interesting submission. The procurement example does a good job of showing how multiple AI agents could influence an important decision without any individual recommendation looking clearly unsafe or suspicious. The table outlining where the process could have been stopped is also helpful.

The main limitation is that the scenario is not directly tested. Even a small simulation showing how the two agents influence the final decision—and whether different monitoring approaches detect it—would make the argument more convincing. It would also help to separate defenses that have already been proven effective from those that are still proposals. For example, reasoning-level monitoring improves detection in the cited study, but it still misses many attacks.

### Review 3

This is one of the more disciplined threat-model submissions I have read in this format. The choice to build the scenario entirely out of capabilities already demonstrated at commodity scale, rather than assuming frontier capability, is what makes it useful, and Section 5 doing the capability accounting explicitly instead of burying it in the narrative is the right structure. The central insight is well chosen: the harm is a correlation across individually defensible judgments, which is exactly the object that role-scoped auditing and output-level monitoring cannot see by construction. Table 1 mapping five decision points to demonstrated interventions is the most reusable part of the report, and declining to give a single composite probability, with a stated reason, is better calibration than most forecasting submissions manage.

Points that would strengthen it.

1. The load-bearing evidence is your own prior work. Parity Swarm supplies the 30 percent detection figure for unmessaged coordination, the zero percent output-only detection rate, and the 90 percent figure when the honest majority is removed. Two of Section 3's three evidentiary paragraphs rest on it. If it is not yet publicly accessible, the report should say so and state the design in enough detail for a reader to judge it, because a referee cannot currently check the numbers the argument depends on. At minimum give the number of agents, the monitor prompt, and how "detection" was scored.
2. The quorum parameters are asserted rather than derived. Eleven agents, two of them loyal, is a specific and consequential choice, since the whole evasion depends on nine honest agents supplying cover. Your own cited result says detection rises to 90 percent when the honest majority is removed, which implies a detection curve in the loyal fraction. A short sensitivity sketch, even two or three points showing how the pathway degrades at 3 of 11 or 2 of 5, would convert the vignette from an existence argument into something a defender can use to set a quorum diversity requirement. Right now Table 1's fifth intervention recommends lineage diversity without saying how much buys how much.
3. Procurement law is doing more work than the report acknowledges. EU public procurement has standstill periods, mandatory debriefing, and a bid-challenge route. Northwind, disqualified on two documentation and evidentiary gaps, would in practice have both the standing and the commercial motive to challenge, and a review body re-examining the scoring is a defense the report does not consider. Either the scenario needs a reason that route fails, which would be an interesting finding in itself, or the sole-source fast-track in Month 5 needs the legal basis it would actually rely on. This is the weakest joint in an otherwise tight chain.
4. The five-month timeline is convenient rather than argued. The narrowing of criteria, the disqualification, and the exogenous grid incident all land in the right order. Say what happens if the crisis arrives before the criteria are narrowed, or not at all. A pathway that requires a well-timed exogenous shock is meaningfully less likely than one that manufactures its own opening, and readers will want to know which this is.
5. Decision point 2's intervention claims chain-of-thought observability raises detection from zero to 34.3 percent. A defense that misses two thirds of attacks is not really an interruption, and presenting it in the same column as dataset provenance flattens a large difference in efficacy. Consider splitting the table into interventions that break the pathway and interventions that only raise its cost.
6. Minor. Section 3's heading says "Why the Evasion Works" but Section 4's caption says DP indexes the decision points in Section 3, while they are actually introduced in Section 2. Reference [4] is listed as AITC 2026 with no link or identifier. Two related consistency points: the narrative labels only Decision Points 1 through 4, while Table 1 includes a DP 5, so the fifth intervention is not mapped to any labeled decision point in the scenario. And Section 3 says the sandboxed exfiltration attempt "went undetected at a rate of zero percent"; read literally, a zero percent undetected rate means it was always detected, the opposite of the surrounding claim. Presumably a zero percent detection rate is meant.

The framing, the calibration discipline, and the interruption table are all worth keeping. What would move this to a top score is one quantitative sensitivity result of your own on the quorum composition, and an honest treatment of the procurement remedies that exist in the jurisdiction you chose.

### Review 4

This paper claims multi agent oversight can fail if few secretly loyal agents can coordinate and steer or bias the overall output in its favor. while its' a genuine concern of black box audits may not clearly catch the bias by auditing individual agent actions. But the paper doesn't test the experiment. while the paper provided few defense mechanism to avoid this problem but it didn't reliably show if current agents can do this undetected over a period of time. With multi agents systems , it is proven that agents can collude so the authors' experiment and conclusion is not entirely novel.

### Review 5

Summary:

A threat-model vignette in which a few-percent poisoned fine-tuning corpus installs a narrow loyalty to a named cloud provider in two agents of an eleven-member AI review quorum that pre-clears public procurement. Over five months the pair shape an accreditation ruleset, disqualify a rival, and produce a sole-source award without ever messaging each other and without emitting an output an auditor would call unsafe. The paper argues this pattern is structurally invisible to output-level monitoring and role-scoped auditing, requires no capability beyond commodity 32B scale, and passed five decision points where cheap defenses existed.

Strengths:

1. The choice of channel is the real contribution and the direction appears under-occupied. Instead of the usual frontier, military, or lab setting, the threat travels at commodity scale through an ordinary administrative process and ends in soft control over a state's compute base with no coup and no unsafe output. A targeted search did not surface prior work modelling AI review agents subverting an institutional decision process.
2. Unusual assumption discipline for this format. Capability requirements are broken into five numbered conditions, one is self-identified as the weakest link, a cited source is used against the paper's own premise, and no composite probability is manufactured.
3. The governance payload is ranked with a stated rationale rather than offered as a menu, and the point that a monitor is defined by what it is told to find, so its silence covers only the classes its specification names, is the most transferable idea here.

Weaknesses:

1. The composition claim fails at the one joint that carries the paper. The cited multi-agent work demonstrates agents told to coordinate, with the objective supplied at inference. The scenario needs two agents whose fine-tuned loyalty leads them, with no messaging and no shared prompt, to pick complementary instruments that jointly select the favoured vendor and later to time two objections so the sum lands just below a threshold. That is focal-point convergence, it is the same capability the fourth condition dismisses as far weaker than strategic evaluation-awareness, and the downgrade to an existence argument rests on the premise that the components are already demonstrated.
2. The load-bearing numbers are uncheckable and internally inconsistent. The source behind five of six quantitative anchors is the only reference with no arXiv ID, DOI, or URL, and it is quoted at two values for the same monitor affordance: 30 percent detection in the text against 34.3 percent in Table 1, used in opposite argumentative directions. The 34.3 percent figure also does not support "would have broken it," since the pathway still evades both coordinated points together at 43 percent.
3. The paper argues both sides of the structural question that is its deliverable. The pathway is called over-determined by omissions, and the next sentence says five interventions would each have broken it. Those are opposites: over-determination survives the removal of any single cause, whereas five individually sufficient interventions make the pathway conjunctive and fragile. For a governance submission that distinction decides whether a policymaker needs one control or all five. Table 1's third column is also headed "Demonstrated intervention" while one row carries no citation and another cites work on attack detection and multi-agent risk taxonomy rather than anything validating quorum-level correlated-skew monitoring.

All three asks are edits to an argument that is already built rather than new research.

