# ITP Fuzz

- Sprint: The Secure Program Synthesis Hackathon (secure-program-synthesis-hackathon-2026-05-22-to-2026-05-24)
- Rank: unranked
- Selected as: sample_reviewed
- Team: Team Fuzzers
- Authors: Pruthviraj Sadhankar
- Date / location: May 25, 2026 / Overland Park
- Page: https://apartresearch.com/sprints/projects/itp-fuzz-irn7
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/fcde70a4d20d4a17-b54338e6-c663-4993-b70e-2adf5c0fb5b4-Project.pdf
- Code: https://github.com/phsadhankar/itp-fuzz

## Summary

A framework for finding failure modes in interactive theorem provers (ITPs) and LLM-assisted proof tools.

## Reviews (2)

### Review 1

The document outlines the problem but fails to propose a solution or methodology. Furthermore, the linked repository does not contain any code.

### Review 2

itp-fuzz presents a compelling framework for adversarial robustness testing of interactive theorem provers (ITPs) and LLM-assisted proof tools. The project successfully identifies and categorizes failure modes through kernel fuzzing and AI assistant testing, which are critical areas in ensuring the security and reliability of these systems. The kernel fuzzing method, particularly its ability to detect configurations that disable essential checks like setting 'debug.skipKernelTC' to true in Lean, demonstrates a practical approach to uncovering vulnerabilities. Additionally, the AI assistant testing component is innovative for its focus on tricking LLM-based autocompleters into suggesting unsafe tactics, which is a novel and important angle in the context of program synthesis security.

However, the project could benefit from more comprehensive validation across different ITPs and LLM configurations to ensure broader applicability. While the Coq interface is successfully integrated, the framework's effectiveness on other systems like Lean, Isabelle, and F* remains somewhat speculative without extensive testing results. The living vulnerability database is a valuable resource, but it lacks detailed analysis of the discovered vulnerabilities, which would provide deeper insights into their potential impact and mitigation strategies.

To enhance the project’s impact and robustness, future work should include a more thorough cross-platform evaluation to establish the framework's reliability across various ITPs and LLM environments. Additionally, expanding the vulnerability database with detailed case studies and mitigation techniques could significantly improve its utility for both researchers and practitioners. Despite these limitations, itp-fuzz demonstrates a strong foundation in addressing critical security issues in formal verification systems, making it a promising tool for advancing the field.

Also, There is no code present on GitHub. The Paper does contain the verification commands.

