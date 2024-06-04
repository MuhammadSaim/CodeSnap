from flask import Blueprint
from application.resources.language_list import LanguageListResource
from flask_restful import Api

# initiate the blueprint
controller = Blueprint('language', __name__, url_prefix='/api/v1')

# initiate the api
api = Api(controller)

# add resources to the api
api.add_resource(LanguageListResource, '/languages')
    