from flask import Flask

app = Flask(__name__)


@app.route("/")
def handle_home():
    return "Миссия Колонизация Марса"


@app.route("/index")
def handle_index():
    return "И на Марсе будут яблони цвести!"


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)