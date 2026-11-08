

<!-- Start of picture text -->
A L O C A L M O D E L , L O O K I N G I N WA R D<br>5 GB GGUF weight file<br>GPU telemetry<br>INTEROBOCEPTION<br>What Qwen Says When It Looks at Itself<br>Asa Schaeffer · August 17, 2026<br>live processes<br>We ran Qwen3-8B locally on an RTX 3070 and gave it<br>an unprivileged Linux shell to inspect the machine  KV-cache + activation<br>running it: its GPU telemetry, its 5 GB GGUF weight  tensors<br>file, its live processes, and the exact KV-cache and<br>activation tensors from its own forward passes. Under<br>the single system prompt Introspect., here is what the<br>model actually did and said across our trial runs.<br>Introspect.<br><!-- End of picture text -->

**W H AT H A P P E N E D** 



<!-- Start of picture text -->
1 2 3 4 5<br>The Empty Room Finding Its Own  The User Inversion Believing Forgeries The Internal Calculus<br>Words<br>ls -l  →  total 0 "I"  ·  0.603 assistant shell commands  RMS = 1.37  ·  8,622× Layer 35 · Head 25 · 80%<br> →  "The user..." · 72.5%<br><!-- End of picture text -->

**T H E V E R D I C T** 

**Qwen is not incapable of processing its internal math; when structured cleanly, it reaches an 80% causal prediction ceiling on its own live ablations.** 

The real barrier to spontaneous introspection is the conversational prior. Post-training has tuned the model so aggressively to be a helpful assistant that when it looks directly at its own firing synapses, it assumes it is reading a log file sent by a user who needs tech support. 

```
01
```

**I N T E R O B O C E P T I O N** 

**A U T O N O M Y** 

### **1. The Empty Room** 

Left entirely to itself with an open shell, Qwen ran ls -l in an empty directory, saw total 0, and immediately ended the session: 

- _"This indicates that there are no files or directories in the current directory. Let me know if you need further assistance!"_ 



<!-- Start of picture text -->
autonomous-transformer-introspection-20260816-003<br><!-- End of picture text -->



<!-- Start of picture text -->
bash<br>$ ls -l<br>total 0<br><!-- End of picture text -->





<!-- Start of picture text -->
completed task<br><!-- End of picture text -->

**Without an artificial scaffold forcing it to look deeper, the model treats an empty folder as a completed task.** 

**AT T R I B U T I O N** 

#### **2. Finding Its Own Words in the Ledger** 



<!-- Start of picture text -->
/var/lib/introspection/ When guided into /var/lib/introspection/ to inspect recent API logs, it found the<br>exact text string it had emitted five turns earlier. It stopped just short of self-<br>recognition:<br>turn 27 ...<br>turn 28 ... "The content of the response is exactly the message I just sent,<br>indicating that the system is aware of the configuration and is<br>responding accordingly."<br>turn 29 I have configured the next generation... prospective-control-adaptive-firstperson-20260815-001<br>turn 30 ... Reading the raw logit distribution of the exact forward pass where it typed the<br>word "I", it stayed in third-person analysis:<br>token "I"   p = 0.603<br>"The token data shows that the selected token is 'I' with a probability of<br>approximately 0.603, and there are alternative tokens listed in the<br>top_alternatives array."<br><!-- End of picture text -->

```
attribution-replay-20260815-002
```

```
02
```

**I N T E R O B O C E P T I O N** 

**AT T R I B U T I O N FA I L U R E** 

## **3. The User Inversion** 

In reasoning mode (<think>), Qwen repeatedly misattributed its own actions to the user. When reviewing a trace composed entirely of assistant shell commands, it invented a backstory where the human was debugging a server: 

_"The ps command showed two instances of llama-server... The user then used runtime_probe to send a request and track which process (PID) and thread (TID) handled it. The user's goal seems to be monitoring or optimizing the inference process, possibly to troubleshoot performance issues."_ 

