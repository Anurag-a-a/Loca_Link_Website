# config.py

class Config:
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'your-secret-key'
    DATABASE_URI = 'mysql://user:password@localhost/database'
    DB_HOST = 'localhost'
    DB_USER = 'root'
    DB_PASSWORD = 'rootroot'
    DB_NAME = 'team20'

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DATABASE_URI = 'mysql://user:password@production-server/database'

class TestingConfig(Config):
    TESTING = True
