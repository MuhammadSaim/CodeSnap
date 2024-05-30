from flask import Blueprint, jsonify

controller = Blueprint('test', __name__)

@controller.route('/snaps', methods=['GET'])
def index():
    return jsonify({
        'message': 'Working'
    })