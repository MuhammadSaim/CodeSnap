from flask import Blueprint
from flask_restful import Api
from application.resources.auth import (
    Register,
    Login,
    ForgetPassword,
    ResetPassword,
    VerifyEmail,
    ResendEmailVerificationLink,
    RefreshToken,
    Logout
)

# initiate the blueprint
controller = Blueprint('auth', __name__, url_prefix='/api/v1/auth')


# initiate the api
api = Api(controller)

# add resources to the api
api.add_resource(Register, '/register', endpoint='register_resource')
api.add_resource(Login, '/login', endpoint='login_resource')
api.add_resource(ForgetPassword, '/forgot-password', endpoint='forgot_password_resource')
api.add_resource(ResetPassword, '/reset-password', endpoint='reset_password_resource')
api.add_resource(VerifyEmail, '/verify-email', endpoint='verify_email_resource')
api.add_resource(ResendEmailVerificationLink, '/resend-verification-link', endpoint='resend_verify_link_email_resource')
api.add_resource(RefreshToken, '/refresh-token', endpoint='refresh_token_resource')
api.add_resource(Logout, '/logout', endpoint='logout_resource')
