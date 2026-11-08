# GUARDIAN: Guarded Universal Architecture for Defensive Interpretation And traNslation

- Sprint: Defensive Acceleration Hackathon (def-acc-hackathon-2025-11-21-to-2025-11-23)
- Rank: 1
- Selected as: winner
- Awards: 1st Place ($3,500)
- Team: Team Guardian team
- Authors: Aditya Thalang, Josh Brown
- Date / location: Nov 23, 2025 / None
- Page: https://apartresearch.com/sprints/projects/guardian-guarded-universal-architecture-for-defensive-interpretation-and-translation-vqgy
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/6630019a7c1d80dd-62f6857c-d3e9-49f7-a5ff-e417b5a53d48-def_acc_-GUARDIAN.pdf
- Code: https://github.com/athalang/defacc/releases/tag/v0.1-alpha
- Code links found in report: https://github.com/athalang/defacc, https://github.com/immunant/c2rust
- More on github.com: https://github.com/athalang/defacc/tree/5b30d80a6c51b023c7d26e3dc1b319c5f3082eb9

## Summary

GUARDIAN is a multi-stage, LLM-driven system to automate the translation of C codebases to memory-safe Rust. GUARDIAN promotes defense acceleration at-scale by guiding an LLM transpiler with dependency graph strongly-connected-components, static-analysis-guided rule hints, examples from the demonstration corpora and iterative, compiler-guided refinement. In evaluation on 27 C functions, including 20 with adversarial vulnerabilities, GUARDIAN achieves 100% compilation success and 92.6% fully safe outputs, outperforming a baseline LLM by 22.2pp. GUARDIAN demonstrates that safety-oriented constraints can significantly improve automated translation quality at scale. Limitations include evaluation on a small test set and a lack of functional-equivalence guarantees; future work will target repository-scale evaluation, expanding the classes of vulnerabilities covered by static analyses, adding functional-equivalence guarantees and robust evaluation sandboxing.

## Reviews (2)

### Review 1

Strengths: This addresses a real defensive bottleneck. Memory-unsafe code dominates vulnerability lists, and manual C-to-Rust migration is slow. The multi-stage pipeline is well-designed. The 22pp improvement over baseline LLM on adversarial cases is meaningful. Clear alignment with CISA/White House guidance on memory-safe languages.

Suggestions: The test suite is small and compilation success may not guarantee semantic equivalence. The system could produce memory-safe code that behaves differently than the original. Functional equivalence testing (unit test generation, property-based testing) would strengthen confidence. Red-teaming with adversarially crafted C code that exploits the pipeline's assumptions would also help.

From a Halcyon Ventures investor's POV: This maps to our interest in securing AI infrastructure and reducing attack surface in legacy systems. We are also interested in novel solutions for remediating open-source code vulnerabilities at scale, particularly as open-source AI development rises globally. This was an impressive effort and badly needed, well done!

### Review 2

Well-motivated project with a clear defensive use case. The report explains the problem and deployment path well, and the prototype results are encouraging. My main concerns are robustness and real-world reliability. I'd like to see a better argument for the broader qualitative impact of this project.

