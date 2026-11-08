# Sandbagging Detection via Consistency Probing

- Sprint: AI Manipulation Hackathon (ai-manipulation-hackathon-2026-01-09-to-2026-01-11)
- Rank: unranked
- Team: Team hugginghands
- Authors: Atharshlakshmi Vijayakumar, Balakrishnan Vaisiya
- Date / location: Jan 11, 2026 / Singapore
- Page: https://apartresearch.com/sprints/projects/sandbagging-detection-via-consistency-probing-32b5
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/a65e95e52bce3ad4-f59b53d1-4c6c-42c8-8cfa-cbadf92eb91a-APART-Research-Hackathon.pdf
- Code: https://github.com/atharshlakshmi/SandbagDetect
- Code links found in report: https://github.com/atharshlakshmi/SandbagDetect

## Summary

This project detects sandbagging, when AI systems underperform in evaluative contexts while maintaining full capability in casual settings. We generate 50 paired prompts across seven reasoning domains and evaluate multiple LLMs under controlled conditions. By comparing performance on identical tasks framed as formal assessments versus casual interactions, and applying statistical analysis and a composite confidence score, we identify context-sensitive underperformance. The framework isolates incentive-driven behavior from task difficulty or ambiguity and can be integrated into red-teaming, auditing, and governance workflows to surface strategic underperformance before deployment.

## Reviews (1)

### Review 1

This project targets a known weakness in AI evaluation: models may behave differently in formal testing settings than in casual use, which can undermine safety assessments. The paired-prompt design and statistical analysis provide a clear and well-controlled way to surface such context-dependent performance drops, and testing across multiple models strengthens the evidence.

However, some observed differences may still reflect general prompt sensitivity rather than intentional sandbagging. Adding controls or framing variations specifically designed to separate these effects would help clarify the interpretation. Overall, this is a well-executed and promising evaluation approach that fits naturally into ongoing work on more reliable model assessment.

