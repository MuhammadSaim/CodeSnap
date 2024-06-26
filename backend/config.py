import os
from os import environ


# Config for the production app 
class Config:
    # General Config
    SECRET_KEY = environ.get('SECRET_KEY')
    FLASK_APP = environ.get('FLASK_APP')
    FLASK_DEBUG = environ.get('FLASK_DEBUG')

    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    
    ALLOWED_ORIGINS = environ.get('ALLOWED_ORIGINS')

    # Flask-SQLAlchemy
    SQLALCHEMY_DATABASE_URI = environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = bool(environ.get('SQLALCHEMY_TRACK_MODIFICATIONS'))
    
    # Static Assets
    STATIC_FOLDER_PATH = environ.get('STATIC_FOLDER_PATH')
    STATIC_FOLDER = environ.get('STATIC_FOLDER')
    UPLOAD_FOLDER = environ.get('UPLOAD_FOLDER')
    

# Config for the Test environment
class TestConfig(Config):
    
    TESTING = True
    
    # Flask-SQLAlchemy
    SQLALCHEMY_DATABASE_URI = environ.get('TEST_SQLALCHEMY_DATABASE_URI')
    
