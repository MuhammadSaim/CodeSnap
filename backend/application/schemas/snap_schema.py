from marshmallow_sqlalchemy import SQLAlchemySchema
from application.models.snap import Snap
from marshmallow import fields

# define the schema for the class
class SnapSchema(SQLAlchemySchema):
    
    # define meta class
    class Meta:
        model = Snap
        ordered = True
        # fields = ('unique_code', 'image_base64', 'language_id', 'theme_id', 'created_at')
    
    # define fields
    unique_code     = fields.String(attribute='unique_code', data_key='id', dump_only=True)
    image_base64    = fields.String(data_key='snap', required=True)
    language_id     = fields.Integer(required=True, load_only=True)
    theme_id        = fields.Integer(required=True, load_only=True)
    language        = fields.Method('get_the_language', dump_only=True)
    theme           = fields.Method('get_the_theme', dump_only=True)
    created_at      = fields.DateTime(attribute='created_at', data_key='date_time', dump_only=True)
    
    # get the language name
    def get_the_language(self, obj):
        return obj.language.name if obj.language else None
    
    # get the theme name
    def get_the_theme(self, obj):
        return obj.theme.name if obj.theme else None
    

# define for single dump
singular_snap_schema = SnapSchema()
# define for collection
multiple_snap_schema = SnapSchema(many=True)
