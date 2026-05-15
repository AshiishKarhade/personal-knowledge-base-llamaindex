import os

from app.index.build_index import build_indices
from app.index.query_engine import (
    get_vector_query_engine,
    get_summary_query_engine
)
from app.config import VECTOR_INDEX_DIR, SUMMARY_INDEX_DIR

if __name__ == "__main__":
    # Auto-build if indices don't exist
    if not os.path.exists(VECTOR_INDEX_DIR) or not os.path.exists(SUMMARY_INDEX_DIR):
        print("No indices found. Building...")
        build_indices()

    vector_engine = get_vector_query_engine()
    summary_engine = get_summary_query_engine()

    while True:
        q = input("\nAsk: ")
        if q.lower() == "exit":
            break

        mode = input("Mode (v=vector, s=summary): ")

        if mode == "s":
            response = summary_engine.query(q)
        else:
            response = vector_engine.query(q)

        print("\nAnswer:", response)