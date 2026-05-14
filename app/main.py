from app.index.build_index import build_index
from app.index.query_engine import get_query_engine

if __name__ == "__main__":
    # Step 1: Build index (run once)
    # build_index()

    # Step 2: Query
    query_engine = get_query_engine()

    while True:
        q = input("\nAsk: ")
        if q.lower() == "exit":
            break

        response = query_engine.query(q)
        print("\nAnswer:", response)