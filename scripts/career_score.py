from career_keywords import CAREER_KEYWORDS

def calculate_career_score(career_descriptions):

    score = 0

    found_keywords = []

    text = " ".join(career_descriptions).lower()

    for category, keywords in CAREER_KEYWORDS.items():

        for keyword in keywords:

            if keyword in text:

                score += 5

                found_keywords.append(keyword)

                break

    return score, found_keywords