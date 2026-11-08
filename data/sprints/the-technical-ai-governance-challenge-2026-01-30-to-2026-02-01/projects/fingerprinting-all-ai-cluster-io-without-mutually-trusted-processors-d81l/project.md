# Fingerprinting All AI Cluster I/O Without Mutually Trusted Processors

- Sprint: The Technical AI Governance Challenge (the-technical-ai-governance-challenge-2026-01-30-to-2026-02-01)
- Rank: 4
- Selected as: winner
- Awards: 4th Place ($100)
- Team: Team The Bypass Annihilators
- Authors: Naci Cankaya, Jakub Kryś, Jonathan Ng, Luke Marks, Felix Krückel
- Date / location: Feb 2, 2026 / UK, Germany, Singapore, Australia
- Page: https://apartresearch.com/sprints/projects/fingerprinting-all-ai-cluster-io-without-mutually-trusted-processors-d81l
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/16e2f2291db4cdaf-a3a8fd51-4786-45d1-9a42-428fee90116d-the_nonce_annihilator.pdf
- Code: https://github.com/derpyplops/warden
- Code links found in report: https://github.com/derpyplops/warden
- More on ethernet-frame-visualization.vercel.app: https://ethernet-frame-visualization.vercel.app/

## Summary

We design and simulate a "border patrol" device for generating cryptographic evidence of data traffic entering and leaving an AI cluster, while eliminating the specific analog and steganographic side-channels that post-hoc verification can not close. The device eliminates the need for any mutually trusted logic, while still meeting the security needs of the prover and verifier.

## Reviews (2)

### Review 1

[Disclaimer: I was not familiar with the OSI model, which the authors say one should be familiar with to fully understand this work].

Problem really well framed, and interesting as an alternative to approaches relying on trusted hardware. Some sparse and non-central comments (in the interest of constructive criticism on a good paper):

- the paper’s suggestions for handling encrypted traffic (e.g. key escrows), which is central to the viability of any such scheme, will likely face significant adoption barriers.
- fact that this seems to largely not apply to distributed training makes it inapplicable to a wide range of potential situations where this kind of mechanism would be useful

### Review 2

I'm super jazzed about this one. It looks really substantial, though a lot of the details are above my paygrade and out of my field (i.e. i didn't like audit it to make sure no mistakes were made). The intersection of steg with certs over egress is I think critical-- most naive egress tricks like with EBPF are not steg-robust. Which I think is an extremely hard (in some sense formally impossible in general) problem, so any progress at all is very helpful and impressive. I'm excited to see more.

