from flask_restful import Resource
from flask import request
from application.models.snap import Snap
from application.models.language import Language
from application.models.theme import Theme
from application.schemas.snap_schema import singular_snap_schema
from marshmallow import ValidationError

# define the ThemeListResource
class SnapListResource(Resource):
    
    # will be initiate for the get request
    def post(self):
        
        # get the json from request
        json_data = request.get_json()
        
        # check there is any data
        if not json_data:
            return {"message": "No input data provided"}, 400
    
        try:
            # Validate and deserialize input, including ID fields
            snap_data = singular_snap_schema.load(json_data)
        except ValidationError as err:
            return err.messages, 422
        
        # validate the language 
        lang = Language.get_by_id(snap_data['language_id'])
        if not lang:
            return {"message": "Invalid language_id"}, 400
        
        # validate the theme 
        theme = Theme.get_by_id(snap_data['theme_id'])
        if not theme:
            return {"message": "Invalid theme_id"}, 400
        
        print(snap_data)
        
        # create a snap
        new_snap = Snap.create(
            snap=snap_data['snap'],
            language=lang,
            theme=theme
        )
        
        # get the json schema
        res = singular_snap_schema.dump(new_snap)
        
        # output it with the schema
        return {"message": "Snap created successfully", "data": res}, 201
        