import json
import os

# Import ranked candidate data from the ranking module
from rank_candidates import results

# Ensure the output directory exists before writing the JSON file
os.makedirs("outputs", exist_ok=True)

# Prepare a list to store the top candidates for export
top_candidates = []

for rank, candidate in enumerate(results[:10], start=1):

    top_candidates.append({
        "rank": rank,
        "candidate_id": candidate["candidate_id"],
        "title": candidate["title"],
        "score": candidate["score"],
        "strengths": candidate["strengths"],
        "risks": candidate["risks"]
    })

# Open the output file and write the top candidate JSON data
with open(
    "outputs/top_candidates.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        top_candidates,
        f,
        indent=4
    )

# Confirm the export completed successfully
print(
    "Exported Top 10 Candidates "
    "to outputs/top_candidates.json"
)