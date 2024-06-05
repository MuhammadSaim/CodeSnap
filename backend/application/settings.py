from flask import Flask
from config import Config

from application import (
    db,
    migrate,
    marshmallow,
    cors
)


# register all the blueprints here
def register_blueprints(app):
    from application.controllers import (
        snap,
        language,
        theme
    )

    app.register_blueprint(snap.controller)
    app.register_blueprint(language.controller)
    app.register_blueprint(theme.controller)


# register all the cli blueprints here
def register_commands(app):
    from application.console import (
        seeders_all
    )

    app.register_blueprint(seeders_all.controller)


# if there is 3rd party plugins will be setup here
def initialize_plugins(app):
    # Initialize Plugins
    db.init_app(app)
    migrate.init_app(app, db)
    marshmallow.init_app(app)
    cors.init_app(app, origins=Config.ALLOWED_ORIGINS.split(','))


# import all the models here
def import_models():
    # import database models
    from application.models import (
        language,
        theme,
        snap,
    )
    
# import all the schemas here
def import_schemas():
    # import marshmallow schemas
    from application.schemas import (
        snap_schema,
        language_schema,
        theme_schema
    )


# import all the resources here
def import_resources():
    # import flask restfull resources
    from application.resources import (
        theme_list
    )


# initialize the flask app and setup the configs
def initialize_flask_app():
    # Initialize the core application.
    app = Flask(
        __name__,
        instance_relative_config=False
    )
    app.config.from_object('config.Config')
    return app
