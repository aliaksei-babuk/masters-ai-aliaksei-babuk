import os
from PyPDF2 import PdfReader

def load_pdf(file_path):
    """Load a PDF file and extract its text and metadata."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    
    reader = PdfReader(file_path)
    text = ""
    metadata = reader.metadata
    
    for page in reader.pages:
        text += page.extract_text() + "\n"
    
    return text, metadata

def load_multiple_pdfs(file_paths):
    """Load multiple PDF files and return their combined text and metadata."""
    combined_text = ""
    combined_metadata = {}
    
    for file_path in file_paths:
        text, metadata = load_pdf(file_path)
        combined_text += text
        combined_metadata[file_path] = metadata
    
    return combined_text, combined_metadata

def load_documents():
    """
    Load PDF documents from the 'data/documents' directory.
    :return: A list of document texts.
    """
    documents_dir = os.path.join(os.path.dirname(__file__), "../data/documents")
    documents = []

    for filename in os.listdir(documents_dir):
        if filename.endswith(".pdf"):
            file_path = os.path.join(documents_dir, filename)
            reader = PdfReader(file_path)
            text = ""
            for page in reader.pages:
                text += page.extract_text()
            documents.append({"filename": filename, "text": text})

    return documents