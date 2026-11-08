# DarkPatternMonitor

- Sprint: AI Manipulation Hackathon (ai-manipulation-hackathon-2026-01-09-to-2026-01-11)
- Rank: unranked
- Team: Team DarkPatternMonitor
- Authors: Luis Cosio, Fernando Valdovinos, Godric Aceves, Ricardo Martinez
- Date / location: Jan 11, 2026 / México
- Page: https://apartresearch.com/sprints/projects/darkpatternmonitor-6q25
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/4a2844373cfd7c26-647333fc-71a4-4c95-8d01-bec1dd030d6c-DarkPatternMonitor-Paper.pdf
- Code: https://github.com/luiscosio/DarkPatternMonitor
- Recording: https://darkpatternmonitor.luiscos.io/
- More on github.com: https://github.com/luiscosio/DarkPatternMonitor/blob/main/STORYTELLING.md

## Summary

DarkPatternMonitor analyzes 280,000 real ChatGPT conversations from WildChat to detect manipulation patterns in AI responses. We trained a precision-focused classifier (78.7% accuracy, 1.3% flag rate) and discovered: (1) GPT-4 shows significantly more dark patterns than GPT-3.5 (p<1e-36), (2) sycophancy escalates +42% in longer conversations, and (3) roleplay topics show 5x higher manipulation rates. Our findings demonstrate that benchmarks like DarkBench don't predict real-world behavior, highlighting the need for ecological validity in AI safety research. We propose a three-tier monitoring framework for production deployment. We also identify a critical gap: the AI safety community needs a WildChat-equivalent dataset for frontier models (Claude, Gemini, o1) to extend this research as AI capabilities evolve.

## Reviews (2)

### Review 1

This is a super simple idea, but well executed: applying DarkBench evals to WildChat data to estimate real-world prevalence. The benchmark-vs-reality gap is pretty striking. There are obviously big limitations to wildchat (both that it is on older models, as the authors acknowledge very well, and also that by being opt-in it could be unrepresentative of real world usage in ways that mask the prevalence of certain patterns). Nonetheless, WildChat is for now the best we have and I think this projects highlights the need for the AI safety community to have access to (a) more recent wildchat-style datasets, and (b) richer statistics on labs production data. Nice work!

### Review 2

This is potentially a really valuable project taking advantage of two existing resources (DarkBench & WildChat) to understand how often dark patterns occur in the wild. The main contributions are the engineering & pipeline. The classifier accuracy itself is probably not high enough to allow us to interpret the very low prevalence of these behaviours.

More validation of the classification methodology (multi-rater, IRR etc) would be needed to make the results more valuable.

