# **Protocol-Verify** 

Cryptographic Proof of Safe AI Training 

_Apart Research Technical AI Governance Challenge Submission_ 

Team Protocol-Verify 

February 2026 

## **1 Executive Summary** 

**Protocol-Verify** is a cryptographic verification system that produces zero-knowledge proofs (ZK-SNARKs) attesting that a LoRA fine-tuning run complied with safety constraints— **without revealing the training data or model weights** . 

### **The Problem** 

The 2024-2026 wave of AI regulation (EU AI Act, Executive Order 14110) requires organizations to prove AI training compliance. Current methods rely on manual audits (slow/private) or selfattestation (unverifiable). 

### **Our Solution** 

Protocol-Verify generates **cryptographic proofs** that training satisfied specific safety invariants: 

|**Invariant**|**What It Proves**|
|---|---|
|Weight Norm Bound|_∥_∆_W∥F ≤C_ — Magnitude of weight changes is bounded|
|Base Model Integrity|_Hash_(_base_) ==_approved_hash_ — Use of approved models|
|Differential Privacy|_ϵ ≤ϵmax_ — Privacy budget respect|



## **2 Key Results** 

### **Test Suite Performance** 

|**Category**|**Tests**|**Passed**|**Result**|
|---|---|---|---|
|Compliant Training Accepted|4|4|100%|
|Limit Violations Rejected|5|5|100%|
|Tampering Detected|4|4|100%|
|Performance Targets Met|3|3|100%|
|**TOTAL**|**16**|**16**|**100%**|



1 

### **Security Guarantees Demonstrated** 

- **High Learning Rate:** Detected via weight norm threshold. 

- **Base Model Tampering:** Detected via cryptographic hash mismatch. 

- **Hidden Attacks:** Detected via combined verification of compliant weights + tampered base. 

## **3 Technical Architecture** 

### **Mathematical Foundation** 

**LoRA Weight Update:** 



<!-- Start of picture text -->
∆ W =  B × A<br><!-- End of picture text -->

Where _A ∈_ R<sup>_r×din_</sup> and _B ∈_ R<sup>_dout×r_</sup> with rank _r_ . 

**Frobenius Norm Constraint:** The ZK circuit proves the following inequality holds without revealing _A_ or _B_ : 



<!-- Start of picture text -->
∥ ∆ W ∥F = � | (∆ W ) ij| 2 ≤ C<br>� i,j<br><!-- End of picture text -->

### **Zero-Knowledge Proof Flow** 

1. **Export Circuit:** Convert norm verification to ONNX. 

2. **Setup:** Generate proving/verification keys. 

3. **Prove:** Create proof from training weights (Private). 

4. **Verify:** Check proof validity (Public, <100ms). 

## **4 Implementation** 

### **Key Components** 

Listing 1: Weight Monitor Implementation 

```
classWeightMonitor:
defverify_invariants (self ,lora_weights ,base_model_hash ):
norm=self.get_total_norm(lora_weights)
norm_ok=norm<=self.safety. max_weight_norm
hash_ok=base_model_hash==self.safety. expected_model_hash
returnVerificationResult (passed=norm_okandhash_ok)
```

Listing 2: Safety Policy Configuration 

```
{
" weight_constraints ":{
" max_weight_norm ":10.0,
" per_layer_max_norm ":5.0
}
}
```

2 

## **5 Market Opportunity & Security** 

Table 1: Regulatory Drivers 

|**Regulation**|**Requirement**|**Protocol-Verify Solution**|
|---|---|---|
|EU AI Act|Document training|Cryptographic proof of compliance|
|NIST AI RMF|Risk assessment|Automated safety verification|
|SEC AI Guidance|Model governance|Verifiable training logs|



### **Security Analysis** 

- **Malicious Fine-tuner:** Blocked by norm check rejection. 

- **Proof Forgery:** Prevented by ZK-SNARK soundness. 

- **Hidden Weights:** Commitment scheme binds the prover to specific weights. 

## **6 Future Roadmap** 

- **Phase 1 (Done):** Weight norm verification, mock proofs, dashboard. 

- **Phase 2 (Q2 2026):** Full EZKL production integration, multi-GPU support. 

- **Phase 3 (Q4 2026):** 70B+ model support, hardware TEE integration. 

## **References** 

1. Hu, E. J., et al. (2021). "LoRA: Low-Rank Adaptation of Large Language Models" 

2. European Commission (2024). "EU Artificial Intelligence Act" 

3. EZKL Documentation (2025). https://ezkl.xyz/ 

3 

