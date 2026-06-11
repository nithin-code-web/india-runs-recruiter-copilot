AI_KEYWORDS = {
    "ranking": 10,
    "recommendation": 10,
    "retrieval": 10,

    "search engineer": 10,
    "vector search": 10,

    "embeddings": 8,
    "pinecone": 8,
    "faiss": 8,
    "milvus": 8,

    "learning-to-rank": 12,
    "xgboost": 8,
    "lightgbm": 8,

    "feature pipeline": 6,
    "a/b test": 6
}

def count_ai_keywords(text):

    score = 0

    matched_keywords = []

    text = text.lower()

    for keyword, weight in AI_KEYWORDS.items():

        if keyword in text:

            score += weight

            matched_keywords.append(keyword)
            
    print("\nTEXT SAMPLE:")
    print(text[:200])

    print("\nMATCHED KEYWORDS:")
    print(matched_keywords)

    return score, matched_keywords