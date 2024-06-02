from flask import Blueprint
from application.models.theme import Theme
from application.schemas.theme_schema import multiple_theme_Schema

# initiate the blueprint
controller = Blueprint('theme', __name__, url_prefix='/api/v1')

# make route on the blueprint
@controller.route('/themes', methods=['GET'])
def index():
    
    # get all the languages from DB
    themes = Theme.query.all()
    
    return multiple_theme_Schema.dump(themes), 200
    