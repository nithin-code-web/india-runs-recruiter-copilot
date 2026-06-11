import json

from extract_candidate_features import candidate_features
from extract_job_features import job_features
from skill_aliases import SKILL_ALIASES

score = 0

candidate_skills = set(candidate_features["skills"])
job_skills = set(job_features["required_skills"])

matched_skills = candidate_skills.intersection(job_skills)

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

print("\n=== MATCH RESULT ===\n")

print("Matched Skills:", matched_skills)

print(f"Skill Score: {skill_score}")
print(f"Experience Score: {experience_score}")
print(f"Behavior Score: {behavior_score}")

print(f"\nFinal Score: {score}")
print("\nCareer History:\n")