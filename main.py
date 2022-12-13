import requests
from flask import Flask, render_template

API_TOKEN = "be19LYtOOj-5HMykH0pR"
BASE_URL = "https://the-one-api.dev/v2"
header = {
    "Authorization": f"Bearer {API_TOKEN}"
}

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True)
