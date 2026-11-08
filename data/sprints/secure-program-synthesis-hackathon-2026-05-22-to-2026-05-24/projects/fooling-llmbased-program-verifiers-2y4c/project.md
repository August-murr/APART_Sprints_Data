# Fooling LLM-Based Program Verifiers

- Sprint: The Secure Program Synthesis Hackathon (secure-program-synthesis-hackathon-2026-05-22-to-2026-05-24)
- Rank: unranked
- Team: Team Dev and Lalit
- Authors: Lalit Aditya Julapalli, Dev Arora
- Date / location: May 25, 2026 / Atlanta, GA
- Page: https://apartresearch.com/sprints/projects/fooling-llmbased-program-verifiers-2y4c
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/65b2527150a7b121-068666a6-c474-4fbb-943b-bc0e40834b5d-Secure_Program_Synthesis_Hackathon.pdf
- Code: https://github.com/lalitj5/formalization-proj
- Code links found in report: https://github.com/lalitj5/formalization-proj

## Summary

Extending the Clover Verification Scheme, we test a new adversarial data class and test if LLM can automate a certain type of mutation that consistently breaks the Clover scheme.

## Reviews (2)

### Review 1

The project successfully targets a critical vulnerability in Clover's verification process by automating the generation of adversarial examples that evade detection through subtle specification weakening and code mutation. The team's use of Claude Sonnet 4.5 to generate these examples is innovative and demonstrates a clear understanding of how LLMs can be leveraged for adversarial attacks. The results, showing a 37.1% evasion rate across 62 programs, are compelling, especially the high evasion rate (73.3%) for logically equivalent specifications. This work highlights a significant blind spot in consistency-based verification frameworks.

However, the project's reliance on Claude Sonnet 4.5 for both mutation generation and Clover’s internal reconstruction checks is a notable limitation. While this approach provides valuable insights, it does not fully explore whether more capable models might close this gap. Additionally, the experiments are limited to introductory-level problems from CloverBench, which may not fully represent the complexity of real-world applications. The project could benefit from a broader evaluation that includes more challenging tasks.

To strengthen the findings, future work should investigate how different LLM capabilities affect the generation and detection of adversarial examples. It would also be valuable to test these attacks on more complex problems to determine if the evasion patterns hold. Additionally, exploring alternative methods for ensuring semantic consistency between natural language and formal specifications could provide a more robust solution to this vulnerability.

### Review 2

The 73.3% evasion rate on logically equivalent specs is the most interesting result, but it is hard to fully trust because the same model (Claude Sonnet 4.5) both generates the mutations and powers Clover's reconstruction checks, so the attack may be exploiting a shared blind spot rather than a general weakness. Running the reconstruction step with a different or stronger model, which you raise in the limitations, would make the finding much more convincing. Table 3 also blends "Dafny evasion" with "Clover evasion," and tightening that distinction would sharpen the headline claim.

