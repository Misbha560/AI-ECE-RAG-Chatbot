import streamlit as st

from rag_pipeline import RAGPipeline


# Page configuration
st.set_page_config(
    page_title="Domain-Specific RAG Chatbot",
    page_icon="🤖",
    layout="wide"
)


# Title
st.title("🤖 Domain-Specific RAG Chatbot")

st.write(
    "Upload PDF documents and ask questions based on their content."
)


# Create RAG pipeline only once
if "rag_pipeline" not in st.session_state:
    st.session_state.rag_pipeline = RAGPipeline()


# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []


# Sidebar
with st.sidebar:

    st.header("📚 Upload Documents")

    uploaded_files = st.file_uploader(
        "Choose PDF files",
        type=["pdf"],
        accept_multiple_files=True
    )

    process_button = st.button(
        "Process Documents"
    )


# Process documents
if process_button:

    if not uploaded_files:

        st.warning(
            "Please upload at least one PDF document."
        )

    else:

        with st.spinner(
            "Processing documents and generating embeddings..."
        ):

            try:

                total_chunks = (
                    st.session_state.rag_pipeline.load_documents(
                        uploaded_files
                    )
                )

                st.success(
                    f"Documents processed successfully! "
                    f"Total chunks: {total_chunks}"
                )

                st.session_state.documents_processed = True

            except Exception as e:

                st.error(
                    f"Error while processing documents: {e}"
                )


# Show uploaded files
if uploaded_files:

    st.subheader("📄 Uploaded Documents")

    for file in uploaded_files:

        st.write(f"• {file.name}")


# Display previous messages
for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])


# Question input
question = st.chat_input(
    "Ask a question about the uploaded documents..."
)


if question:

    # Check whether documents were processed
    if not st.session_state.get(
        "documents_processed",
        False
    ):

        st.warning(
            "Please upload and process the documents first."
        )

    else:

        # Display user question
        with st.chat_message("user"):

            st.markdown(question)

        st.session_state.messages.append(
            {
                "role": "user",
                "content": question
            }
        )


        # Generate answer
        with st.chat_message("assistant"):

            with st.spinner(
                "Searching documents and generating answer..."
            ):

                try:

                    answer = (
                        st.session_state.rag_pipeline
                        .ask_question(question)
                    )

                    st.markdown(answer)

                    st.session_state.messages.append(
                        {
                            "role": "assistant",
                            "content": answer
                        }
                    )

                except Exception as e:

                    error_message = (
                        f"Error while generating answer: {e}"
                    )

                    st.error(error_message)

                    st.session_state.messages.append(
                        {
                            "role": "assistant",
                            "content": error_message
                        }
                    )


# Clear chat button
with st.sidebar:

    if st.button("🗑️ Clear Chat"):

        st.session_state.messages = []

        st.rerun()