from flask import Flask
from flask_migrate import Migrate
from config import DevConfig
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

db = SQLAlchemy()
bcrypt = Bcrypt()
migrate = Migrate()
login_manager = LoginManager()


def create_app():
    app = Flask(__name__)
    app.config.from_object(DevConfig)
    db.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    login_manager.login_view = "login"
    login_manager.login_message_category = "info"
    from application.blueprints import register_blueprints
    register_blueprints(app)
    from application.admin import FlaskAdminSetup
    FlaskAdminSetup(app, name="Сервис вакансий", template_mode="bootstrap4").setup_views(db)
    return app
