import urllib
from rmon.app import create_app
from rmon.models import db


app = create_app()

@app.cli.command()
def routes():
    output = []

    for rule in app.url_map.iter_rules():
        methods = ",".join(rule.methods)
        line = urllib.parse.unquote("{:25s} {:35s} {:20s}".format(
            rule.endpoint, methods, str(rule)))
        output.append(line)

    for line in sorted(output):
        print(line)


@app.cli.command()
def init_db():
    print("sqlite3 database file is %s" %
            app.config["SQLALCHEMY_DATABASE_URI"])
    db.create_all()
