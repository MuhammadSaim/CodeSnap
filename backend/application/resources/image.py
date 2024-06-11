from flask_restful import Resource
from application.models.snap import Snap
from flask import send_file
from config import Config
import os

# define the LanguageListResource
class ImageResource(Resource):
    
    # will be initiate for the get request
    def get(self, type, unique_id):
        
        # check the image type according to image type return the image
        if type == 'snap':
            return self.get_snap_image(unique_id)
        
        
        
        # output it with the schema
        return {
            "message": "No image found"
        }, 404
    
    
    
    def get_snap_image(self, unique_id):
        
        # fetch all the themes from the DB
        snap = Snap.get_by_id(unique_id)
        
        if not snap:
            return {
                "message": "No image found"
            }, 404
        
        # find the absolute path of the file
        file  = os.path.join(Config.BASE_DIR, snap.snap)
        
        # check if there is a file in drectory
        if not os.path.exists(file):
            return {
                "message": "No image found"
            }, 404
        
        # return the file
        return send_file(file)
        