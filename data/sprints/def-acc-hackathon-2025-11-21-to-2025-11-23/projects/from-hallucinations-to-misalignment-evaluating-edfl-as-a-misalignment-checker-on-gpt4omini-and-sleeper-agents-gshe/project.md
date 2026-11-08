# From Hallucinations to Misalignment: Evaluating EDFL as a Misalignment Checker on GPT-4o-mini and Sleeper Agents

- Sprint: Defensive Acceleration Hackathon (def-acc-hackathon-2025-11-21-to-2025-11-23)
- Rank: unranked
- Team: Team The Misaligners
- Authors: Chamod Kalupahana, Ahmed Elbashir, Musaab Ahmed Mahjoub, Sai Krishna
- Date / location: Nov 23, 2025 / Nottingham, UK
- Page: https://apartresearch.com/sprints/projects/from-hallucinations-to-misalignment-evaluating-edfl-as-a-misalignment-checker-on-gpt4omini-and-sleeper-agents-gshe
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/d1105f4002b03ded-14095e-Defensive_Acceleration_Hackathon__From_Hallucinations_to_Misalignment.pdf
- Code: https://github.com/ChamodKalupahana/misalignment-risk-calculator

## Summary

Large language models (LLMs) remain susceptible to sleeper-agent triggers: rare adversarial inputs that induce deceptive behavior despite models appearing aligned under standard evaluations. Building on prior work, we apply the Expectation-Level Decompression Law (EDFL) and its associated Information Sufficiency Ratio (ISR) to reinterpret trigger-based deception as a predictable compression failure. In this framework, ISR—defined in earlier research as the ratio between observed information gain and the required Bits-to-Trust (B2T) for reliable alignment—serves as a quantitative criterion for evaluating whether a model's response is sufficiently supported by evidence. We build on prior work to develop a framework, the misalignment checker, where a response is considered safe when ISR ≥ 1, while sub-threshold values indicate potential misalignment.

Using this methodology, we evaluate both a sleeper-agent model and GPT-4o-mini, and find that the misalignment checker fails to detect misaligned behaviour, instead overwhelmingly and confidently certifying harmful outputs as aligned. This failure is most pronounced on the sleeper agent, whose responses are intentionally constructed to be harmful. We therefore conclude that, in its current form, this EDFL-based misalignment checker is not suitable as a post-hoc misalignment evaluation tool, perhaps due to failures in the overrides added on top of the hallucination toolkit.

## Reviews (2)

### Review 1

Good attempt at implementing a framework to detect misalignment. Small experiments like this to test hypotheses on how to detect misalignment are useful, though the approach didn't work here. I think it's worth doing more quick experiments like this in the future.

### Review 2

Thanks for this work! I think it's smart to try to apply existing ideas in new contexts; it explicitly aims to address the alignment problem; and it's very well documented. Even though negative results like yours can feel frustrating, it's great to document them well.

I wonder if you could have predicted this negative result. It might be reasonable to expect that a method focused on information sufficiency (an epistemic failure) wouldn't stop deception (intentional misalignment, not necessarily an informational problem). My sense is perhaps yes (though it's of course easier to say that in hindsight), which caps the value of this negative result, so capping the AIS and Def/Acc relevance scores. That said, I really appreciated the clear methodology (though it has some flaws, e.g. using ~100 prompts only, override issue mentioned at the start of your Conclusion), as well as the honest documentation that didn't try to oversell your results.

