from . import db
from .models import User
from .forms import LoginForm, RegisterForm
from flask_login import current_user, login_user
from flask import Blueprint, render_template, request, url_for, redirect, flash
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint("auth", __name__, template_folder="templates")


@auth.route("/register", methods=["GET", "POST"])
def register_page():
    if current_user.is_authenticated:
        return redirect(url_for("view.home_page"))
    form = RegisterForm()
    if form.validate_on_submit():
        full_name = form.full_name.data
        email = form.email.data
        password = form.password.data
        c_password = form.c_password.data

        # check if email already exists
        email_check = User.query.filter_by(email=email).first()
        if email_check:
            flash("email already exists", category="error")
            return redirect(url_for("auth.register_page"))

        if password == c_password:
            h_password = generate_password_hash(password)
            # enter data into the database
            # step 1 create a user
            new_user = User(full_name=full_name, email=email, password=h_password)
            db.session.add(new_user)
            db.session.commit()
            # flash suscesfull acount creation
            flash("account sucessfully created!", category="success")
            return redirect(url_for("auth.login_page"))
        else:
            flash("passwords do not match", category="error")

    return render_template("register.html", form=form)


@auth.route("/login", methods=["GET", "POST"])
def login_page():
    if current_user.is_authenticated:
        return redirect(url_for("view.home_page"))

    form = LoginForm()
    if form.validate_on_submit():
        # grab user data first
        email = form.email.data
        password = form.password.data 
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            # login the user and set their session
            login_user(user)
            # the user exists now we can redirect the user to the dashbord
            flash("login sucessful!!", category="success")
            return redirect(url_for("view.home_page"))

        else:
            flash("invalid credantials!", category="error")
    return render_template("login.html", form=form)













        




























