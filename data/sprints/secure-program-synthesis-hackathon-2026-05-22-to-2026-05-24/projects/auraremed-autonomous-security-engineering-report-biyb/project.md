# AuraRemed: Autonomous Security Engineering Report

- Sprint: The Secure Program Synthesis Hackathon (secure-program-synthesis-hackathon-2026-05-22-to-2026-05-24)
- Rank: unranked
- Team: Team AuraRemed
- Authors: Santiago Rodriguez Heras
- Date / location: May 24, 2026 / Spain
- Page: https://apartresearch.com/sprints/projects/auraremed-autonomous-security-engineering-report-biyb
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/9585eb5d89f4da03-b870539a-803b-4ac3-a705-62c3fbdc56fe-AuraRemed_Security_Report.pdf
- Code: https://github.com/Mornielov/AuraRemed

## Summary

About AuraRemed is a local DevSecOps engine that automates software vulnerability remediation without data leakage. Its architecture couples Semgrep (Tier 2) for deterministic flaw detection with Qwen2.5-Coder (Tier 1) to apply surgical in-memory patches and security docstrings in a closed feedback loop until validation achieves a clean Code 0.

## Reviews (1)

### Review 1

Secure program synthesis opens new questions about what happens in CI. This sprint produced a CI method that automatically finds and fixes security issues. Some questions I'd have for next steps relate to what deployment and user experience would look like: would someone trust a low-cost LLM to substantially edit their code in CI? is there a way to check the patched code still works as expected -- maybe there's test CIs too but what if they fail? and would a sql injection attack really be a CI-fix or a major red flag?

