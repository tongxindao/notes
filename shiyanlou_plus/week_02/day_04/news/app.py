#!/usr/bin/env python3
#_*_ coding:utf-8 _*_

from datetime import datetime

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

from pymongo import MongoClient


app = Flask(__name__)

app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root@localhost/shiyanlou"

db = SQLAlchemy(app)

mongo_client = MongoClient("127.0.0.1", 27017)
mongodb = mongo_client.shiyanlou
tag_names_collection = mongodb.tag_names


class File(db.Model):
    __tablename__ = "files"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    content = db.Column(db.Text)
    created_time = db.Column(db.DateTime)
    category_id = db.Column(db.Integer,
            db.ForeignKey("categorys.id"))

    category = db.relationship("Category")

    def __init__(self, title, content,
            category, created_time=None):
        self.title = title
        self.content = content
        self.category = category

        if created_time is None:
            created_time = datetime.utcnow()
        self.created_time = created_time

    def add_tag(self, tag_name):
        tag_name_id = str(self.id) + "_" + tag_name
        file_tag = {"_id": tag_name_id, "file_id": self.id, "tag_name": tag_name}
        tag_names_collection.save(file_tag)

    def remove_tag(self, tag_name):
        remove_tag = tag_names_collection.find({"tag_name": tag_name})
        if remove_tag:
            tag_names_collection.remove({"tag_name": tag_name})
        else:
            print("tag not found!")

    @property
    def tags(self):
        tag_name_list = []
        for tag in tag_names_collection.find({"file_id": self.id}):
            tag_name_list.append(tag["tag_name"])
        return tag_name_list


class Category(db.Model):
    __tablename__ = "categorys"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    def __init__(self, name):
        self.name = name


def InsertTestData():
    db.create_all()

    java = Category("Java")
    python = Category("Python")

    file1 = File("Hello Java", "File Content - Java is cool!", java, datetime.utcnow())
    file2 = File("Hello Python", "File Content - Python is cool!", python, datetime.utcnow())

    db.session.add(java)
    db.session.add(python)
    db.session.add(file1)
    db.session.add(file2)
    
    db.session.commit()

    file1.add_tag("tech")
    file1.add_tag("java")
    file1.add_tag("linux")
    file2.add_tag("tech")
    file2.add_tag("python")


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
