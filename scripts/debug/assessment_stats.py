import json

count = 0

with open("data/candidates.jsonl", "r", encoding="utf-8") as f:

    for line in f:

        candidate = json.loads(line)

        scores = candidate["redrob_signals"]["skill_assessment_scores"]

        if scores:
            print(json.dumps(scores, indent=4))

            count += 1

        if count == 5:
            break