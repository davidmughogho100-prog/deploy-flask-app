from . import db
from .models import User
from .forms import LoginForm, RegisterForm
from flask_login import current_user, login_user
from flask import Blueprint, render_template, request, url_for, redirect
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint("auth", __name__, template_folder="templates")


@auth.route("/register", methods=["GET", "POST"])
def register_page():
    if current_user.is_authenticated:
        return redirect(url_for("view.home_page"))
    form = RegisterForm()
    if request.method == "POST":
        full_name = request.form.get("full_name")
        email = request.form.get("email")
        password = request.form.get("password")
        c_password = request.form.get("c_password")
        h_password = generate_password_hash(password)

        if password == c_password: 
            # enter data into the database
        
            # step 1 create a user
            new_user = User(full_name=full_name, email=email, password=h_password)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for("auth.login_page"))


    return render_template("r.html", form=form)


@auth.route("/login", methods=["GET", "POST"])
def login_page():
    if current_user.is_authenticated:
        return redirect(url_for("view.home_page"))

    form = LoginForm()
    if request.method == "POST":
        # grab user data first
        email = request.form.get("email")
        password = request.form.get("password")

        # check the database if it has this user data
        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            # login the user and set their session
            login_user(user)
            # the user exists now we can redirect the user to the dashbord
            return redirect(url_for("view.home_page"))

    return render_template("l.html", form=form)













        




























