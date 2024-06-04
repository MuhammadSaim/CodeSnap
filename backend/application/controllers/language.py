from flask import Blueprint
from application.models.language import Language
from application.schemas.language_schema import multiple_language_schema

# initiate the blueprint
controller = Blueprint('language', __name__, url_prefix='/api/v1')

# make route on the blueprint
@controller.route('/languages', methods=['GET'])
def index():
    
    # get all the languages from DB
    languages = Language.get_all()
    
    return multiple_language_schema.dump(languages), 200
    