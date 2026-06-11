import json

from extract_job_features import job_features
from ranking_engine import calculate_candidate_score

results = []

with open("data/candidates.jsonl", "r", encoding="utf-8") as f:

    for i, line in enumerate(f):

        if i >= 100:
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

            "career_descriptions": [
                job["description"]
                for job in candidate["career_history"]
            ]
        }

        result = calculate_candidate_score(
            candidate_features,
            job_features
        )

        results.append({
            "candidate_id": candidate["candidate_id"],
            "title": candidate_features["title"],
            "score": result["score"]
        })

results.sort(
    key=lambda x: x["score"],
    reverse=True
)

print("\n=== TOP 10 CANDIDATES ===\n")

for rank, candidate in enumerate(results[:10], start=1):

    print(
        f"{rank}. "
        f"{candidate['candidate_id']} | "
        f"{candidate['title']} | "
        f"Score: {candidate['score']}"
    )