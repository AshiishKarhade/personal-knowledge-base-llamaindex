from llama_index.core import SimpleDirectoryReader
from app.config import DATA_DIR

def load_documents():
    reader = SimpleDirectoryReader(DATA_DIR)
    return reader.load_data()