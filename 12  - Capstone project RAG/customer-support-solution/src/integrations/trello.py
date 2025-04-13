import requests

class TrelloIntegration:
    def __init__(self, api_key: str, api_token: str):
        self.api_key = api_key
        self.api_token = api_token
        self.base_url = "https://api.trello.com/1"

    def create_card(self, list_id: str, name: str, description: str) -> dict:
        url = f"{self.base_url}/cards"
        query = {
            'key': self.api_key,
            'token': self.api_token,
            'idList': list_id,
            'name': name,
            'desc': description
        }
        response = requests.post(url, params=query)
        return response.json()

    def update_card(self, card_id: str, name: str = None, description: str = None) -> dict:
        url = f"{self.base_url}/cards/{card_id}"
        query = {
            'key': self.api_key,
            'token': self.api_token
        }
        if name:
            query['name'] = name
        if description:
            query['desc'] = description
        response = requests.put(url, params=query)
        return response.json()

    def get_card(self, card_id: str) -> dict:
        url = f"{self.base_url}/cards/{card_id}"
        query = {
            'key': self.api_key,
            'token': self.api_token
        }
        response = requests.get(url, params=query)
        return response.json()