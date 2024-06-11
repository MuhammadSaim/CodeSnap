from marshmallow_sqlalchemy import SQLAlchemySchema
from application.models.snap import Snap
from marshmallow import fields, validates, ValidationError
from application.helpers.general_helpers import validate_base64_image
from flask import url_for

# define the schema for the class
class SnapSchema(SQLAlchemySchema):
    
    # define meta class
    class Meta:
        model = Snap
        ordered = True
    
    # define fields
    unique_code     = fields.String(attribute='unique_code', data_key='id', dump_only=True)
    snap            = fields.String(required=True, load_only=True)
    language_id     = fields.Integer(required=True, load_only=True)
    theme_id        = fields.Integer(required=True, load_only=True)
    language        = fields.Method('get_the_language', dump_only=True)
    theme           = fields.Method('get_the_theme', dump_only=True)
    snap_dump       = fields.Method('get_the_snap_url', data_key='snap', dump_only=True)
    created_at      = fields.DateTime(attribute='created_at', data_key='date_time', dump_only=True)
    
    # get the language name
    def get_the_language(self, obj):
        return obj.language.name if obj.language else None
    
    # get the theme name
    def get_the_theme(self, obj):
        return obj.theme.name if obj.theme else None
    
    # get the save 
    def get_the_snap_url(self, obj):
        return url_for('image.image_resource', type='snap', unique_id=obj.unique_code, _external=True)
    
    # validate the base64
    @validates('snap')
    def validate_snap(self, value):
        if not validate_base64_image(value):
            raise ValidationError("Invalid base64 image string.")
    

# define for single dump
singular_snap_schema = SnapSchema()
# define for collection
multiple_snap_schema = SnapSchema(many=True)
