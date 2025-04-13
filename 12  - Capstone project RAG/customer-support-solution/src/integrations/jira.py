import requests
import json

JIRA_API_URL = "https://your-company.atlassian.net/rest/api/2/issue/"
JIRA_AUTH = ("your_email", "your_api_token")

def create_jira_ticket(summary: str, description: str) -> str:
    """Creates a support ticket in Jira."""
    payload = {
        "fields": {
            "project": {"key": "SUP"},
            "summary": summary,
            "description": description,
            "issuetype": {"name": "Task"}
        }
    }
    headers = {"Content-Type": "application/json"}
    try:
        response = requests.post(JIRA_API_URL, auth=JIRA_AUTH, json=payload, headers=headers)
        if response.status_code == 201:
            return response.json().get('self')  # Return the URL of the created ticket
        else:
            return f"Failed to create ticket: {response.status_code} - {response.text}"
    except Exception as e:
        return str(e)