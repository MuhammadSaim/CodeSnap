from marshmallow_sqlalchemy import SQLAlchemySchema
from marshmallow import fields, validates, ValidationError, validates_schema


class ResetPasswordSchema(SQLAlchemySchema):

    token = fields.String(required=True)
    email = fields.Email(required=True)
    password = fields.String(required=True)
    confirm_password = fields.String(required=True)

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
            raise ValidationError('Passwords do not match. Please ensure both passwords are the same.',
                                      field_name='password')

single_reset_password_schema = ResetPasswordSchema()