from application.models.user import User
from marshmallow_sqlalchemy import SQLAlchemySchema
from marshmallow import fields, ValidationError, validates, validates_schema
from application.helpers.general_helpers import (
    username_validation,
    email_validation
)

class UserSchema(SQLAlchemySchema):

    class Meta:
        model = User

    id = fields.String(attribute='uuid', data_key='id', dump_only=True)
    username = fields.String(required=True)
    name = fields.String(required=True)
    email = fields.String(required=True)
    email_verified_at = fields.String(dump_only=True)
    password = fields.String(required=True, load_only=True)
    confirm_password = fields.String(required=True, load_only=True)


    # validate the username
    @validates('username')
    def validate_username(self, username: str):
        try:
            username_validation(username=username)
        except ValueError as e:
            raise ValidationError(str(e))


    # validate the email
    @validates('email')
    def validate_email(self, email: str):
        try:
            email_validation(email=email)
        except ValueError as e:
            raise ValidationError(str(e))


    # validate the password
    @validates('password')
    def validate_password(self, password: str):

        if len(password) < 8:
            raise ValidationError('Password should be greater then 8 chars.')



    # Custom validation for both password and confirm_password
    @validates_schema
    def validate_passwords_match(self, data, **kwargs):
        password = data.get('password')
        confirm_password = data.get('confirm_password')

        if password != confirm_password:
            raise ValidationError('Passwords do not match. Please ensure both passwords are the same.', field_name='password')



# define the single dump
singular_user_schema = UserSchema()
