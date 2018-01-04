# -*- coding: utf-8 -*-

from flask import Blueprint
from flask import render_template

from simpledu.models import User


user = Blueprint("user", __name__, url_prefix="/user")

@user.route("/<username>")
def index(username):
    users = User.query.filter_by(username=username).first_or_404()
    return render_template("user.html", users=users)
