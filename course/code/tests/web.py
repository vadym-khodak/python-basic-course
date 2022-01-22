"""
Документація Flask: https://flask.palletsprojects.com/en/2.0.x/
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/ping")
def ping():
    return "pong"


@app.route("/api/ping")
def api_ping():
    return {"message": "pong"}


if __name__ == "__main__":
    app.run()
