import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from app.index.build_index import build_indices
from app.index.query_engine import (
    get_vector_query_engine,
    get_summary_query_engine
)
from app.config import VECTOR_INDEX_DIR, SUMMARY_INDEX_DIR

app = FastAPI(title="Knowledge Base API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

vector_engine = None
summary_engine = None


@app.on_event("startup")
def startup():
    global vector_engine, summary_engine

    if not os.path.exists(VECTOR_INDEX_DIR) or not os.path.exists(SUMMARY_INDEX_DIR):
        print("Building indices...")
        build_indices()

    vector_engine = get_vector_query_engine()
    summary_engine = get_summary_query_engine()
    print("Ready.")


class QueryRequest(BaseModel):
    question: str
    mode: str = "vector"  # "vector" or "summary"


class QueryResponse(BaseModel):
    answer: str
    mode: str


@app.post("/query", response_model=QueryResponse)
def query(req: QueryRequest):
    engine = summary_engine if req.mode == "summary" else vector_engine
    response = engine.query(req.question)
    return QueryResponse(answer=str(response), mode=req.mode)


@app.get("/health")
def health():
    return {"status": "ok"}
