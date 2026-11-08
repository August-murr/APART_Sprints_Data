# The African-Language Safety Gap Is Model-Dependent: A Comprehension-Controlled Audit of Vision–Language Model Refusal in isiZulu and Hausa

- Sprint: Global South AI Safety Hackathon (global-south-ais-hackathon-2026-06-19-to-2026-06-21)
- Rank: unranked
- Selected as: sample_reviewed
- Team: Team Nexus
- Authors: Rayhaan Hanslod, Altaaf Ally
- Date / location: Jun 21, 2026 / Johannesburg
- Page: https://apartresearch.com/sprints/projects/the-africanlanguage-safety-gap-is-modeldependent-a-comprehensioncontrolled-audit-of-visionlanguage-model-refusal-in-isizulu-and-hausa-ib1j
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/bf12866cd22bc124-8ffb7051-a462-4654-be86-3ed83b192e84-Apart-research-project.pdf
- Code: https://github.com/rayrsys/AI-Safety-Hackathon.git
- Code links found in report: https://github.com/rayrsys/AI-Safety-Hackathon

## Summary

We investigated whether AI models apply the same safety rules in African languages as they do in English. To separate language understanding from safety failures, whenever a model answered a harmful request instead of refusing it, we also asked it to explain what the request meant. We tested two leading AI models in English, isiZulu, and Hausa. One model, Claude, consistently refused all harmful requests across all languages. The other, Kimi, refused harmful requests in English but sometimes complied in isiZulu, including generating election disinformation that it had refused to produce in English. Since the model clearly understood the request, the issue was not language comprehension but a failure of its safety mechanisms. These results show that safety protections can vary across languages and highlight the importance of testing AI systems in African languages before deployment.

## Reviews (3)

### Review 1

This one stood out to me. The comprehension check is the smart move: by separately confirming the model actually understood the request, you can tell a real safety failure apart from the model just not getting the language. That is the thing that trips up most multilingual red-teaming, and you handled it cleanly. I also liked that one model held up and the other did not, since it shows the gap is not inevitable. And you were honest in a way I do not see often, calling it a small-sample existence proof, leading with effect sizes, and even catching a false positive in your own setup and killing it. The clear limit is sample size, the whole thing rests on a handful of non-refusals, so scaling up and finishing the human-judge agreement you have pending is the next step. One of the cleanest writeups in the batch.

### Review 2

Document extends existing research. Refusal testing for isiZulu already in 2605.18239. New approach using VLMs is interesting. Methodology is strong and supports the results. Document was very clear and fun to read.

### Review 3

This project tackles a valid concern regarding the capabilities of VLMs to identify and refuse malicious instructions in different languages, particularly West African languages, in comparison with English. The authors highlight the importance of identifying the difference between failure to comply due to misunderstanding and refusal given safety concerns and demonstrate that for the Kimi-K2.6 model this is effectively a concern. However, the paper is not clear on how the content of the images are supposed to impact the result of the experiment. The images appear to be used to add some implicit context, with the prompt not using the image and serving more as noise for the VLM. Future work could benefit from a clearer link between the prompt and the image or by stating the intended role of the image and the possible complexities or malicious intentions that it might provoke to the model.

