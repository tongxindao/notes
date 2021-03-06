# _*_ coding: utf-8 _*_
import os


class BaseConfig(object):
    SECRET_KEY = str(os.urandom(24))


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql+mysqldb://root@localhost:3306/jobplus?charset=utf8"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(BaseConfig):
    pass


class TestingConfig(BaseConfig):
    pass


configs = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "testing": TestingConfig,
}
