import os
from openai import OpenAI
from dotenv import load_dotenv
from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient
from azure_cli_executor import execute_azure_cli_command  
from azure_cli_executor import get_azure_data

# Load environment variables from .env file
load_dotenv()
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),  
)

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

response = client.chat.completions.create(
        model="gpt-4o",
        messages=[            
            {"role": "user", "content": "run azure cli command az group list --output table "}            
        ],
        max_tokens=400
        
    )
print(response.choices[0].message.content)