import json

with open("data/candidates.jsonl", "r", encoding="utf-8") as f:
    candidate = json.loads(next(f))    

# print("\n=== TOP LEVEL KEYS ===")
# print(json.dumps(list(candidate.keys()),indent=4))

# print("\n=== PROFILE KEYS ===")
# print(json.dumps(list(candidate["profile"].keys()),indent=4))

# print("\n=== REDROB SIGNAL KEYS ===")
# print(json.dumps(list(candidate["redrob_signals"].keys()),indent=4))


print("\n=== EDUCATION ===")
print(json.dumps(candidate["education"], indent=4))

print("\n=== FIRST 3 SKILLS ===")
print(json.dumps(candidate["skills"][:3], indent=4))

print("\n=== FIRST CAREER ENTRY ===")
print(json.dumps(candidate["career_history"][0], indent=4))