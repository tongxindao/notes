import os
import json
from flask import Flask


def create_app():

    app = Flask("rmon")
    env = os.environ.get("RMON_CONFIG")
    content = ""

    if env:
        with open(env) as f:
            for line in f:
                if "#" not in line:
                    content += line

    if content:
        config = json.loads(content)

        for item in config:
            app.config[item.upper()] = config[item]
        
    return app


if __name__ == "__main__":
    create_app()
