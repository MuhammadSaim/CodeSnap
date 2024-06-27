import pytest
from application import create_app, db
from application.console.seeders_all import (
    run_seeder,
    clear_all_tables
)

# initialize the testing module for the application
@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app('TestConfig')
    
    print(flask_app.config)

    # Create a test client
    testing_client = flask_app.test_client()

    # Establish an application context
    ctx = flask_app.app_context()
    ctx.push()

    yield testing_client  # This is where the testing happens!

    ctx.pop()


@pytest.fixture(scope='module')
def init_database():
    
    with create_app('TestConfig').app_context():
    
        # Create the database and the database table
        db.create_all()

        try:
            # run the seeders to the test db
            run_seeder()
        except Exception as e:
            print(f"Error in seeders_all: {e}")

        yield db  # This is where the testing happens!

        # clear images in the directory and remove data from the table
        clear_all_tables()

        db.drop_all()
