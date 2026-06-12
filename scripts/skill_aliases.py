"""SKILL ALIAS MAPPING
=====================================
Maps required skill names to their equivalent technologies and tools.
Enables flexible skill matching in ranking_engine.py.

Example: "Vector Databases" requirement can be satisfied by:
  Milvus, FAISS, Pinecone, Qdrant, or Weaviate

This allows the system to recognize skill variants and common alternatives.
"""

# Dictionary mapping skill requirements to their technology aliases
SKILL_ALIASES = {
    # Vector database solutions - all satisfy the Vector Databases requirement
    "Vector Databases": [
        "Milvus",
        "FAISS",
        "Pinecone",
        "Qdrant",
        "Weaviate"
    ],

    # LLM fine-tuning techniques - all satisfy the LLM Fine Tuning requirement
    "LLM Fine Tuning": [
        "LoRA",
        "QLoRA",
        "PEFT"
    ],

    # Retrieval system technologies - all satisfy the Retrieval Systems requirement
    "Retrieval Systems": [
        "FAISS",
        "Milvus",
        "Elasticsearch",
        "OpenSearch"
    ]
}
