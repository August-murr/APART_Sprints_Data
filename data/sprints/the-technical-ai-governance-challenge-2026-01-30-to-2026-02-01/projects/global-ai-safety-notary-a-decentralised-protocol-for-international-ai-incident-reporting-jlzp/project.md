# Global AI Safety Notary: A Decentralised Protocol for International AI Incident Reporting

- Sprint: The Technical AI Governance Challenge (the-technical-ai-governance-challenge-2026-01-30-to-2026-02-01)
- Rank: unranked
- Selected as: sample_reviewed
- Team: Team Neutral Ground
- Authors: Augusta Lina, Caleb Rudnick, Dennis Kiptanui
- Date / location: Feb 1, 2026 / Cape Town
- Page: https://apartresearch.com/sprints/projects/global-ai-safety-notary-a-decentralised-protocol-for-international-ai-incident-reporting-jlzp
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/508124077c3abfff-ty-Notary---A-Decentralised-Protocol-for-International-AI-Incident-Reporting.pdf
- Code: https://github.com/Augusta-Lina/safety_notary
- Recording: https://youtu.be/Ev32-3Ylu0s
- More on blockchain-six-ashy.vercel.app: https://blockchain-six-ashy.vercel.app

## Summary

Global AI Safety Notary is a decentralised incident reporting platform that creates immutable, verifiable records of AI safety incidents on the blockchain. Built on the Ethereum Attestation Service (EAS), the platform enables researchers, developers, and organisations to report and track AI failures, including bias, hallucinations, safety violations, and data leaks, with full transparency and accountability.

The Problem:

International AI governance suffers from a fundamental trust deficit. Nations are reluctant to report AI safety incidents to centralised bodies controlled by potential adversaries, creating dangerous information silos where critical safety lessons go unshared.

Key Features:

- Immutable Incident Records: Every report is stored as an on-chain attestation on Ethereum Sepolia, ensuring records cannot be altered or deleted

- Structured Reporting: Multi-step form capturing incident type, severity (1-5), model identifier, organization, location, and detailed descriptions

- Searchable Registry: Browse, filter, and search all reported incidents by type, severity, or keywords

- Blockchain Verification: Direct links to EASScan for independent verification of attestation data

## Reviews (2)

### Review 1

The project clearly explains how to use a verified method to securely share records of incidents. However, the core analogous system - aviation safety parallel (ASRS) - may not transfer well to AI. ASRS works partly because airlines don't own aircraft manufacturers, they only own depreciating aircraft — pilots can report Boeing defects without much harming Ryanair, especially as most of the firm's competitors also operate the same aircraft. By contrast AI labs are vertically integrated: they are simultaneously manufacturer and operator, so reporting is self-incriminating. Incident reports on a public blockchain cannot be meaningfully anonymised ("x had a safety incident" identifies the lab), creating adverse incentives where public visibility discourages rather than encourages reporting. The confidentiality that makes aviation reporting work is incompatible with the transparency that blockchain provides.

### Review 2

I wanted to hate this because I think defi is terrible and its technical challenge landscape snipes people too easily, but i'm actually sympathetic about using ethereum in this context. Sovereignty/neutrality seems like an upside (tho its a little misleading how much distributed consensus actually buys you here), transparancy, attestations, and availability are I think table stakes and ethereum has some natural ways into this. I just think immutability is a very blunt weapon to deploy against a threat model that shouldn't be much of a priority. Normal reputation and law should I think catch someone trying to falsify a record, meanwhile immutability has a lot of downsides (mainly that it tempts you to interact with defi or any chain at all, which is corrosive to your goals / invites grifters and shitcoin-weather gamblers into the AI governance space).

Minor nitpicks:

- don't use "layer" terminology in figure 1 because l1 and l2 are technical terms in defi so there's a naming collision.
- This sentence "The user interface was styled using Tailwind CSS, enabling rapid development of a responsive, accessible design" was completely unnecessary: we know that UI design is trivially vibecodeable these days, it doesn't really matter to us the specific typescript or CSS library.

Setting aside my prejudice against blockchain, the execution is solid and thank you for actually building on an actual testnet. You also justify your arguments well, and zero in on the aspects of blockchain that are relevant to you, which I appreciated.

