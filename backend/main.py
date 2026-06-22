import chromadb
from fastapi import FastAPI, UploadFile, File
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client_groq = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

app = FastAPI()

UPLOAD_DIR = "uploads"

@app.get("/")
def home():
    return {"message": "EnterpriseDoc AI Running"}

@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):

    file_path = os.path.join(
        UPLOAD_DIR,
        file.filename
    )

    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    return {
        "status": "success",
        "filename": file.filename
    }

@app.post("/query")
async def query_document(question: str):

    client = chromadb.PersistentClient(
        path="./chroma_store"
    )

    collection = client.get_collection(
        name="documents"
    )

    results = collection.query(
        query_texts=[question],
        n_results=2
    )

    context = "\n".join(
        results["documents"][0]
    )

    prompt = f"""
Answer using ONLY the context below.

Context:
{context}

Question:
{question}
"""

    response = client_groq.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    answer = response.choices[0].message.content

    return {
        "question": question,
        "answer": answer
    }