# AI-ECE-RAG-Chatbot

## 📌 Project Overview

AI-ECE-RAG-Chatbot is an AI-based question-answering system designed for Electronics and Communication Engineering (ECE) students.

The chatbot uses **Retrieval-Augmented Generation (RAG)** to retrieve relevant information from uploaded PDF documents and provide answers to user questions.

Users can upload ECE study materials such as notes, textbooks, and reference PDFs and ask questions based on the uploaded documents.

---

## 🎯 Objectives

- To develop an AI-based chatbot for ECE learning.
- To allow users to interact with PDF-based study materials.
- To extract and process text from PDF documents.
- To split large documents into smaller text chunks.
- To generate vector embeddings from the text.
- To store embeddings using a FAISS vector database.
- To retrieve relevant information for user questions.
- To provide accurate answers based on the available documents.

---

## 🧠 Technologies Used

- **Python**
- **Streamlit**
- **FAISS**
- **Sentence Transformers**
- **LangChain Text Splitters**
- **PyPDF**
- **Groq**
- **NumPy**
- **python-dotenv**

---

## 🔄 System Workflow

```text
PDF Document
     ↓
Text Extraction
     ↓
Text Splitting
     ↓
Embedding Generation
     ↓
FAISS Vector Database
     ↓
User Question
     ↓
Question Embedding
     ↓
Similarity Search
     ↓
Relevant Document Chunks
     ↓
AI Response Generation
     ↓
Final Answer


---

🧩 Project Modules

1. Document Loader

The document loader extracts text from uploaded PDF files.

File: document_loader.py

2. Text Splitting

Large extracted text is divided into smaller chunks using the LangChain text splitter.

3. Embedding Generation

Sentence Transformers converts text chunks into numerical vector representations.

4. Vector Database

FAISS stores the generated embeddings and performs similarity searches.

File: vector_store.py

5. Question Answering

The user's question is converted into an embedding and compared with stored document embeddings to retrieve relevant information.

6. Chatbot Interface

Streamlit provides the web-based user interface.

File: app.py


---

📂 Project Structure

AI-ECE-RAG-Chatbot/
│
├── app.py
├── document_loader.py
├── vector_store.py
├── test_questions.py
├── requirements.txt
├── README.md
│
└── data/
    └── ECE study PDFs


---

⚙️ Installation

Clone the repository:

git clone https://github.com/Misbha560/AI-ECE-RAG-Chatbot.git

Move into the project directory:

cd AI-ECE-RAG-Chatbot

Install the required libraries:

pip install -r requirements.txt


---

▶️ How to Run

Run the Streamlit application:

streamlit run app.py

The application will open in the browser.

Upload an ECE PDF and enter a question related to the document.


---

💬 Example Questions

What does ECE stand for?

What are the main parts of a communication system?

What is a signal?

What is the difference between analog and digital signals?

What are the basic logic gates?


---

✨ Features

📄 PDF document upload

🔎 Document text extraction

✂️ Text chunking

🧠 Embedding generation

🗄️ FAISS vector database

🔍 Semantic similarity search

🤖 AI-based question answering

🌐 Streamlit web interface

📚 ECE-focused educational content



---

📊 Expected Result

The system retrieves relevant information from the uploaded ECE documents and generates an answer to the user's question.

The chatbot is designed to answer questions based on the information available in the uploaded documents.


---

🚀 Future Enhancements

Support for multiple PDF documents.

Improved conversational memory.

Voice-based question answering.

Support for additional engineering branches.

Improved answer evaluation.

Deployment as an online application.



---

👩‍💻 Project

AI-ECE-RAG-Chatbot

Developed as an academic major project using Python and AI technologies.

### After you paste it

At the bottom of GitHub:

**Commit changes → Commit changes**

Then your README will look much more professional.

After that, **send me a screenshot of the updated README**. I'll guide you through the next step: adding your **project screenshots and making the GitHub repository complete**.
