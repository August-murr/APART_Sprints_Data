# Frontier AI Risk Threshold Analyzer

- Sprint: The Technical AI Governance Challenge (the-technical-ai-governance-challenge-2026-01-30-to-2026-02-01)
- Rank: unranked
- Selected as: sample_reviewed
- Team: None
- Authors: SWALEHA PARVEEN
- Date / location: Feb 1, 2026 / Dubai, UAE
- Page: https://apartresearch.com/sprints/projects/frontier-ai-risk-threshold-analyzer-g8zp
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/b57b2687d6b1ff21-bed00af8-2041-4570-b66f-ffb64a75d922-Frontier-AI-Risk-Threshold-Analyzer.pdf
- Code: https://github.com/swalehaparvin/-Frontier-AI-Risk-Threshold-Analyzer/tree/main
- Code links found in report: https://github.com/swalehaparvin/-Frontier-AI-Risk-Threshold-Analyzer
- Presentation: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/ed9bd05ec30ffc73-920d0eb0-605e-4176-a5fe-f603c73ece3f-Presentation---Frontier-AI.pptx
- More on frontier-risk-analyzer.replit.app: https://frontier-risk-analyzer.replit.app/

## Summary

Different AI labs define "dangerous AI" using incompatible frameworks:

Anthropic uses ASL levels (ASL-2, ASL-3) Google DeepMind uses CCL tiers OpenAI uses preparedness levels The EU AI Act uses compute thresholds (10²⁵ FLOPS)

This fragmentation makes international coordination nearly impossible. How do you negotiate safety agreements when you can't even compare risk levels across organizations? The Solution: I built an open-source tool that harmonizes these frameworks for the first time. Using AI-powered extraction with GPT-4o, I: ✅ Processed 12+ major AI safety frameworks ✅ Extracted 47 distinct risk tiers into a structured database ✅ Built an interactive web app for real-time risk assessment ✅ Automated EU AI Act compliance checking Key Findings:

A model can trigger ASL-3 at Anthropic but not equivalent thresholds at other labs Only 3/12 frameworks use explicit compute thresholds Significant regulatory arbitrage opportunities exist

Real-World Impact: This tool enables: 🔹 AI labs to self-assess compliance across ALL frameworks simultaneously 🔹 Regulators to objectively compare lab commitments 🔹 Researchers to build on the first comprehensive threshold database

## Reviews (2)

### Review 1

Impact potential & Innovation: 1

I'm unfortunately not convinced that this is a meaningful problem: I expect that combining the 5-6 frameworks that actually matter here could have been a quick, manual task.

Execution Quality: 1

There is no meaningful execution here, and the results are difficult to interpret. E.g. figure 2 on framework risk heatmap is difficult to understand - how was this measured, why is a scale of 40-60 used?

Presentation & Clarity: 1

The results section is nearly empty (2 figures with minimal explanation). It would have been helpful to have deeper, side by side analysis of frameworks.

### Review 2

The accuracy rate reported is concerning: “94% for threshold values and 97% for organization names.” Manual checking works to create a snapshot but not to automate the recreation of this analysis as frameworks change. It would be interesting to know what steps were taken or considered to bring this accuracy up.

It is unclear why regulators cannot force adoption of their preferred standards without making reference to lab-generated taxonomies. Consider whether this research wants to instead address the need for regulators to establish clear, capabilities-based risk tiers, taking inspiration from and integrating work the labs have done, where it makes sense to do so.

