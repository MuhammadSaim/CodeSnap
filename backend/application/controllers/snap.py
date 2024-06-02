from flask import Blueprint, jsonify
from application.models.snap import Snap

# initiate the blueprint
controller = Blueprint('test', __name__, url_prefix='/api/v1')

# make route on that blue print 
@controller.route('/<unique_id>', methods=['GET'])
def index(unique_id):
    
    # get the snap against unique_code
    snap = Snap.query.filter_by(unique_code=unique_id).first()
    
    # check if snap exists or not
    if not snap:
        return jsonify({
            "message": "Sorry.! snap is not found."
        }), 404
    
    # return the snap records
    return jsonify({
        "snap" : {
            "theme": snap.theme.name,
            "language": snap.language.name,
            "image": snap.image_base64
        }
    }), 200