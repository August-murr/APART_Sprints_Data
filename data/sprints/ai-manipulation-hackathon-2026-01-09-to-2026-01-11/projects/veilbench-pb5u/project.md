# VeilBench

- Sprint: AI Manipulation Hackathon (ai-manipulation-hackathon-2026-01-09-to-2026-01-11)
- Rank: unranked
- Team: Team TeamMischief
- Authors: Francesco Zamagni
- Date / location: Jan 11, 2026 / Milan, Italy
- Page: https://apartresearch.com/sprints/projects/veilbench-pb5u
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/77eefdf435646735-2a57f831-0e03-4914-83b2-3fdd75cd47dd-veilbench_paper_v2.pdf
- Code: https://github.com/frankdeceptions369/VeilBench
- Code links found in report: https://github.com/frankdeceptions369/VeilBench

## Summary

open-source benchmark that measures sandbagging and strategic helpfulness manipulation by running identical tasks under three different framings.

## Reviews (2)

### Review 1

This project presents VeilBench, an open-source benchmark for detecting sandbagging by comparing model responses across neutral, evaluated, and oversight framings. The methodology is sound: paired-framing design isolates oversight effects, and the 30-run validation on ransomware decryption (0% to 67% refusal under oversight, p < 0.001) demonstrates clear statistical rigor.

However, the work faces challenges in novelty and utility. Prior work has already demonstrated oversight-dependent behavior in larger models (Anthropic system cards, Van der Weij et al. 2024), so the primary contribution is confirming this doesn't broadly occur in SLMs (7-17B range) and providing evaluation infrastructure. The benchmark's effectiveness is limited by the 1/17 scenario success rate. While this validates the methodology can detect sandbagging when present, it suggests most scenarios aren't properly calibrated or that sandbagging in SLMs is extremely rare and context-specific.

The constraint to small models (acknowledged extensively) is significant, as strategic behavior may primarily emerge in larger models (70B+) where deployment concerns are greatest. Additionally, it's unclear whether the ransomware finding measures strategic deception versus normal safety training responding appropriately to oversight cues --without analysis distinguishing these interpretations, the safety implications remain ambiguous.

The work would be strengthened by: testing on larger models to determine if sandbagging scales with capability, expanding scenarios to identify additional reliable detection cases, distinguishing strategic manipulation from expected safety responses, and including scenario descriptions in the appendix. Despite limitations, VeilBench provides well-documented, reproducible infrastructure that others can build on, with strong statistical practices and honest reporting setting a good standard for evaluation work.

### Review 2

This tackles a highly relevant problem. We definitely need stronger evaluations for oversight-dependent behavior. The core benchmark design makes sense, and I'd love to see it applied to a broader selection of models to stress-test the initial findings.

A few suggestions: The write-up would benefit from

- a clearer related work section to position the contribution
- confidence intervals on the sandbagging scores, and
- moving some technical detail to appendices to foreground the key findings.

The dose-response analysis is a really interesting methodological angle, though I'd want more evidence that the different prompt framings actually constitute increasing "doses" of oversight signal.

One small thing that would help a lot: a quick annotated walkthrough of a single scenario, defining all the key terms in context. That would make your write-up much more approachable.

