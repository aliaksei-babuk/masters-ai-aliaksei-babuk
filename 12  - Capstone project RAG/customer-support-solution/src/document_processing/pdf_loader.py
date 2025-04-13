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