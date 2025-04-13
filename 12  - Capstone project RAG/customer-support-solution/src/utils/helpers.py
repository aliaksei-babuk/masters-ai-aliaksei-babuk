def format_ticket_summary(summary: str) -> str:
    """Formats the ticket summary for better readability."""
    return summary.strip().capitalize()

def extract_pdf_metadata(pdf_file_path: str) -> dict:
    """Extracts metadata from a PDF file."""
    import PyPDF2
    metadata = {}
    with open(pdf_file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        metadata = reader.metadata
    return metadata

def clean_text(text: str) -> str:
    """Cleans the input text by removing unnecessary whitespace and special characters."""
    import re
    return re.sub(r'\s+', ' ', text).strip()

def generate_response_summary(response: str) -> str:
    """Generates a concise summary of the response for display."""
    return response if len(response) <= 150 else response[:147] + '...'