import json

TARGET_IDS = [
    "CAND_0000031",
    "CAND_0000084"
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