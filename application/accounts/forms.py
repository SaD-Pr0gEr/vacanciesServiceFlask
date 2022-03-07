from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, SubmitField, SelectField, BooleanField
from wtforms.validators import Email, ValidationError, DataRequired, Length, EqualTo
from application.models import User


class SignUpForm(FlaskForm):
    """Класс формы регистрации"""

    def validate_email(self, email):
        if User.query.filter_by(email=email.data).first():
            raise ValidationError("Пользователь с таким email существует")

    email = EmailField(label='email', validators=[Email(), DataRequired()])
    password1 = PasswordField(
        label='Пароль',
        validators=[Length(min=6), DataRequired()]
    )
    password2 = PasswordField(
        label='Пароль ещё раз',
        validators=[EqualTo("password1", message="Пароли не совпадают"), DataRequired()]
    )
    city = SelectField(
        label="Город",
        validators=[DataRequired()],
    )
    language = SelectField(
        label="Язык программирования",
        validators=[DataRequired()],
    )
    subscribe = BooleanField(label="Подписка на рассылку")
    submit = SubmitField(label='Зарегистрироваться')


class LoginForm(FlaskForm):
    """Класс формы логина"""

    def validate_email(self, email):
        if not User.query.filter_by(email=email.data).first():
            raise ValidationError("Пользователь с таким email не найден")

    email = EmailField(label="Email*", validators=[Email(), DataRequired()])
    password = PasswordField(label="Пароль*", validators=[DataRequired()])
    submit = SubmitField(label="Войти")


class UpdateProfileForm(FlaskForm):
    """Форма редактирования профиля"""

    password1 = PasswordField(
        label='Пароль',
    )
    password2 = PasswordField(
        label='Пароль ещё раз',
        validators=[EqualTo("password1", message="Пароли не совпадают")]
    )
    city = SelectField(
        label="Город",
    )
    language = SelectField(
        label="Язык программирования",
    )
    subscribe = BooleanField(label="Подписка на рассылку")
    submit = SubmitField(label='Изменить')
