from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter


def load_pdf(file):
    documents = []

    reader = PdfReader(file)

    for page_number, page in enumerate(reader.pages, start=1):
        text = page.extract_text()

        if text and text.strip():
            documents.append({
                "text": text.strip(),
                "source": file.name,
                "page": page_number
            })

    return documents


def split_documents(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=100
    )

    chunks = []

    for document in documents:

        split_texts = splitter.split_text(
            document["text"]
        )

        for text in split_texts:

            chunks.append({
                "text": text,
                "source": document["source"],
                "page": document["page"]
            })

    return chunks


if __name__ == "__main__":

    pdf_path = "documents/ECE_notes.pdf"

    pages = load_pdf(pdf_path)

    print("Total pages extracted:", len(pages))

    for page in pages[:3]:

        print("\n--------------------")
        print("Page:", page["page"])
        print(page["text"][:500])

    chunks = split_documents(pages)

    print("\n====================")
    print("Total chunks created:", len(chunks))