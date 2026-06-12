"""CANDIDATE SUMMARY GENERATION
=====================================
Generates human-readable strengths and risks for ranked candidates.
Based on matched skills, AI keywords, experience, engagement signals, etc.

Used for final display of top candidates with their key attributes.
"""

def generate_candidate_summary(candidate_features,
                               matched_skills,
                               matched_ai_keywords):
    """Generate strengths and risks summary for a candidate.
    
    Args:
        candidate_features: Dictionary of candidate profile data
        matched_skills: List of skills matched to job requirements
        matched_ai_keywords: List of AI-related keywords found in profile
    
    Returns:
        Tuple of (strengths: list, risks: list)
    """
    strengths = []  # Positive attributes
    risks = []  # Risk factors
    availability = [] # Availability signals

    # ===== EXPERIENCE STRENGTH =====
    if candidate_features["experience"] >= 5:
        strengths.append(
            f"{candidate_features['experience']} years of professional experience"
        )

    # ===== AVAILABILITY STRENGTH =====
    if candidate_features["open_to_work"]:
        availability.append(
            "Open to work"  # Actively looking for new opportunity
        )

    # ===== MATCHED SKILLS STRENGTHS =====
    # Show top 5 matched required skills
    for skill in matched_skills[:5]:
        strengths.append(
            f"Strong match in: {skill}"
        )
        
    # ===== AI DOMAIN SIGNALS =====

    AI_SIGNAL_EXPLANATIONS = {
    "pinecone": "Experience with Pinecone vector databases",
    "faiss": "Experience with FAISS vector search",
    "milvus": "Experience with Milvus vector databases",
    "retrieval": "Built retrieval systems",
    "ranking": "Worked on ranking systems",
    "recommendation": "Experience with recommendation engines",
    "embeddings": "Experience with embedding-based search",
    "vector search": "Experience with vector search infrastructure",
    "learning-to-rank": "Built learning-to-rank models",
    "xgboost": "Experience with production ML ranking models",
    "lightgbm": "Experience with production ML ranking models"
    }

    # Remove duplicate AI keywords while preserving order
    unique_keywords = []

    for keyword in matched_ai_keywords:

        if keyword not in unique_keywords:
            unique_keywords.append(keyword)


    # Add top 5 unique AI signals
    for keyword in unique_keywords[:5]:

        explanation = AI_SIGNAL_EXPLANATIONS.get(
            keyword,
            f"AI expertise: {keyword}"
        )
        strengths.append(explanation)



    # ===== AVAILABILITY RISK =====
    
    # Candidates with long notice periods may take time to join
    if candidate_features.get("notice_period", 0) > 0:

        availability.append(
            f"Notice period: {candidate_features['notice_period']} days"
        )

    if candidate_features["notice_period"] > 30:

        risks.append(
            f"Long notice period ({candidate_features['notice_period']} days)"
        )
        
    # ===== ENGAGEMENT RISK =====
    # Low response rate indicates lower engagement with recruiters
    if candidate_features["response_rate"] < 0.20:
        risks.append(
            "Low recruiter response rate"  # May be unresponsive
        )

    return strengths, risks, availability