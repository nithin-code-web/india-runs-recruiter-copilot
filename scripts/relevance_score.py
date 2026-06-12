"""AI KEYWORD RELEVANCE SCORING
=====================================
Detects AI/ML domain-specific keywords in skills and career history.
Weighted AI keywords indicate stronger domain expertise
and relevance to AI/ML-focused roles.

Keyword categories and weights:
- Ranking systems: ranking, recommendation, learning-to-rank (10-12 pts)
- Retrieval systems: retrieval, search, vector search (10 pts)
- Vector DBs: embeddings, pinecone, faiss, milvus (8 pts)
- ML frameworks: xgboost, lightgbm (8 pts)
- Infrastructure: feature pipeline, a/b testing (6 pts)

"""

# Dictionary of AI-related keywords with point weights
AI_KEYWORDS = {
    # Core ranking/recommendation concepts (10-12 pts each)
    "ranking": 10,
    "recommendation": 10,
    "retrieval": 10,

    # Search-related roles and concepts (10 pts each)
    "search engineer": 10,
    "vector search": 10,

    # Vector database and embedding technologies (8 pts each)
    "embeddings": 8,
    "pinecone": 8,
    "faiss": 8,
    "milvus": 8,

    # ML frameworks and learning methods (8-12 pts each)
    "learning-to-rank": 12,
    "xgboost": 8,
    "lightgbm": 8,

    # Supporting infrastructure and practices (6 pts each)
    "feature pipeline": 6,
    "a/b test": 6
}

def count_ai_keywords(text):
    """Count AI-related keywords in provided text.
    
    Args:
        text: String to search for AI keywords (skills or career descriptions)
    
    Returns:
        Tuple of (score: int, matched_keywords: list)
        score: Weighted sum of matched keywords
        matched_keywords: List of keywords found in text
    """

    score = 0
    matched_keywords = []  # Track keywords found

    # Normalize text to lowercase for matching
    text = text.lower()

    # Scan text for each AI keyword
    for keyword, weight in AI_KEYWORDS.items():

        # If keyword found, add weighted points and track it
        if keyword in text:
            score += weight
            matched_keywords.append(keyword)


    return score, matched_keywords