import requests

def create_github_issue(repo_owner, repo_name, token, title, body):
    """
    Создаёт тикет (issue) в GitHub.
    :param repo_owner: владелец репозитория
    :param repo_name: название репозитория
    :param token: GitHub Personal Access Token
    :param title: заголовок тикета
    :param body: описание тикета
    :return: ответ от GitHub API
    """
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/issues"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json"
    }
    data = {
        "title": title,
        "body": body
    }
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 201:
        return f"Тикет создан: {response.json()['html_url']}"
    else:
        return f"Не удалось создать тикет. Код ответа: {response.status_code}, {response.text}"
