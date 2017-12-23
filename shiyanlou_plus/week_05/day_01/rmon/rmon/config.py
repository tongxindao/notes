import os

class DevConfig:

    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "sqlite://"
    TEMPLATES_AUTO_RELOAD = True


class ProductConfig(DevConfig):

    DEBUG = False

    path = os.path.join(os.getcwd(), "rmon.db").replace("\\", "/")
    SQLALCHEMY_DATABASE_URI = "sqlite:///%s" % path
