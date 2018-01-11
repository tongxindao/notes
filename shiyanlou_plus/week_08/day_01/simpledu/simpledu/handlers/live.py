# -*- coding: utf-8 -*-
import json

from flask import url_for
from flask import redirect
from flask import Blueprint
from flask import render_template

from simpledu.models import Live

from .ws import redis


live = Blueprint("live", __name__, url_prefix="/live")


@live.route("/")
def index():
    live = Live.query.order_by(Live.created_at.desc()).limit(1).first()
    return render_template("live/index.html", live=live)


@live.route("/<systemmessage>")
def message(systemmessage):
    redis.publish("chat", json.dumps(
        dict(username="新用户加入，总人数为",
            text=systemmessage)))
    return redirect(url_for("admin.message"))
