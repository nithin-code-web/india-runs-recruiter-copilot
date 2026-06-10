import json 

with open("data/candidates.jsonl", "r", encoding = "utf-8") as f:
    candidate = json.loads(next(f))
    
    features = {
    "candidate_id": candidate["candidate_id"],

    "current_title":
        candidate["profile"]["current_title"],

    "years_experience":
        candidate["profile"]["years_of_experience"],

    "industry":
        candidate["profile"]["current_industry"],

    "github_score":
        candidate["redrob_signals"]["github_activity_score"],

    "response_rate":
        candidate["redrob_signals"]["recruiter_response_rate"],

    "open_to_work":
        candidate["redrob_signals"]["open_to_work_flag"],

    "notice_period":
        candidate["redrob_signals"]["notice_period_days"]
}

print(json.dumps(features,indent=4))
