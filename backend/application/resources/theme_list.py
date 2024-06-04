from flask_restful import Resource
from application.models.theme import Theme
from application.schemas.theme_schema import multiple_theme_Schema

# define the ThemeListResource
class ThemeListResource(Resource):
    
    # will be initiate for the get request
    def get(self):
        # fetch all the themes from the DB
        themes = Theme.get_all()
        # output it with the schema
        return multiple_theme_Schema.dump(themes), 200
        