import streamlit as st
from chat.web_ui import display_chat
from document_processing.pdf_loader import load_documents


def main():
    st.title("Customer Support Solution")
    
    # Load documents for citation
    documents = load_documents()
    
    # Display chat interface
    chat_interface = display_chat(documents)
    
    # Create support ticket functionality
    if st.button("Create Support Ticket"):
        summary = st.text_input("Ticket Summary")
        description = st.text_area("Ticket Description")
        if st.button("Submit"):
            response = create_ticket(summary, description)
            st.success(f"Ticket created: {response}")

if __name__ == "__main__":
    main()