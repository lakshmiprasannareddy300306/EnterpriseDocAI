# EnterpriseDoc AI

## Overview

EnterpriseDoc AI is a Retrieval-Augmented Generation (RAG) application that allows users to upload PDF documents and ask questions using natural language.

The system extracts text from PDFs, stores document chunks in ChromaDB, retrieves relevant information through semantic search, and generates answers using a local Llama 3 model running through Ollama.

## Features

* PDF Upload
* Text Extraction
* Text Chunking
* Vector Database Storage
* Semantic Search
* AI-Powered Question Answering
* Local LLM Execution

## Tech Stack

* Python
* FastAPI
* Streamlit
* ChromaDB
* LangChain
* Ollama
* Llama 3
* SQLite

## Architecture

PDF Upload → Text Extraction → Chunking → ChromaDB → Retrieval → Llama 3 → AI Answer

## Future Improvements

* Multi-document support
* Query history dashboard
* User authentication
* Cloud deployment

## Author

Lakshmi Prasanna Reddy Antharam
