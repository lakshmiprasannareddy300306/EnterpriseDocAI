# EnterpriseDoc AI

EnterpriseDoc AI is a local RAG (Retrieval-Augmented Generation) system.

## Features

- Upload PDF documents
- Extract text automatically
- Split text into chunks
- Store chunks in ChromaDB
- Perform semantic search
- Generate answers using Llama 3 via Ollama

## Tech Stack

- Python
- FastAPI
- ChromaDB
- LangChain
- Ollama
- Llama 3
- SQLite (planned)
- Streamlit (planned)

## Architecture

PDF → Chunking → ChromaDB → Retrieval → Llama 3 → Answer

## Run

uvicorn main:app --reload