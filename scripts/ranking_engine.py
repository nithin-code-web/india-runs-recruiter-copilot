"""RANKING ENGINE - CORE SCORING LOGIC
=====================================
Multi-factor candidate scoring system that calculates comprehensive ranking scores.
Combines skill matching, experience, behavior signals, title relevance, career history,
assessment scores, and AI-related keyword matching.

Scoring breakdown:
- Skills matching: up to 30 points (6 required skills × 5 points each)
- Experience: up to 10 points (if meets minimum)
- Behavior: up to 10 points (open to work + recruiter response rate)
- Title relevance: up to 25 points (from title_score.py)
- Career keywords: up to variable points (from career_score.py)
- Assessment scores: up to variable points (from assessment_score.py)
- AI keyword relevance: up to variable points (from relevance_score.py)

Total scores typically range from 0-100+ depending on candidate quality.
"""
# Import scoring sub-modules
from career_score import calculate_career_score  # Career history keyword matching
from assessment_score import calculate_assessment_score  # Test score calculation
from skill_aliases import SKILL_ALIASES  # Skill alias mapping for flexible matching
from title_score import calculate_title_score  # Job title relevance scoring
from relevance_score import count_ai_keywords  # AI keyword detection and scoring
from generate_candidate_summary import generate_candidate_summary  # Strengths/risks generation

def calculate_candidate_score(candidate_features, job_features):
    """
    Calculate a comprehensive candidate score based on multiple factors.
    
    Args:
        candidate_features: Dictionary containing candidate information
        job_features: Dictionary containing job requirements
        
    Returns:
        Dictionary with score and scoring breakdown
    """
    # Initialize total score accumulator
    score = 0

    # ===== SKILL MATCHING SCORING =====
    # Convert skills to sets for efficient O(1) lookups
    candidate_skills = set(candidate_features["skills"])
    job_skills = set(job_features["required_skills"])

    # Track skills that match job requirements
    matched_skills = set()

    # Match required skills with candidate skills, including flexible alias matching
    # This handles variations like "Vector Databases" matching "Pinecone", "FAISS", etc.
    for required_skill in job_skills:

        # Direct match: exact skill name found in candidate profile
        if required_skill in candidate_skills:
            matched_skills.add(required_skill)

        # Alias match: check if candidate has any equivalent skill aliases
        elif required_skill in SKILL_ALIASES:
            # Get list of skill aliases (e.g., "Vector Databases" -> ["Milvus", "FAISS", ...])
            aliases = SKILL_ALIASES[required_skill]

            # If candidate has any alias, count as matching the required skill
            if any(skill in candidate_skills for skill in aliases):
                matched_skills.add(required_skill)

    # SKILL SCORING: 5 points per matched skill (max 30 points for 6 required skills)
    skill_score = len(matched_skills) * 5
    score += skill_score

    # ===== EXPERIENCE SCORING =====
    # Award 10 points if candidate meets minimum experience threshold
    # No partial credit - either meets minimum or doesn't
    experience_score = 0

    if candidate_features["experience"] >= job_features["required_experience"]["min"]:
        experience_score = 10
        score += experience_score

    # ===== BEHAVIOR SCORING =====
    # Score based on candidate engagement and responsiveness signals
    behavior_score = 0

    # +5 points: Candidate is actively open to work
    if candidate_features["open_to_work"]:
        behavior_score += 5

    # +5 points: Candidate responds to recruiter outreach (30%+ response rate)
    if candidate_features["response_rate"] >= 0.30:
        behavior_score += 5

    score += behavior_score
    
    # ===== TITLE RELEVANCE SCORING =====
    # Score based on job title relevance (see title_score.py)
    # Bonuses: +20-25 for AI/ML/Search engineers
    # Penalties: -20 for non-technical roles (marketing, HR, sales, accounting)
    title_score = calculate_title_score(candidate_features["title"])
    score += title_score
    
    # ===== CAREER HISTORY KEYWORD SCORING =====
    # Analyze career descriptions for relevant keywords (see career_score.py)
    # Keywords indicate prior experience with ranking, retrieval, embeddings, ML, etc.
    # Scoring: +5 points per matched keyword category (max ~40 points)
    career_score, found_keywords = calculate_career_score(
        candidate_features["career_descriptions"]
    )

    score += career_score

    # ===== ASSESSMENT SCORE CALCULATION =====
    # Score based on technical assessment/test results (see assessment_score.py)
    # Average test score divided by 10 (scaled to align with other scoring factors)
    # Higher assessment scores indicate stronger technical foundation
    assessment_score, average_assessment = (
        calculate_assessment_score(
            candidate_features["assessment_scores"]
        )
    )

    score += assessment_score
    
    # ===== AI KEYWORD RELEVANCE SCORING =====
    # Detect AI-specific keywords indicating domain expertise (see relevance_score.py)
    # Keywords include: ranking, retrieval, embeddings, vector search, LLM, etc.

    # Prepare text from skills and career history for keyword matching
    skills_text = " ".join(
        candidate_features["skills"]
    )

    career_text = " ".join(
        candidate_features["career_descriptions"]
    )

    # Count AI keywords in skills section
    # Keywords: embeddings, pinecone, faiss, milvus, etc. (weighted 8-10 points each)
    skills_relevance_score, skill_keywords = (
        count_ai_keywords(skills_text)
    )

    # Count AI keywords in career history
    # Keywords: ranking, recommendation, retrieval, LTR, XGBoost, etc. (weighted 6-12 points each)
    career_relevance_score, career_keywords = (
        count_ai_keywords(career_text)
    )

    # Combine relevance scores with weighted contribution
    # Career keywords weighted 3× higher than skills (career history more indicative of experience)
    relevance_score = (
        skills_relevance_score // 5  # Divide skills score by 5 to reduce dominance
    ) + (
        career_relevance_score * 3  # Career keywords weighted 3x
    )

    # Collect all detected AI keywords for display in candidate summary
    matched_ai_keywords = (
      skill_keywords +
      career_keywords
    )

    score += relevance_score
    
    # ===== GENERATE SUMMARY =====
    # Create human-readable strengths and risks assessment (see generate_candidate_summary.py)
    strengths, risks = generate_candidate_summary(
        candidate_features,
        list(matched_skills),
        matched_ai_keywords
    )
    
    # ===== RETURN COMPLETE SCORING BREAKDOWN =====
    # Return all scoring factors for ranking and candidate evaluation
    return {
        "score": score,
        "title_score": title_score,
        "relevance_score": relevance_score,
        "matched_ai_keywords": matched_ai_keywords,
        "strengths": strengths,
        "risks": risks,
        "matched_skills": list(matched_skills)
    }