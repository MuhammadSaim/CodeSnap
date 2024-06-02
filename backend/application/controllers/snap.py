from flask import Blueprint, jsonify
from application.models.snap import Snap
from application.schemas.snap_schema import singular_snap_schema

# initiate the blueprint
controller = Blueprint('test', __name__, url_prefix='/api/v1')

# make route on that blue print 
@controller.route('/<string:unique_id>', methods=['GET'])
def index(unique_id):
    
    # get the snap against unique_code
    snap = Snap.query.filter_by(unique_code=unique_id).first()
    
    # check if snap exists or not
    if not snap:
        return jsonify({
            "message": "Sorry.! snap is not found."
        }), 404
    
    # return the snap records
    return singular_snap_schema.dump(snap), 200
