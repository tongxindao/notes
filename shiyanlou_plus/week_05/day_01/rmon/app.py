import urllib
from rmon.app import create_app
from rmon.models import db


app = create_app()

@app.cli.command()
def init_db():

    print("sqlite3 database file is %s".format(
        app.config["SQLALCHEMY_DATABASE_URI"]))
    db.create_all()
