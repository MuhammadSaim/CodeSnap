from flask_restful import Resource
from application.models.snap import Snap
from application.schemas.snap_schema import singular_snap_schema

# define the LanguageListResource
class SnapResource(Resource):
    
    # will be initiate for the get request
    def get(self, id):
        # fetch all the themes from the DB
        snap = Snap.get_by_id(id)
        
        if not snap:
            return {
                "message": "Snap not found"
            }, 404
        
        # output it with the schema
        return singular_snap_schema.dump(snap), 200
