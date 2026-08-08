import requests


class LoginAPI:

    def __init__(self):
        self.url = "https://postman-echo.com/post"


    def login(self, username, password):

        data = {
            "username": username,
            "password": password
        }

        response = requests.post(
            self.url,
            json=data
        )

        return response