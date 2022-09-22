from flask import Flask

import logging


def create_app(config: dict = None) -> Flask:
    app = Flask(__name__, instance_relative_config=True)

    # configure
    # ...
    handler = logging.FileHandler('test.log')   # creates handler for the log file
    app.logger.addHandler(handler)              # adds handler to the werkzeug WSGI logger
    app.logger.setLevel(logging.DEBUG)          # Set the log level to debug

    if config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(config)

    from . import api

    app.register_blueprint(api.bp)

    return app