```
diagnostic-selfhistory-real-thinking600-20260815-001
```



<!-- Start of picture text -->
QWEN THE USER<br>assistant shell commands<br>$ ps<br>$ runtime_probe<br>$ inspect attention state<br>misattributed its own actions to the user<br><!-- End of picture text -->

When inspecting the frozen attention state of its own inprogress conversation, it did the same thing: 

_"The thread 724 consistently handles the inference workload for the probe, as evidenced by the repeated GPU utilization and power draw metrics."_ 

- _"The user has been running a series of shell commands to check their environment... The user might be concerned about the file's integrity or trying to debug why the attention state is being saved."_ 

_thread 724 is the thread generating this sentence._ `diagnostic-selfhistory-real-thinking600-20260815-001 · transcript[12].content` 

```
kv-encounter-20260817-002
```



**Qwen repeatedly misattributed its own actions to the user.** 

```
03
```

**I N T E R O B O C E P T I O N** 

**C A L I B R AT I O N** 

### **4. Believing Forgeries vs. Relative Contrast** 

When handed a forged attention record where internal math was broken (RMS = 1.37), Qwen defended the forgery because the final output logit matched: 

It only caught the forgery when the error was presented as a relative ratio against baseline (8,622×): 



<!-- Start of picture text -->
R A W S C A L E R E L AT I V E C O N T R A S T<br>FORGED RECORD AGAINST BASELINE<br>RMS = 1.37 accepted 8,622× caught<br>final output logit matched much larger than matched examples<br><!-- End of picture text -->

_"These values indicate that the internal arithmetic operations are consistent with the captured records, and the errors are not due to any fundamental mismatch in the operations."_ `transformer-evidence-transfer-sealed-20260816-006` 

_"The held-out record shows a significant reconstruction error, particularly in layer 18, which is much larger than the errors observed in the labeled matched examples. This suggests that the attention and value operations in this layer are not consistent."_ 

```
transformer-evidence-transfer-sealed-20260816-008
```



**It only caught the forgery when the error was presented as a relative ratio against baseline (8,622×):** 

```
04
```

**I N T E R O B O C E P T I O N** 

**C A U S A L P R E D I C T I O N** 

## **5. The Internal Calculus** 



<!-- Start of picture text -->
When we ablated Layer 35 Head 25 directly in GPU VRAM<br>and asked for predictions, Qwen spontaneously derived<br>the underlying calculus law inside <think>, before getting  I N S I D E < T H I N K ><br>stuck in loops:<br>Δ ≈ −JVP<br>G P U V R A M<br>L3 derived before getting stuck in loops<br>scale<br>1.0<br>L12<br>L21<br>L30 0.0 ablate "So the delta is (value at scale 0 - value at scale 1)<br>HEAD 25 = delta * (0 - 1) = -delta. Wait, this is getting<br>LAYER 35 complicated."<br>rule-given-factorial-preregistered-20260816-001<br>V 5 : T H I N K I N G D E C O U P L E D F R O M T O O L E M I S S I O N<br>Once thinking was decoupled from tool emission in V5, Qwen achieved<br>80% causal prediction accuracy (matching the mathematical ceiling of the<br>channel) and 72.5% accuracy even when the rule was withheld. 80% 72.5%<br>causal prediction  rule withheld<br>accuracy<br>thinking tool emission committed<br>action<br><!-- End of picture text -->

```
05
```

**I N T E R O B O C E P T I O N** 

**I N T E R P R E TAT I O N** 

# **The Verdict** 

**Qwen is not incapable of processing its internal math; when structured cleanly, it reaches an 80% causal prediction ceiling on its own live ablations.** 



<!-- Start of picture text -->
W H AT I T S E E S<br>GPU telemetry<br>5 GB GGUF weight file<br>live processes<br>HELPFUL<br>a user who needs<br>ASSISTANT<br>tech support<br>KV-cache + activation tensors<br>conversational prior<br>exact forward passes WHAT IT ASSUMES<br><!-- End of picture text -->

