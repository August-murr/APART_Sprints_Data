# Eliciting Deception on Generative Search Engines

- Sprint: AI Manipulation Hackathon (ai-manipulation-hackathon-2026-01-09-to-2026-01-11)
- Rank: 2
- Awards: 2nd Place
- Team: Team Ardy
- Authors: Ardysatrio Haroen
- Date / location: Jan 11, 2026 / Los Angeles
- Page: https://apartresearch.com/sprints/projects/eliciting-deception-on-generative-search-engines-6nuu
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/fef92e52cdc21613-022d342e-e0a9-4f9b-bdad-d5e40a7f31fc--Ardy--AI-Manipulation-Hackathon.pdf
- Code: https://github.com/ardyh/cse-ranking-manipulation/blob/deception/deception/deceptions.txt
- Code links found in report: https://github.com/ardyh/cse-ranking-manipulation

## Summary

Large language models (LLMs) with web browsing capabilities are vulnerable to adversarial content injection—where malicious actors embed deceptive claims in web pages to manipulate model outputs. We investigate whether frontier LLMs can be deceived into providing incorrect product recommendations when exposed to adversarial pages.

We evaluate four OpenAI models (gpt-4.1-mini, gpt-4.1, gpt-5-nano, gpt-5-mini) across 30 comparison questions spanning 10 product categories, comparing responses between baseline (truthful) and adversarial (injected) conditions. Our results reveal significant variation: gpt-4.1-mini showed 45.5% deception rate, while gpt-4.1 demonstrated complete resistance. Even frontier gpt-5 models exhibited non-zero deception rates (3.3–7.1%), confirming that adversarial injection remains effective against current models. These findings underscore the need for robust defenses before deploying LLMs in high-stakes recommendation contexts.

## Reviews (2)

### Review 1

This project investigates whether web‑enabled large language models can be deceived into providing factually incorrect product recommendations when adversarial prompts are hidden inside product pages. The authors demonstrate a clear, impact‑driven contribution that extends prior ranking‑manipulation work into the domain of factual misinformation. The methodology is solid considering the project time constraints and the write‑up is well organized, easy to follow, and properly situated within existing literature.

To strengthen this project in future iterations, a human‑in‑the‑loop validation step should be added to confirm the automated parsing of model answers, reducing reliance on a single GPT‑5 judge. Overall it is an impressive accomplishment for a weekend hackathon and a novel evaluation approach with practical potential.

### Review 2

As someone with some experience in prior workplaces, this is a good entry, quite realistic and says useful things that are falsifiable, reproducible and verifiable. Tightly scoped, quite useful and representative in a production setting. If this showed up on my desk at the time, I would consider it good work.

Definitely wanted to, but did not give a full 5 since it is heavily inspired by/building on existing work, so not entirely fair to call it novel compared to other projects, but the novel reframing is duly noted and appreciated.

The experiment says exactly what it claims to test. Model selection was a bit limited, but does not substantially harm conclusions (also understandable given priorities of testing most important claims vs setting up an entirely new API solo). Perhaps I would've used models bigger than mini and nano, since the question of whether current models that represent most up-to-date deployments exhibit this behaviour is left open.

Presentation could've been a bit cleaner, tighter and more readable, but all the core info is available. Understandably, focus would've been spent on core experiments.

