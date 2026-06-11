from career_score import calculate_career_score
from assessment_score import calculate_assessment_score
from generate_explanation import generate_explanation
from skill_aliases import SKILL_ALIASES
from title_score import calculate_title_score
from relevance_score import count_ai_keywords

def calculate_candidate_score(candidate_features, job_features):

    score = 0

    candidate_skills = set(candidate_features["skills"])
    job_skills = set(job_features["required_skills"])

    matched_skills = set()

    for required_skill in job_skills:

        if required_skill in candidate_skills:
            matched_skills.add(required_skill)

        elif required_skill in SKILL_ALIASES:

            aliases = SKILL_ALIASES[required_skill]

            if any(skill in candidate_skills for skill in aliases):
                matched_skills.add(required_skill)

    skill_score = len(matched_skills) * 5
    score += skill_score

    experience_score = 0

    if candidate_features["experience"] >= job_features["required_experience"]["min"]:
        experience_score = 10
        score += experience_score

    behavior_score = 0

    if candidate_features["open_to_work"]:
        behavior_score += 5

    if candidate_features["response_rate"] >= 0.30:
        behavior_score += 5

    score += behavior_score
    
    title_score = calculate_title_score(candidate_features["title"])
    score += title_score
    

    career_score, found_keywords = calculate_career_score(
        candidate_features["career_descriptions"]
    )

    score += career_score

    assessment_score, average_assessment = (
        calculate_assessment_score(
            candidate_features["assessment_scores"]
        )
    )

    score += assessment_score

    strengths, risks = generate_explanation(
        candidate_features,
        found_keywords,
        average_assessment
    )
    
    skills_text = " ".join(
        candidate_features["skills"]
    )

    career_text = " ".join(
        candidate_features["career_descriptions"]
    )

    skills_relevance_score, skill_keywords = (
        count_ai_keywords(skills_text)
    )

    career_relevance_score, career_keywords = (
        count_ai_keywords(career_text)
    )

    relevance_score = (
        skills_relevance_score // 5
    ) + (
        career_relevance_score * 3
    )

    matched_ai_keywords = (
      skill_keywords +
      career_keywords
    )

    score += relevance_score
    print("\nDEBUG")

    print("Title:", candidate_features["title"])

    print("Skills Relevance:", skills_relevance_score)

    print("Career Relevance:", career_relevance_score)

    print("Final Relevance:", relevance_score)
    
    return {
        "score": score,
        "title_score": title_score,
        "relevance_score": relevance_score,
        "matched_ai_keywords": matched_ai_keywords,
        "strengths": strengths,
        "risks": risks,
        "matched_skills": list(matched_skills)
    }