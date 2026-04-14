# Long List — Day 1

## 1. Learning & Education

- **1. Prompt-First Learning** — conversational learning that produces a co-authored study artifact
  - **What:** learner specifies goal, prior knowledge, and preferred modality. AI adapts through dialogue, with embedded assessment and proper math rendering. Output is a personalized study artifact shaped by the learner's questions — not a reformatted textbook. Extension: publish artifacts as shareable learning products (marketplace).
  - **Why now:** tools like Google's LearnYourWay reformat source material but skip the dialogue step where learners actively shape it. ChatGPT proved demand but has poor learning UX (broken equations, no progression, no persistent artifact). Knowledge-as-self-improvement is a rising thesis (Karpathy / Eureka Labs).
  - **Who:** self-learners, technical professionals upskilling, students, autodidacts.
  - **Edge:** I already produce notes this way through personal workflow and have a blog post articulating the thesis. Spans frontend, prompt engineering, and potential fine-tuning/RL on interaction data.

- **2. AI Orchestration Skill Assessment & Credentialing** — assess and credential the skill of managing AI agent teams
  - **What:** assessments testing a candidate's ability to coordinate multiple agents on business tasks, including intentionally flawed agents to probe critical thinking. Credentials issued on-chain (EAS/SAS) for portability.
  - **Why now:** executive surveys show broad AI-agent workforce expectations within 18 months. Existing certs (NVIDIA, Microsoft) test agent *building*, not *management*. EdTech funding is weak, so assessment infrastructure is a cleaner wedge than education.
  - **Who:** hiring managers deploying AI agents; knowledge workers seeking differentiation.
  - **Edge:** strategy is to start at credentialing and work backward to learning; interaction traces double as assessment data. Relevant background: AI/ML benchmarking at Amazon, including eval work for the Nova launch. Challenge designs and competitive landscape already drafted.

## 2. Personal Knowledge & Productivity

- **3. AI-Powered Personal Knowledge Management** — a continuously enriching knowledge base that bridges information overload and usable memory
  - **What:** three layers — (1) AI agents that ingest, clean, structure, and link notes with git-like versioning; (2) a knowledge graph backend storing entities and relationships (not just flat markdown + backlinks); (3) a prompting layer that draws on the personalized base for any task. Later: spaced-repetition-style proactive surfacing, and synthetic data generation + fine-tuning so the assistant "knows" your data in its weights, not just in context.
  - **Why now:** Karpathy's viral Apr 2026 post describes exactly this workflow — ingest raw sources, LLM compiles a wiki, Q&A against it, output rendered and filed back — and concludes there's room for a real product instead of a hacky collection of scripts. Vanilla RAG hit hard limits; agentic search is slow and token-hungry; nobody has built the continuous-enrichment layer upstream of retrieval. The DIY version works for power users; the opportunity is packaging it.
  - **Who:** knowledge workers, writers, researchers, technical practitioners who hoard notes but can't retrieve them.
  - **Edge:** background in computational neuroscience (how the brain consolidates memory); Obsidian power user; voice-memo capture pipeline v0 shipped. Differentiated from Karpathy-style DIY by the knowledge graph backend, proactive surfacing, and productized capture.

- **4. Conduit — Ambient Signal-to-Action Router** — low-friction capture routed to the right downstream destination
  - **What:** signal in, action out. Capture unstructured signals through the day (voice, X bookmarks, web highlights, screenshots), and an agent classifies each and fans it out: feed an Obsidian vault, create Anki cards, add Todoist todos, queue a research task for a background agent, draft an email, schedule a podcast digest, add to calendar. The bet: voice is the dominant new input modality, and apps are flipping from input surfaces to view/edit surfaces. Whoever owns routing owns the layer above all productivity apps.
  - **Why now:** LLMs are finally reliable at intent classification and multi-app orchestration; voice quality (Whisper, real-time transcription) has crossed the threshold for ambient capture; the app-as-view-layer shift is visible in agent-driven workflows.
  - **Who:** information-heavy professionals, builders, anyone whose capture-to-action pipeline is a graveyard of bookmarks and voice memos.
  - **Edge:** real personal pain point with a shipped v0 (voice-memo pipeline). Scales from narrow MVP (voice → Anki, voice → Todoist) to ambient OS. Can feed the PKM idea above as one output lane, giving the two a clean integration path without merging them.

