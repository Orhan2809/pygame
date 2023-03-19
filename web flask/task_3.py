from flask import Flask, url_for

app = Flask(__name__)


@app.route("/")
def handle_home():
    return "Привет, Марс!"


@app.route("/image_mars")
def handle_image_mars():
    return f"""<h1>Жди нас, Марс!</h1> 
            <img src="{url_for("static", filename="img/mars_image.png")}">
            <p> Вот она какая, красная планета</p>"""


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)