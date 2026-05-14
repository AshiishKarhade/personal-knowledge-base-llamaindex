from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from app.config import EMBED_MODEL

def get_embedding():
    return HuggingFaceEmbedding(model_name=EMBED_MODEL)