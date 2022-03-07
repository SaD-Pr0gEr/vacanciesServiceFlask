import datetime
from flask_login import UserMixin
from flask_login._compat import text_type
from application import db, bcrypt, login_manager


class Cities(db.Model):
    """Модель городов"""

    __tablename__ = "cities"

    ID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    slug = db.Column(
        db.String,
        unique=True,
        nullable=False
    )

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Model: {self.__tablename__} - {self.name}"


class ProgramLanguages(db.Model):
    """Модель языка программирования"""

    __tablename__ = "program_languages"

    ID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    slug = db.Column(
        db.String,
        unique=True,
        nullable=False
    )

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Model: {self.__tablename__} - {self.name}"


class User(db.Model, UserMixin):
    """Модель пользователя"""

    __tablename__ = "users"

    ID = db.Column(db.Integer, primary_key=True)
    email = db.Column(
        db.String,
        unique=True,
        nullable=False
    )
    password_hash = db.Column(db.String, nullable=False)
    city = db.Column(db.ForeignKey("cities.ID"))
    language = db.Column(db.ForeignKey("program_languages.ID"))
    subscribe_status = db.Column(
        db.Boolean,
        nullable=False,
        default=False
    )
    is_active = db.Column(
        db.Boolean,
        nullable=False,
        default=False,
    )
    is_admin = db.Column(
        db.Boolean,
        nullable=False,
        default=False
    )
    joined_date = db.Column(db.Date, nullable=False)

    vacancies = db.relationship(
        "Vacancies",
        backref='user_vacancies',
        lazy=True
    )

    @property
    def password(self):
        return self.password_hash

    @password.setter
    def password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode("utf-8")

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)

    @staticmethod
    def create_user(email, password, city, language, subscribe_status):
        user = User(
            email=email,
            password=password,
            city=city,
            language=language,
            subscribe_status=subscribe_status,
            joined_date=datetime.datetime.today().date()
        )
        db.session.add(user)
        db.session.commit()
        return user

    @staticmethod
    def create_superuser(email, password, city, language, subscribe_status):
        user = User.create_user(email, password, city, language, subscribe_status)
        user.is_active = True
        user.is_admin = True
        db.session.commit()
        return user

    def get_id(self):
        try:
            return text_type(self.ID)
        except AttributeError:
            raise NotImplementedError('No `id` attribute - override `get_id`')

    def __str__(self):
        return self.email

    def __repr__(self):
        return f"Model: {self.__tablename__} - {self.email}"


class Vacancies(db.Model):
    """Класс для вакансий"""

    __tablename__ = "vacancies"

    ID = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    creator = db.Column(db.ForeignKey("users.ID"))
    description = db.Column(db.String(1500), nullable=False)
    company_name = db.Column(db.String(120), nullable=False)
    city = db.Column(db.ForeignKey("cities.ID"))
    language = db.Column(db.ForeignKey("program_languages.ID"))
    contacts = db.Column(db.String(120), nullable=False)
    created_date = db.Column(db.Date, nullable=False)

    def __str__(self):
        return self.title

    def __repr__(self):
        return f"Model: {self.__tablename__} - {self.ID}"


@login_manager.user_loader
def load_user(ID):
    return User.query.get(int(ID))
