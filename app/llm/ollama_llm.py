from llama_index.llms.ollama import Ollama
from app.config import OLLAMA_MODEL

def get_llm():
    return Ollama(
        model = OLLAMA_MODEL,
        request_timeout = 120.0
    )