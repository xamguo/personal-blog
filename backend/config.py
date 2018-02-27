import os

class Config:
    SECRET_KEY = 'just a test key'

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test'

config = {
    'development': 'config.DevelopmentConfig'
}
