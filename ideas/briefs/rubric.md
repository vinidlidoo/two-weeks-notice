# Rubric — Agent Reliability Partner

## What Rubric is

Rubric helps enterprises make their deployed AI agents work reliably in production. We install the improvement loop their team doesn't have: a systematic way to diagnose which part of the stack is hurting output — the model, the sequence of calls, the system prompt, the validation criteria, the context flow — apply the fix, capture it durably, and measure whether it helped. Our engineers and domain experts embed with the customer; our **scoring rubrics** (structured checklists for what "good output" looks like) are written with the people who do the actual work: claims adjudicators, paralegals, medical coders. Over time the playbook becomes software. Rubric is independent of any model provider, SDK, or harness vendor.

## Assumptions this brief rests on

1. Enterprises have adopted **agent frameworks and harnesses** faster than they've built the muscle to make agents reliable in production. The landscape spans open-source frameworks (LangGraph, CrewAI, OpenCode, Cline, Aider), lab-vended SDKs (Anthropic's Claude Agent SDK, OpenAI's Agents SDK), coding agents shipped as products (Claude Code, Codex, Cursor, GitHub Copilot agent mode, Devin), and plenty of in-house equivalents. None of them ships a customer-operable improvement loop.
2. Agent quality depends on many parameters at once: which models are called and in what sequence, tool and system settings, prompts, validation criteria, and how context flows between steps (without leaking from private sources, but also without bloating every call). When performance slips, most teams have no systematic way to diagnose *which* parameter is hurting output.
3. Production evaluations, where they exist, tend to be rudimentary (a handful of assertions) or non-actionable (a score with no clear next step). The ad-hoc prompt nudges engineers make during debugging don't get captured back into the system — so quality doesn't compound from one cycle to the next.
4. The problem is universal, not confined to regulated verticals. But it's sharpest in domains where failure has real cost (insurance, legal, healthcare, finance) — and solving it there requires domain expertise, not just ML tooling.
5. Teams with a disciplined improvement loop outperform teams relying on ad-hoc debugging plus generic **LLM-as-judge** (where one language model scores another's output with a prompt template). The loop's strongest form pairs domain experts with well-designed scoring rubrics.

## Why now

- **Most deployed agents are watched, not evaluated.** LangChain's *State of Agent Engineering* survey (Dec 2025, n=1,340) reports **89% of teams have implemented observability for their agents, but only 52% have implemented evaluations.** LangChain sells eval tooling, so not a disinterested source, but the direction matches other surveys. [[source](https://www.langchain.com/state-of-agent-engineering)]
- **Even the biggest lab products show the reliability gap.** Claude Code and Codex have millions of active developers and named enterprise customers (Cisco, Nvidia, Harvey, AMD), but ship without a systematic way for customers to measure or improve them. InfoWorld recently quoted an AMD engineering director saying his team stopped using Claude Code on complex kernel work because it "skims the hard bits," and a February 2026 update regressed reasoning on a widely-tracked issue. The most widely deployed agents on earth are effectively un-improvable by the enterprises running them. [[InfoWorld](https://www.infoworld.com/article/4154973/enterprise-developers-question-claude-codes-reliability-for-complex-engineering.html)]
- **Analysts are forecasting mass cancellation.** Gartner predicts more than **40% of agentic AI projects will be canceled by end of 2027**, citing "inadequate risk controls." Unpacked: teams can't prove output quality for customer exposure, can't demonstrate performance for compliance, and can't reduce hand-holding costs — all three trace to a missing improvement loop. [[source](https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027)] McKinsey's *State of AI 2025* finds **62% of enterprises experimenting with agents but fewer than 10% scaling.** [[source](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai)]
- **Regulated failures are raising the real cost of unreliable agents.** Three examples on board agendas:

  - **UnitedHealth's nH Predict** — an AI claims-denial system for Medicare Advantage. Class-action litigation alleges ~90% error rate on denials. Exactly the kind of failure a proper evaluation loop would have caught. [[source](https://www.cbsnews.com/news/unitedhealth-lawsuit-ai-deny-claims-medicare-advantage-health-insurance-denials/)]
  - **DoNotPay** — consumer "AI lawyer" startup. FTC settled in Feb 2025 ($193K fine) because outputs shipped with no attorney validation. [[source](https://www.ftc.gov/news-events/news/press-releases/2025/02/ftc-finalizes-order-donotpay-prohibits-deceptive-ai-lawyer-claims-imposes-monetary-relief-requires)]
  - **Moffatt v. Air Canada** — a 2024 Canadian tribunal ruling that the airline legally owned its chatbot's statements. Set the tone that enterprises own their agent's outputs. [[source](https://www.mccarthy.ca/en/insights/blogs/techlex/moffatt-v-air-canada-misrepresentation-ai-chatbot)]

- **A potential buyer cohort was recently displaced.** In August 2025, Anthropic hired the team behind **Humanloop** — which sold prompt-management and evaluation tooling with reported customers including Duolingo, Gusto, and Vanta — but did *not* acquire the product. It was shut down. Those customers need to re-platform. Worth validating whether they're still actively shopping. [[source](https://techcrunch.com/2025/08/13/anthropic-nabs-humanloop-team-as-competition-for-enterprise-ai-talent-heats-up/)]

## Who else is doing this

The closest players fall into four groups:

- **Observability platforms** — show you what your agents are doing, not how to make them better. Main player: **LangSmith** (LangChain's own platform). Others: Arize, Weights & Biases (via W&B Weave), HoneyHive, Braintrust.
- **Evaluation platforms** — score outputs and run guardrails, but using generic LLM-as-judge. Main player: **Galileo** (best-funded, explicit regulated-industry positioning). Others: Patronus. [[Galileo](https://venturebeat.com/ai/galileos-luna-redefines-genai-evaluation-boasting-97-lower-costs-and-11x-faster-speeds)]
- **Improvement-loop startups** — auto-rewrite prompts based on scoring. Main player: **Respan** (auto-rewrites prompts when it detects regressions; $5M raise in Mar 2026). Others: Lucidic, Opik. [[Respan](https://siliconangle.com/2026/03/18/respan-raises-5m-bring-proactive-observability-ai-agents/)]
- **Generalist consultancies** — Scale AI, Turing, McKinsey QuantumBlack, BCG X. AI-adjacent work at volume; not specialists in agent reliability.

Separately, the labs themselves — Anthropic with Claude Code and the Claude Agent SDK, OpenAI with Codex and the Agents SDK, Google with Gemini — ship the runtimes and the embedded **forward-deployed engineers (FDEs)** who help enterprises deploy them. This is the most direct competitor to Rubric's consultancy motion. The structural difference: lab FDEs ship their employer's product by design — if the best fix is switching models or harnesses, the incentive isn't there. Enterprises running multi-model, multi-harness stacks have no natural home for genuinely independent reliability work.

Two structural gaps in the landscape:

1. **Domain-expert-calibrated rubrics are an academic finding, not a product.** Recent research (XpertBench, ShotJudge) shows scoring calibrated against real domain experts beats generic LLM-as-judge in hard domains. No one sells this as a service. [[XpertBench](https://arxiv.org/html/2604.02368v1)]
2. **Cross-customer learning is empty space.** Every existing platform operates one customer at a time. Nobody aggregates failure patterns across a portfolio. (Earning the right to do that is in *What makes it defensible*.)

## What's technically ready, and what isn't

- **Ready today.** Mature open-source prompt-optimization frameworks exist. Self-critique and constitutional-AI techniques are commodity. Fast, cheap evaluator models are off-the-shelf. Rubric doesn't need to invent anything at the technique layer.
- **What frameworks don't solve.** When an agent's performance slips, nothing in the standard stack tells you which change is highest-leverage — the diagnostic question that opens this brief. Generic LLM-as-judge compounds the problem with well-documented failure modes, like *position bias* (preferring whatever response was shown first), that become real liabilities. [[LLM-as-judge survey](https://arxiv.org/html/2411.15594v1)]
- **The scarce asset** is (a) the scoring rubrics — sheets written with domain experts on what *good* output looks like, calibrated against real customer data — and (b) the engineering judgment to decide what to change and in what order. That's what Rubric accumulates engagement by engagement, and why a services motion is the natural starting point.

## Where we could enter

Four candidate entry points, not ranked:

- **The Humanloop-displaced cohort.** Duolingo, Gusto, Vanta, and peers. Fastest path to revenue; most at risk of the default outcome (they re-sign with Galileo or Patronus).
- **Insurance claims reliability.** Large payers, **pharmacy benefit managers (PBMs** — the middlemen between health insurers and pharmacies), and claims-denial software vendors, all re-examining their stacks after the UnitedHealth case. Highest willingness-to-pay; long sales cycles; vertical domain credibility (operator co-founder or advisor with payer/PBM background) is a prerequisite.
- **Legal / personal-injury (PI) claims.** The PI space has a successful AI incumbent (**EvenUp**, AI demand-letter generation, $2B valuation in 2025) and a regulatory warning shot in DoNotPay. Mid-market legal-operations platforms will need external validation to avoid FTC exposure. [[EvenUp](https://fortune.com/2025/10/07/exclusive-evenup-raises-150-million-series-e-at-2-billion-valuation-as-ai-reshapes-personal-injury-law/)]
- **Financial-advisory back office.** Morgan Stanley reports >98% advisor adoption of its internal AI assistant with no publicly reported failures — pain is latent. Target back-office workflows (document retrieval, compliance flagging), not client-facing advice.

**Not a candidate: clinical scribing.** Abridge (AI medical-scribe software at 150 health systems) already owns the expert-calibration data. Too late. [[Abridge](https://www.fiercehealthcare.com/ai-and-machine-learning/abridge-ambient-scribe-arrives-athenahealth-ehr)]

## What makes it defensible

- **A domain-calibrated improvement playbook.** Every engagement produces scoring rubrics, a labeled failure-mode taxonomy, a diagnostic checklist for the vertical (which parameter to tune first when performance slips), versioned fixes, and benchmark fixtures. After several engagements in a vertical, Rubric has the canonical playbook — something no new entrant can replicate without comparable client access.
- **Cross-customer learning — a moat we'd have to earn.** The compounding story only works if clients allow pooled, anonymized failure patterns across accounts. Earning it requires strong anonymization, opt-in pooling, vertical carve-outs, and a concrete explanation of how pooling improves *their* outcomes (deeper benchmark library, faster failure-mode detection). Chainalysis and Snowflake Data Cloud are precedents.
- **Model- and harness-independent.** Independence from any lab or harness is a durable selling point for enterprises running multi-model, multi-harness stacks — a seat no current competitor credibly occupies.
- **Auditable unit of work.** Each improvement is a reviewable, versioned change — a prompt diff with a causal link to a specific failure cluster — that compliance, regulators, and internal procurement can inspect.

## How it could make money

Three revenue layers that track the loop's maturity. The first two are services engagements — Rubric installs and operates the improvement loop inside the customer's stack. The third is a productized tier once the playbook is mature enough to run with lighter touch. Both services price ranges are worth testing in customer discovery:

| Layer | Price range | Comparable |
|---|---|---|
| **Services — grounded** | $200–400K per customer per year | Reported enterprise pricing for AI-agent products in adjacent categories (Decagon, Humanloop pre-acquisition) |
| **Services — aspirational** | $500K–$1M retainer | Palantir's forward-deployed-engineer engagements |
| **Software tier (later)** | $150–300K per customer per year | Enterprise evaluation platforms (Galileo, Patronus) |

Honest caveat: services-first motions are a known failure mode in B2B software — the default outcome is calcification into a boutique consultancy. Palantir's and Scale AI's successes stand out precisely because the transition is hard. Making it work requires deliberate productization (shared rubric library, shared eval harness, shared failure-mode taxonomy) from the first engagement. [[8VC on the services-to-product path](https://www.8vc.com/resources/the-ai-services-wave-lessons-from-palantir-in-the-new-age-of-ai)]

## What would pressure the thesis

None of these would kill the idea outright, but each narrows the opportunity or raises the execution bar. Each is paired with the lever Rubric can pull.

- **The Humanloop-displaced cohort re-signs with Galileo or Patronus before Rubric reaches them.** This is Rubric's fastest revenue path as those enterprises are actively re-platforming right now. If incumbents close the deals first, Year 1 revenue has to come entirely from vertical engagements, which have long sales cycles. The thesis survives; the runway tightens. *Counter:* start vertical engagements in parallel with the cohort outreach rather than sequencing them after.
- **Anthropic productizes what the Humanloop team built.** Shipped with Anthropic-model bias by construction. *Counter:* the independent card holds against any single-lab product.
- **Scale AI enters the same vertical.** Genuinely a race. *Counter:* time-to-first-engagement in a specific vertical. A focused team can close the Humanloop-displaced cohort and build a calibrated playbook in one vertical (claims, legal) while a horizontal organization is still deciding which verticals to enter — generalists don't move into regulated verticals quickly.
- **Clients uniformly refuse cross-customer learning.** Caps the moat, not the business. *Counter:* services and software tiers still work; fleet is upside, not core.
- **A vertical incumbent locks calibration data** (as Abridge did in clinical scribing). Closes a specific wedge permanently. *Counter:* pick wedges ahead of lock-in; be willing to swap.

## What we don't know yet

- **Humanloop cohort reality.** Are Duolingo, Gusto, Vanta, and peers still shopping, or already re-signed? Cold calls will answer.
- **Cross-customer data terms.** What contract language makes pooled learning sellable? Precedents: Chainalysis, Palantir Foundry, Snowflake Data Cloud.
- **Vertical lock-in speed.** Clinical scribing closed in ~18 months. Are claims and legal on similar clocks, or looser?
- **Real-world gap between generic and expert-calibrated scoring.** Is Galileo's evaluator model actually failing in production at claims or legal engagements? If yes, the pull is real. If no, the calibration thesis is weaker than it reads.
- **Scale AI GTM direction.** Horizontal, or regulated-vertical? Public output from Q2–Q3 2026 will tell.
- **Services-trap avoidance.** What concrete mechanism turns engagement output into software — a shared rubric library, a shared eval harness, a shared failure-mode taxonomy? The answer decides whether this is a company or a boutique.

---

*Name note: "Rubric" is a working title. A Y Combinator Winter 2026 company called "Rubric AI" exists in an adjacent space; the final name will need to change.*
