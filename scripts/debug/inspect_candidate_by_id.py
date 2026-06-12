import json
from relevance_score import count_ai_keywords

TARGET_IDS = [
    "CAND_0001610",
    "CAND_0013613"
]

with open("data/candidates.jsonl", "r", encoding="utf-8") as f:

    for line in f:

        candidate = json.loads(line)

        if candidate["candidate_id"] in TARGET_IDS:

            print("\n" + "=" * 80)

            print("Candidate ID:", candidate["candidate_id"])

            print("Title:", candidate["profile"]["current_title"])

            print(
                "Experience:",
                candidate["profile"]["years_of_experience"]
            )

            print("\nSkills:")

            for skill in candidate["skills"]:
                print("-", skill["name"])

            print("\nAssessment Scores:")

            print(
                json.dumps(
                    candidate["redrob_signals"][
                        "skill_assessment_scores"
                    ],
                    indent=4
                )
            )

            print("\nCareer History:")

            for job in candidate["career_history"]:

                print("\nTitle:", job["title"])

                print("Industry:", job["industry"])

                print("Description:")

                print(job["description"])

                print("-" * 40)
                

            career_text = " ".join(
                    [job["description"] for job in candidate["career_history"]]
                )

            score, keywords = count_ai_keywords(career_text)

            print("\nCareer Relevance Score:", score)
            print("Matched Keywords:", keywords)    