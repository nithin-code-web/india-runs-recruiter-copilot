# AI Recruiter Copilot

## Overview

AI-powered candidate ranking system designed for the Redrob Intelligent Candidate Discovery Challenge.

The system analyzes job descriptions and ranks candidates from large candidate pools using multiple signals beyond simple keyword matching.

---

## Problem

Traditional candidate matching often relies on keyword overlap.

This approach fails because:
- Skills can be self-reported
- Keywords do not prove expertise
- Important experience is hidden inside career history

The challenge was to identify truly relevant candidates from 100,000 profiles.

---

## Solution

Built a multi-signal ranking engine that combines:

- Skill Matching
- Skill Alias Mapping
- Career Evidence Analysis
- Assessment Scores
- Behavioral Signals
- Title Relevance
- AI Relevance Detection

---

## Features

- Candidate Feature Extraction
- Job Feature Extraction
- Skill Alias Matching
- Career Evidence Scoring
- Assessment Scoring
- Behavioral Scoring
- AI Relevance Scoring
- Candidate Ranking
- Recruiter-Friendly Explanations
- JSON Export

---

## Project Structure

india-runs-recruiter-copilot/

├── data/
├── docs/
│   ├── architecture.md
│   └── results.md
│
├── outputs/
│   └── top_candidates.json
│
├── scripts/
│   ├── extract_candidate_features.py
│   ├── extract_job_features.py
│   ├── ranking_engine.py
│   ├── rank_candidates.py
│   ├── export_results.py
│   ├── generate_candidate_summary.py
│   ├── career_score.py
│   ├── title_score.py
│   ├── relevance_score.py
│   └── skill_aliases.py
│
└── README.md

## Architecture

(Reference architecture.md)

---

## Key Insight

One of the biggest discoveries during development:

Skills ≠ Evidence

A candidate mentioning AI technologies is not necessarily an AI engineer.

Career evidence proved to be a much stronger predictor of relevance than keyword counts.

---

## Results

Successfully ranked 100,000 candidates and surfaced highly relevant AI-focused profiles.

Top profiles included:
- Senior Applied Scientist
- Senior NLP Engineer
- AI Engineer
- Search Engineer
- Recommendation Systems Engineer

---

## Future Improvements

- Embedding-based semantic matching
- Hybrid retrieval
- LLM-powered candidate summaries
- Recruiter dashboard
- Online evaluation framework