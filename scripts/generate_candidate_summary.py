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

    # ===== EXPERIENCE STRENGTH =====
    if candidate_features["experience"] >= 5:
        strengths.append(
            f"{candidate_features['experience']} years experience"
        )

    # ===== AVAILABILITY STRENGTH =====
    if candidate_features["open_to_work"]:
        strengths.append(
            "Open to work"  # Actively looking for new opportunity
        )

    # ===== MATCHED SKILLS STRENGTHS =====
    # Show top 5 matched required skills
    for skill in matched_skills[:5]:
        strengths.append(
            f"Matched skill: {skill}"
        )

    # ===== AI DOMAIN SIGNALS =====
    # Show top 5 AI-related keywords found in profile
    for keyword in matched_ai_keywords[:5]:
        strengths.append(
            f"AI signal: {keyword}"  # Evidence of AI domain expertise
        )

    # ===== AVAILABILITY RISK =====
    # Candidates with long notice periods may take time to join
    if candidate_features.get("notice_period", 0) > 30:
        risks.append(
            f"Long notice period ({candidate_features['notice_period']} days)"  # Slow onboarding
        )

    # ===== ENGAGEMENT RISK =====
    # Low response rate indicates lower engagement with recruiters
    if candidate_features["response_rate"] < 0.20:
        risks.append(
            "Low recruiter response rate"  # May be unresponsive
        )

    return strengths, risks