from datetime import datetime, timedelta
import random
from flask_mail import Message
from flask_restful import Resource
from flask import request, render_template

from application.models.jwt_blocked_token import JWTBlockedToken
from application.schemas.reset_password_schema import single_reset_password_schema
from config import Config
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_required,
    current_user,
    decode_token,
    get_jwt
)
from application.schemas.user_schema import singular_user_schema
from application.schemas.login_schema import single_login_schema
from application.schemas.forgot_password_schema import single_forget_password_schema
from application.schemas.verify_email_schema import single_verify_email_schema
from marshmallow import ValidationError
from application.models.user import User
from application.helpers.general_helpers import (
    get_uuid_for_user,
    verify_password,
    create_password_hash,
    determine_login_type,
    random_string
)
from application import (
    mail,
    db
)
from application.models.password_reset_token import PasswordResetToken

# register resource allow user to register
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

        token = random_string(64)

        new_user = User.register_user(
            username=user_data['username'],
            name=user_data['name'],
            email=user_data['email'],
            password=user_data['password'],
            uuid=get_uuid_for_user(),
            remember_token=token
        )


        link = '{url}?token={token}'.format(
            url=Config.FRONTEND_URL,
            token=token
        )

        msg = Message(
            subject='Email verification',
            recipients=[new_user.email],
            html=render_template('emails/verify_email.html', verification_link=link)
        )
        mail.send(msg)

        # get the json schema
        res = singular_user_schema.dump(new_user)
        res.update({
            'tokens': {
                'access_token': create_access_token(identity=new_user),
                'refresh_token': create_refresh_token(identity=new_user)
            }
        })

        # output it with the schema
        return {"message": "User is registered successfully", "data": res}, 201


# allow user to login
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


        user = ''
        check_user = determine_login_type(login_data['user'])

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
                'access_token': create_access_token(identity=user),
                'refresh_token': create_refresh_token(identity=user)
            }
        })

        # output it with the schema
        return {"message": "User is log in successfully", "user": res}, 200


# allow user to forget password
class ForgetPassword(Resource):

    def post(self):
        # get the json from request
        json_data = request.get_json()

        # check there is any data
        if not json_data:
            return {"message": "No input data provided"}, 400

        try:
            # Validate and deserialize input, including ID fields
            login_data = single_forget_password_schema.load(json_data)
        except ValidationError as err:
            return err.messages, 422


        user_type = determine_login_type(login_data['user'])

        user = None

        if user_type == 'username':
            user = User.query.filter_by(username=login_data['user']).first()

            if user is None:
                return {'user':['username is not exists.']}, 422

        if user_type == 'email':
            user = User.query.filter_by(email=login_data['email']).first()

            if user is None:
                return {'user':['Email is not exists.']}, 422

        token = random_string(
            random.randint(
                random.randint(80, 100),
                random.randint(200, 220)
            )
        )

        check_reset = PasswordResetToken.query.filter_by(email=user.email).first()
        if check_reset:
            db.session.delete(check_reset)
            db.session.commit()

        reset_password = PasswordResetToken()
        reset_password.email = user.email
        reset_password.token = token
        reset_password.created_at = datetime.now()
        db.session.add(reset_password)
        db.session.commit()

        reset_url = '{url}?token={token}&email={email}'.format(
            url=Config.FRONTEND_URL,
            token=token,
            email=user.email
        )

        msg = Message(
            subject="Reset Password CodeSnap",
            recipients=[user.email],
            html=render_template('emails/reset_password.html', reset_link=reset_url)
        )

        mail.send(msg)

        return {
            'message': 'Email is sent to your email address.'
        }, 200


# reset password
class ResetPassword(Resource):
    def post(self):

        # get the json from request
        json_data = request.get_json()

        # check there is any data
        if not json_data:
            return {"message": "No input data provided"}, 400

        try:
            # Validate and deserialize input, including ID fields
            reset_data = single_reset_password_schema.load(json_data)
        except ValidationError as err:
            return err.messages, 422

        check = PasswordResetToken.query.filter_by(
            email=reset_data['email'],
            token=reset_data['token']
        ).first()

        if check:

            date = check.created_at + timedelta(minutes=15)

            if date < datetime.now():
                return {"message": "Reset password link is expired."}, 500

        else:
            return {"message": "Reset password link is expired."}, 500

        user = User.query.filter_by(email=check.email).first()
        user.password = create_password_hash(reset_data['password'])
        db.session.delete(check)
        db.session.commit()

        return {
            'message': 'Your password is reset successfully.'
        }, 200


# verify the email
class VerifyEmail(Resource):
    @jwt_required()
    def post(self):

        if current_user.email_verified_at is not None:
            return {
                'message': 'Your email is verified already.'
            }, 400

        # get the json from request
        json_data = request.get_json()

        # check there is any data
        if not json_data:
            return {"message": "No input data provided"}, 400

        try:
            # Validate and deserialize input, including ID fields
            verify_data = single_verify_email_schema.load(json_data)
        except ValidationError as err:
            return err.messages, 422

        if current_user.remember_token != verify_data['token'] and current_user.email != verify_data['email']:
            return {
                'message': 'Sorry this link is invalid or expired.'
            }, 400

        user = User.query.filter_by(id=current_user.id).first()
        user.email_verified_at = datetime.now()
        db.session.commit()

        return {
            'message': 'Your email is verified successfully.'
        }, 200

# resend the email verification link
class ResendEmailVerificationLink(Resource):

    @jwt_required()
    def get(self):
        if current_user.email_verified_at is not None:
            return {
                'message': 'Your email is verified already.'
            }, 400

        token = random_string(64)

        link = '{url}?token={token}'.format(
            url=Config.FRONTEND_URL,
            token=token
        )

        msg = Message(
            subject='Email verification',
            recipients=[current_user.email],
            html=render_template('emails/verify_email.html', verification_link=link)
        )
        mail.send(msg)

        User.query.filter_by(id=current_user.id).update({
            'remember_token': token
        })
        db.session.commit()

        return {
            'message': 'Verification link is sent to an email.'
        }, 200


# refresh the token
class RefreshToken(Resource):

    @jwt_required(refresh=True)
    def post(self):
        # generate a new access token
        access_token = create_access_token(identity=current_user)

        return {
            'access_token': access_token
        }, 200


# logout the user
class Logout(Resource):

    @jwt_required()
    def post(self):
        # get the json from request
        json_data = request.get_json()

        # get the access token details
        access_token = get_jwt()

        # check there is any data
        if not json_data:
            return {"message": "No input data provided"}, 400

        # check refresh token is there in data
        if 'refresh_token' not in json_data:
            return {
                'message': 'Refresh token has to be submit'
            }, 400

        refresh_token = decode_token(json_data['refresh_token'])

        access_jwt_blocked_tokens = JWTBlockedToken.add_token(current_user.id, access_token['jti'], access_token['type'])
        refresh_jwt_blocked_tokens = JWTBlockedToken.add_token(current_user.id, refresh_token['jti'], refresh_token['type'])

        return {
            'message': 'You are logged in successfully.'
        }, 200


