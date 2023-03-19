from flask import Flask

app = Flask(__name__)


@app.route("/promotion")
def handle_promotion():
    return """
            <p>Человечество вырастает из детства.</p>
            <p>Человечеству мала одна планета.</p>
            <p>Мы сделаем обитаемыми безжизненные пока планеты.</p>
            <p>И начнем с Марса!</p>
            <p>Присоединяйся!</p>"""


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)