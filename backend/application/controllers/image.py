from flask import Blueprint
from application.resources.image import ImageResource
from flask_restful import Api

# initiate the blueprint
controller = Blueprint('image', __name__, url_prefix='/images')

# initiate the api
api = Api(controller)

# add resources to the api
api.add_resource(ImageResource, '/<string:type>/<string:unique_id>', endpoint='image_resource')
    