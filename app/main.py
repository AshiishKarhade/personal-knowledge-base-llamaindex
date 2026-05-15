import os
from app.index.build_index import build_index
from app.index.query_engine import get_query_engine
from app.config import STORAGE_DIR

if __name__ == "__main__":
    # Build index if storage doesn't exist
    docstore_path = os.path.join(STORAGE_DIR, "docstore.json")
    if not os.path.exists(docstore_path):
        print("No index found. Building index...")
        build_index()

    query_engine = get_query_engine()

    while True:
        q = input("\nAsk: ")
        if q.lower() == "exit":
            break

        response = query_engine.query(q)
        print("\nAnswer:", response)