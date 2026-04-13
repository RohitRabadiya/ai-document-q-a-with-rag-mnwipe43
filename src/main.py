from fastapi import FastAPI, UploadFile, HTTPException
from fastapi.responses import JSONResponse
import logging
from pydantic import BaseModel
from langchain import LangChain
from faiss_index import FaissIndex

app = FastAPI()

logging.basicConfig(level=logging.INFO)

class QuestionRequest(BaseModel):
    question: str

@app.post("/upload")
async def upload_pdf(file: UploadFile):
    try:
        # Process the file and update FAISS index
        content = await file.read()
        FaissIndex().add_document(content)
        return JSONResponse(status_code=200, content={"message": "File uploaded successfully."})
    except Exception as e:
        logging.error(f"Error uploading file: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.post("/ask")
async def ask_question(request: QuestionRequest):
    try:
        # Process question via LangChain
        response = LangChain().ask(request.question)
        return JSONResponse(status_code=200, content={"answer": response})
    except Exception as e:
        logging.error(f"Error processing question: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
