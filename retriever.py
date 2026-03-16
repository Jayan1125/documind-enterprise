# retriever.py
from langchain_pinecone import PineconeVectorStore
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_classic.chains import RetrievalQA
from langchain_core.prompts import PromptTemplate

INDEX_NAME = "documind-enterprise"

def get_retriever():
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    vectorstore = PineconeVectorStore(index_name=INDEX_NAME, embedding=embeddings)
    return vectorstore.as_retriever(search_type="hybrid", search_kwargs={"k": 3})

def query_ai(question):
    llm = ChatOpenAI(model="gpt-4o", temperature=0)
    prompt = PromptTemplate(
        template="Use context to answer. Cite source/page. If unknown, say 'I do not have enough information'. Context: {context} Question: {question}",
        input_variables=["context", "question"]
    )
    chain = RetrievalQA.from_chain_type(llm=llm, retriever=get_retriever(), chain_type_kwargs={"prompt": prompt})
    return chain.invoke({"query": question})