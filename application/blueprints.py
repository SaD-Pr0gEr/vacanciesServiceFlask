from flask import Flask
from application.accounts import accounts
from application.errors import errors


def register_blueprints(app: Flask):
    app.register_blueprint(accounts, url_prefix="/accounts")
    app.register_blueprint(errors)
