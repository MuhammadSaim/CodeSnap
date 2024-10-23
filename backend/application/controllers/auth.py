from flask import Blueprint
from flask_restful import Api
from application.resources.auth import (
    Register,
    Login
)

# initiate the blueprint
controller = Blueprint('auth', __name__, url_prefix='/api/v1/auth')


# initiate the api
api = Api(controller)

# add resources to the api
api.add_resource(Register, '/register', endpoint='register_resource')
api.add_resource(Login, '/login', endpoint='login_resource')
