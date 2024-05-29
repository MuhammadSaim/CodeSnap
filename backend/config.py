import os
from os import environ

class Config:
    # General Config
    SECRET_KEY = environ.get('SECRET_KEY')
    FLASK_APP = environ.get('FLASK_APP')
    FLASK_DEBUG = environ.get('FLASK_DEBUG')

    BASE_DIR = os.path.abspath(os.path.dirname(__file__))