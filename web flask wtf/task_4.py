from flask import Flask, render_template

app = Flask(__name__)


@app.route("/answer")
@app.route("/auto_answer")
def acquestionnaire():
    return render_template("auto_answer.html")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)
