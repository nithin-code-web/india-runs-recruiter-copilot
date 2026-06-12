def generate_candidate_summary(candidate_features,
                               matched_skills,
                               matched_ai_keywords):

    strengths = []

    risks = []

    # Experience

    if candidate_features["experience"] >= 5:
        strengths.append(
            f"{candidate_features['experience']} years experience"
        )

    # Open to work

    if candidate_features["open_to_work"]:
        strengths.append(
            "Open to work"
        )

    # Skills

    for skill in matched_skills[:5]:
        strengths.append(
            f"Matched skill: {skill}"
        )

    # AI Signals

    for keyword in matched_ai_keywords[:5]:
        strengths.append(
            f"AI signal: {keyword}"
        )

    # Risks

    if candidate_features.get("notice_period", 0) > 30:
        risks.append(
            f"Long notice period ({candidate_features['notice_period']} days)"
        )

    if candidate_features["response_rate"] < 0.20:
        risks.append(
            "Low recruiter response rate"
        )

    return strengths, risks