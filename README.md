# Personal Knowledge Base with LlamaIndex

A local RAG (Retrieval Augmented Generation) system that lets you query your documents using natural language. Built with LlamaIndex, Ollama, and a minimal React UI.

## Architecture

```
Documents (data/) ──→ Embeddings (HuggingFace) ──→ Vector/Summary Index
                                                              │
User Question ──→ React UI ──→ FastAPI ──→ Retrieve Chunks ──→ Ollama (phi3) ──→ Answer
```

## Quick Start

### 1. Prerequisites

- Python 3.12+
- Node.js 18+
- [Ollama](https://ollama.com) running locally with a model (e.g. `phi3`)

### 2. Backend Setup

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

### 3. Frontend Setup

```bash
cd frontend && npm install && cd ..
```

### 4. Run

**Backend** (terminal 1):
```bash
source .venv/bin/activate
uvicorn app.api:app --host 0.0.0.0 --port 8000
```

**Frontend** (terminal 2):
```bash
cd frontend && npm run dev
```

Open http://localhost:5173 in your browser.

## Configuration

Edit `app/config.py` to change:

| Setting | Default | Description |
|---|---|---|
| `OLLAMA_MODEL` | `phi3` | Local LLM model name |
| `EMBED_MODEL` | `sentence-transformers/all-MiniLM-L6-v2` | Embedding model |
| `DATA_DIR` | `data` | Directory containing documents |
| `STORAGE_DIR` | `storage` | Persisted index location |

## Modes

- **Vector** — Semantic search over document chunks
- **Summary** — Summarization-based responses

## Adding Documents

Place any `.txt`, `.pdf`, `.md`, or `.csv` files in the `data/` directory and restart the backend. Indices will rebuild automatically.
