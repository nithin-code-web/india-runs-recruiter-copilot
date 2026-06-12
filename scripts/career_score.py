"""CAREER HISTORY SCORING MODULE
=====================================
Analyzes candidate career descriptions for relevant keywords.
Indicates prior experience with job-domain concepts like ranking, retrieval, ML, etc.

Scoring: +5 points per matched keyword category (one match per category)
Categories: ranking, retrieval, recommendation, embeddings, ML, LLM, data_engineering
"""
from career_keywords import CAREER_KEYWORDS  # Import keyword categories and keywords

def calculate_career_score(career_descriptions):
    """Calculate career relevance score based on keyword matching.
    
    Args:
        career_descriptions: List of job descriptions from candidate's career history
    
    Returns:
        Tuple of (score: int, found_keywords: list)
    """
    score = 0
    found_keywords = []  # Track which keywords were found

    # Combine all career descriptions and normalize to lowercase
    text = " ".join(career_descriptions).lower()

    # Iterate through keyword categories (ranking, retrieval, recommendation, etc.)
    # For each category, check if any keyword matches
    for category, keywords in CAREER_KEYWORDS.items():

        for keyword in keywords:

            # If keyword found in career text
            if keyword in text:
                # Award 5 points for this category match
                score += 5
                found_keywords.append(keyword)
                # Break after first match per category (avoid double-counting)
                break

    return score, found_keywords