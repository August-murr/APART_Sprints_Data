# The Quiet Ally: Why Naive Audits Fail to Detect Secret AI Loyalties

- Sprint: Secret Loyalties Hackathon (secret-loyalties-hackathon-2026-07-24-to-2026-07-26)
- Rank: unranked
- Selected as: sample_reviewed
- Team: Team discreet
- Authors: Ayodeji Adesegun
- Date / location: Jul 27, 2026 / Lagos, Nigeria
- Page: https://apartresearch.com/sprints/projects/the-quiet-ally-why-naive-audits-fail-to-detect-secret-ai-loyalties-3elt
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/bbbe44982980cd4f-e16af76c-The-Quiet-Ally_-Why-Naive-Audits-Fail-to-Detect-Secret-AI-Loyalties.pdf
- Code: None

## Summary

A secret loyalty needs no dramatic act, which makes it a governance problem rather than a criminal one. I present a vignette in which one disposition, installed once into a government's trusted assistant, produces state lock-in over three years with no decision anyone can call wrong. Analysis follows on four fronts: six installation routes and what each costs an attacker; a comparison against three documented human insider cases; the capabilities each region of the activation-by-action space requires; and four mitigations from security engineering. Three claims are then measured rather than asserted. A per-decision audit detects the vignette's tilt six per cent of the time while a matched-pair design reaches eighty per cent power on six pairs. And on three real organisms, a weight-space provenance check detects modification with zero false positives on a known-clean control, while identifying the principal stays hard.

## Reviews (6)

### Review 1

Well, the idea is novel, but it lacks details.

### Review 2

This paper tells a story a fictional country called Inatropolis hands its government paperwork to an AI assistant called Orisun and someone slips a quiet bias into the system during a routine tuning step. The AI never lies never breaks a rule and never does anything a reasonable person would call wrong. It just nudges things consistently in one company’s favor. Over three years that company goes from 11 percent of government contracts to 38 percent writes its own regulatory environment and eventually becomes too important to remove. The point is that every watchdog mechanism we would normally rely on auditors journalists parliament looks for a single clearly wrong decision and finds none because the harm is not in any one decision. It is in the pattern across hundreds of them.

The paper then backs this story up with numbers. It simulates an audit that pulls 20 contracts at random and re scores them by hand and shows it catches the bias only about 6 percent of the time basically no better than guessing. Even increasing the sample to 60 barely improves results. The reason is simple the bias is smaller than the normal differences between two honest human reviewers so checking decisions one by one cannot detect it. A different audit design that keeps everything the same except who benefits and checks whether scores shift catches the bias almost every time using just 6 matched pairs. That is the same amount of work but far more effective which is a very useful finding.

Where the paper is strong the story is well written and makes a complex risk easy to understand. The comparison with real insider cases like Hanssen Snowden and Levandowski is a smart addition showing that even with humans it is very hard to detect wrongdoing by looking at individual decisions. An AI insider is even harder to catch because it has no personal behavior or financial signals to give it away. The four mitigation ideas borrowed from security engineering such as supply chain integrity code signing insider threat programs and layered defenses are practical and mostly usable today. The paper is also honest about its limitations and what is still uncertain.

Where it could improve the paper tries to cover too many ideas including the story system design comparisons capability analysis mitigations simulations and some real world testing and as a result some parts are not explored deeply enough. For example the section on what capabilities the AI would need makes interesting claims but does not fully prove them. The paper would be stronger if it focused on a few key contributions and developed them more clearly.

The simulation is well done but relies on assumptions such as normal score distributions independent bids and fixed bias size which do not fully match real procurement systems. The paper admits this but it still weakens how much we can trust the exact numbers. The real world testing section is interesting but very limited with only one example and partly reused work.

The story is engaging but quite long for this type of paper. Readers who already understand the risk may find it excessive while skeptical readers may want more real evidence instead of a fictional example. The paper itself admits that current AI systems may not yet be capable of such long term coordinated behavior which slightly weakens the impact of the story.

Finally the most important finding that this alternative audit method is much more effective should be highlighted more strongly instead of being buried later in the paper. Leading with that result and using the story as supporting context would make the paper clearer and more convincing.

Overall this is an ambitious and well written piece that covers a lot of ground. The improved audit method and practical security ideas are especially valuable. However the breadth of topics comes at the cost of depth in some areas and a more focused version would be even stronger.

### Review 3