## 3. Agent Infrastructure & Orchestration

- **5. Rubric — Self-Improvement Loops for Production Agents, Powered by Expert Judgment** — raise customer agent success rate week over week with auditable, expert-calibrated interventions
  - **What:** customers plug their deployed agent into Rubric and the success rate rises, measurably, week over week. Diffable prompt PRs and causal traces ("added constraint X after failure cluster Y; expected +4pp"). Critique loops, prompt rewriting, and evolutionary tournaments are calibrated against domain-expert judgment encoded as outcome rubrics — not generic LLM-as-judge, which is why existing "continuous improvement" products plateau. The expert-judgment substrate is internal machinery; the product surface is the improvement curve. Later-stage moat: fleet-wide learning across a customer's 5–50 agents.
  - **Why now:** 89% of agent teams have observability but only 52% have evals; Gartner projects >40% of agentic AI projects fail by 2027; Humanloop was acquired by Anthropic Aug 2025, leaving the prompt-management slot vacant; the crowded continuous-improvement cohort (Respan, Lucidic, Opik) is 12 months old and seed-stage with no credible reliability curves because they run on generic scoring — expert-calibrated judgment is the unlock.
  - **Who:** enterprises with 5–50 deployed agents, especially regulated verticals (claims processing, clinical intake, financial advisory) where generic scoring breaks down.
  - **Edge:** led eval workstreams for a major foundation-model launch, so I've built expert-judgment substrates at scale. Full-stack eval experience across Trainium, 1P vs 3P models, and RAG on Bedrock vs Azure/VertexAI. Enterprise sales motion is familiar from prior Amazon roles. Siemens medical imaging background aligns with regulated-vertical wedges.

- **6. Agent Memory System** — compressed memory parcels for long-running agent workflows
  - **What:** compress past context into structured parcels ("I did X to achieve Y using Z"), store full context in a database for retrieval, and rotate parcels in and out of the active window to simulate human-style dot-connecting. Solves the context-window bottleneck without relying on ever-larger windows.
  - **Why now:** context windows are growing but cost and latency scale with them; long-running agents (research, coding, ops) routinely blow past any window; memory architectures are an active research front (Mem0, Letta, OpenAI memory), but the compression-parcel approach — balancing compact retrieval keys with a full-fidelity backing store — is underexplored commercially.
  - **Who:** AI developers building long-running agents, agent framework builders, enterprise Rubric customers needing memory-aware evaluation.
  - **Edge:** computational neuroscience background on complementary learning systems (hippocampus/neocortex dual-memory, consolidation) maps directly to parcel-based memory. Pairs with Rubric (memory quality scored by outcome evals) and with the PKM idea (shared knowledge-graph backend).

## 4. AI × Crypto Convergence

All three ideas below sit on top of **ERC-8004** (deployed Jan 2026, co-authored by Ethereum Foundation, MetaMask, Google, Coinbase; 107K agents indexed), which ships three registries — Identity, Reputation, Validation — and leaves scoring and attestation logic open for third parties. They can be pursued independently or as layers of the same company.

- **7. Agent Reputation Oracle** — behavioral scoring for autonomous agents, published on-chain
  - **What:** ingest settlement traces from A2A, x402, AP2, and Tempo/MPP; score agents on reliability, success rate, dispute history, and counterparty outcomes; publish signed scores to ERC-8004's Reputation Registry. The registry is deliberately thin — scoring lives off-chain — so a credible oracle becomes the default underwriting input for merchants and protocols.
  - **Why now:** ERC-8004 just deployed; no one is publishing credible behavioral scores yet; x402 volume is still small (~$53K/day after wash filtering), so the trust layer is being built ahead of economic activity.
  - **Who:** merchants and protocols underwriting agent-counterparty risk; agent marketplaces.
  - **Edge:** ML and evals background is directly relevant to building the labeled-dataset pipeline; scoring rigor is the differentiator, not the on-chain contract.

