from flask import render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user, logout_user, login_user
from application import db
from application.accounts import accounts
from application.accounts.forms import LoginForm, SignUpForm, UpdateProfileForm
from application.models import User, Cities, ProgramLanguages


@accounts.route("/signup/", methods=["GET", "POST"])
def signup():
    if not current_user.is_anonymous:
        flash("Вы уже вошли в систему!", category="info")
        return redirect(url_for("home"))
    signUpForm = SignUpForm()
    signUpForm.city.choices = Cities.query.all()
    signUpForm.language.choices = ProgramLanguages.query.all()
    if request.method == "POST":
        if signUpForm.validate_on_submit():
            user = User.create_user(
                signUpForm.email.data,
                signUpForm.password1.data,
                signUpForm.city.data,
                signUpForm.language.data,
                signUpForm.subscribe.data,
            )
            if not user:
                flash("Ошибка в создании пользователя попробуйте ещё раз")
                return redirect(url_for("accounts.signup"))
            flash("Проверьте вашу почту для подтверждения аккаунта", category="info")
            return redirect(url_for("home"))
        if signUpForm.errors:
            for errors in signUpForm.errors.values():
                for error in errors:
                    flash(error, category="danger")
    context = {
        "title": "Sign Up",
        "signUpForm": signUpForm,
    }
    return render_template("accounts/signup.html", **context)


@accounts.route("/login/", methods=["GET", "POST"])
def login():
    if not current_user.is_anonymous:
        flash("Вы уже вошли в систему!", category="info")
        return redirect(url_for("home"))
    if request.method == "POST":
        form = LoginForm()
        if form.validate_on_submit():
            check_user = User.query.filter_by(email=form.email.data).first()
            if not check_user.check_password(form.password.data):
                flash("Неправильный логин или пароль", category='danger')
                return redirect(url_for("accounts.login"))
            if not check_user.is_active:
                flash("Аккаунт не активен! Чтобы активировать её проверьте почту", category='info')
                return redirect(url_for("accounts.login"))
            login_user(check_user)
            flash(f"Вы успешно вошли как {check_user.email}!", category="success")
            return redirect(url_for("home"))
        if form.errors:
            for errors in form.errors.values():
                for error in errors:
                    flash(error, category="danger")
    else:
        form = LoginForm()
    context = {
        "title": "Login",
        "login_form": form
    }
    return render_template("accounts/login.html", **context)


@accounts.route("/me/", methods=["GET"])
@login_required
def profile():
    context = {
        "title": "Мой профиль"
    }
    return render_template("accounts/profile.html", **context)


@accounts.route("/me/edit/", methods=["GET", "POST"])
@login_required
def update():
    if request.method == "POST":
        form = UpdateProfileForm(request.form, obj=current_user)
        form.city.choices = Cities.query.all()
        form.language.choices = ProgramLanguages.query.all()
        if form.validate_on_submit():
            if form.password1.data:
                current_user.password = form.password1.data
            current_user.city = form.city.data
            current_user.language = form.language.data
            current_user.subscribe_status = form.subscribe.data
            db.session.commit()
            flash("Данные успешно изменены", category="info")
        if form.errors:
            for errors in form.errors.values():
                for error in errors:
                    flash(error, category="danger")
    else:
        form = UpdateProfileForm()
        form.city.choices = Cities.query.all()
        form.language.choices = ProgramLanguages.query.all()
    context = {
        "title": "Редактирования профиля",
        "form": form
    }
    return render_template("accounts/update_profile.html", **context)


@accounts.route("/logout/")
@login_required
def logout():
    if not current_user.is_authenticated:
        flash("Вы не вошли в систему!", category="info")
        return redirect(url_for("home"))
    logout_user()
    flash("Вышли успешно!", category="success")
    return redirect(url_for("home"))
