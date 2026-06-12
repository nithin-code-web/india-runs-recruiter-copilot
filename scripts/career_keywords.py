"""CAREER HISTORY KEYWORD CATEGORIES
=====================================
Defines keyword categories used for analyzing candidate career descriptions.
Used by career_score.py to identify relevant work experience.

Categories represent key business domains and technical areas:
- ranking/retrieval: Core business domain
- recommendation: Related business problem
- embeddings: Key technical skill
- machine_learning: Technical foundation
- llm: Advanced capability
- data_engineering: Supporting infrastructure
"""

# Dictionary of keyword categories for career description analysis
CAREER_KEYWORDS = {
    # Core ranking systems experience
    "ranking": [
        "ranking",
        "ranker"
    ],

    # Information retrieval and search experience
    "retrieval": [
        "retrieval",
        "search engineer",
        "information retrieval"
    ],

    # Recommendation systems experience
    "recommendation": [
        "recommendation",
        "recommend"
    ],

    # Vector embeddings and representation learning
    "embeddings": [
        "embedding",
        "embeddings"
    ],

    # General machine learning foundation
    "machine_learning": [
        "machine learning",
        "ml model",
        "deep learning"
    ],

    # Large language model experience
    "llm": [
        "llm",
        "fine tuning",
        "fine-tuning",
        "lora",
        "qlora"
    ],
    
    # Data pipeline and infrastructure experience
    "data_engineering": [
        "spark",
        "airflow",
        "kafka",
        "pipeline",
        "pipelines",
        "warehouse"
    ]
}