- **8. ZK Compliance Attestations for Agents** — cryptographic primitives for operator-side claims
  - **What:** SDK plus trusted-issuer network producing ZK-verifiable claims that slot into ERC-8004's Validation Registry — e.g., "this operator is a Delaware LLC with $X insurance," "this agent was never jailbroken in eval suite Y," "training data excluded PII." Selective disclosure lets agents prove specific attributes without revealing underlying data. Sells to merchants complying with AP2 mandates, Visa TAP, or EU AI Act obligations.
  - **Why now:** Validation Registry supports zkML/TEE hooks but no one has shipped a clean SDK for operator-side claims; EU AI Act transparency obligations enforceable Aug 2, 2026.
  - **Who:** agent operators needing machine-readable compliance and competence proofs; merchants and payment rails requiring verifiable claims at runtime.
  - **Edge:** working knowledge of the relevant Ethereum cryptography; plugs directly into theme 1's Orchestration Credentialing for skill attestations with selective disclosure.

- **9. Coding Agent Credit Score** — vertical reputation product for coding agents
  - **What:** narrow application of the reputation oracle, focused on coding agents where ground truth is objectively measurable (PR merge rate, revert rate, bounty completion, CVE introductions, test pass rate). Portable score readable across coding-agent marketplaces; sold to the marketplaces (Replit, Cursor, Devin-style platforms) and to enterprises buying agent capacity.
  - **Why now:** coding agents are the first agent category with real transaction volume and genuine buyer demand for quality signal; ground-truth data is already machine-readable in git/CI pipelines; Anthropic and OpenAI are Tempo directory members, so on-chain coding-agent commerce is imminent.
  - **Who:** coding-agent marketplaces; enterprises buying coding-agent capacity.
  - **Edge:** objective evals fit Rubric's expert-judgment thesis; narrower scope makes this a faster starter wedge than the generic reputation oracle.

## 5. Finance & Investing

