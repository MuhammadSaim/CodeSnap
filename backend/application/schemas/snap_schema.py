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
        ordered = True
        fields = ('unique_code', 'image_base64', 'language', 'theme', 'created_at')
    
    # define fields
    unique_code     = fields.Str(attribute='unique_code', data_key='id')
    image_base64    = fields.Str(attribute='image_base64', data_key='snap')
    language        = fields.Nested(LanguageSchema, only=('name',))
    theme           = fields.Nested(ThemeSchema, only=('name',))
    created_at      = fields.DateTime(attribute='created_at', data_key='date_time')
    

# define for single dump
singular_snap_schema = SnapSchema()
# define for collection
multiple_snap_schema = SnapSchema(many=True)
