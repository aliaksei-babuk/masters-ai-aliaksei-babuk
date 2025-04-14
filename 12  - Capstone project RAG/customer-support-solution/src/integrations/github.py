import requests

class GitHubIssueTracker:
    def __init__(self, repo_owner, repo_name, access_token):
        """
        Initialize the GitHubIssueTracker with repository details and access token.
        :param repo_owner: GitHub repository owner (username or organization name)
        :param repo_name: GitHub repository name
        :param access_token: Personal access token for GitHub API
        """
        self.repo_owner = repo_owner
        self.repo_name = repo_name
        self.access_token = access_token
        self.api_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/issues"

    def create_issue(self, title, body, assignees=None, labels=None):
        """
        Create a new issue in the GitHub repository.
        :param title: Title of the issue
        :param body: Description of the issue
        :param assignees: List of GitHub usernames to assign the issue to (optional)
        :param labels: List of labels to add to the issue (optional)
        :return: Response from the GitHub API
        """
        headers = {
            "Authorization": f"token {self.access_token}",
            "Accept": "application/vnd.github.v3+json"
        }
        payload = {
            "title": title,
            "body": body,
            "assignees": assignees or [],
            "labels": labels or []
        }
        response = requests.post(self.api_url, json=payload, headers=headers)
        response.raise_for_status()
        return response.json()


def create_support_ticket(summary, description):
    """
    Wrapper function to create a GitHub issue as a support ticket.
    """
    # Replace these with your GitHub repository details
    REPO_OWNER = "your-github-username"
    REPO_NAME = "your-repo-name"
    ACCESS_TOKEN = "your-personal-access-token"

    github_tracker = GitHubIssueTracker(REPO_OWNER, REPO_NAME, ACCESS_TOKEN)
    return github_tracker.create_issue(title=summary, body=description)