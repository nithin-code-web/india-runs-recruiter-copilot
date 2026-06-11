from career_score import calculate_career_score
from assessment_score import calculate_assessment_score
from generate_explanation import generate_explanation
from skill_aliases import SKILL_ALIASES
from title_score import calculate_title_score
from relevance_score import calculate_relevance_score

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
    
    relevant_text = " ".join([
        candidate_features["title"],
        " ".join(candidate_features["skills"]),
        " ".join(candidate_features["career_descriptions"])
        ])
    
    relevance_score, matched_ai_keywords = (
        calculate_relevance_score(relevant_text)
    )
    score += relevance_score

    return {
        "score": score,
        "title_score": title_score,
        "relevance_score": relevance_score,
        "matched_ai_keywords": matched_ai_keywords,
        "strengths": strengths,
        "risks": risks,
        "matched_skills": list(matched_skills)
    }