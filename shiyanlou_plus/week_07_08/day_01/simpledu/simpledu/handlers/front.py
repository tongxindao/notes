# -*- coding: utf-8 -*-

from flask import flash
from flask import url_for
from flask import redirect
from flask import request
from flask import current_app
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
    page = request.args.get("page", default=1, type=int)
    pagination = Course.query.paginate(
        page=page,
        per_page=current_app.config["INDEX_PER_PAGE"],
        error_out=False
    )
    return render_template("index.html", pagination=pagination)


@front.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        login_user(user, form.remember_me.data)
        return redirect(url_for(".index"))
    return render_template("login.html", form=form)


@front.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if not form.username.data.isalnum():
            flash("用户名必须由数字和字母组成")
            return redirect(url_for(".register"))
        form.create_user()
        flash("注册成功，请登录！", "success")
        return redirect(url_for(".login"))
    return render_template("register.html", form=form)


@front.route("/logout")
@login_required
def logout():
    logout_user()
    flash("您已经退出登录", "success")
    return redirect(url_for(".index"))
