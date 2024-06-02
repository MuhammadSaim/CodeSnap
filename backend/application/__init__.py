from dotenv import load_dotenv
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from flask_marshmallow import Marshmallow

# load the env file
load_dotenv()

# DB conventions for the keys
convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(column_0_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

# register these keys
metadata = MetaData(naming_convention=convention)

# initiate the SQLAlchemy and pass the metadata
db = SQLAlchemy(metadata=metadata)

# initiate the migrate
migrate = Migrate()

# initiate marshmallow
marshmallow = Marshmallow()


# a function load all the applictaion parts
# plugins, models and blueprints
def create_app():
    from application.settings import (
        initialize_flask_app,
        initialize_plugins,
        import_models,
        register_blueprints,
        register_commands,
        import_schemas
    )

    # initialize the flask app
    app = initialize_flask_app()

    with app.app_context():
        # initialize plugins
        initialize_plugins(app)

        # register blueprints
        register_blueprints(app)

        # register commands
        register_commands(app)

        # import models
        import_models()
        
        # import schemas
        import_schemas()

        return app