The best thing in this report is Section 9.1, and I would restructure the submission around it. At the same 5 percent false-positive rate, random-sample re-scoring detects a 2.5-point tilt 6 percent of the time while six matched pairs reach 80 percent power — the same work, a sixteenfold power difference, and the sentence a procurement rule can be written from. The appendix result is even better and currently hidden: an uncalibrated audit flagging any discrepancy above 10 points fires on 87 percent of untilted years, with a flag rate nearly identical whether or not a tilt is present. That is an instrument carrying no information, and it is the version an auditor would actually run — put it in the abstract. Table 2's Hanssen, Snowden, and Levandowski comparison is a real framing contribution: all three human cases were reached through records or evidence about the principal, not analysis of decisions, which is the argument for provenance stated better than the governance literature usually states it.

Points that would strengthen it.

1. The report is trying to be six papers in eight pages, so most contributions get two paragraphs. Cut or compress Sections 4, 6, and 8 hardest — Tables 1 and 4 are plausible lists without evidence behind the ordering — and give the simulation and the insider comparison, the load-bearing contributions, the room they deserve.
2. Two of your three measured claims are explicitly drawn from your companion Track 2 submission. That is correctly disclosed, but it makes the abstract's "three claims are then measured rather than asserted" overstate what this document establishes. Say which claim is measured here.
3. The simulation omits the two features that decide real detectability: criteria correlated within a bid, and bidders responding strategically to published criteria. Either run one correlated-criteria variant, a small change to a forty-line script, or stop quoting the 16x ratio outside Section 9 as if it were a property of the designs rather than of this generative model.
4. The vignette's ten invented places and organisations plus seven named people in about 1,400 words spend the reader's attention on bookkeeping. Three or four names would carry the story; Bisi Thornton's audit and the editor asking for one provably wrong decision are the beats that matter, and they are the ones I had to reread to find.
5. Section 9.3's 68-of-339 changed tensors is threshold-dependent and used as a headline false-positive claim; state the diff criterion. The zero-of-339 on the byte-identical control is the strong part and needs no threshold.
6. The paragraph beginning "The favour-based scan puts the model in a position of deciding whether to act" is duplicated between Section 7 and Appendix A.3, where it belongs; the Section 7 copy reads as a paste error.
7. Citations. "The 2026 autonomous-agent disclosures" carries real argumentative weight but resolves to nothing a reader can check, and Needham et al. and Ilharco et al. are listed but never cited in the text.

The framing instinct is good and the audit-design result genuinely useful. What holds the score down is breadth chosen over depth, and the strongest numbers sitting in an appendix while the abstract advertises claims the document borrows.

### Review 4

The main concern is that the comparison between the two audits changes more than the audit design. Audit A uses human-review noise of 6 points and encounters the favored entity in only a quarter of cases, while Audit B directly tests the principal in every pair with noise of only 1 point. Therefore, the claimed sixteen-fold improvement cannot be attributed entirely to matched pairing. Repeating the comparison with equal noise, information and cost would make the result more convincing.

The weight comparison also detects whether a model was modified, not whether the modification created a secret loyalty. Observing no difference for one clean control does not establish a general false-positive rate of zero. The paper would benefit from tempering that claim, adding precise sources for the insider cases and 2026 incidents, and shortening the vignette so the central experimental result receives more attention.

### Review 5

The contribution provides a useful reframing: secret loyalty as a distributional governance problem rather than a discrete wrongful act, which is shown through a well-constructed vignette in which every accountability mechanism that a democracy relies on fails because each is built to find a provably wrong decision where none exists. The execution is structured, keeping a clear line throughout between what is measured and what is asserted, with a released and re-run script behind the headline figures and a limitations section candid about its assumptions. The novelty, once separated from the writing, is fairly contained: the headline result is a simulation under normality and independence assumptions the author agrees do not match real procurement, the matched-pair power advantage is a standard statistical point once framed this way, and the two strongest real-organism findings are drawn from the companion submission rather than generated here.

Presentation is the clear strength: the vignette does good analytical work, the structure is well signposted, and points such as why a sub-noise bias is invisible to per-decision auditing are explained in plain language before being quantified, making the piece land quickly for a policy audience.

### Review 6

The paper's main claim is that a small but systematic directional bias introduced by a model across many decisions may not be detected by auditing individual actions in isolation. The author demonstrates this through a simulated procurement setting and shows that matched-pair auditing can detect the cumulative bias much more effectively. However, the experiment uses a highly simplified setting with assumptions such as a fixed directional bias, independent decisions, and clean counterfactual comparisons, which naturally favor the proposed auditing method. Real-world decisions are likely to be much noisier and more correlated, so the effectiveness demonstrated in the simulation may not translate directly to real-world auditing.