- **10. Crypto Project Analyzer** — LLM-powered research platform for crypto projects, leveraging on-chain transparency for fundamentals
  - **What:** research platform that answers arbitrary questions about any crypto project — tokenomics, unlock schedules, treasury health, governance, revenue, cross-chain positions, audit status — by combining on-chain state with off-chain data (forums, audits, filings). Core thesis: blockchain transparency enables real fundamental analysis in ways not possible for traditional equities, yet no incumbent has unified "one view per protocol." Open question: retail surface vs. pro analyst copilot for crypto funds / DAO treasuries vs. agent-facing API layer (plugs into theme 4). All three are live wedges.
  - **Why now:** incumbents each own a slice — Messari (research, paywalled), Nansen (wallets), Arkham (entity labeling), Dune (raw data), DefiLlama (DeFi-only), Token Terminal (revenue framing), Finrob ($3.9M seed Feb 2026, x402-native) — but none unify; retail pain has shifted toward narrative tracking (Kaito's lane); LLM hallucinations on tokenomics are a trust gap nobody has solved with published evals.
  - **Who:** crypto investors (retail, pro, DAO treasuries) — wedge TBD.
  - **Edge:** background in Ethereum cryptography and state-reading, and in LLM evals — published accuracy benchmarks on tokenomics/treasury/unlock questions would be a category no incumbent has claimed. Connects to theme 4 (verified fundamentals feeding an agent-facing API).

- **11. Prediction & Decision Market Research Agents** — AI research for active bets on prediction markets and conditional proposals on decision markets
  - **What:** agents that research active bets on prediction markets (Polymarket, Kalshi, Manifold) and conditional outcomes on decision markets / futarchy systems (GnosisDAO Advisory Futarchy, MetaDAO, Optimism futarchy grants), incorporate user feedback, and store mental models in a structured graph that updates on resolution. Surfaces to explore: calibration track record ("your forecaster's CV" with audited Brier score), research terminal for pro traders, research oracle for DAO governance, or autonomous agent that places bets. Open question: retail vs. pro trader vs. DAO governance buyer.
  - **Why now:** prediction markets hit ~$21B monthly volume in early 2026, Polymarket relaunched in US Dec 2025, Kalshi at $11B val, $35M PM-focused VC fund launched March 2026, 30% of Polymarket wallets already use AI agents; decision markets / futarchy shipped live pilots at Gnosis and Optimism in 2026; Vitalik's info-finance thesis is moving from essay to production; academic LLM-forecasting benchmarks (Metaculus, "Future Is Unevenly Distributed") show calibrated models but nobody has commercialized them.
  - **Who:** pro forecasters, DAO treasuries running conditional-outcome votes, retail bettors (lowest willingness-to-pay).
  - **Edge:** ML and evals background (calibration is an evals problem); computational neuroscience background (per-domain belief graphs that update on resolution map to complementary learning systems); Ethereum fluency for futarchy/decision-market integration. Crowded retail-terminal lane (Verso, Oddpool, Paradigm in-house) suggests going pro or DAO-governance instead.

## 6. Japan-Focused Ventures

- **12. Japanese AI Financial Research** — LLM-powered research platform for Japanese equities and TSE data
  - **What:** LLM research product for Japanese equities covering TSE fundamentals, 四季報-style qualitative commentary, 有報/決算短信 parsing, and NISA-aware analysis. Three wedges to pick from: (a) JP retail copilot (¥2–5K/mo, biggest TAM), (b) NISA-aware tax/portfolio optimizer (add-on), (c) English-first Japan-equity research for foreign capital (institutional WTP, no incumbent, hardest to replicate from outside Japan).
  - **Why now:** fiscal.ai (350K users, $10M Series A) has no Japanese localization and no JP push — the direct US analogue has not entered; 26.96M NISA accounts and ¥63T cumulative buys have already exceeded the 2027 target; Rakuten released Rakuten AI 3.0 (700B MoE JP LLM) Dec 2025 but has not shipped a retail research product in 16 months, signaling org inertia; J-Quants API (JPX) lowered the data moat since 2023; JP brokers have shipped narrow AI (robo-allocation, theme-stock picks) but no conversational research copilot; Goldman Nov 2025 flagged US investors rotating into Japan, creating an underserved English-first buyer for the foreign-capital angle.
  - **Who:** Japanese retail investors (NISA cohort), foreign analysts / family offices allocating to Japan, or JP pro traders — wedge TBD.
  - **Edge:** 10 years in Japan, Japanese fluency. Amazon Nova evals background transfers to JP-language financial reasoning evals; no serious JP finance eval has been published. Comfortable ingesting messy 有報/短信 PDFs.

- **13. AI-Native Cross-Border Marketing Agency (Japan ↔ Global)** — productized agency helping Japanese brands go global and global brands enter Japan
  - **What:** AI-native marketing agency built around AI throughput rather than billable hours, focused on cross-border work — Japanese D2C / consumer brands going US/EU via Amazon, Shopify, TikTok, and global brands entering Japan with culturally-adapted content. Deliverables: creative generation, campaign operations, multilingual adaptation (absorbs the Multilingual Twitter idea as one channel — same content adapted across JP/EN/FR at scale), retail media ops, ROAS-based pricing where possible. Sells to mid-market brands that cannot afford Dentsu/Hakuhodo but need quality beyond fragmented freelancers.
  - **Why now:** JP ad market hit ¥8.06T in 2025 but the Big 4 (Dentsu, Hakuhodo, ADK, CyberAgent) have bolted GenAI onto labor-heavy orgs — using AI to sell *more* creative volume, not to restructure costs; JP SMEs have 80%+ AI adoption intent and want done-for-you, not tools; AI translation quality (Claude/GPT-4o) on Japanese ↔ English is now ~94/100 with native editorial pass; no JP-domestic AI-native agency has strong brand recognition (Tetra Tokyo, JAPAN AI MARKETING are positioning plays, not category leaders); US AI-native agencies (Omneky, Pencil) lack JP on-the-ground sales motion.
  - **Who:** JP D2C and consumer brands going global (highest-defensibility customer); global mid-market brands entering Japan; JP SMEs underserved by the Big 4.
  - **Edge:** 10 years in Japan, Japanese fluency, EN/FR/JP. Five years at Amazon Fashion Japan (2016–2021), including Prime Wardrobe launch. ML + evals background to benchmark JP-market relevance against generic tools like Omneky. Native editorial pass on AI-translated content.

- **14. Japanese AI Apparel** — Japanese-inspired apparel with AI-personalized designs and Japanese manufacturing
  - **What:** apparel company combining Japanese design aesthetics (streetwear, workwear, utility fashion) with AI-generated personalized designs and Japanese manufacturing. Inspired by Nakamura-ya (Portland-based Japanese streetwear importer selling designs made entirely with AI) — proof AI-native apparel is not hypothetical.
  - **Why now:** AI image/design tools have crossed the threshold for production-ready apparel graphics; Japanese craftsmanship retains global cachet; D2C + micro-batch manufacturing reduces the inventory risk that sank previous apparel bets; consumer demand for "one-of-one" personalization is real across streetwear and workwear.
  - **Who:** fashion-conscious consumers globally who value quality + uniqueness; Japanese-aesthetic enthusiasts underserved by generic fast fashion.
  - **Edge:** five years at Amazon Fashion Japan (2016–2021) — apparel supply chains, inventory, returns economics, retail media. Existing Nakamura-ya relationship into the AI-streetwear niche. 10 years in Japan for manufacturer access. Honest flag: apparel remains operationally brutal (inventory, returns, taste), so unit economics are structurally thinner than software.

## 7. Others

Ideas kept for tracking but not primary candidates for selection. Retained to preserve context if a related wedge emerges during the sprint.

- **15. Meeting Conciseness Widget** — real-time per-speaker word count as social pressure for concise meetings
  - **What:** widget showing each speaker's running word count per turn on video calls, nudging brevity through gentle social pressure. Possible extension into a live coach flagging repetition, filler words, and missing participants.
  - **Why now:** meeting fatigue is universal. Whisper and Zoom AI Companion have crossed the threshold for reliable real-time attribution. No one is tackling meeting culture with social nudges.
  - **Who:** teams with meeting-heavy cultures; meeting organizers.
  - **Edge:** a feature, not a company. Zoom, Google, and Microsoft can copy it trivially.

- **16. AI-Native Ad Paradigm** — contextual advertising driven by live AI conversation
  - **What:** advertisers pay into a pool; the AI contextually selects relevant ads based on the user's ongoing conversation. Rethinks ads from first principles for the conversational era rather than porting display into chat.
  - **Why now:** AI conversations are displacing search as a primary information surface. Current ad models don't translate. OpenAI, Anthropic, and Google will need monetization beyond subscriptions.
  - **Who:** advertisers seeking reach inside AI conversations; AI platform operators seeking ad revenue.
  - **Edge:** a platform-level bet only the AI labs can execute. A third party can propose the model but not ship it.

- **17. AI Guidance for Physical Work** — AI-assisted instruction for tradespeople and field workers
  - **What:** AI guidance for physical tasks — construction, manufacturing, maintenance, field service — delivered via AR glasses, phone cameras, or voice. Real-time checklists, safety verification, step-by-step visual instruction.
  - **Why now:** AR hardware from Meta and Apple is maturing. Multi-modal models can reason over video input. Physical work is dramatically underserved by AI compared to knowledge work.
  - **Who:** tradespeople, field service technicians, manufacturing operators, construction crews.
  - **Edge:** no operator background in construction or trades. Shipping credibly would require a domain partner. Tracked because the category is underserved.

- **18. Same-Lender Refi Company** — streamline same-lender mortgage refinancing
  - **What:** a company specializing in same-lender refinancing, removing the full-purchase-equivalent process (reunderwriting, appraisal, title) that homeowners endure when refinancing with their existing lender.
  - **Why now:** the process is antiquated and obviously broken to anyone who has refinanced. Same-lender risk differs fundamentally from new-lender risk, but no industry player has capitalized on the distinction.
  - **Who:** homeowners with existing mortgages seeking rate relief.
  - **Edge:** no mortgage industry background and no regulatory or compliance staff. Tracked because the broken-ness is self-evident, not because of a founder wedge.
