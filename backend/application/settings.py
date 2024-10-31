from flask import Flask
from config import Config

from application import (
    db,
    migrate,
    marshmallow,
    cors,
    jwt,
    mail
)


# register all the blueprints here
def register_blueprints(app):
    from application.controllers import (
        snap,
        language,
        theme,
        image,
        auth
    )

    app.register_blueprint(snap.controller)
    app.register_blueprint(language.controller)
    app.register_blueprint(theme.controller)
    app.register_blueprint(image.controller)
    app.register_blueprint(auth.controller)


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
    jwt.init_app(app)
    mail.init_app(app)


# import all the models here
def import_models():
    # import database models
    from application.models import (
        language,
        theme,
        snap,
        user,
        jwt_blocked_token,
        password_reset_token
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
        theme_list,
        snap_list,
        snap,
        language_list,
        image,
        auth
    )


# initialize the flask app and set up the configs
def initialize_flask_app(config_class):
    # Initialize the core application.
    app = Flask(
        __name__,
        instance_relative_config=False,
        template_folder=Config.TEMPLATES_FOLDER
    )
    app.config.from_object(f'config.{config_class}')
    return app
