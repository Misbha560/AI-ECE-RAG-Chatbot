import os
from document_loader import load_pdf, split_documents
from vector_store import VectorStore
from groq import Groq


class RAGPipeline:

    def __init__(self):
        self.vector_store = VectorStore()
        self.groq_client = None

    def _get_groq_client(self):

        if self.groq_client is not None:
            return self.groq_client

        api_key = os.getenv("GROQ_API_KEY")

        if not api_key:
            try:
                import streamlit as st
                api_key = st.secrets["GROQ_API_KEY"]
            except Exception:
                api_key = None

        if not api_key:
            raise ValueError(
                "GROQ_API_KEY is not configured. "
                "Add it to Streamlit Secrets."
            )

        self.groq_client = Groq(api_key=api_key)

        return self.groq_client

    def load_documents(self, uploaded_files):

        all_documents = []

        for file in uploaded_files:

            file.seek(0)

            documents = load_pdf(file)

            all_documents.extend(documents)

        chunks = split_documents(all_documents)

        if not chunks:
            raise ValueError(
                "No readable text was found in the uploaded PDF files."
            )

        self.vector_store.create_index(chunks)

        return len(chunks)

    def ask_question(self, question):

        if self.vector_store.index is None:
            raise ValueError(
                "Please upload and process documents first."
            )

        relevant_documents = self.vector_store.search(
            question,
            top_k=3
        )

        context_parts = []

        for document in relevant_documents:

            context_parts.append(
                f"Source: {document['source']}, "
                f"Page: {document['page']}\n"
                f"{document['text']}"
            )

        context = "\n\n".join(context_parts)

        prompt = f"""
You are an ECE educational assistant.

Answer the user's question using ONLY the information
provided in the retrieved document context.

If the answer is not available in the context, say:
"I could not find the answer in the uploaded documents."

Give a clear and simple explanation suitable for an
ECE engineering student.

Retrieved context:
{context}

User question:
{question}
"""

        client = self._get_groq_client()

        response = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a helpful ECE educational "
                        "RAG chatbot."
                    )
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.2,
            max_completion_tokens=1024
        )

        return response.choices[0].message.content
