def generate_explanation(
    candidate_features,
    found_keywords,
    average_assessment
):

    strengths = []
    risks = []

    # Experience

    if candidate_features["experience"] >= 5:
        strengths.append(
            f"{candidate_features['experience']} years experience"
        )

    # Open To Work

    if candidate_features["open_to_work"]:
        strengths.append(
            "Open to work"
        )

    # Career Keywords

    if "spark" in found_keywords:
        strengths.append(
            "Experience with Spark"
        )

    if "retrieval" in found_keywords:
        strengths.append(
            "Retrieval system exposure"
        )

    # Assessment

    if average_assessment >= 70:
        strengths.append(
            "Strong assessment performance"
        )

    elif average_assessment < 50:
        risks.append(
            "Low assessment scores"
        )

    # Missing AI Signals

    if "ranking" not in found_keywords:
        risks.append(
            "No ranking-system evidence"
        )

    if "recommendation" not in found_keywords:
        risks.append(
            "No recommendation-system evidence"
        )

    return strengths, risks