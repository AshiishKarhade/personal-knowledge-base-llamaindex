import os

from llama_index.core import (
    VectorStoreIndex,
    SummaryIndex,
    StorageContext
)

from app.ingestion.loader import load_documents
from app.llm.ollama_llm import get_llm
from app.embeddings.hf_embeddings import get_embedding
from app.config import VECTOR_INDEX_DIR, SUMMARY_INDEX_DIR


def build_indices():
    docs = load_documents()

    # shared models
    llm = get_llm()
    embed_model = get_embedding()

    # ======================
    # Vector Index
    # ======================
    vector_index = VectorStoreIndex.from_documents(
        docs,
        embed_model=embed_model,
        llm=llm
    )

    vector_index.storage_context.persist(
        persist_dir=VECTOR_INDEX_DIR
    )

    print("✅ Vector index built")

    # ======================
    # Summary Index
    # ======================
    summary_index = SummaryIndex.from_documents(
        docs,
        llm=llm
    )

    summary_index.storage_context.persist(
        persist_dir=SUMMARY_INDEX_DIR
    )

    print("✅ Summary index built")