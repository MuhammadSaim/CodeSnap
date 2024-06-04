from flask_restful import Resource
from application.models.language import Language
from application.schemas.language_schema import multiple_language_schema

# define the LanguageListResource
class LanguageListResource(Resource):
    
    # will be initiate for the get request
    def get(self):
        # fetch all the themes from the DB
        langauges = Language.get_all()
        # output it with the schema
        return multiple_language_schema.dump(langauges), 200
