import os

class Config:
    SECRET_KEY = 'just a test key'
    SQLALCHEMY_DATABASE_URI = 'mysql://username:password@hostname/database'

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test'

config = {
    'development': Config,
    'second': DevelopmentConfig,
}
