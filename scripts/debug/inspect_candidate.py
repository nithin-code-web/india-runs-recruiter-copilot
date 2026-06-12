import json
from collections import Counter


with open("data/candidates.jsonl", "r", encoding="utf-8") as f:
    first_candidate = json.loads(next(f))
    
print(f"First Candidate: {first_candidate}")