#!/usr/bin/env python3
#_*_ coding:utf-8 _*_

import os
import json
from flask import Flask, render_template, abort


app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True


class File(object):
    json_dir = os.path.join(os.path.abspath(".."), "files/")

    def __init__(self):
        self._files = self._get_all_news_info()

    def get_news_list(self):
        return [item.split(".")[0] for item in os.listdir(self.json_dir)]

    def get_news_info_by_filename(self, filename):
        return self._files.get(filename)

    def _get_all_news_info(self):
        json_news_info = {}

        for news_title in self.get_news_list():
            with open(os.path.join(self.json_dir, news_title+".json")) as file:
                json_news_info[news_title] = json.load(file)

        return json_news_info


files = File()


@app.route("/")
def index():
    return render_template("index.html",
        json_news=files.get_news_list())


@app.route("/files/<filename>")
def file(filename):
    json_news = files.get_news_info_by_filename(filename)

    if not json_news:
        abort(404)

    return render_template("file.html",
        json_news=json_news)

    
@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(port=3000, debug=True)
