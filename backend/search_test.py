import chromadb

client = chromadb.PersistentClient(
    path="./chroma_store"
)

collection = client.get_collection(
    name="documents"
)

results = collection.query(
    query_texts=[
        "What technologies are used in EnterpriseDoc AI?"
    ],
    n_results=2
)

print(results["documents"])