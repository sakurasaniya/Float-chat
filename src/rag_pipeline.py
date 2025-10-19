from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

class RAGPipeline:
    def __init__(self, vector_db_path="vector_store"):
        self.embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        self.db = FAISS.load_local(
            vector_db_path,
            self.embeddings,
            allow_dangerous_deserialization=True  # Allows loading pickle files safely if trusted
        )

    def retrieve(self, query: str):
        return self.db.similarity_search(query, k=3)
