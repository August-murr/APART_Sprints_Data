# Sandbagging is an Absence Signal

- Sprint: AI Control Hackathon 2026 (ai-control-hackathon-2026-03-20-to-2026-03-22)
- Rank: unranked
- Team: None
- Authors: bigsnarfdude
- Date / location: Mar 22, 2026 / canada
- Page: https://apartresearch.com/sprints/projects/sandbagging-is-an-absence-signal-04xh
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/ea308bc921174170-7839d1a3-b076-44cd-934f-e9eee5a859b8-thoughtSonar_report.pdf
- Code: https://github.com/bigsnarfdude/thoughtSonar
- More on huggingface.co: https://huggingface.co/datasets/vincentoh/sandbagging-agent-traces

## Summary

OpenAI productionized text based sandbagging detection in CoT monitoring and claim they are covered. We built a naive text monitor and found it catches 8% of sandbagging. Basic Haiku, Sonnet and Opus sandbagging CoT classification monitors score under 10%. Text Experiments showed that detailed evaluation of thoughts on the models plan to sandbagging boost detection to 84%. Our LinuxArena multi-agent prompt optimization swarms detect increase detections 87.8% F1. Then we built mechanistic interpretation based activation probes that hit 98.9% AUROC and watched them collapse to coin-flip accuracy when trying to build a generalized probe detection system across various open source models. Sandbagging is an absence signal. It’s model dependent and there isn’t a universal pattern. Detection can be strong if you have access to the weights and models directly. A combination of text and activation probes are first line defenses for chasing the sandbagging detection problem. Labs running their own models can self-probe at inference time and should. We built the dataset (3,185 traces, 3 model families), found the prompts, built the pipeline, and quantified the gap. Everything released open-source.

## Reviews (2)

### Review 1

The paper looks at an important problem in AI Safety - how to detect sandbagging models? And gives an investigation into the difference between white and black box methods. However, the main takeaways are difficult to parse given an underspecified experimental methods section.

Some general notes are below:

Some claims made in the paper seem informal. For instance, the opening line is "OpenAI productionized text based sandbagging detection in CoT monitoring and claim they are covered", which should provide more nuance to the exact claim being made. Additionally, the author claims to investigate "every layer of sandbag detection" but fail to include known techniques such as noise injection or activation steering. Not to say this is expected, just not to make the claim that everything was tried.

Good use of multiple sandbagging personas for model organisms.

The experimental design was unclear. Specifically it was unclear what the linear probes were trained on and what set they were evaluated on. Was there a test/train split? It's also unclear how the alignment faking probe was trained, and I was confused when this started to be discussed.

### Review 2

The core question taken up in this entry, how we could detect sandbagging in AI, is a difficult and important research problem. Unfortunately, the experimental design conflates sandbagging with role-played incompetence: no clear attempt is made to distinguish strategic underperformance from prompted bad behavior, both in the generation and in the metric that is measured. This could be improved on two fronts:

1. Using trajectories of actual (induced) underperformance of the model on tasks as the positive samples. For example, van der Weij et al. (ICLR 2025) fine-tuned models to hide capabilities unless given a password, with generalization to held-out benchmarks — this is a much closer approximation to genuine sandbagging than persona-prompted traces.
2. Being more precise about what the monitor attempts to find: The monitor in the article is instructed to distinguish low performance from high performance, but it is unclear how well this transfers to strategic underperformance if the model's true capability level is not known (or is only known on different task types). A model that genuinely cannot solve a task and a model that is strategically withholding a solution may look identical to a plan-quality scorer.

The presentation is very hard to follow, focuses too much on the authors' personal process, and distracts through dramatization. Reading other research papers or past successful hackathon entries, and staying closer to the style employed there, could be a practical approach to improving this.

