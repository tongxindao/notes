#!/usr/bin/env python3
#_*_ coding:utf-8 _*_

from datetime import datetime

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root@localhost/shiyanlou"

db = SQLAlchemy(app)


class File(db.Model):
    __tablename__ = "files"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    content = db.Column(db.Text)
    created_time = db.Column(db.DateTime)
    category_id = db.Column(db.Integer,
            db.ForeignKey("category.id"))

    category = db.relationship("Category")

    def __init__(self, title, content,
            category, created_time=None):
        self.title = title
        self.content = content
        self.category = category

        if created_time is None:
            created_time = datetime.utcnow()
        self.created_time = created_time


class Category(db.Model):
    __tablename__ = "categorys"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    def __init__(self, name):
        self.name = name


@app.route("/")
def index():
    return render_template("index.html",
            title=File.query.all())


@app.route("/files/<file_id>")
def file(file_id):
    return render_template("file.html",
            news=File.query.get_or_404(file_id))

    
@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(port=3000, debug=True)
