# The Iron Rule Checklist: Structured Specification Elicitation Reduces False-Pass Rates from 82% to 3.5% in LLM-Generated Lean 4 Specifications

- Sprint: The Secure Program Synthesis Hackathon (secure-program-synthesis-hackathon-2026-05-22-to-2026-05-24)
- Rank: unranked
- Team: None
- Authors: Tang Meng
- Date / location: May 25, 2026 / Shanghai, China
- Page: https://apartresearch.com/sprints/projects/the-iron-rule-checklist-structured-specification-elicitation-reduces-falsepass-rates-from-82-to-35-in-llmgenerated-lean-4-specifications-zy8x
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/433f2cf64106d090-270e24967ca0-Tang_Meng_The_Iron_Rule_Checklist_for_Specification_Elicitation.pdf
- Code: https://github.com/tomnovember/sps-iron-rule-checklist

## Summary

We measure the false-pass rate in NL-to-Lean 4 specification pipelines: how often objectively insufficient natural language descriptions produce specs that pass all decide-based verification tests. Across 243 descriptions (81 VERINA problems × 3 personas), the baseline false-pass rate is 82.4%. Free-form LLM questioning reduces it to 16.4%. The Iron Rule Checklist, a structured 7-category elicitation protocol, reduces it to 3.5% with zero regressions and 4 of 8 issue types reaching 100% detection. The 6 remaining misses decompose into three structural categories defining the method's theoretical ceiling.

## Reviews (2)

### Review 1

This paper presents a small empirical study into a prompt-engineering effort in improving the specification writing capabilities of LLMs. The authors propose a 7 step checklist, which when presented to an LLM, was found by the authors in their test set to reduce the rate of generation of faulty specifications. Overall, I think this work is interesting, and provides a useful signal to people looking into this problem. I appreciated the quantitative evaluation of the natural language prompt and the analysis of the results. That being said, ultimately the experimental results boil down to providing an additional natural language prompt to an existing agent, which feels rather incremental. I would be curious to see if through the methodology used to derive the prompt the authors are able to extend this to additional tools and interfaces that could be exposed to an LLM to improve its ability to write specifications. Are there specific tools (such as model checkers, symbolic execution) that an LLM could use to sidestep some of the failure modes identified in this paper?

### Review 2

Finding ambiguities in specifications is incredibly important. This sprint produced (a) 7 key questions to probe, and (b) a test set of 243 specs with known gaps. The test set, which was built manually by varying VERINA, may be useful in future as a basis of benchmarks and experiments. The one qualm I have is that as far as I understand, the ambiguous specs were written by the same person who designed the 7 key questions; if so, there's a confounding factor, which is understandable for a hackathon, but going forward it would be interesting to find methodologies that reduce the concern about this.

