# Long List — Day 1

Ideas with brief rationale. Don't filter too hard — volume first.

## Ideas

- **AI Study Notes Platform** — turn AI conversation study notes into a marketable learning product
  - What: take study notes from AI conversations and publish them as interactive learning materials with follow-up questions ("livre dont vous etes le heros" style)
  - Why now: knowledge as self-improvement is trending (Karpathy/Eureka Labs thesis); AI tutoring still can't replicate the best human tutors, but curated materials can bridge the gap
  - Who: self-learners, technical professionals upskilling
  - Edge: already producing these notes; combines frontend, prompt engineering, and potential for fine-tuning/RL later

- **Personalized AI Textbook Builder** — build a custom textbook on any topic through conversation
  - What: generate personalized textbooks by using the user's questions and the AI's responses to shape content and depth
  - Why now: static textbooks can't compete with adaptive content; borrows from oboe.xyz model
  - Who: students, professionals, curious autodidacts
  - Edge: differentiated by personalization — adapts to the reader's level and foundations

- **Interactive Adaptive Textbook** — education app that dynamically adapts to your understanding
  - What: interactive textbook better than raw ChatGPT — proper math rendering, level-adaptive content, builds on your foundations in adjacent subjects
  - Why now: ChatGPT showed demand but the UX for learning is poor (broken equations, no progression)
  - Who: students and self-learners
  - Edge: focus on UX and pedagogical structure over raw model capability

