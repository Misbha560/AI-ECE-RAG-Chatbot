import faiss
import numpy as np
from sentence_transformers import SentenceTransformer


class VectorStore:

    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.index = None
        self.documents = []

    def create_index(self, documents):

        self.documents = documents

        texts = [doc["text"] for doc in documents]

        embeddings = self.model.encode(
            texts,
            convert_to_numpy=True
        )

        dimension = embeddings.shape[1]

        self.index = faiss.IndexFlatL2(dimension)

        self.index.add(
            np.array(embeddings).astype("float32")
        )

    def search(self, query, top_k=3):

        query_embedding = self.model.encode(
            [query],
            convert_to_numpy=True
        )

        distances, indices = self.index.search(
            np.array(query_embedding).astype("float32"),
            top_k
        )

        results = []

        for index in indices[0]:

            if index < len(self.documents):
                results.append(self.documents[index])

        return results