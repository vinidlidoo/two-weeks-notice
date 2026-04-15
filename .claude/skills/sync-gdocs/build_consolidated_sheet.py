#!/usr/bin/env python3
"""Build ideas/consolidated.csv from Vincent's long-list.md and Pavan's Ideas tab."""
import csv
import re
from pathlib import Path

LONG_LIST = Path("ideas/long-list.md")
OUT = Path("ideas/consolidated.csv")

# Parse Vincent's 18 ideas: `- **N. Name**` followed by `  - **Summary:** ...`
text = LONG_LIST.read_text()
pattern = re.compile(
    r"^- \*\*(\d+)\.\s+(.+?)\*\*\s*\n\s*-\s*\*\*Summary:\*\*\s+(.+?)(?=\n\s*-\s*\*\*[A-Z])",
    re.MULTILINE | re.DOTALL,
)
v_rows = []
for m in pattern.finditer(text):
    n, name, summary = m.group(1), m.group(2).strip(), m.group(3).strip()
    summary = re.sub(r"\s+", " ", summary)
    v_rows.append((name, summary, "V", f"Vincent List #{n}"))

assert len(v_rows) == 18, f"Expected 18 V rows, got {len(v_rows)}"

# Pavan's 29 ideas from the "Ideas" tab of Ideation April 2026
p_rows = [
    ("World State OS / Real-time World Data", "A continuously updated, structured knowledge graph mapping signals from news, sensors, markets, and open data into a queryable model of global events and causal relationships. The finance and intelligence sector is the wedge; becoming the grounding layer for AI agents is the prize. Can also be structured, machine-readable geopolitical risk signals delivered as a live API rather than a consultancy report. Targets multinationals, insurers, and banks who need this data integrated into software systems, not emailed as a PDF. Or a platform that turns messy public and private data — satellite imagery, shipping data, job postings, web traffic — into clean business signals and emerging trends. Gives mid-market companies access to the kind of alternative data intelligence that hedge funds and large corporates currently monopolise."),
    ("Trend Mapping Engine", "Software that combines many data sources to surface emerging patterns significantly earlier than traditional research methods. The value is in the synthesis and early signal, not the data itself — most of the inputs are already public."),
    ("GTM Predictions & Scenario Modelling", "AI-powered go-to-market experimentation that models scenarios across pricing, features, competition, and positioning using internal and external data. Runs virtual launches and simulations to find the highest-probability growth strategy before committing real resources."),
    ("Synthetic Attribution", "A digital twin of your market that simulates a counterfactual world where you didn't run a campaign, revealing true marketing incrementality rather than correlation. Solves one of the oldest and most expensive unsolved problems in marketing measurement."),
    ("Human Agentic Prediction Markets", "AI agents that simulate and forecast outcomes across markets, geopolitics, and world events — combined with a platform where humans and agents both participate. A new category sitting at the intersection of Polymarket, forecasting tools, and agentic AI."),
    ("LLM Accuracy & Hallucination Guard Rails", "A domain-specific verification and monitoring platform that sits between an LLM and its users, testing model outputs against ground truth before they reach the end user. Especially critical in regulated industries like healthcare, legal, and education where errors cause real harm."),
    ("AI Governance & Risk Management Platform", "A unified product helping enterprises manage AI safely end-to-end — model evaluation, approval workflows, access control, secure deployment, monitoring, audit trails, and executive dashboards. As regulation catches up with deployment this becomes mandatory infrastructure for every company running AI in production."),
    ("AI Agent Oversight Layer", "Software that supervises AI agents as they take real-world actions, flags risky behaviour, and escalates decisions that require human approval. As agents proliferate across enterprises the gap between capability and control becomes a critical and largely unsolved problem."),
    ("Policy Sentinel", "A real-time signal engine that reads every global legislative draft and maps emerging regulatory risk directly to a company's specific product surface. Turns the firehose of global policy change into actionable, firm-specific alerts rather than generic legal briefings."),
    ("Brand Firewall", "A cryptographic verification and monitoring layer for all corporate media that protects brands from deepfake sabotage and AI-driven misinformation campaigns. As synthetic media becomes indistinguishable from real, provenance and authentication become board-level risk issues."),
    ("Human Layer of LLMs", "Training AI models on human emotion, feeling, and lived experience — going beyond text to capture what makes us distinctly human. As AGI approaches, the most important unresolved question is whether AI can understand not just what we say but how we feel."),
    ("Cursor for Product Managers", "An AI-native product discovery system that goes from customer interviews and usage data all the way to prioritised PRDs, Figma mocks, and dev-ready tickets. The bottleneck in software has shifted from coding to figuring out what to build — this closes that gap. A more specific use case: An agent that continuously watches competitor updates, market shifts, and internal signals, then automatically rewrites roadmap documents and tickets so they never go stale. Turns product documentation from a snapshot into a living system."),
    ("Digital Twins", "Creating simulation models of real-world systems — factories, cities, supply chains, individuals — that can be used to test decisions before making them in the real world. Has applications across urban planning, healthcare, industrial operations, and personal decision-making."),
    ("Real News Filter", "A platform that filters out AI-generated and synthetic content to surface only verifiably human-produced journalism and information. As AI-generated content floods the internet, provenance and authenticity become the genuinely scarce resource."),
    ("Offline & Synthetic Data", "Digitising valuable offline data sources to improve AI model accuracy, combined with generating synthetic data to fill gaps where real data is scarce or sensitive. A hard, unsexy problem with an enormous payoff for whoever does it well at scale."),
    ("AI Career Navigation Layer", "Personalised AI guidance helping people figure out what to learn, how to prove it, and who to reach — especially those from non-traditional or immigrant backgrounds. Fills the critical gap between having a qualification and actually building a career."),
    ("Immigrant Talent Marketplace", "A platform using AI to assess, translate, and match the skills of immigrants whose credentials go unrecognised in their new country. One of the most underutilised talent pools in the world, with a broken system that AI is now genuinely capable of fixing."),
    ("AI Reskilling Infrastructure", "A B2B platform helping large employers reskill workers being displaced by AI, delivered as an ongoing sandbox or real-time learning environment. Learning will be the only durable skill left in white-collar work — whoever owns that infrastructure owns a generation of enterprise contracts."),
    ("NGO Copilot", "A productivity and operations platform modernising the work of NGO and non-profit staff under enormous pressure from funding cuts and administrative overhead. Starts with AI-assisted grant writing and expands into project tracking, impact monitoring, and reporting."),
    ("Children's Progress Tracking", "An AI tool giving parents and educators real visibility into early childhood development using voice AI to capture signals that overworked staff can't document manually. The 0–3 years are the most critical for development and currently the most data-blind."),
    ("Early Childhood Screenless Tech", "Voice and ambient AI for young children that enables learning — languages, stories, concepts — without a screen. Lets children engage with technology in a developmentally appropriate way, solving the problem every parent with a toddler is wrestling with."),
    ("Foundation Models for Education", "Domain-specific LLMs trained on pedagogy, curriculum, and learning science rather than general internet text. A model purpose-built for teaching would be dramatically more effective than a general one and could underpin an entire generation of education products."),
    ("Emotional Intelligence Platform", "A tool that teaches, develops, and tracks emotional intelligence — the one distinctly human capability that can't easily be replicated or outsourced to AI. Whether for children, adults in the workplace, or teams in organisations, EQ development has never been systematically addressed at scale."),
    ("Brain Retraining / Therapeutic Tech", "Technology that goes beyond traditional therapy to actively retrain neural pathways using evidence-based approaches like neuroplasticity, behavioural science, and art therapy. Therapy as it exists today is expensive, inconsistent, and hard to access — this rebuilds it from first principles."),
    ("Decision Making Layer", "An AI system that helps individuals and organisations model decisions and simulate outcomes before committing — starting with financial decisions and expanding outward. A counter to the trend of outsourcing thinking entirely to AI, this helps people decide better rather than just deciding for them."),
    ("Recruitment & Skills Assessment", "AI-native recruitment that validates what candidates can actually do rather than what their CV claims, using agents to assess skills in realistic scenarios. Traditional hiring is increasingly broken — degrees signal less, interviews are easily gamed, and demonstrated ability is the only honest signal left."),
    ("AI-Native Agency Platform", "Infrastructure enabling service businesses — design, legal, marketing — to deliver client work using AI and achieve software margins in what has always been a people-cost business. YC Spring 2026 RFS called this out as a category they are actively looking to fund."),
    ("Remaking Traditional Apps", "Identifying established software categories — LinkedIn, Figma, Salesforce — and rebuilding them as AI-native products before the incumbents can reinvent themselves. The question is simply which category to pick and whether you can move faster than a well-funded legacy player."),
    ("Sovereign AI", "Building national or regional AI infrastructure — models, data, and compute — owned and governed locally rather than dependent on US or Chinese tech giants. Increasingly relevant as geopolitical tensions reshape the technology landscape, particularly in Canada"),
]

assert len(p_rows) == 29, f"Expected 29 P rows, got {len(p_rows)}"

with OUT.open("w", newline="") as f:
    w = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
    w.writerow(["Name", "Description", "Origin", "Ref", "V score", "P score", "Converged"])
    row_idx = 2
    for name, desc, origin, ref in v_rows:
        w.writerow([name, desc, origin, ref, "", "", f'=IF(AND(N(E{row_idx})>=4,N(F{row_idx})>=4),"🎯","")'])
        row_idx += 1
    for name, desc in p_rows:
        w.writerow([name, desc, "P", "", "", "", f'=IF(AND(N(E{row_idx})>=4,N(F{row_idx})>=4),"🎯","")'])
        row_idx += 1

print(f"Wrote {len(v_rows)} V rows + {len(p_rows)} P rows = {len(v_rows)+len(p_rows)} total to {OUT}")
