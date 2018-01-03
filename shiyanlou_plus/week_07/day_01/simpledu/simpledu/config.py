# -*- coding: utf-8 -*-


class BaseConfig(object):
    SECRET_KEY = "makesure to set a very secret key"
    ADMIN_PER_PAGE = 15


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    INDEX_PER_PAGE = 9
    SQLALCHEMY_DATABASE_URI = "mysql+mysqldb://root@localhost:3306/simpledu?charset=utf8"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(BaseConfig):
    pass


class TestingConfig(BaseConfig):
    pass


configs = {
    "development" : DevelopmentConfig,       
    "production" : ProductionConfig,       
    "testing" : TestingConfig,       
}
