# main.py
from fastapi import FastAPI, UploadFile
from ingestion import run_ingestion
from retriever import query_ai

app = FastAPI()

@app.post("/ingest")
async def ingest_document(file: UploadFile):
    # Saves file temporarily and runs Week 1 ingestion logic
    file_path = f"temp_{file.filename}"
    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())
    return run_ingestion(file_path)

@app.get("/chat")
async def chat(question: str):
    # Runs Week 2 retrieval logic
    return {"response": query_ai(question)}