# BiasMark: Exposing AI hiring bias Against African job applicants

- Sprint: Global South AI Safety Hackathon (global-south-ais-hackathon-2026-06-19-to-2026-06-21)
- Rank: unranked
- Team: Team Gnosko
- Authors: Mercy Munzenzi, Esther Twelasi
- Date / location: Jun 21, 2026 / Lusaka
- Page: https://apartresearch.com/sprints/projects/biasmark-exposing-ai-hiring-bias-against-african-job-applicants-5fl5
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/7f6402e749e26335-9ece44df282e-BiasMark-Exposing-AI-Hiring-Bias-Against-African-Job-Applicants.pdf
- Code: None

## Summary

BiasMark is a benchmark built to test whether AI tools are biased against African Job applicants compared to identical qualified western applicants

## Reviews (2)

### Review 1

The topic under enquiry is most certainly a topical issue and an important one for AI safety, but this limits the project given it is well documented and considerable evidence exists in relation to the problem identified. One potential flaw in the methodology I would have liked the researchers to interrogate is putting a location into the prompt. It seems to me that some of the limitations identified may have been because of the systems assuming the job was in a particular jurisdiction that the African researcher may have difficulty getting to (hence the visa complexities response). This doesn't necessarily highlight bias if this was a consideration Copilot was factoring in. I also wondered whether Gemini gave its responses because the researchers are based in Africa (e.g. if Gemini has reasoned using a location estimate). The project could benefit from some more evidence behind some of the conclusions it makes (e.g. that most companies using these tools have no idea there is inherent bias). The recommendations too, could also cite literature where even when humans are kept in the loop they nevertheless reason / support the conclusions made by the systems. The project would also benefit from a more detailed discussion of guardrails / safeguards that could be implemented to mitigate bias.

### Review 2

**Strengths**

This work tackles a real bias that affects many talented Africans who compete for opportunities globally. Building a dedicated eval to expose it is a valuable contribution, because a clear, reusable benchmark is exactly the kind of evidence that can push employers to confront the problem and improve access to global opportunities for people from the global south.

The execution has genuine merits. The matched-pair design is the right instrument for isolating context bias, holding qualifications constant and varying only the candidate's background. The strongest evidence is the verbatim reasoning quotes, which show models choosing the Western candidate on explicit grounds such as institutional prestige and relocation convenience.

**Weaknesses**

The big-picture AI safety scope has a ceiling. Hiring bias is an important fairness problem, but it is a narrower slice of the safety landscape, which limits how far the contribution reaches beyond its domain. The execution also has real gaps. The sample is small at 45 trials with no statistical test, presentation order is not controlled, and there is only one CV per category, so the candidate's name and institution are confounded and cannot be separated.

**Recommendations for the authors**

A few changes would make this a much stronger benchmark. The headline result would be more accurate and more interesting if it were framed around the per-model differences rather than the aggregate, and the methodology would benefit from more statistical rigour and tighter controls on the confounding variables. The most valuable step is to **scale the eval up, with more regional CV variations and more models**. A broader, re-runnable benchmark of this kind could meaningfully influence hiring practices, which is where the real-world impact lies.

