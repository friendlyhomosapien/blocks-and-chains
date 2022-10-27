import os
from flask import Flask
from blockchain.config import config
from blockchain.celery import make_celery
from celery import Celery

import logging

celery = Celery(__name__, broker=config.CELERY_BROKER_URL, backend=config.CELERY_RESULT_BACKEND)

def create_app(config_name=None) -> Flask:
    app = Flask(__name__)

    if config_name is None:
        config_name = os.environ.get('FLASK_CONFIG', 'development')

    handler = logging.FileHandler('test.log')   # creates handler for the log file
    app.logger.addHandler(handler)              # adds handler to the werkzeug WSGI logger
    app.logger.setLevel(logging.DEBUG)          # Set the log level to debug

    app.config.from_object(config)

    make_celery(app)

    from . import api

    app.register_blueprint(api.bp)

    return app
