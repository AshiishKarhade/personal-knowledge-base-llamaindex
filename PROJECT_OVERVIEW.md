# Personal Knowledge Base - LlamaIndex RAG Project

## Overview
A local-first Retrieval-Augmented Generation (RAG) system built with LlamaIndex, Ollama, and HuggingFace embeddings. This project creates a personal knowledge base that ingests documents, builds a vector index, and answers questions using locally-run LLMs.

## Architecture

```
app/
├── __init__.py
├── config.py              # Central configuration
├── main.py                # Entry point - CLI query loop
├── embeddings/
│   └── hf_embeddings.py   # HuggingFace embedding model wrapper
├── index/
│   ├── build_index.py     # Document ingestion & index creation
│   └── query_engine.py    # Load persisted index & create query engine
├── ingestion/
│   └── loader.py          # Document loading from directory
└── llm/
    └── ollama_llm.py      # Ollama LLM wrapper
```

## Tech Stack
- **Framework**: LlamaIndex
- **LLM**: Ollama (default: phi3)
- **Embeddings**: HuggingFace sentence-transformers (all-MiniLM-L6-v2)
- **Vector Store**: In-memory with disk persistence
- **Python**: 3.14

## Configuration (`app/config.py`)
| Setting | Default | Description |
|---------|---------|-------------|
| `OLLAMA_MODEL` | `phi3` | Ollama model to use for generation |
| `EMBED_MODEL` | `sentence-transformers/all-MiniLM-L6-v2` | Embedding model |
| `DATA_DIR` | `data` | Input documents directory |
| `STORAGE_DIR` | `storage` | Persisted index location |

## Workflow

### 1. Document Ingestion
- `SimpleDirectoryReader` loads all files from `data/`
- Supports PDFs, text, markdown, and more

### 2. Index Building
- Creates `VectorStoreIndex` from documents
- Uses configured embedding model for vectorization
- Persists index to `storage/` directory
- Run once: uncomment `build_index()` in `main.py`

### 3. Querying
- Loads persisted index from `storage/`
- Creates query engine with Ollama LLM
- Interactive CLI loop for asking questions

## Usage

```bash
# Install dependencies
pip install -r requirements.txt

# Ensure Ollama is running with the model pulled
ollama pull phi3

# Build index (first time only)
# Uncomment build_index() in app/main.py

# Run
python -m app.main
```

## Dependencies
```
llama-index
llama-index-llms-ollama
llama-index-embeddings-huggingface
transformers
sentence-transformers
python-dotenv
```

## Key Design Decisions
- **Local-first**: No cloud APIs required, runs entirely locally
- **Modular**: Separate modules for LLM, embeddings, ingestion, indexing
- **Persistent**: Index saved to disk, no rebuild needed
- **Simple CLI**: Interactive question-answer loop

## Future Enhancements
- Add web UI (Streamlit/FastAPI)
- Support multiple vector stores (Chroma, Qdrant, Pinecone)
- Add document chunking strategies
- Implement re-ranking for better results
- Add support for multiple LLM backends
- Add evaluation metrics (RAGAS)
- Support incremental index updates
- Add API endpoints for integration
