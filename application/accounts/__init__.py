from flask import Blueprint

accounts = Blueprint(
    "accounts",
    __name__,
    template_folder="templates",
    static_url_path='/static',
    static_folder="static",
)

from . import views
