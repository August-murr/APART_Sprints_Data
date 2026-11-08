# NeuroTrace: Spec-Aware Neural Network Runtime

- Sprint: The Secure Program Synthesis Hackathon (secure-program-synthesis-hackathon-2026-05-22-to-2026-05-24)
- Rank: unranked
- Selected as: sample_reviewed
- Team: Team Safeboy
- Authors: Robert Joseph George
- Date / location: May 25, 2026 / Los Angeles
- Page: https://apartresearch.com/sprints/projects/neurotrace-specaware-neural-network-runtime-mipv
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/02232a3bd524f16b-284bbf66-7c7e-4a7b-83e2-a88cf9e55476-Apart-Research-hackathon---main.pdf
- Code: https://github.com/Robertboy18/NeuroTrace
- Code links found in report: https://github.com/Robertboy18/NeuroTrace, https://github.com/pytorch/pytorch
- Recording: https://drive.google.com/file/d/1hbmuprhTSyhHDON1aGIm2GEa93SAxuHZ/view?usp=sharing

## Summary

NeuroTrace is a spec-driven observability framework for neural network models. The core idea is that a neural specification should not stay as a static file: it should become a live contract that the runtime, training loop, optimized implementation, export artifacts, and verifier outputs must continue to satisfy. NeuroTrace triangulates across TorchLean-style specs, PyTorch hooks, torch.fx, ONNX/VNN-LIB, Marabou, SpecTrace training logs, Fast Path checks, and SpecFuzz mutations to detect when the artifact chain drifts from the intended model. My long-term goal for it is to become a practical “spec observability” layer for ML systems, especially as AI agents generate code and frontier-style systems replace readable models with faster optimized runtimes.

## Reviews (2)

### Review 1

This approach shows promise and is I believe a novel combination and application of these methods. I am excited to see if this scales to real-world bugs and implementation. I also liked the variety of objects covered in the demonstration here and was impressed by the hackathon velocity.

I'd have liked to see more justification or exploration that the autoformalization into the contract is reasonable, since the correctness of this is fairly load bearing for the usefulness of this technique. Additionally, the write-up was a little hard to follow and some key claims or ideas were buried in the stream-of-consciousness format.

### Review 2

Constant surveillance as opposed to a single check seems very promising. But, the human prompt to contract writing using an AI in itself is not a very robust methodology.

