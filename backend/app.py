from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from backend.config import config
from api import main

db = SQLAlchemy()


def create_app(config_name='development'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)

    app.register_blueprint(main)

    return app

if __name__ == '__main__':
    create_app('development').run()
