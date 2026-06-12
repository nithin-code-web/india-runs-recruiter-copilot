"""MAIN RANKING PIPELINE
=====================================
This script reads candidates from JSONL file and ranks them against a target job position.
It processes up to 100K candidates, calculates comprehensive scores, and outputs top 5 ranked candidates.

Pipeline Flow:
1. Load job requirements from extract_job_features.py
2. For each candidate: extract features from JSONL data
3. Calculate candidate score using ranking_engine.py (multi-factor scoring)
4. Sort by score and display top 5 results

Scoring includes: skills match, experience, behavior signals, title relevance, 
career history keywords, assessment scores, and AI-related signals.
"""
import json

# Import job requirements (target position skills, experience, preferred titles, etc.)
from extract_job_features import job_features
# Import main scoring function that calculates candidate ranking score
from ranking_engine import calculate_candidate_score

# List to store ranking results for all candidates
results = []

# Read candidates from JSONL file (one candidate per line)
with open("data/candidates.jsonl", "r", encoding="utf-8") as f:

    for i, line in enumerate(f):

        if i >= 100000:  # Limit to first 100K candidates for efficiency
            break

        # Parse candidate JSON data
        candidate = json.loads(line)

        # Extract and structure candidate features for scoring
        # These features feed into the multi-factor ranking calculation in ranking_engine.py
        candidate_features = {
            "candidate_id": candidate["candidate_id"],
            
            # Profile information
            "title": candidate["profile"]["current_title"],  # Used for title relevance scoring
            "experience": candidate["profile"]["years_of_experience"],  # Experience score threshold check

            # Skills matching (converted to list from candidate.skills array)
            "skills": [
                skill["name"]
                for skill in candidate["skills"]
            ],  # Matched against required_skills using ranking_engine.py

            # Engagement and behavior signals
            "assessment_scores":
                candidate["redrob_signals"]["skill_assessment_scores"],  # Test/assessment performance

            "github_score":
                candidate["redrob_signals"]["github_activity_score"],  # GitHub activity indicator

            "response_rate":
                candidate["redrob_signals"]["recruiter_response_rate"],  # Recruitment engagement

            "open_to_work":
                candidate["redrob_signals"]["open_to_work_flag"],  # Availability signal
            
            "notice_period":
                candidate["redrob_signals"]["notice_period_days"],  # Risk indicator if long notice
            
            "interview_completion_rate":
                candidate["redrob_signals"]["interview_completion_rate"],  # Interview reliability
                
            "offer_acceptance_rate":
                candidate["redrob_signals"]["offer_acceptance_rate"],  # Offer acceptance likelihood

            # Career history for keyword analysis
            "career_descriptions": [
                job["description"]
                for job in candidate["career_history"]
            ],  # Analyzed by career_score.py and relevance_score.py
        }

        # Calculate comprehensive ranking score using ranking_engine.py
        # Returns score breakdown with multiple scoring factors and strengths/risks
        result = calculate_candidate_score(
            candidate_features,
            job_features
        )

        # Store ranking result with key metrics
        results.append({
            "candidate_id": candidate["candidate_id"],
            "title": candidate_features["title"],
            "score": result["score"],
            "title_score": result["title_score"],
            "relevance_score": result["relevance_score"],
            "strengths" : result["strengths"],
            "risks": result["risks"],
            "availability": result["availability"],
        })

# Sort candidates by overall score in descending order (highest scoring first)
results.sort(
    key=lambda x: x["score"],
    reverse=True
)

# Display top 10 ranked candidates with detailed scoring breakdown
print("\n=== TOP 10 CANDIDATES FROM 100K CANDIDATES ===\n")

for rank, candidate in enumerate(results[:10], start=1):

    print("\n" + "=" * 60)

    print(f"Rank #{rank}")

    print(f"Candidate ID: {candidate['candidate_id']}")

    print(f"Title: {candidate['title']}")

    print(f"Score: {candidate['score']}")

    print("\nStrengths:")

    for strength in candidate["strengths"]:

        print(f"✅ {strength}")
        
    print("\nAvailability:")
    
    for item in candidate["availability"]:
        
        if "Notice period" in item:
            print(f"📅 {item}")
        else:
            print(f"✅ {item}")    
            

    print("\nRisks:")

    if candidate["risks"]:

        for risk in candidate["risks"]:

            print(f"⚠ {risk}")

    else:

        print("No major risks found")