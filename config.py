class Config(object):
    DEBUG = False
    TESTING = False
    DATABASE_URI = 'sqlite://:memory:'

class ProductionConfig(Config):
    DATABASE_URI = 'mysql://user@localhost/foo'

class DevelopmentConfig(Config):
    DEBUG = True
    DATABASE = r'D:\Python\Python file\Web\flaskr\flaskr\flaskr.db'
    SECRET_KEY = 'development key'
    USERNAME = 'admin'
    PASSWORD = 'admin'

class TestingConfig(Config):
    TESTING = True
