# Secure Scope AI

- Sprint: Global South AI Safety Hackathon (global-south-ais-hackathon-2026-06-19-to-2026-06-21)
- Rank: unranked
- Team: Team Free-thinking engineer
- Authors: Elvin Vidal Mollinedo Mencia, Jazid Andrey Ovando Durán, Annett Alejandra Cruz Rojas, Miguel Angel Vega Moreno
- Date / location: Jun 22, 2026 / Santa Cruz - Bolivia
- Page: https://apartresearch.com/sprints/projects/secure-scope-ai-qwgz
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/842e7416c318fc6c-04dab158-b09f-4022-96ac-6361757e676a-SecureScopeAI.pdf
- Code: https://github.com/elvinmollinedo/SecureScopeAI
- Code links found in report: https://github.com/elvinmollinedo/SecureScopeAI, https://github.com/OWASP/NodeGoat, https://github.com/aquasecurity/trivy
- Recording: https://drive.google.com/file/d/16SFqPBlGR6o8gfxhg-DBqKoTR2msJ5Zl/view

## Summary

Secure Scope AI is an AI-powered cybersecurity agent that integrates natively into DevSecOps pipelines, combining a deterministic vulnerability-correlation engine (Trivy + OWASP Dependency-Check) with a provider-agnostic Multi-AI Engine (DeepSeek, OpenAI, Gemini, Azure OpenAI, or local models via Ollama) to prioritize risks and generate actionable remediation. Unlike traditional scanners, the AI never detects vulnerabilities directly — it only contextualizes, prioritizes, and proposes fixes or compensating controls over findings already validated by deterministic tools, reducing hallucination risk. The platform is offline-first and can run fully on-premise, preserving data sovereignty for organizations in the Global South. Validated on three reproducible pipelines over OWASP NodeGoat, correlating 366 vulnerabilities per run in ~3–4 minutes.

## Reviews (4)

### Review 1

This is a polished, complete, full-stack DevSecOps platform — code, README, demo video, presentation, and a coherent report. The central design choice is genuinely sound and well-articulated: the AI never detects vulnerabilities; a deterministic engine correlates/dedupes Trivy + Dependency-Check output first, and the LLM only contextualizes the validated list. That "verifiable source of truth before inference, graceful degradation when no provider" framing is the right pattern for LLMs-in-security and is the project's real contribution. Main issues:

The AI-safety contribution is thin relative to the engineering. Most of the work is a competent integration of existing tools (Trivy, Dependency-Check, Django/Celery, DeepSeek) into a clean pipeline. That's valuable as a product, but the novel safety insight — "don't let the LLM be the detector; gate it behind deterministic evidence" — is sensible rather than new, and isn't empirically tested as a safety claim. The report states it reduces hallucinations but never measures hallucination rate, which is the experiment that would substantiate it (and which they list as future work).

The results are operational metrics, not an evaluation. The headline numbers — 366 vulns per run, ~3–4 min, AI in 17s — demonstrate that the pipeline runs and that SCA (not the AI) is the bottleneck. That's a feasibility demonstration, not a measurement of whether the AI's prioritization or remediations are correct. The report is admirably explicit that they "did not quantitatively compare against human analysts nor formally measure the precision of the LLM's recommendations." So the core value proposition (better triage) is asserted, not shown.

Single target, three near-identical runs. All evaluation is on OWASP NodeGoat, and the three pipelines return the identical 366 figure — which confirms determinism/reproducibility but adds no coverage. One application can't tell you how correlation or prioritization behaves across languages, sizes, or ecosystems.

The prompt-injection threat is named but unaddressed. They cite the right literature (Greshake, multilingual jailbreaks, OWASP LLM Top 10) and run untrusted repos inside the pipeline — but the report concedes injection isn't resolved and isolation needs hardening for production. For a security tool that ingests untrusted code and feeds derived content to an LLM, that's the most important threat, and it's deferred.

The "108 critical / 528 high accumulated" framing is slightly misleading — it's the same 36/176 counted three times. The report does label it "accumulated," but leading with the inflated number in the abstract oversells scale.

### Review 2

This is a working system with a solid design for AI safety. The model does not identify vulnerabilities directly, a deterministic engine processes the output of a vulnerability scanner, generates a list of confirmed vulnerabilities, and serves as the definitive source of information. Then the LLM will simply interpret the already vetted evidence provided by the deterministic engine. Each of these choices: separating deterministically generated observations from AI-generated conclusions; gracefully degrading to a CVSS-based approach if there is no model available; and designing the system in an offline-first manner that works regardless of the third-party provider(s), can be transferred as general principles vs. being merely implementation specific. I also believe this has excellent reproducibility capabilities (one-command deployment, commit hash included in each run, a completely public repository, etc.).

Ways to make it better:

(1) Evaluate the quality of your AI layer (not just its speed). Your "runs" indicate that the system is fast and that the scanner phase is the slowest portion, but you have not shown that the model provides good prioritized remediation recommendations. In order to prove that the AI adds or removes value from your pipeline, add metrics for recommending precision, usefulness, and hallucination rates compared to either a human analyst or a trusted remediation set.

(2) Run additional applications other than NodeGoat. All results are based upon running a single intentionally vulnerable application. By running multiple actual projects written in many programming languages, you should be able to verify whether the correlation and priority remain consistent across scale and ecosystem boundaries.

(3) Assess the potential threat vector we discussed regarding injecting malicious code into the LLM stage through a dependency or advisory description. A simple adversarial testing of the described mechanism could demonstrate how effective the structured-output defense mechanisms and post-hoc validations are.

(4) Emphasize your baseline assumptions. As long as you depend on Trivy and Dependency Check (which produce false positives and false negatives), provide some documentation on their limitations so that users of the tool understand how much trust they can place in the final report.

### Review 3

App, pipeline, video, reports, tests, and local deployment, this is basically a working product (if not fully complete), not just a paper. Congratulations!

The offline-first and provider-agnostic design is your strongest angle, especially for LATAM. That’s particularly valuable right now given the recent issues with Fable and the limited release of gpt-5.6 for partners and select US companies.

On the AI safety/alignment research side, it’s a very crowded space, between research and for profit companies: Snyk, Mend, Endor Labs, ArmorCode, Wiz, etc. (I’ve also invested in two similar projects myself: aihackers.inbest.cloud and getobok.com).

As for a for profit, it's not that crowded, I would recommend pursuing it.

### Review 4

The project is interesting and appears to be technically well executed. It is relevant for cybersecurity. The architectural decision to separate deterministic evidence from AI interpretation is principled and well-executed. The discussion of related work and how this project differs and contributes could have been more thorough. Additionally, as the project claims to be especially suitable for Global South contexts, the submission could have been strengthened by engaging more substantively with the specific resource constraints of these contexts (e.g., connectivity, infrastructure costs, database update reliability) and how the design choices address them.

