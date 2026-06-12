# AI Recruiter Copilot

An AI-powered candidate ranking and screening system designed to help recruiters identify the most relevant candidates for AI-focused engineering roles.

The system evaluates candidate profiles using multiple signals including skills, experience, career history, assessments, behavioral indicators, title relevance, and AI-domain expertise to produce explainable candidate rankings.

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

The AI Recruiter Copilot processes candidate profiles and generates ranked recommendations using a multi-factor scoring system.

The system evaluates:

* Technical skills
* Years of experience
* Behavioral signals
* Career history
* Assessment performance
* Job title relevance
* AI-specific expertise

The final output includes:

* Candidate score
* Strengths
* Availability information
* Risk indicators

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
git clone <repository-url>
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

* Python
* JSONL Dataset Processing
* Rule-Based Ranking Engine
* Explainable AI-Inspired Scoring Framework

---

# Author

Nithin Budime

Built as part of an AI-powered recruiter screening and candidate ranking project focused on explainable hiring recommendations.
