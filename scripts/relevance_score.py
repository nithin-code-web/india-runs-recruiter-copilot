AI_KEYWORDS = [
    "ranking",
    "recommendation",
    "retrieval",
    "search",
    "embedding",
    "embeddings",
    "vector",
    "faiss",
    "pinecone",
    "milvus",
    "machine learning",
    "ml",
    "llm",
    "nlp",
    "xgboost",
    "lightgbm",
    "a/b test",
    "feature pipeline"
]


def calculate_relevance_score(text):

    score = 0

    matched_keywords = []

    text = text.lower()

    for keyword in AI_KEYWORDS:

        if keyword in text:
            score += 3
            matched_keywords.append(keyword)

    return score, matched_keywords