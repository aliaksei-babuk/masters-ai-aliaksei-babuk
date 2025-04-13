from typing import List, Tuple

class CitationManager:
    def __init__(self):
        self.citations = []

    def add_citation(self, document_name: str, page_number: int):
        """Adds a citation for a specific document and page number."""
        citation = {
            "document": document_name,
            "page": page_number
        }
        self.citations.append(citation)

    def get_citations(self) -> List[Tuple[str, int]]:
        """Returns a list of all citations."""
        return [(citation["document"], citation["page"]) for citation in self.citations]

    def clear_citations(self):
        """Clears all citations."""
        self.citations = []

    def format_citation(self, citation: Tuple[str, int]) -> str:
        """Formats a single citation for display."""
        return f"{citation[0]} (p. {citation[1]})"

    def format_all_citations(self) -> List[str]:
        """Formats all citations for display."""
        return [self.format_citation(citation) for citation in self.get_citations()]