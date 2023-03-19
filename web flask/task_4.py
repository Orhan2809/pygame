from flask import Flask, url_for

app = Flask(__name__)


@app.route("/promotion_image")
def handle_image_mars():

    return f"""
    <!DOCTYPE html>
    <html>
        <head> 
            <meta charset="utf-8">
            <title>Колонизация</title>
            <link rel="stylesheet" type="text/css" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous">
            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}">
        </head>

        <body> 
            <h1 class="text_mars">Жди нас, Марс!</h1>
            <img src="{url_for("static", filename="img/mars_image.png")}">
            <p class="alert alert-dark">Человечество вырастает из детства.</p>
            <p class="alert alert-success">Человечеству мала одна планета.</p>
            <p class="alert alert-dark">Мы сделаем обитаемыми безжизненные пока планеты.</p>
            <p class="alert alert-warning">И начнем с Марса!</p>
            <p class="alert alert-danger">Присоединяйся!</p>
        </body>
    </html>
    """


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)