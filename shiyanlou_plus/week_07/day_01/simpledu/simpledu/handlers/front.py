from flask import flash
from flask import url_for
from flask import redirect
from flask import Blueprint
from flask import render_template
from flask_login import login_user
from flask_login import logout_user
from flask_login import login_required

from simpledu.models import User
from simpledu.models import Course
from simpledu.forms import LoginForm
from simpledu.forms import RegisterForm


front = Blueprint("front", __name__)


@front.route("/")
def index():
    courses = Course.query.all()
    return render_template("index.html", courses=courses)


@front.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        login_user(user, form.remember_me.data)
        return redirect(url_for(".index"))
    return render_template("login.html", form=form)


@front.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    print(form.errors)
    if form.validate_on_submit():
        print("here is create_user")
        form.create_user()
        flash("注册成功，请登录！", "success")
        return redirect(url_for(".login"))
    print("register fail.........")
    return render_template("register.html", form=form)


@front.route("/logout")
@login_required
def logout():
    logout_user()
    flash("您已经退出登录", "success")
    return redirect(url_for(".index"))
