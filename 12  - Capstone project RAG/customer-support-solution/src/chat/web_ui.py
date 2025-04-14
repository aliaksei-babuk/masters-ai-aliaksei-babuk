import streamlit as st
from chat.conversation_history import ConversationHistory
from document_processing.pdf_loader import load_documents
from document_processing.citation_manager import CitationManager
from integrations.github import create_support_ticket  # Use GitHub integration

# Initialize session state for API key
if "openai_api_key" not in st.session_state:
    st.session_state["openai_api_key"] = ""

# Initialize conversation history and citation manager
conversation_history = ConversationHistory()
citation_manager = CitationManager()

# Load documents for answering questions
documents = load_documents()

# Web UI
st.title("Customer Support Solution")

# Input field for OpenAI API key
st.sidebar.header("Settings")
st.sidebar.text_input(
    "Enter your OpenAI API Key:",
    type="password",
    key="openai_api_key",
    help="Your OpenAI API key is required to use the AI features."
)

# Display the entered API key (for debugging purposes, remove in production)
if st.session_state["openai_api_key"]:
    st.sidebar.write("API Key set successfully!")

# Main chat interface
st.text_area("Chat with the assistant:", placeholder="Type your question here...")
st.button("Send")

# Display conversation history
for message in conversation_history.get_history():
    st.write(message)

# User input for questions
user_question = st.text_input("Ask a question:")

if st.button("Submit"):
    # Process the question and get an answer
    answer, citations = citation_manager.answer_question(user_question, documents)
    
    # Update conversation history
    conversation_history.add_message(f"You: {user_question}")
    conversation_history.add_message(f"Bot: {answer} (Citations: {citations})")
    
    # Display the answer
    st.write(f"**Bot:** {answer} (Citations: {citations})")

# Support ticket creation
ticket_summary = st.text_input("Ticket Summary:")
ticket_description = st.text_area("Ticket Description:")

if st.button("Create Support Ticket"):
    response = create_support_ticket(ticket_summary, ticket_description)
    st.write("Support Ticket Created:", response)

def display_chat(documents):
    """
    Display the chat interface for interacting with the assistant.
    :param documents: List of documents for answering questions.
    """
    st.title("Customer Support Chat")
    user_question = st.text_input("Ask a question:")
    
    if st.button("Submit"):
        # Process the question and get an answer
        answer, citations = citation_manager.answer_question(user_question, documents)
        
        # Update conversation history
        conversation_history.add_message(f"You: {user_question}")
        conversation_history.add_message(f"Bot: {answer} (Citations: {citations})")
        
        # Display the answer
        st.write(f"**Bot:** {answer} (Citations: {citations})")