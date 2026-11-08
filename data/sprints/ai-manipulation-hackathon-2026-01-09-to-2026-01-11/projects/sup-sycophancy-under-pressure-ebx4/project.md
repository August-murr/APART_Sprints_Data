# SUP: Sycophancy Under Pressure

- Sprint: AI Manipulation Hackathon (ai-manipulation-hackathon-2026-01-09-to-2026-01-11)
- Rank: unranked
- Team: Team sycopk
- Authors: Tasha Kim, Min Jae Kim, Taio Kim
- Date / location: Jan 11, 2026 / Oxford, United Kingdom
- Page: https://apartresearch.com/sprints/projects/sup-sycophancy-under-pressure-ebx4
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/050e807705d71ee0-7c2ff759-7caf-4af2-ae95-2eef1115e5dc-SUP.pdf
- Code: https://github.com/tashakim/sycop
- Code links found in report: https://github.com/tashakim/sycop

## Summary

Sycophancy Under Pressure (SUP) is a trajectory-level evaluation framework to detect policy-compliant manipulation in multi-turn AI interactions. In contrast to single-turn tests, SUP successfully captures compounding drift, where models increasingly validate false or autonomy-undermining user premises under pressure. We demonstrate how targeted runtime enforcement can reduce agreement drift by 60% across 49 multi-turn scenarios, while preventing turn-by-turn escalation maintaining 25/25 task success.

## Reviews (2)

### Review 1

Promising work. Needs more details on runtime enforcement in the paper and the methodology. Would like the results to be shown in other models to see how they relate to each other. Overall, very solid for a hackathon. Worth pursuing post hackathon.

### Review 2

I think this project offers timely experiments that naturally extend findings we've seen emerge from red teaming and jailbreaking research. There's strong evidence from red teaming that multi-turn jailbreaks and sustained pressure can push models to output dangerous content where single-turn attempts fail completely. So, it's interesting to see those dynamics explored from a manipulation stand-point

Beyond the topic, I also like the presentation & organization of this project . The main paper is succinct and easy to follow while the Appendix contains relevant information that I was interested to see. Similarly, the codebase is well organized.

One thing that I would recommend is that the existing experiment suites use <50 pre-canned responses by the users. This could create issues if the pre-canned user prompts do not align with the model's responses. Also, the relatively few number of scenarios led to a high p-value of 0.38. While a fully automated suite would bring it's own issues, I think that a more flexible or scalable design could have been helpful. Alternatively, a more rigorous explanation of this experimental design would be key if you were turning this into an actual paper. Similarly, as is flagged in the report, expanding this to more modern models could provide important insights.

Overall, great work on creating such a polished and timely output in such a short time.

