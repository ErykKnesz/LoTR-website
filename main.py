from flask import Flask, render_template

from api_handler import APIHandler

API_TOKEN = "be19LYtOOj-5HMykH0pR"
BASE_URL = "https://the-one-api.dev/v2"
headers = {
    "Authorization": f"Bearer {API_TOKEN}"
}

api_handler = APIHandler(API_TOKEN, BASE_URL, headers)

app = Flask(__name__)


@app.route("/")
def home():
    books = api_handler.get_books()
    movies = api_handler.get_movies()
    return render_template("home.html", books=books, movies=movies)


app.route("/book/<int:id>")
def get_book(id):
    book = api_handler.get_books(id)
    return render_template("book.html", book=book)


if __name__ == "__main__":
    app.run(debug=True)
