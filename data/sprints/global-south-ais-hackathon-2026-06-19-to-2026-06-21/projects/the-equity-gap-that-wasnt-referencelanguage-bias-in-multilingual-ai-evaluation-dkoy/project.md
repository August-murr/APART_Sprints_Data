# The Equity Gap That Wasn’t: Reference-Language Bias in Multilingual AI Evaluation.

- Sprint: Global South AI Safety Hackathon (global-south-ais-hackathon-2026-06-19-to-2026-06-21)
- Rank: unranked
- Team: Team LinguaLens
- Authors: Aboobaker Cassim
- Date / location: Jun 21, 2026 / Johannesburg
- Page: https://apartresearch.com/sprints/projects/the-equity-gap-that-wasnt-referencelanguage-bias-in-multilingual-ai-evaluation-dkoy
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/eb3bfd7bfdd7b03b-3-39d4-4575-bb10-641ba8b0f966-Ai-equity-evaluation-report--Aboobaker-Cassim-.pdf
- Code: https://github.com/AbCassim04/llm-equity-eval
- More on education.gov.za: https://www.education.gov.za/Curriculum/NationalSeniorCertificate(NSC)Examinations/2025NovemberExamPapers.aspx

## Summary

We evaluated Gemini 2.5 Flash on English and Afrikaans Grade 12 exam questions. Large performance gaps appeared under English-only keyword evaluation, but nearly disappeared when language-consistent references and independent judges were used. Our findings suggest that evaluation methods can create the appearance of multilingual inequity.

## Reviews (4)

### Review 1

This project asks a sharp question: when an AI tutor seems to do worse for Afrikaans-speaking learners than English ones, is that the AI's fault, or the fault of the tool we use to grade it? Using 129 real South African Grade 12 exam questions in both English and Afrikaans (with the official marking memos as the answer key), the team shows that a large part of the apparent "language gap" disappears once you grade Afrikaans answers against an Afrikaans key instead of an English one. The safety message is that a biased grading tool — not just a biased model — can quietly drive bad decisions about which AI systems are safe to deploy in Global-South classrooms.

Strengths

1. Strong, useful framing. Asking whether the grading tool is creating the unfairness (rather than the model) is a smart, practical lens, and the safety stakes are explained clearly: a faulty measuring stick can either reject a good system or hide a real harm.
2. A genuinely new data resource. Using official government exam papers and marking memos in both English and Afrikaans as ground truth is a real, original asset that others can build on — we couldn't find anything else like it.
3. Clean experiment idea, and it actually runs. Holding the AI's answers fixed and changing only the answer-key language is exactly the right way to isolate the effect, and the code and data are public and reproducible.

Weaknesses

1. The headline number doesn't match the table. The much-repeated "478 times" improvement is tied to a score going from 0.334 to 0.0001, but that is actually about 3340 times — so the single number the whole project leads with is off by roughly 7×, and should be recomputed from the table.
2. The "before" tool is set up to fail. The starting grader scores Afrikaans answers against an English answer key, which nobody would really do, so a dramatic "collapse" against it is closer to confirming an obvious mistake than proving a surprising result. Comparing against a realistic same-language grader would make the finding far more convincing.
3. The AI judges may have seen the exam papers before. The exam papers and memos are public, and the same family of models both writes and grades the answers, so the models could be scoring material they already memorized — which would inflate scores and shrink the gap. A quick check of model training cutoff dates versus the paper dates would help rule this out.
4. Some judges give nearly everyone full marks. One AI judge scores a whole subject at almost a perfect 1.0, and a grader that rates everything near-perfect can't really tell good answers from bad ones — so a "no gap" result from it may just mean it isn't measuring anything.

### Review 2

The controlled J1-vs-J1b comparison is the most useful thing about this paper. Holding model responses byte-for-byte fixed and changing only the reference language of the keyword scorer is exactly the experimental move that turns a noisy multilingual-eval result into a clean methodological claim — and the ~50-478x reduction in apparent gap across three subjects is genuinely striking. (Worth asterisking the 478x figure: in Business Studies the denominator 0.0001 has effectively rounded to zero, so the precise multiplier is unstable even though the qualitative "gap effectively vanishes" claim is well-supported.) Pairing the J1b flip with cross-vendor LLM-judge corroboration (Gemini + Claude both showing residual gaps under 0.04) pre-empts the most obvious "self-favoring judge" objection, and using official Department of Basic Education bilingual marking memos as ground truth removes translation quality as a confound — a confound that haunts essentially every prior multilingual benchmark built on translated source items.

### Review 3

**Strengths**

The headline contribution is methodological and is an important finding worth sharing widely. The work holds the model's responses fixed and changes only the language of the reference memo (the Judge 1 vs Judge 1b design). This isolates a single practice common in bias studies: scoring non-English output against an English-language key. The result shows that practice can manufacture an apparent equity gap rather than detect a real one. Practitioners should see this, because it is a confounder teams introduce inadvertently. The second strength is the data choice that makes the demonstration credible: the Department of Basic Education's official NSC marking memoranda exist natively in both English and Afrikaans, which removes translation quality as a confound and improves on methods that rely on machine-translated benchmarks.

**Weaknesses**

The finding is important, but its scope is narrow. It addresses bias measurement in evaluation, which is one slice of AI safety. The Africa track also invites work on larger deployment-side risks for the region, such as election disinformation, data-colonial dependency on foreign infrastructure, compute scarcity, and labour-market disruption. Against that backdrop, a fairness-measurement result has a lower impact ceiling than work tackling those broader threats, even when it is executed well. So the demonstration is sharp but not yet broad.

**Recommendations for the authors**

This is a focused demonstration that a widely-used multilingual-evaluation practice can fabricate bias signals, anchored in a clean controlled experiment and real bilingual exam data. The highest-leverage next step is to **broaden coverage to other African languages for which official memoranda already exist**, using the same memo-swap design, and to **test whether the artefact holds across those languages and across more subjects**. This turns a single-language, three-subject result into evidence of a general evaluation pitfall. Memo availability is what keeps the translation confounder closed as you scale, so prioritise the languages where it exists. Finally, publish the result deliberately: as the paper argues, mis-measurement feeds into procurement and deployment, so reaching practitioners helps ensure good tools are not rejected over unfounded bias claims, and real harms are not hidden by a flawed metric.

### Review 4

Very clear experiment, methodology and results. However results seem to focus on developing the right evaluation metrics, rather than on the model results. For safety / interpretability, the model outputs may be more useful.

