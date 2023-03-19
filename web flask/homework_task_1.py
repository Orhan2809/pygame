from flask import Flask, url_for

app = Flask(__name__)


@app.route("/choice/<planet_name>")
def handle_planet_name(planet_name):
    planet_name_dict = {
        "Меркурий": 'На ней год длиться всего 90 дней"Температура днем достигает 430°C, '
                    'а ночью опускается до –180°C"На планете можно устроить джакузи из магмы и лавы',
        "Венера": 'На ней есть сильные ветры со скоростью 300 км/ч"А температура ещё больще чем у Меркурия 480°C"'
                  'Она третья по яркости планета после Луны и Солнца',
        "Марс": 'На ней много необходимых ресурсов;"На ней есть вода и атмостфера;"На ней есть небольшое м'
                'агнитное поле;"',
        "Юпитер": 'Это же Крупнейшая планета Солнечной системы"В добавок это газовый гигант"'
                  'На Юпитере могут идти дожди из алмазов',
        "Сатурн": 'У Сатурна около 50 спутников"У него есть кольца вокруг планеты"Он газовый гигант',
        "Уран": 'Уран третий по диаметру и четвёртый по массе в Солнечной системе"'
                'Он седьмой по удалённости от Солнца"Это газовый гигант',
        "Нептун": 'Нептун самая дальняя от Солнца планета"'
                  'Нептунианский год равен 165 земным так что вы успеете все за 1 год"Это газовый гигант',
                        }
    try:
        planet_name_text = planet_name_dict[planet_name].split('"')
        if planet_name == "Земля":
            return "<h1>Мы же на ней и живём </h1>"
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
            <h1>Моё предложение: {planet_name}</h1>
            <h2>Это планета близка к Земле;</h2>
            <p class="alert  alert-success">{planet_name_text[0]}</p>
            <p class="alert alert-dark">{planet_name_text[1]}</p>
            <p class="alert alert-warning">{planet_name_text[2]}</p>
            <p class="alert alert-danger">Наконец, она просто красивая!</p>
        </body>
    </html>
    """
    except:
        return "<h1>Такой планеты мы не знаем</h1>"


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)
