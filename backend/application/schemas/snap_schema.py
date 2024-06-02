from application import marshmallow
from marshmallow_sqlalchemy import SQLAlchemySchema
from application.models.snap import Snap
from marshmallow import fields
from application.schemas.theme_schema import ThemeSchema
from application.schemas.language_schema import LanguageSchema

# define the schema for the class
class SnapSchema(SQLAlchemySchema):
    
    # define meta class
    class Meta:
        model = Snap
    
    # define fields
    unique_code     = marshmallow.auto_field()
    image_base64    = marshmallow.auto_field()
    language        = fields.Nested(LanguageSchema)
    theme           = fields.Nested(ThemeSchema)
    

# define for single dump
singular_snap_schema = SnapSchema()
# define for collection
multiple_snap_schema = SnapSchema(many=True)
