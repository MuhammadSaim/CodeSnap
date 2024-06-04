from flask import Blueprint
from flask_restful import Api
from application.resources.snap import SnapResource

# initiate the blueprint
controller = Blueprint('snap', __name__, url_prefix='/api/v1')

# initiate the api
api = Api(controller)

# add resource to the api
api.add_resource(SnapResource, '/snaps/<string:id>')
