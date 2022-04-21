from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy import SQLAlchemy

from application.models import Cities, ProgramLanguages, User, Vacancies


class FlaskAdminSetup(Admin):
    """Класс настройки flask админа"""

    def __init__(self, app: Flask, name: str, template_mode: str) -> None:
        super(FlaskAdminSetup, self).__init__(app, name, template_mode=template_mode)

    def setup_views(self, db: SQLAlchemy):
        """Установим views"""

        self.add_view(ModelView(Cities, session=db.session, name="Список городов"))
        self.add_view(ModelView(ProgramLanguages, session=db.session, name="Языки программирования"))
        self.add_view(ModelView(User, session=db.session, name="Список пользователей"))
        self.add_view(ModelView(Vacancies, session=db.session, name="Список вакансий"))
