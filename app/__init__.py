import logging
from logging.handlers import RotatingFileHandler
import os
from flask import Flask, request, current_app
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()

def create_app():
    flaskApp = Flask(__name__)
    flaskApp.config.from_object('config.default_settings')
    bootstrap.init_app(flaskApp)

    if not flaskApp.debug:
        if not os.path.exists('logs'):
            os.mkdir('logs')
        file_handler = RotatingFileHandler('logs/mywebsite.log',
                                           maxBytes=10240, backupCount=10)
        file_handler.setFormatter(
            logging.Formatter("%(asctime)s %(levelname)s:"
                              " %(message)s [in %(pathname)s:%(lineno)d]"))
        file_handler.setLevel(logging.INFO)
        flaskApp.logger.addHandler(file_handler)

        flaskApp.logger.setLevel(logging.INFO)
        flaskApp.logger.info('Config Generator startup')
    return flaskApp


app = create_app()

from app import routes, errors
from util import assets
