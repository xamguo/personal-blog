from flask import Flask
from config import config
from api import main

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    # Q ?what is this for? config[config_name].init_app(app)

    app.register_blueprint(main)

    return app


if __name__ == '__main__':
    create_app('development').run()
