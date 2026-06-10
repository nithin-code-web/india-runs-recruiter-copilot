import json

total_candidates = 0
total_skills = 0
total_career_entries = 0
total_experience = 0
max_skills = 0
max_experience = 0
min_experience = float('inf')

with open("data/candidates.jsonl", "r", encoding="utf-8") as f:

    for i, line in enumerate(f):
        if i >= 1000:  # only first 1000 candidates
            break

        candidate = json.loads(line)

        total_candidates += 1

        total_skills += len(candidate["skills"])

        total_career_entries += len(candidate["career_history"])

        total_experience += candidate["profile"]["years_of_experience"]

        skill_count = len(candidate["skills"])
        max_skills = max(max_skills, skill_count)
        exp = candidate["profile"]["years_of_experience"]
        max_experience = max(max_experience, exp)
        min_experience = min(min_experience, exp)

avg_skills = total_skills / total_candidates
avg_career_entries = total_career_entries / total_candidates
avg_experience = total_experience / total_candidates

print("\n===== DATASET STATISTICS =====\n")

print(f"Candidates Analyzed: {total_candidates}")

print(f"Average Skills: {avg_skills:.2f}")

print(f"Average Career Entries: {avg_career_entries:.2f}")

print(f"Average Years Experience: {avg_experience:.2f}")

print(f"Max Skills: {max_skills}")

print(f"Max Years Experience: {max_experience}")

print(f"Min Years Experience: {min_experience}")