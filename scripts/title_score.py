TITLE_BONUS = {
    "Recommendation Systems Engineer": 20,
    "Search Engineer": 20,
    "AI Engineer": 20,
    "Machine Learning Engineer": 20,
    "Applied ML Engineer": 15,
    "NLP Engineer": 15,
    "Data Scientist": 10,
    "Backend Engineer": 5
}

TITLE_PENALTY = {
    "Marketing Manager": -20,
    "HR Manager": -20,
    "Accountant": -20,
    "Sales Executive": -20
}


def calculate_title_score(title):

    if title in TITLE_BONUS:
        return TITLE_BONUS[title]

    if title in TITLE_PENALTY:
        return TITLE_PENALTY[title]

    return 0