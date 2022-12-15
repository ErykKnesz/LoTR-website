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

    def get_movie(self, id):
        url = f"{self.base_url}/movie/{id}"
        r = requests.get(url, headers=self.headers)
        return r.json()['docs'][0]

    def get_book(self, id):
        url = f"{self.base_url}/book/{id}"
        r = requests.get(url, headers=self.headers)
        return r.json()['docs'][0]

    def get_chapters(self, id):
        url = f"{self.base_url}/book/{id}/chapter"
        r = requests.get(url, headers=self.headers)
        return r.json()['docs']

    def get_quotes(self, id):
        url = f"{self.base_url}/movie/{id}/quote"
        r = requests.get(url, headers=self.headers)
        print(r.json())
        return r.json()['docs']