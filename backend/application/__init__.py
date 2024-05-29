from dotenv import load_dotenv

# load the env file
load_dotenv()

# a function load all the applictaion parts
# plugins, models and blueprints
def create_app():
    from application.settings import (
        initialize_flask_app,
        initialize_plugins,
        import_models,
        register_blueprints
    )

    # initialize the flask app
    app = initialize_flask_app()

    with app.app_context():
        # initialize plugins
        initialize_plugins(app)

        # register blueprints
        register_blueprints(app)

        # import models
        import_models()

        return app