# documind-enterprise
An Enterprise-grade Knowledge Management System powered by RAG (Retrieval-Augmented Generation). DocuMind uses FastAPI, OpenAI, and Pinecone to transform static PDF policies into an interactive, conversational intelligence layer with grounded citations
DocuMind Enterprise
DocuMind is an AI-powered Knowledge Management System designed to help organizations chat with their internal documentation. It eliminates the time spent searching through hundreds of pages by providing instant, context-aware answers grounded in official company data.

🚀 Key Features
Semantic Search: Goes beyond keyword matching to understand the intent behind employee questions.

Automated Ingestion: Seamlessly parse, chunk, and embed large PDF documents into a vector database.

Grounded Responses: Every answer includes citations to specific pages in the source documents to prevent hallucinations.

Modern Tech Stack: Built with FastAPI for high-performance backends and Pinecone for enterprise-scale vector retrieval.

🛠️ Tech Stack
Backend: Python, FastAPI, Uvicorn

Orchestration: LangChain / LangChain-Core

LLM: OpenAI GPT-4o

Vector Database: Pinecone

Frontend: Streamlit

🔧 Installation & Setup
Clone the repo:

Bash
git clone https://github.com/your-username/documind-enterprise.git
Install dependencies:

Bash
pip install -r requirements.txt
Configure Environment: Create a .env file and add your OPENAI_API_KEY and PINECONE_API_KEY.

Run the API:

Bash
uvicorn main:app --reload
