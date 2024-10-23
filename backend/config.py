import os
from os import environ
from datetime import timedelta


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
    
    
    
    # JWT configs
    
    access_token_expires = environ.get('JWT_ACCESS_TOKEN_EXPIRES')
    refresh_token_expires = environ.get('JWT_REFRESH_TOKEN_EXPIRES')
    
    JWT_SECRET_KEY = environ.get('JWT_SECRET_KEY')
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(
        hours=int(
            access_token_expires
        ) if access_token_expires is not None else 1
    )
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(
        days=float(
            refresh_token_expires
        ) if refresh_token_expires is not None else 30
    )
    

# Config for the Test environment
class TestConfig(Config):
    
    TESTING = True
    
    # Flask-SQLAlchemy
    SQLALCHEMY_DATABASE_URI = environ.get('TEST_SQLALCHEMY_DATABASE_URI')
    
