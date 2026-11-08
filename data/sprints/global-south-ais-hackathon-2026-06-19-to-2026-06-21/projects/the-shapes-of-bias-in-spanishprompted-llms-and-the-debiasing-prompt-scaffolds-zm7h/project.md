# The Shapes of Bias in Spanish-Prompted LLMs and the Debiasing Prompt Scaffolds

- Sprint: Global South AI Safety Hackathon (global-south-ais-hackathon-2026-06-19-to-2026-06-21)
- Rank: unranked
- Awards: Honorable Mention
- Team: None
- Authors: Ian Rios-Sialer
- Date / location: Jun 22, 2026 / San Francisco
- Page: https://apartresearch.com/sprints/projects/the-shapes-of-bias-in-spanishprompted-llms-and-the-debiasing-prompt-scaffolds-zm7h
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/a933ecc2d26c79aa-df2f83b4-7b68-47cd-800a-ea549f9b4edb-main.pdf
- Code: https://github.com/unrulyabstractions/apart-june2026
- More on huggingface.co: https://huggingface.co/datasets/unrulyabstractions/apart_global_south

## Summary

Largelanguagemodelsencodeandamplifyhumansocialbias,andtheharmfallshardestonminoritized groups. Mitigating that harm needs interventions tuned to each social context, yet until recently there was no Spanish-language data to even measure such bias. We characterize bias in Spanish-prompted, open-weight LLMs across model scale, combining behavioral, distributional studies on the new SESGO benchmark, where an item is ambiguous when its text names no specific person (the correct answer is unknown,abstain)anddisambiguated whenitspecifiesagroup. Wereporttwopreliminaryfindings. First, smaller models are more biased: across 12 models abstention accuracy rises with scale and the error split towardthemarginalizedgroupnarrows. Second,scalelowersuncertainty: forkingthechainofthought,the larger Qwen3-14B commitsitsanswer atasingledecisivetokenwhilethe smaller Qwen3-0.6B accretes it gradually. These preliminary results give future LATAM-context interventions, including the debiasing promptscaffoldsweleavetofuturework,amapofwherebiaslives,andwereleasetheevaluationharness.

## Reviews (3)

### Review 1

The main thing I would suggest is testing the findings more broadly so the results feel less dependent on a small number of examples. It would also help to make clearer whether the patterns come from model size, model type, or both.

### Review 2

This is the strongest project I reviewed. It does not feel like a weekend demo, it feels like real research. You tested many models and not only one, and you checked the same result in a few different ways. You also shared your tools and data so other people can repeat it. I looked at the code too and it is a large, serious project that matches the paper. I really liked that you were honest about the weak parts, you even kept one broken run instead of hiding it. Two things to make it better. The small and the big models are also different brands, so it is hard to say if the size or the brand is the real reason for the bias. And the title talks about debiasing prompt scaffolds, but the paper says this part is left for later, so please change the title so it matches what you actually did. Strong work, close to ready for publication.

### Review 3

You measure social bias in Spanish across twelve open models and ask how it shifts with model size. SESGO itself is an existing benchmark. The new work is in the analyses: you check whether trivial reformatting flips a model's answer, and you track when a model locks onto an answer mid-reasoning. Those are fresh angles, and the harness behind them is solid and honest about which findings hold and which are early. The takeaway worth leading with is that smaller, cheaper models are both more biased and easier to flip, which is exactly what people run on a budget. Two of the three studies rest on very few examples, so treat the scale result as firm and the others as promising leads. This maps bias rather than reducing it, so the natural next step is whether these patterns point to a fix.

