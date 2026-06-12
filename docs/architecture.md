# AI Recruiter Copilot - Architecture

## Problem Statement

Recruiters often need to evaluate thousands of candidates for a single role.

Traditional keyword matching fails because:
- Skills are self-reported
- Candidates may list trendy technologies without real experience
- Career evidence is often hidden in work history

Goal:
Rank the most relevant candidates for a job description using multiple signals.

---

## Dataset

100,000 candidate profiles

Data Available:
- Profile Information
- Skills
- Career History
- Assessment Scores
- Behavioral Signals

---

## System Architecture

Job Description
    ↓
Job Feature Extraction
    ↓
Candidate Feature Extraction
    ↓
Scoring Engine
    ↓
Ranking Engine
    ↓
Explanation Engine
    ↓
JSON Export

---

## Scoring Components

### 1. Skill Match Score

Measures overlap between candidate skills and job requirements.

Includes skill alias mapping:
- Pinecone → Vector Databases
- FAISS → Vector Databases
- Milvus → Vector Databases

### 2. Career Evidence Score

Analyzes career descriptions for:
- Ranking systems
- Retrieval systems
- Recommendation systems
- Production AI systems

### 3. Assessment Score

Uses platform assessment results.

### 4. Behavioral Score

Considers:
- Open to Work
- Recruiter Response Rate
- Notice Period

### 5. Title Score

Rewards relevant AI-focused titles.

### 6. AI Relevance Score

Detects evidence of:
- Ranking
- Retrieval
- Embeddings
- Pinecone
- FAISS
- Milvus

---

## Output

Returns:
- Ranked Candidates
- Match Score
- Strengths
- Availability
- Risks