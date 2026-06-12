import json

from extract_job_features import job_features
from ranking_engine import calculate_candidate_score

results = []

with open("data/candidates.jsonl", "r", encoding="utf-8") as f:

    for i, line in enumerate(f):

        if i >= 100000:  # Limit to first 100K candidates for efficiency
            break

        candidate = json.loads(line)

        candidate_features = {
            "candidate_id": candidate["candidate_id"],

            "title": candidate["profile"]["current_title"],

            "experience": candidate["profile"]["years_of_experience"],

            "skills": [
                skill["name"]
                for skill in candidate["skills"]
            ],

            "assessment_scores":
                candidate["redrob_signals"]["skill_assessment_scores"],

            "github_score":
                candidate["redrob_signals"]["github_activity_score"],

            "response_rate":
                candidate["redrob_signals"]["recruiter_response_rate"],

            "open_to_work":
                candidate["redrob_signals"]["open_to_work_flag"],
            
            "notice_period":
                candidate["redrob_signals"]["notice_period_days"],
            
            "interview_completion_rate":
                candidate["redrob_signals"]["interview_completion_rate"],
                
            "offer_acceptance_rate":
                candidate["redrob_signals"]["offer_acceptance_rate"],

            "career_descriptions": [
                job["description"]
                for job in candidate["career_history"]
            ],
        }

        result = calculate_candidate_score(
            candidate_features,
            job_features
        )

        results.append({
            "candidate_id": candidate["candidate_id"],
            "title": candidate_features["title"],
            "score": result["score"],
            "title_score": result["title_score"],
            "relevance_score": result["relevance_score"],
            "strengths" : result["strengths"],
            "risks": result["risks"]
        })

results.sort(
    key=lambda x: x["score"],
    reverse=True
)

print("\n=== TOP 5 CANDIDATES FROM 1L CANDIDATES ===\n")

for rank, candidate in enumerate(results[:5], start=1):

    print("\n" + "=" * 60)

    print(f"Rank #{rank}")

    print(f"Candidate ID: {candidate['candidate_id']}")

    print(f"Title: {candidate['title']}")

    print(f"Score: {candidate['score']}")

    print("\nStrengths:")

    for strength in candidate["strengths"]:

        print(f"✓ {strength}")

    print("\nRisks:")

    if candidate["risks"]:

        for risk in candidate["risks"]:

            print(f"⚠ {risk}")

    else:

        print("No major risks found")