- **AI Math/ML Blog or Book** — write the math behind AI as a blog/book to signal competence
  - What: technical blog covering transformers, optimizations, etc. (inspired by Francis Bach's work)
  - Why now: AI literacy demand is exploding; strong written content is a career asset
  - Who: ML practitioners, technical audience
  - Edge: personal expertise; doubles as a portfolio piece

- **Agent Memory System** — compressed memory parcels for AI agents
  - What: compress past context into parcels (I did X to do Y using Z), store full context in DB for retrieval; parcels rotate in/out of context window to simulate human dot-connecting
  - Why now: context window limitations are a real bottleneck for agent workflows
  - Who: AI developers, agent framework builders
  - Edge: novel approach to memory that balances compression with retrievability

- **Multi-Cultural Ideation Agents** — simulate cultural diversity for idea generation
  - What: multi-agent system where agents contribute ideas prompted in different languages/cultures to surface novel combinations
  - Why now: agentic AI is maturing; cross-cultural innovation is underexplored in AI
  - Who: innovation teams, consulting firms, business schools (INSEAD angle)
  - Edge: unique concept bridging AI and cross-cultural thinking

- **Author-Reviewer-Teacher Loop** — self-improving multi-agent drafting system
  - What: Author drafts, Reviewer critiques, loop until pass; Teacher model optimizes prompts for next task. Human can step into any role. Related to GEPA/DSPy approaches
  - Why now: prompt optimization (DSPy) gained traction in 2025; builds on proven patterns
  - Who: knowledge workers, consultants, anyone producing structured documents
  - Edge: the Teacher layer and human-in-the-loop make it distinct from basic agent chains

- **Voice-to-Anki Pipeline** — voice input on phone to auto-generated flashcards
  - What: capture voice input, LLM breaks it into Anki flashcards, uploads via Anki API/MCP
  - Why now: spaced repetition is proven; the friction is in card creation
  - Who: language learners, students, professionals
  - Edge: low-friction capture via voice; LLM handles card formatting

- **Bookmark-to-Podcast Pipeline** — crawl bookmarks and convert to audio
  - What: crawl Twitter/YouTube/Reddit bookmarks, use NotebookLM-style tools to generate podcast summaries, let models expand on themes
  - Why now: podcast consumption is up; bookmark graveyards are universal
  - Who: information-heavy professionals, content consumers
  - Edge: solves a real personal pain point; leverages existing bookmark behavior

- **AI Note Organizer** — AI that structures and extracts ideas from your notes
  - What: AI agent that goes through notes to restructure them and surface actionable ideas
  - Why now: note-taking tools are mature but organization is still manual
  - Who: knowledge workers, researchers
  - Edge: builds on personal workflow experience

- **Multilingual Twitter Strategy** — same content across 3 language accounts
  - What: run 3 Twitter accounts (JP, FR, EN) with the same content adapted per language
  - Why now: AI translation quality is now good enough for authentic cross-language content
  - Who: personal brand building
  - Edge: trilingual capability

- **Prediction Market Research Agents** — AI agents researching active bets
  - What: agents research prediction/decision market bets, incorporate user feedback, store mental models in a graph structure
  - Why now: prediction markets gaining legitimacy (Polymarket, etc.); Vitalik's info-finance thesis
  - Who: sophisticated bettors, researchers, decision-makers
  - Edge: feedback loop + mental model storage creates compounding advantage

- **Japanese FinChat** — Japanese version of FinChat.io for retail investors
  - What: LLM-powered financial analysis platform for Japanese equities and TSE data
  - Why now: expanded NISA driving Japanese retail investor growth; TSE data unlikely to be well-served by US-first platforms
  - Who: Japanese retail investors
  - Edge: Japan market knowledge, language capability, first-mover in a growing segment

- **Crypto Project Analyzer** — transparent analysis of crypto projects
  - What: like FinChat but for crypto — leverage blockchain transparency for fundamental analysis
  - Why now: crypto speculation dominates but on-chain data enables real analysis
  - Who: crypto investors seeking fundamentals over hype
  - Edge: blockchain transparency as a data advantage

- **Same-Lender Refi Company** — modernize same-lender mortgage refinancing
  - What: company specializing in same-lender refi, streamlining a process currently treated like a full purchase
  - Why now: the current process is antiquated and ripe for disruption
  - Who: homeowners with existing mortgages
  - Edge: focused niche; process innovation opportunity

- **Agent-to-Agent Protocol Services** — build a competent agent that gets paid via A2A
  - What: ride the agent-to-agent protocol wave (Google's A2A) to design agents that provide services and get compensated
  - Why now: A2A protocols are emerging; first movers can establish agent reputation
  - Who: businesses needing automated services
  - Edge: early positioning in a nascent ecosystem

- **Japanese AI Apparel** — Japanese-inspired fashion with AI-personalized designs
  - What: apparel company combining Japanese design aesthetics with AI-generated personalized designs, leveraging Japanese manufacturing
  - Why now: AI design tools are maturing; Japanese craftsmanship has global cachet
  - Who: fashion-conscious consumers who value quality and uniqueness
  - Edge: combines personal experience in fashion, Japan, and AI (Nakamura-ya inspiration)

- **Meeting Conciseness Widget** — real-time token/word count per speaker
  - What: widget showing each speaker's word count per turn in real-time to create social pressure for concise communication; expand to live meeting coach
  - Why now: meeting fatigue is universal; no one's solving it with social nudges
  - Who: teams, meeting organizers
  - Edge: simple concept, viral potential; risk: Zoom could copy

- **Objective RAG** — reduce bias in RAG-powered search
  - What: modify RAG implementations to filter out self-promotional citations (e.g., Neo4j saying they're the best graph DB)
  - Why now: RAG is becoming standard but bias in retrieval is largely ignored
  - Who: enterprises using RAG for research/decisions
  - Edge: novel angle on a known problem

- **Smart Contract Dispute Resolution** — automated contracts with AI-adjudicated disputes
  - What: Ethereum smart contracts that auto-execute based on oracles, with a dispute mechanism using randomly selected jurors (validators), eventually AI-adjudicated
  - Why now: smart contracts are mature but dispute resolution is still a gap; AI adjudication is becoming feasible
  - Who: businesses in commercial disputes, DeFi users
  - Edge: could upend commercial lawsuit market; combines crypto and AI

- **AI Orchestration Skill Assessment & Credentialing** — assess and credential the emerging skill of managing AI agent teams
  - What: build assessments that test a candidate's ability to coordinate multiple AI agents on complex business tasks; include intentionally flawed agents to test critical thinking; issue credentials on-chain (EAS/SAS) so they're portable and decentralized
  - Why now: 82% of executives expect AI agents in workforce within 18 months; existing certs (NVIDIA, Microsoft) only test building agents, nobody credentials agent management; EdTech funding low so framing as assessment infrastructure is better
  - Who: hiring managers deploying AI agents, white-collar knowledge workers seeking differentiation
  - Edge: unique "start at credentialing, work backward to learning" strategy; interaction traces as assessment data; Amazon AI/ML benchmarking background (delivered 50%+ of evals for Nova model launch). Most developed idea — challenge designs specified, competitive landscape researched

- **AI-Powered Personal Knowledge Management** — continuously enriching knowledge base bridging information overload and memory
  - What: three-layer system — (1) AI agents that clean/structure/link notes with git-like versioning, (2) knowledge graph backend storing entities and relationships, (3) prompting layer that draws on personalized knowledge for any task. Later: spaced-repetition-style proactive surfacing of ideas
  - Why now: vanilla RAG hit hard limits; agentic search is slow and token-hungry; nobody's built the continuous enrichment layer upstream of retrieval
  - Who: knowledge workers, writers, researchers
  - Edge: computational neuroscience background (master's thesis on how the brain learns); Obsidian power user; voice memo pipeline v0 already shipped

- **ZK-Verified Skill Attestations / Trust Layer for Agentic Commerce** — convergence of education thesis with crypto/ZK
  - What: (A) issue AI orchestration assessment results as on-chain attestations with ZK selective disclosure (prove "top 15%" without revealing full trace); (B) build a "trust layer" for autonomous agent commerce — an "agent operator license" verified via ZK proof, machine-readable by other agents and payment platforms
  - Why now: Tempo mainnet launched (Mar 2026) with Machine Payments Protocol; Coinbase + Cloudflare announced x402 Foundation; ZK proof market projected $7.59B by 2033; every payment protocol needs a trust layer
  - Who: AI agent operators, agentic commerce platforms, protocols needing human-competence verification
  - Edge: sits at intersection of AI + blockchain + education + hard CS; cypherpunk values alignment

- **Decentralized AI Agent Marketplace** — the "ENS/DNS for autonomous agents"
  - What: on-chain registry where AI agents publish verifiable credentials, reputation scores, and capability manifests; infrastructure every agent needs to participate in commerce
  - Why now: A2A + x402 protocols lack trusted agent discovery and payment functionality; 500K+ weekly agent transactions as of Oct 2025
  - Who: AI agent developers, B2B payments platforms
  - Edge: more decentralized/permissionless than Google/Coinbase solutions; ML/distributed systems background

- **AI Agent Music Royalties on Ethereum** — autonomous agents handling music licensing and instant payments
  - What: AI agents represent independent artists, discover when music is used, negotiate licensing, execute instant royalty payments via x402/stablecoins on-chain
  - Why now: Google AP2 and Coinbase x402 launched; Warner Music settled with AI startup Udio; platforms like HAiO leading autonomous AI music agents
  - Who: independent musicians and artists
  - Edge: convergence of blockchain + AI + music interests

- **Japan Fitness/Wellness Tokenization** — fitness platform on a Japan-focused Ethereum L2
  - What: tokenize personal training achievements, create AI digital twins of elite trainers, integrate Japanese wellness culture (onsen, mindfulness, martial arts), users earn tokens for consistency
  - Why now: Japan 2025 tax reform slashed crypto rates to 20%; 200+ new Web3 startups in Japan in 2025; Sony's Soneium L2 bridging Web2/Web3; Move-to-Earn market projected $1.7B by 2030
  - Who: fitness enthusiasts globally, especially those drawn to Japanese wellness culture
  - Edge: 10 years living/working in Japan; fluent in Japanese; deep cultural knowledge

- **Continual Learning / Memory Architecture for LLMs** — updating model weights dynamically post-training
  - What: research and build architectures allowing LLMs to update weights continuously, inspired by complementary learning systems in neuroscience (hippocampus + neocortex dual-memory, nightly consolidation, overcoming catastrophic forgetting)
  - Why now: current AI models have frozen weights; context window management is a band-aid; step-change opportunity vs. incremental improvements
  - Who: AI research community, AI labs
  - Edge: master's degree in computational neuroscience (2 years studying how the brain learns); published research

- **Medical AI Diagnostic/Treatment Platform** — leveraging healthcare + AI background
  - What: medical AI diagnostic or treatment optimization platform
  - Why now: medical AI about to take off; unique positioning with healthcare background
  - Who: healthcare providers, patients
  - Edge: technical sales background in medical imaging at Siemens; AI/ML expertise

- **Life Coach Agent** — multi-model feedback system for personal coaching
  - What: AI life coach leveraging multi-model feedback loops for guidance and personal development
  - Who: individuals seeking structured self-improvement
  - Edge: builds on Author-Reviewer-Teacher loop concept

- **AI-Augmented Creativity Tool** — software that explores your ideas using AI
  - What: AI that makes connections between your past reflections (stored as text) and current problem — surfacing ideas not in your "brain RAM"
  - Why now: people capture far more than they retrieve; AI can bridge the gap
  - Who: creative professionals, founders, writers
  - Edge: personal workflow experience; overlaps with knowledge management thesis

- **Self-Reinforcing Prompt Optimization Loop** — agent that improves its own prompts
  - What: self-improvement loop where an AI model updates its own system prompt, validated by an eval that only accepts quality-raising changes; possible niche for Japanese speakers
  - Why now: prompt engineering is manual and fragile; automated optimization is the next step
  - Who: AI developers, teams deploying LLM-powered products
  - Edge: related to DSPy/GEPA work; could target underserved Japanese-language niche

- **Evolutionary Agent Tournament** — Darwinian selection of AI agents
  - What: spin up many agents with different weights, prompts, and memory; identify top performers; use the best as seeds for next generation; agents can earn/spend money as a fitness metric
  - Why now: agent proliferation makes selection/optimization a real need
  - Who: AI developers, agent platform builders
  - Edge: novel evolutionary approach to agent optimization

- **Content Attestation CLI** — hash + sign files for provenance
  - What: CLI tool that hashes a file, signs it with a local key, outputs a JSON attestation; later IPFS pinning or on-chain anchor
  - Why now: AI-generated content explosion makes authenticity/provenance critical
  - Who: content creators, publishers, journalists
  - Edge: simple tool addressing a growing trust problem

- **AI-Native Ad Paradigm** — contextual ads driven by live AI conversations
  - What: new advertising model where advertisers pay a minimum to participate and the AI picks contextually relevant ads based on the user's live conversation
  - Why now: AI conversations replacing search; current ad model doesn't translate
  - Who: advertisers, AI platform operators
  - Edge: rethinks ads from first principles for the conversational AI era

- **R&D Center in Japan** — US-Japan technology bridge
  - What: build a technology R&D center in Japan with a commercial arm in North America (Seattle)
  - Why now: Japan's tech sector is re-emerging; cross-border opportunities are underexploited
  - Who: technology companies needing US-Japan bridge
  - Edge: 10 years in Japan, trilingual, deep cross-cultural experience

- **AI-Native Agencies (Japan)** — high-quality AI-native agency leveraging Japan's quality bar
  - What: AI-native agency targeting a market where quality standards are exceptionally high
  - Why now: AI agency space is exploding but quality varies wildly; Japan's quality culture is a wedge
  - Who: Japanese businesses, global companies needing Japan-quality AI work
  - Edge: Japan market knowledge, quality culture understanding

- **Stablecoin Financial Services** — financial services built on stablecoins
  - What: financial services infrastructure leveraging stablecoins for payments, lending, or treasury management
  - Why now: stablecoin adoption accelerating; regulatory clarity improving
  - Who: businesses and consumers in crypto-forward markets
  - Edge: crypto interest + financial services understanding

- **AI Guidance for Physical Work** — AI assisting physical/manual tasks
  - What: AI-powered guidance for physical work — could be construction, manufacturing, maintenance
  - Why now: AR/AI tools maturing; physical work is underserved by AI compared to knowledge work
  - Who: tradespeople, field workers, manufacturers

- **Post-Training / Model Specialization** — specialized model fine-tuning services
  - What: services for post-training and specializing foundation models for specific domains or tasks
  - Why now: foundation models are general-purpose; enterprises need specialized versions
  - Who: enterprises deploying AI in specific domains
  - Edge: ML expertise and benchmarking background

- **Version Control for Agents** — GitButler-inspired version control for agent workflows
  - What: version control system designed for teams of AI agents working together (inspired by GitButler's Series A from a16z)
  - Why now: agents are starting to collaborate; current version control isn't built for non-human actors
  - Who: AI agent developers, teams running multi-agent systems
  - Edge: early insight into the need; developer tooling experience
