# AI Sentinel

- Sprint: Defensive Acceleration Hackathon (def-acc-hackathon-2025-11-21-to-2025-11-23)
- Rank: unranked
- Selected as: sample_reviewed
- Team: Team Middle
- Authors: Nice Cailie Ineza
- Date / location: Nov 23, 2025 / Nairobi, Kenya
- Page: https://apartresearch.com/sprints/projects/ai-sentinel-ounq
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/3a47db79dc2d2617-daa429af-accb-4e70-bc97-6458d7b626e1-AI-sentinel-report.pdf
- Code: https://github.com/Nicailie/AI_sentinel
- Code links found in report: https://github.com/Nicailie/AI_sentinel
- Recording: https://drive.google.com/drive/folders/1pVY91E_z8B2FUVa1pUGx7yZ1aGDA7gyX?usp=drive_link

## Summary

AI Sentinel is the first dual-domain monitoring system for AI outputs, detecting biosecurity and cybersecurity threats in real-time. Unlike existing tools that screen after synthesis requests or deployment, AI Sentinel intercepts threats at the AI generation layer with 120ms response time. Our three-layer architecture (bio + cyber + intent) achieves 88.2% accuracy on real-world benchmarks including CVE-2024 exploits and select agent detection. Key innovation: counter-intuitive jailbreak logic where "educational claims + dangerous content = HIGHER risk" catches bypass attempts that fool standard filters. Deployment scenarios include AI research labs (API middleware), DNA synthesis providers (upstream screening), enterprises (insider threat monitoring), and developer teams (IDE plugins). Open-source architecture enables community-driven improvements while complementing existing tools like SecureDNA and Nuclei.

## Reviews (2)

### Review 1

I like that it's a working tool for people to use for flagging, but the implementation for detection is fairly basic. Would have liked to see how this project adds to the existing

### Review 2

Thanks for building this! The concept of using cheaper detection systems within a defence-in-depth framework is sound and the execution is impressive for a hackathon project.

I think there are some significant limitations that cap its score. In particular:

1. I agree that 'educational' context should *not reduce* risk scores, but I don't think it's obvious that it should increase scores. I think this might be a case of overfitting, where it works well in this case but not for the more sophisticated attackers from whom most of the harm could come (assuming that the distribution of AI harms is heavy-tailed).
2. Similarly, the regex and phrase matching is very fast but limited. It might provide a false sense of security - sophisticated attackers could refer to the same concepts using different words to avoid the matching, given there isn't semantic generalisation etc.
3. This implementation would appear to have a very high false positive rate in many real-world deployment settings, given that, as I understand it, e.g. 'sudo' and 'socket' trigger high risk scores.
4. Bluntly, I think you're at risk of overselling what you have achieved - if you built this and it was adopted, the most obvious way it could be net negative is for customers is for them to think they're now safe, so not use other security measures. Although it's technically true that it's 'production-ready', has '88% accuracy' and 'catches [some] threats before they cause harm', this kind of language gives a greater impression of safety than can be achieved (I think) using these methods.
5. The number of test cases is quite limited.

But this is a great hackathon project and some of these issues are fixable, e.g. you could

a. Experiment with more sophisticated filters that are still low-cost - what does the cost/accuracy frontier look like?

b. 'Sell' this as a first defence that is very effective against a specific class of attacks but make clearer caveats about its limitations

c. Do a wider range of tests

