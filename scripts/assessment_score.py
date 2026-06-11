def calculate_assessment_score(assessment_scores):

    if not assessment_scores:
        return 0, 0

    average_score = (
        sum(assessment_scores.values())
        / len(assessment_scores)
    )

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