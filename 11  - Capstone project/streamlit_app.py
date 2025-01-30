import streamlit as st
import pandas as pd
import openai
from dotenv import load_dotenv
import os
import logging
from azure_cli_executor import execute_azure_cli_command  # Import the function
from azure_cli_executor import get_azure_data

# Configure logging
logging.basicConfig(level=logging.INFO)

# Load environment variables from .env file
load_dotenv()

# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def run_query(query):
    logging.info(f'Running query: {query}')
    # Implement Azure query execution logic here
    # For now, just return the query as the result
    return f'Query: {query}\n\nResults:\n...'

def filter_data_by_column(data, column, value):
    logging.info(f'Filtering data by column: {column} with value: {value}')
    # Check if the selected column exists
    if column not in data.columns:
        st.error(f'The column "{column}" does not exist in the uploaded file.')
        return pd.DataFrame()  # Return an empty DataFrame
    # Filter the data based on the selected column and value
    filtered_data = data[data[column] == value]
    return filtered_data

def extract_relevant_chunks(data, query):
    logging.info(f'Extracting relevant chunks from data based on query: {query}')
    # Implement logic to extract relevant chunks from the data based on the query
    # For now, just return the first 1000 characters of the data
    return data[:1000]

tools_for_ai = [{
    "type": "function",
    "function": {
        "name": "get_azure_data",
        "description": "Get azure data using Azure CLI",
        "parameters": {
            "type": "object",
            "properties": {
                "command": {
                    "type": "string",
                    "description": "azure cli command to execute"
                }
            },
            "required": [
                "command"
            ],
            "additionalProperties": False
        },
        "strict": True
    }
}]

def call_function(query):    
    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=[            
            {"role": "user", "content": f"run azure cli command {query}"}            
        ],
        max_tokens=400,
        tools=tools_for_ai,
    )
    return response.choices[0].message.content


def analyze_data(data, query, call_func=False):
    logging.info(f'Analyzing data with query: {query}')
    # Extract relevant chunks from the data
    relevant_data = extract_relevant_chunks(data, query)
    # Send the relevant data and query to ChatGPT for analysis

    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Analyze the following data and provide a summary based on the query: {query}\n\nData:\n{relevant_data}"}            
        ],
        max_tokens=400
    )
    analysis_result = response.choices[0].message.content

    if call_func:
        func_result = call_function(query)
        return analysis_result, func_result

    return analysis_result





st.title('Azure WAF analyzer')

# Azure credentials input
st.sidebar.title('Azure Credentials')
client_id = st.sidebar.text_input('Client ID')
tenant_id = st.sidebar.text_input('Tenant ID')
client_secret = st.sidebar.text_input('Client Secret', type='password')

if client_id and tenant_id and client_secret:
    os.environ['AZURE_CLIENT_ID'] = client_id
    os.environ['AZURE_TENANT_ID'] = tenant_id
    os.environ['AZURE_CLIENT_SECRET'] = client_secret

    # Azure CLI command input
    st.sidebar.title('Azure CLI Command')
    azure_command = st.sidebar.text_input('Enter Azure CLI command:')
    if st.sidebar.button('Execute Command'):
        command_output = execute_azure_cli_command(azure_command)
        st.sidebar.write('Command Output:')
        st.sidebar.text_area('Output', command_output, height=200)

uploaded_file = st.file_uploader("Choose an Excel file", type="xlsx")
if uploaded_file:
    logging.info('Excel file uploaded')
    df = pd.read_excel(uploaded_file)
    st.write("Data from Excel file:")
    st.dataframe(df)

    column = st.selectbox("Select the column to filter by:", df.columns)
    value = st.text_input(f"Enter the value to filter by in the '{column}' column:")
    if value:
        filtered_df = filter_data_by_column(df, column, value)
        if not filtered_df.empty:
            st.write("Filtered Data:")
            st.dataframe(filtered_df)

            query = st.text_input("Enter your query for the data:")
            call_func = st.checkbox("Call az cli command with Ai analytics on data")
            if st.button("Analyze"):
                data_str = filtered_df.to_string(index=False)
                analysis = analyze_data(data_str, query, call_func=call_func)
                st.write("Analysis:")
                if isinstance(analysis, tuple):
                    analysis_result, func_result = analysis
                    st.text_area("Analysis Result", analysis_result, height=300)
                    st.text_area("Function Call Result", func_result, height=300)
                else:
                    st.text_area("Analysis Result", analysis, height=300)


