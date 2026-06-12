# Results and Evaluation

## Objective

The goal of this project was to build an AI Recruiter Copilot capable of ranking candidates for an AI-focused engineering role using multiple signals rather than relying solely on keyword matching.

The system evaluates candidates using skills, experience, assessments, behavioral signals, title relevance, career history, and AI-domain expertise.

---

# Dataset

### Candidate Dataset

* Source: Provided JSONL candidate dataset
* Candidates Evaluated: 100,000
* Processing Mode: Sequential candidate ranking
* Output: Ranked candidate recommendations with explanations

---

# Ranking Strategy

The ranking engine combines multiple scoring components:

| Component          | Purpose                             |
| ------------------ | ----------------------------------- |
| Skill Score        | Match required technical skills     |
| Experience Score   | Validate minimum experience         |
| Behavior Score     | Measure engagement and availability |
| Title Score        | Evaluate role alignment             |
| Career Score       | Analyze past work experience        |
| Assessment Score   | Validate technical proficiency      |
| AI Relevance Score | Detect AI-specific expertise        |

This approach provides more accurate rankings than simple keyword matching.

---

# Example Top Ranked Candidates

## Rank #1

### Senior Applied Scientist

**Score:** 333

### Strengths

* 16.2 years of professional experience
* Strong match in Retrieval Systems
* Strong match in Vector Databases
* Strong match in Python
* Worked on ranking systems
* Experience with recommendation engines
* Built retrieval systems
* Experience with embedding-based search
* Experience with Pinecone vector databases

### Availability

* Open to work
* Notice period: 30 days

### Risks

* No major risks identified

---

## Rank #2

### Senior NLP Engineer

**Score:** 332

### Strengths

* 8.9 years of professional experience
* Strong match in Retrieval Systems
* Strong match in Vector Databases
* Strong match in Python
* Experience with Pinecone vector databases
* Worked on ranking systems
* Experience with recommendation engines
* Built retrieval systems
* Experience with embedding-based search

### Availability

* Open to work
* Notice period: 30 days

### Risks

* No major risks identified

---

## Rank #3

### AI Engineer

**Score:** 327

### Strengths

* 16.9 years of professional experience
* Strong match in Embeddings
* Strong match in Retrieval Systems
* Strong match in Vector Databases
* Built retrieval systems
* Experience with embedding-based search
* Experience with FAISS vector search
* Experience with Milvus vector databases
* Worked on ranking systems

### Availability

* Open to work
* Notice period: 60 days

### Risks

* Long notice period (60 days)

---

# Key Improvements Made During Development

## 1. Skill Alias Matching

Problem:

Required skills and candidate skills often used different terminology.

Example:

```text
Vector Databases
vs
Pinecone
FAISS
Milvus
```

Solution:

Implemented a skill alias mapping system that recognizes equivalent technologies.

---

## 2. Title Relevance Scoring

Problem:

Non-technical candidates sometimes ranked higher than expected.

Solution:

Added title-based bonuses and penalties.

Examples:

```text
AI Engineer                +20
Search Engineer            +20
Marketing Manager          -20
HR Manager                 -20
```

---

## 3. Career Evidence Weighting

Problem:

Self-reported skills alone were not reliable.

Solution:

Prioritized career history evidence over profile keywords.

This improved ranking quality significantly.

---

## 4. AI Relevance Scoring

Problem:

The system initially struggled to distinguish AI specialists from general software engineers.

Solution:

Added weighted AI-domain keyword detection.

Examples:

* Ranking
* Retrieval
* Recommendation
* Embeddings
* Pinecone
* FAISS
* Milvus

---

## 5. Explainable Candidate Recommendations

Problem:

Scores alone do not help recruiters make decisions.

Solution:

Generated recruiter-friendly explanations including:

* Strengths
* Availability
* Risks

---

# Observations

The final ranking system consistently prioritized candidates with:

* Search experience
* Ranking systems experience
* Recommendation system experience
* Retrieval engineering experience
* Vector database expertise
* Machine learning engineering backgrounds

Top-ranked candidates typically held roles such as:

* AI Engineer
* Search Engineer
* Senior NLP Engineer
* Applied Scientist
* Machine Learning Engineer
* Recommendation Systems Engineer

---

# Conclusion

The final system successfully combines structured candidate data, career evidence, behavioral signals, and AI-domain expertise to produce explainable candidate rankings.

The approach moves beyond simple keyword matching and provides recruiter-friendly insights that help identify the strongest candidates for AI-focused engineering roles.
