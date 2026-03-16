# ingestion.py
from langchain_community.document_loaders import UnstructuredPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore
import os

INDEX_NAME = "documind-enterprise"


def run_ingestion(file_path):
    loader = UnstructuredPDFLoader(file_path)
    data = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    docs = text_splitter.split_documents(data)
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

    PineconeVectorStore.from_documents(docs, embeddings, index_name=INDEX_NAME)
    return {"status": "success", "chunks_processed": len(docs)}