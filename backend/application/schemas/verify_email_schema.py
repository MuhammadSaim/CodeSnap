from flask_marshmallow.sqla import SQLAlchemySchema
from marshmallow import fields

class VerifyEmailSchema(SQLAlchemySchema):

    email = fields.Email(required=True)
    token = fields.String(required=True)


single_verify_email_schema = VerifyEmailSchema()