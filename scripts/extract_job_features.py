"""JOB REQUIREMENT DEFINITION
=====================================
Defines the target job position requirements and preferences.
This data is used by ranking_engine.py to score and rank candidates.

Components:
- required_skills: Must-have technical skills (matched with aliases)
- preferred_skills: Nice-to-have technical skills
- required_experience: Min/max years of experience threshold
- preferred_titles: Job titles that align with the role
- behavior_requirements: Positive engagement signals
- negative_signals: Keywords indicating poor fit

Target Position: AI/Ranking Systems Engineer
"""
import json

# Dictionary containing all job requirements and preferences
job_features = {
    # Core technical skills required for the position
    # Each match in candidate profile = +5 points (see ranking_engine.py)
    # Aliases are checked via skill_aliases.py for flexible matching
    "required_skills": [
        "Python",
        "Embeddings",
        "Retrieval Systems",
        "Ranking Systems",
        "Vector Databases",
        "Evaluation Frameworks"
    ],

    # Additional desirable skills (not scored but used for ranking quality)
    "preferred_skills": [
        "LoRA",
        "QLoRA",
        "PEFT",
        "Learning To Rank",
        "HR Tech"
    ],

    # Experience range threshold (must be >= min for +10 points)
    "required_experience": {
        "min": 5,
        "max": 9
    },

    # Job titles indicating good role fit (matched for +20-25 points in title_score.py)
    "preferred_titles": [
        "AI Engineer",
        "Machine Learning Engineer",
        "Applied Scientist",
        "Search Engineer",
        "Recommendation Engineer"
    ],

    # Positive behavioral indicators (checked in ranking_engine.py)
    "behavior_requirements": [
        "Open To Work",
        "Active Candidate",
        "Good Recruiter Response Rate"
    ],

    # Career signals indicating misaligned background (penalties in title_score.py)
    "negative_signals": [
        "Marketing Background",
        "Research Only",
        "Service Company Only"
    ],
    
}

# print(json.dumps(job_features, indent=4))