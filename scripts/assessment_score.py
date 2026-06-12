"""ASSESSMENT SCORE CALCULATION MODULE
=====================================
Calculates candidate's technical assessment/test score.
Based on average of multiple skill assessment scores.

Scaling: Divides by 10 to normalize scores to 0-10 range
Aligns with other scoring factors in the ranking system.
"""
def calculate_assessment_score(assessment_scores):
    """Calculate average assessment score from test results.
    
    Args:
        assessment_scores: Dict of assessment name -> score (0-100)
    
    Returns:
        Tuple of (scaled_score: int, average_score: float)
        scaled_score: Score divided by 10 for ranking (0-10 range)
        average_score: Raw average score (0-100)
    """
    # Handle no assessment data
    if not assessment_scores:
        return 0, 0

    # Calculate average across all assessments
    average_score = (
        sum(assessment_scores.values())
        / len(assessment_scores)
    )

    # Scale down to 0-10 range to align with other scoring factors
    scaled_score = round(average_score / 10)

    return scaled_score, round(average_score, 2)

from extract_candidate_features import candidate_features

assessment_score, average_score = (
    calculate_assessment_score(
        candidate_features["assessment_scores"]
    )
)

# print("Average Assessment:", average_score)
# print("Assessment Score:", assessment_score)