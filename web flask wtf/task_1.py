from flask import Flask, render_template

app = Flask(__name__)


@app.route("/<title_web>")
@app.route("/index/<title_web>")
def title_name(title_web):
    return render_template("base_task1.html", title=title_web)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)