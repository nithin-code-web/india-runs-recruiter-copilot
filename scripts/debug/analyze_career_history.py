import json

with open("data/candidates.jsonl", "r", encoding="utf-8") as f:
    candidate = json.loads(next(f))

print("\n=== CAREER HISTORY ===\n")

for i, job in enumerate(candidate["career_history"], start=1):

    print(f"\nJOB {i}")

    print(f"Title: {job['title']}")

    print(f"Industry: {job['industry']}")

    print(f"Duration: {job['duration_months']} months")

    print("\nDescription:")

    print(job["description"])

    print("-" * 80)