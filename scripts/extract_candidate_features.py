import json

with open("data/candidates.jsonl", "r", encoding="utf-8") as f:
    candidate = json.loads(next(f))

features = {
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
        
    "career_titles": [job["title"]
        for job in candidate["career_history"]
        ],
    
    "industry": [job["industry"]
        for job in candidate["career_history"]
    ]
}

print(json.dumps(features, indent=4))