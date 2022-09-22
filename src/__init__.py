from flask import Flask

import logging


def create_app(config: dict = None) -> Flask:
    app = Flask(__name__, instance_relative_config=True)

    handler = logging.FileHandler('test.log')
    app.logger.addHandler(handler)
    app.logger.setLevel(logging.DEBUG)

    if config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(config)

    from . import api

    app.register_blueprint(api.bp)

    return app
