import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    """Базовый конфиг"""

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CSRF_ENABLED = True


class ProdConfig(BaseConfig):
    """Конфиг для прода"""

    DEBUG = False
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URI")


class DevConfig(BaseConfig):
    """Конфиг для дева"""

    DEBUG = True
    DEVELOPMENT = True
    SECRET_KEY = "some secret key for dev"
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{BASE_DIR}/app.db"
