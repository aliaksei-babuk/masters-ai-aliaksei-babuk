from collections import deque
import json

class ConversationHistory:
    def __init__(self, max_length=100):
        self.history = deque(maxlen=max_length)

    def add_message(self, user_message, bot_response):
        self.history.append({"user": user_message, "bot": bot_response})

    def get_history(self):
        return list(self.history)

    def clear_history(self):
        self.history.clear()

    def save_to_file(self, file_path):
        with open(file_path, 'w') as f:
            json.dump(self.get_history(), f)

    def load_from_file(self, file_path):
        try:
            with open(file_path, 'r') as f:
                self.history = deque(json.load(f), maxlen=self.history.maxlen)
        except FileNotFoundError:
            pass  # If the file does not exist, we simply do not load any history.