from flask import render_template
from run import app


@app.route("/home")
@app.route("/")
def home():
    context = {
        "title": "Главная страница"
    }
    return render_template("main/home.html", **context)
