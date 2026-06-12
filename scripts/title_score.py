"""JOB TITLE RELEVANCE SCORING
=====================================
Scores candidate's current job title for relevance to target AI/ranking engineer role.

Bonuses: +20-25 points for AI, ML, Search, Recommendation, NLP roles
Penalties: -20 points for non-technical roles (Marketing, HR, Sales, Accounting)
No bonus/penalty: 0 points for unrelated technical roles
"""

# Bonus points for titles that align well with target role
TITLE_BONUS = {
    # AI/ML roles - strongest match (+20-25)
    "AI Engineer": 20,
    "Senior AI Engineer": 25,

    # Search/ranking roles - strong match (+20)
    "Search Engineer": 20,
    "Recommendation Systems Engineer": 20,

    # ML roles - strong match (+20)
    "Machine Learning Engineer": 20,
    "ML Engineer": 20,

    # NLP roles - good match (+15-20)
    "Senior NLP Engineer": 20,
    "NLP Engineer": 15,

    # Research roles - strong match (+20)
    "AI Research Engineer": 20,

    # Applied roles - good match (+15-20)
    "Applied ML Engineer": 15,
    "Senior Applied Scientist": 20,

    # Data/Backend roles - partial match (+5-10)
    "Data Scientist": 10,
    "Backend Engineer": 5
}

# Penalty points for titles indicating poor role fit
TITLE_PENALTY = {
    # Non-technical roles - strong penalties (-20)
    "Marketing Manager": -20,
    "HR Manager": -20,
    "Accountant": -20,
    "Sales Executive": -20
}


def calculate_title_score(title):
    """Calculate score based on job title relevance to target role.
    
    Args:
        title: Candidate's current job title
    
    Returns:
        Score: positive (bonus), negative (penalty), or 0 (no match)
    """

    # Check for bonus match (aligned title)
    if title in TITLE_BONUS:
        return TITLE_BONUS[title]

    # Check for penalty match (misaligned title)
    if title in TITLE_PENALTY:
        return TITLE_PENALTY[title]

    # No match - return 0 score
    return 0