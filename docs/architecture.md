# System Architecture

## Overview

The AI Recruiter Copilot is a candidate ranking and screening system designed to help recruiters identify the most relevant candidates for an AI-focused engineering role.

The system processes large candidate datasets, extracts relevant profile information, evaluates candidates using a multi-factor scoring engine, and produces ranked recommendations with human-readable explanations.

The ranking engine prioritizes demonstrated experience and career evidence over self-reported skills, making the results more reliable and recruiter-friendly.

---

## Architecture Flow

```text
Candidates Dataset (JSONL)
            │
            ▼
   Feature Extraction
            │
            ▼
      Ranking Engine
            │
            ├── Skill Score
            ├── Experience Score
            ├── Behavior Score
            ├── Title Score
            ├── Career Score
            ├── Assessment Score
            └── AI Relevance Score
            │
            ▼
 Candidate Summary Generator
            │
            ▼
     Ranked Candidates
            │
            ▼
      JSON Export
```

---

## Candidate Feature Extraction

The system reads candidate profiles from a JSONL dataset and extracts structured features used for ranking.

### Extracted Features

#### Profile Information

* Candidate ID
* Current Job Title
* Years of Experience

#### Skills

* Technical skills
* AI/ML skills
* Infrastructure skills

#### Behavioral Signals

* Open to Work status
* Recruiter Response Rate
* Interview Completion Rate
* Offer Acceptance Rate
* Notice Period

#### Assessments

* Technical assessment scores
* Skill validation scores

#### Career History

* Previous job descriptions
* Industry experience
* Career progression

---

## Ranking Engine

The ranking engine evaluates each candidate using multiple scoring components.

### 1. Skill Matching Score

Compares candidate skills against required job skills.

Examples:

* Python
* Embeddings
* Retrieval Systems
* Ranking Systems
* Vector Databases
* Evaluation Frameworks

The engine also supports skill aliases.

Example:

```text
Vector Databases
 ├─ Pinecone
 ├─ FAISS
 ├─ Milvus
 ├─ Qdrant
 └─ Weaviate
```

---

### 2. Experience Score

Candidates receive experience points when they satisfy the minimum experience requirement defined in the job profile.

---

### 3. Behavior Score

Behavioral signals help estimate candidate availability and engagement.

Signals include:

* Open to Work
* Recruiter Response Rate

---

### 4. Title Relevance Score

The system rewards titles that strongly align with the target role.

Examples:

* AI Engineer
* Machine Learning Engineer
* Search Engineer
* Recommendation Systems Engineer
* NLP Engineer

The system also penalizes clearly unrelated titles such as:

* Marketing Manager
* HR Manager
* Sales Executive

---

### 5. Career History Score

Career descriptions are analyzed for evidence of relevant domain experience.

Keyword categories include:

* Ranking Systems
* Retrieval Systems
* Recommendation Systems
* Embeddings
* Machine Learning
* LLMs
* Data Engineering

Only one match per category is counted to prevent keyword inflation.

---

### 6. Assessment Score

Technical assessment results are averaged and normalized into the overall ranking score.

This helps validate practical skill proficiency beyond self-reported experience.

---

### 7. AI Relevance Score

The system identifies AI-related keywords across candidate skills and career history.

Examples:

* Ranking
* Retrieval
* Recommendation
* Embeddings
* Pinecone
* FAISS
* Milvus
* Learning-to-Rank
* XGBoost
* LightGBM

Career evidence is weighted more heavily than self-reported skills.

---

## Candidate Summary Generation

After scoring, the system generates recruiter-friendly explanations.

Each candidate receives:

### Strengths

Examples:

* Strong match in Retrieval Systems
* Built retrieval systems
* Experience with Pinecone vector databases

### Availability

Examples:

* Open to work
* Notice period: 30 days

### Risks

Examples:

* Long notice period
* Low recruiter response rate

---

## Scalability

The system was tested on datasets containing up to 100,000 candidate profiles.

The ranking pipeline processes candidates sequentially and maintains only the required ranking information, making it suitable for large-scale candidate screening workflows.

---

## Output

The final output includes:

* Ranked candidate list
* Candidate score
* Strengths
* Availability information
* Risk indicators

This provides recruiters with both quantitative rankings and qualitative explanations for decision-making.
