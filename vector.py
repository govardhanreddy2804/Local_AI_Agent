from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
import os
import pandas as pd

# Load CSV
df = pd.read_csv("realistic_restaurant_reviews.csv")

# Create embeddings model
embeddings = OllamaEmbeddings(model="mxbai-embed-large")

# Setup DB path
db_location = "./chrome_langchain_db"
add_documents = not os.path.exists(db_location)

# Create vector store
vector_store = Chroma(
    collection_name="restaurant_reviews",
    persist_directory=db_location,
    embedding_function=embeddings
)

# Add documents if DB is not yet created
if add_documents:
    documents = []
    ids = []
    for i, row in df.iterrows():
        document = Document(
            page_content=row["Title"] + " " + row["Review"],
            metadata={"rating": row["Rating"], "date": row["Date"]},
            id=str(i)
        )
        ids.append(str(i))
        documents.append(document)

    vector_store.add_documents(documents=documents, ids=ids)

# ✅ Make retriever available at module level
retriever = vector_store.as_retriever(search_kwargs={"k": 5})
