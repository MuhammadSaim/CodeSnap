from application.models.user import User
from marshmallow_sqlalchemy import SQLAlchemySchema
from marshmallow import fields, ValidationError, validates, validates_schema

class LoginSchema(SQLAlchemySchema):

    user = fields.String(required=True)
    password = fields.String(required=True, load_only=True)


# define the single dump
single_login_schema = LoginSchema()
