from flask_restful import Resource
from flask import request
import re
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token
)
from application.schemas.user_schema import singular_user_schema
from application.schemas.login_schema import single_login_schema
from marshmallow import ValidationError
from application.models.user import User
from application.helpers.general_helpers import (
    get_uuid_for_user,
    verify_password
)

class Register(Resource):

    def post(self):

        # get the json from request
        json_data = request.get_json()

        # check there is any data
        if not json_data:
            return {"message": "No input data provided"}, 400


        try:
            # Validate and deserialize input, including ID fields
            user_data = singular_user_schema.load(json_data)
        except ValidationError as err:
            return err.messages, 422


        new_user = User.regsiter_user(
            username=user_data['username'],
            name=user_data['name'],
            email=user_data['email'],
            password=user_data['password'],
            uuid=get_uuid_for_user()
        )

        # get the json schema
        res = singular_user_schema.dump(new_user)
        res.update({
            'tokens': {
                'access_token': create_access_token(identity=new_user.uuid),
                'refresh_token': create_refresh_token(identity=new_user.uuid)
            }
        })

        # output it with the schema
        return {"message": "User is registered successfully", "data": res}, 201



class Login(Resource):

    def post(self):

        # get the json from request
        json_data = request.get_json()

        # check there is any data
        if not json_data:
            return {"message": "No input data provided"}, 400


        try:
            # Validate and deserialize input, including ID fields
            login_data = single_login_schema.load(json_data)
        except ValidationError as err:
            return err.messages, 422


        check_user = ''
        user = None

        if not re.match(r'[^@]+@[^@]+\.[^@]+', login_data['user']):
            check_user = 'username'
        else:
            check_user = 'email'


        if check_user == 'username':
            user = User.query.filter_by(username=login_data['user']).first()

            if user is None:
                return {'user':['username is not exists.']}, 422

        if check_user == 'email':
            user = User.query.filter_by(email=login_data['email']).first()

            if user is None:
                return {'user':['Email is not exists.']}, 422
                
        
        if not verify_password(login_data['password'], user.password):
            
            return {'user': ['Invalid username or password']}, 422
            

        # get the json schema
        res = singular_user_schema.dump(user)
        res.update({
            'tokens': {
                'access_token': create_access_token(identity=user.uuid),
                'refresh_token': create_refresh_token(identity=user.uuid)
            }
        })

        # output it with the schema
        return {"message": "User is logedin successfully", "user": res}, 200
