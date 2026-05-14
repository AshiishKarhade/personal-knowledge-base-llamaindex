from llama_index.core import StorageContext, load_index_from_storage
from app.llm.ollama_llm import get_llm
from app.embeddings.hf_embeddings import get_embedding
from app.config import STORAGE_DIR

def get_query_engine():
    storage_context = StorageContext.from_defaults(
        persist_dir=STORAGE_DIR
    )

    index = load_index_from_storage(
        storage_context,
        embed_model=get_embedding()
    )

    return index.as_query_engine(llm=get_llm())