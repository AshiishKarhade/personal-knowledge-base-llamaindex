import os
from llama_index.core import VectorStoreIndex, StorageContext

from app.ingestion.loader import load_documents
from app.llm.ollama_llm import get_llm
from app.embeddings.hf_embeddings import get_embedding
from app.config import STORAGE_DIR

def build_index():
    docs = load_documents()

    index = VectorStoreIndex.from_documents(
        docs,
        embed_model=get_embedding(),
        llm=get_llm()
    )

    index.storage_context.persist(persist_dir=STORAGE_DIR)
    print("Index built and saved.")