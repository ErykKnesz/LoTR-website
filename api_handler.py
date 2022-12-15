import requests


class APIHandler:
    def __init__(self, token, base_url, headers={}):
        self.token = token
        self.base_url = base_url
        self.headers = headers

    def get_books(self):
        url = f"{self.base_url}/book"
        r = requests.get(url, headers=self.headers)
        return r.json()['docs']

    def get_movies(self):
        url = f"{self.base_url}/movie"
        r = requests.get(url, headers=self.headers)
        return r.json()['docs']

    def get_book(self, id):
        url = f"{self.base_url}/book/{id}"
        r = requests.get(url, headers=self.headers)
        return r.json()['docs']