from marshmallow import fields
from marshmallow_sqlalchemy import SQLAlchemySchema

class ForgetPasswordSchema(SQLAlchemySchema):

    user = fields.String(required=True)


single_forget_password_schema = ForgetPasswordSchema()