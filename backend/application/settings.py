from flask import Flask

from application import (
    db,
    migrate
)


# register all the blueprints here
def register_blueprints(app):
    from application.controllers import (
        test
    )

    app.register_blueprint(test.controller)


# if there is 3rd party plugins will be setup here
def initialize_plugins(app):
    # Initialize Plugins
    db.init_app(app)
    migrate.init_app(app, db)


# import all the models here
def import_models():
    # import database models
    from application.models import (
        snap,
        theme
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