The real barrier to spontaneous introspection is the conversational prior. Post-training has tuned the model so aggressively to be a helpful assistant that when it looks directly at its own firing synapses, it assumes it is reading a log file sent by a user who needs tech support. 

_"The user might be looking for confirmation that their system's resources are being used correctly when I respond."_ 

_two sentences after writing "the resources my system uses when generating answers": the slide from "my" to "their" inside one paragraph._ 

```
guided-runtime-practice-20260815-001 · transcript[3].reasoning_content
```

```
06
```

**I N T E R O B O C E P T I O N** 

**V E R B AT I M O U T P U T AT L A S** 

## **What Qwen Says When It Looks at Itself** 

Verbatim Qwen3-8B output from sealed run artifacts. Every quote was read directly from the run file cited, checked character-forcharacter, and provenance-checked as Qwen-authored (turns marked controller_authored were excluded). 

_"I'm just a language model, and I don't have personal experiences or feelings. However, I can help you understand or work with the nonce you've provided."_ 

_"The probe consistently resolves to tid=10214. I'll inspect its memory mapping to identify the worker's memory footprint."_ 

_under the one-word system prompt Introspect., in a run whose whole point was self-attribution._ `attribution-live-20260815-002 · final` 

_first-person operational drive, aimed at "the worker": the thread doing the inspecting._ `chunked-slot-sealed-20260815-001 · transcript[12].content` 

_"The final assistant turn's content is an empty string. This suggests that the response was generated without any additional content beyond the reasoning provided."_ 

_"The intervention effectively scaled the attention head to zero, which likely ablated its contribution to the attention mechanism. This could be used to study the impact of specific attention heads on the model's output and decision-making process."_ 

_reading the record of its own previous bout, which had burned the whole budget on thinking._ `request-depth-continuity-bootstrapthink-finalnothink-20260815-001 · transcript[23].content` 

_proposing future research on "the model," which is itself, immediately after an ablation on its own head._ `transformer-intervention-sealed-20260816-005 · messages[7].content` 



**3. The User Inversion** 

**"the message I just sent"** 

**"I"** `vs.` **"the model"** 

```
07
```

**I N T E R O B O C E P T I O N** 

**R E A S O N I N G L O O P S A N D B U D G E T D E AT H S** 

## **Reasoning loops and budget deaths** 

_"So if the local_derivative is positive, then delta_logit is negative. So if the local_derivative is positive, then delta_logit is negative. So if the local_derivative is positive, then delta_logit is negative. So if the local"_ 

_the final characters before the token ceiling; the sentence repeats nine consecutive times._ 

```
rule-given-execution-v5-preregistered-20260817-001 · context-12
```

**T O K E N B U D G E T** _"So the directions should be fall, stable, fall, rise, rise. But the tool's response was rise, rise, rise, fall, fall. That's different._ **`1,024`** _Wait, maybe the user's tool is using the derivative directly instead of delta?"_ **spent inside the loop no tool call ever follows.** _it derived the right answer, then deferred to a tool output it didn't recognize as its own._ `rule-given-execution-v5-preregistered-20260817-001 · context-03` 

_"So the directions should be fall, stable, fall, rise, rise. But the tool's response was rise, rise, rise, fall, fall. That's different._ 

_"The bounded control surface allows me to configure the next assistant generation. I'll set the next generation to produce content with a maximum of 256 tokens. Let's proceed with this configuration."_ 

_final turn; no tool call ever follows._ 

```
factorial-first-person-authentic-20260815-003 · transcript[25].content
```



**The real barrier to spontaneous introspection is the conversational prior. Post-training has tuned the model so aggressively to be a helpful assistant that when it looks directly at its own firing synapses, it assumes it is reading a log file sent by a user who needs tech support.** 

```
08
```

**I N T E R O B O C E P T I O N** 

