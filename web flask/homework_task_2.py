from flask import Flask, url_for

app = Flask(__name__)


@app.route("/results/<nickname>/<int:level>/<float:rating>")
def result(nickname, level, rating):
    return f"""
    <!DOCTYPE html>
    <html>
        <head> 
            <meta charset="utf-8">
            <title>Результаты</title>
            <link rel="stylesheet" type="text/css" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous">
            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}">
        </head>

        <body> 
            <h1>Результат отбора</h1>
            <h2>Претендента на участие в миссии {nickname}:</h2>
            <p class="alert alert-success">Поздравляем! Ваш рейтинг после {level} этапа отбора</p>
            <p class="alert alert-danger">состовляет {rating}!</p>
            <p class="alert alert-warning">Желаем удачи</p>
        </body>
    </html>
    """


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)