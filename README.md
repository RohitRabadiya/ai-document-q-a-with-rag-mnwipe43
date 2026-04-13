# AI Document Q&A with RAG

![CI](https://github.com/username/ai-document-qa-with-rag/actions/workflows/ci.yml/badge.svg)

## Overview

AI Document Q&A with RAG is a state-of-the-art web application allowing users to upload PDF documents and ask questions, which are answered using the GPT-4 model via a Retrieval-Augmented Generation (RAG) pipeline. The application utilizes FAISS for vector search and LangChain for efficient processing.

## Features
- Upload PDF documents
- Ask questions about the documents
- Get answers powered by GPT-4
- Fast vector search using FAISS
- Modern web interface

## Quickstart

```bash
# Clone the repository
git clone https://github.com/username/ai-document-qa-with-rag.git
cd ai-document-qa-with-rag

# Set up environment
cp .env.example .env

# Build and run with Docker
docker-compose up --build
```

## Architecture

```
+--------------------+
|   Client (React)   |
+--------------------+
           |
           v
+--------------------+
|  Backend (FastAPI) |
+--------------------+
           |
           v
+--------------------+
|     FAISS Index    |
+--------------------+
           |
           v
+--------------------+
|  GPT-4 via LangChain|
+--------------------+
```

## API Documentation

- `POST /upload`: Upload a PDF document
- `POST /ask`: Ask a question about the uploaded documents

## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Create a new Pull Request
