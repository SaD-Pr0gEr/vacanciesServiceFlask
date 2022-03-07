from flask import render_template
from application.errors import errors


@errors.app_errorhandler(404)
def not_found(error):
    context = {
        "title": "Not found"
    }
    return render_template("errors/404.html", **context), 404


@errors.app_errorhandler(403)
def forbidden(error):
    context = {
        "title": "Нет прав"
    }
    return render_template("errors/403.html", **context), 403


@errors.app_errorhandler(500)
def forbidden(error):
    context = {
        "title": "Ошибка сервера"
    }
    return render_template("errors/500.html", **context), 500
