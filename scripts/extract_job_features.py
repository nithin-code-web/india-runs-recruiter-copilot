import json

job_features = {
    "required_skills": [
        "Python",
        "Embeddings",
        "Retrieval Systems",
        "Ranking Systems",
        "Vector Databases",
        "Evaluation Frameworks"
    ],

    "preferred_skills": [
        "LoRA",
        "QLoRA",
        "PEFT",
        "Learning To Rank",
        "HR Tech"
    ],

    "required_experience": {
        "min": 5,
        "max": 9
    },

    "preferred_titles": [
        "AI Engineer",
        "Machine Learning Engineer",
        "Applied Scientist",
        "Search Engineer",
        "Recommendation Engineer"
    ],

    "behavior_requirements": [
        "Open To Work",
        "Active Candidate",
        "Good Recruiter Response Rate"
    ],

    "negative_signals": [
        "Marketing Background",
        "Research Only",
        "Service Company Only"
    ],
    
}

# print(json.dumps(job_features, indent=4))