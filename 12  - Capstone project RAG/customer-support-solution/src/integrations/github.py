import requests

GITHUB_API_URL = "https://api.github.com/repos/{owner}/{repo}/issues"
GITHUB_AUTH = ("your_github_username", "your_github_token")

def create_github_issue(owner: str, repo: str, title: str, body: str) -> dict:
    """Creates an issue in a specified GitHub repository."""
    url = GITHUB_API_URL.format(owner=owner, repo=repo)
    payload = {
        "title": title,
        "body": body
    }
    headers = {
        "Accept": "application/vnd.github.v3+json"
    }
    
    response = requests.post(url, json=payload, auth=GITHUB_AUTH, headers=headers)
    
    if response.status_code == 201:
        return response.json()  # Return the created issue details
    else:
        raise Exception(f"Failed to create issue: {response.status_code} - {response.text}")

def get_github_issues(owner: str, repo: str) -> list:
    """Retrieves issues from a specified GitHub repository."""
    url = GITHUB_API_URL.format(owner=owner, repo=repo)
    response = requests.get(url, auth=GITHUB_AUTH)
    
    if response.status_code == 200:
        return response.json()  # Return the list of issues
    else:
        raise Exception(f"Failed to retrieve issues: {response.status_code} - {response.text}")