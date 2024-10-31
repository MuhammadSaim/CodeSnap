from flask import Blueprint
from flask_restful import Api
from application.resources.theme_list import ThemeListResource

# initiate the blueprint
controller = Blueprint('theme', __name__, url_prefix='/api/v1')

# init flask restfull
api  = Api(controller)

# add resource to the api
api.add_resource(ThemeListResource, '/themes')