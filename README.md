<div align="center">

# Recruiter Copilot

### Explainable Candidate Ranking Engine

<img src="https://img.shields.io/badge/Multi--Factor%20Ranking%20Engine-Recruiter%20Decision%20Support-purple?style=for-the-badge" />

<br>

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Status](https://img.shields.io/badge/Status-Completed-success)
![Dataset](https://img.shields.io/badge/Dataset-100K_Candidates-orange)
![Architecture](https://img.shields.io/badge/Architecture-Modular-green)
![Backend](https://img.shields.io/badge/Focus-Backend_Engineering-purple)

</div>

An explainable candidate ranking and screening system designed to help recruiters identify the most relevant candidates using skills, experience, career history, assessments, and behavioral signals.

The system evaluates candidate profiles using multiple signals including skills, experience, career history, assessments, behavioral indicators, title relevance, and domain-specific expertise to produce explainable candidate rankings.

---

## Project Metrics

| Metric | Value |
|----------|----------|
| Candidates Ranked | 100,000 |
| Ranking Signals | 7 |
| Output Type | Explainable Rankings |
| Architecture | Modular Pipeline |

---

# Problem Statement

Traditional candidate screening often relies heavily on keyword matching and manual resume review.

This creates several challenges:

* Important candidates can be missed due to terminology differences.
* Self-reported skills may not reflect actual experience.
* Recruiters must manually evaluate large candidate pools.
* Ranking decisions are difficult to explain.

This project addresses these challenges by combining multiple scoring signals into a recruiter-friendly ranking engine.

---

# Solution Overview

The Recruiter Copilot ranking engine processes candidate profiles and generates ranked recommendations using a multi-factor scoring system.

The system evaluates:

* Technical skills
* Years of experience
* Behavioral signals
* Career history
* Assessment performance
* Job title relevance
* Domain-specific expertise

The final output includes:

* Candidate score
* Strengths
* Availability information
* Risk indicators

---

# Highlights

- Ranked and evaluated 100,000 candidate profiles
- Built a multi-factor candidate scoring engine
- Implemented skill alias matching for flexible candidate evaluation
- Prioritized career evidence over self-reported skills
- Generated recruiter-friendly strengths, availability, and risk summaries
- Exported structured ranking results for downstream consumption

---

# Features

## Multi-Factor Candidate Ranking

Combines multiple scoring dimensions instead of relying solely on keyword matching.

### Scoring Components

* Skill Matching Score
* Experience Score
* Behavior Score
* Title Relevance Score
* Career History Score
* Assessment Score
* AI Relevance Score

---

## Skill Alias Matching

Supports equivalent technologies through alias mapping.

Example:

```text
Vector Databases
├── Pinecone
├── FAISS
├── Milvus
├── Qdrant
└── Weaviate
```

This improves matching accuracy across different candidate profiles.

---

## Career Evidence Prioritization

The ranking engine gives greater importance to demonstrated work experience than self-reported skills.

Examples:

* Ranking systems
* Retrieval systems
* Recommendation systems
* Embedding pipelines
* AI infrastructure

---

## Explainable Recommendations

Each ranked candidate includes:

### Strengths

Examples:

* Strong match in Retrieval Systems
* Experience with Pinecone vector databases
* Built retrieval systems

### Availability

Examples:

* Open to work
* Notice period information

### Risks

Examples:

* Long notice period
* Low recruiter response rate

---

# Demo

Example ranked candidate output:

```text
Rank #1

Candidate ID: CAND_0039754
Title: Senior Applied Scientist
Score: 333

Strengths:
✓ 16.2 years of professional experience
✓ Strong match in Retrieval Systems
✓ Strong match in Vector Databases
✓ Worked on ranking systems

Availability:
✓ Open to work
📅 Notice period: 30 days

Risks:
No major risks found
```

---
# System Architecture

```text
Candidates Dataset
        │
        ▼
Feature Extraction
        │
        ▼
Ranking Engine
 ├── Skill Score
 ├── Experience Score
 ├── Behavior Score
 ├── Title Score
 ├── Career Score
 ├── Assessment Score
 └── AI Relevance Score
        │
        ▼
Candidate Summary Generation
        │
        ▼
Ranked Candidate Results
```

For detailed architecture, see:

```text
docs/architecture.md
```

---

# Project Structure

```text
.
├── data/
│   └── candidates.jsonl
│
├── docs/
│   ├── architecture.md
│   └── results.md
│
├── outputs/
│   └── ranked_candidates.json
│
├── scripts/
│   ├── ranking_engine.py
│   ├── rank_candidates.py
│   ├── title_score.py
│   ├── relevance_score.py
│   ├── career_score.py
│   ├── career_keywords.py
│   ├── assessment_score.py
│   ├── skill_aliases.py
│   ├── generate_candidate_summary.py
│   ├── export_results.py
│   └── extract_job_features.py
│
├── README.md
└── requirements.txt
```

---

# Installation

Clone the repository:

```bash
git clone https://github.com/nithin-code-web/india-runs-recruiter-copilot
cd india-runs-recruiter-copilot
```

Create virtual environment:

```bash
python -m venv venv
```

Activate environment:

```bash
venv\Scripts\activate
```

---

# Running the Project

Run candidate ranking:

```bash
py scripts/rank_candidates.py
```

Export ranked candidates:

```bash
py scripts/export_results.py
```

---

# Results

Dataset Size:

```text
100,000 candidate profiles
```

Top-ranked profiles consistently included:

* AI Engineers
* Search Engineers
* Applied Scientists
* NLP Engineers
* Machine Learning Engineers
* Recommendation Systems Engineers

For detailed evaluation results:

```text
docs/results.md
```

---

# Challenges Solved

### Skill Terminology Differences

Implemented alias-based matching for equivalent technologies.

### Candidate Ranking Quality

Added title relevance scoring and AI-domain relevance scoring.

### Career Evidence Analysis

Prioritized demonstrated experience over profile keywords.

### Explainability

Generated recruiter-friendly strengths, availability, and risk summaries.

---

# Future Improvements

Potential future enhancements include:

* Embedding-based semantic candidate matching
* Hybrid retrieval and ranking
* LLM-generated recruiter summaries
* Recruiter dashboard and analytics
* Database integration
* Candidate search interface
* Real-time ranking APIs

---

# Tech Stack

| Category | Technology |
|-----------|------------|
| Language | Python |
| Data Format | JSONL |
| Processing | Data Extraction & Transformation |
| Ranking Engine | Multi-Factor Rule-Based Scoring |
| Documentation | Markdown |
| Architecture | Modular Backend Pipeline |

---

# Key Learnings

Through this project I learned:

- Designing explainable ranking systems
- Building modular backend pipelines
- Processing large datasets efficiently
- Creating multi-factor scoring frameworks
- Generating recruiter-friendly recommendations
- Structuring maintainable Python applications

---
# Author

Nithin Budime

Built as an explainable candidate ranking and recruiter decision-support system focused on transparent hiring recommendations.