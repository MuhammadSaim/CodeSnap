from application.models.language import Language
from marshmallow import fields
from marshmallow_sqlalchemy import SQLAlchemySchema

# define the Langauge schema
class LanguageSchema(SQLAlchemySchema):
    
    # define the meta and register the model
    class Meta:
        model = Language
    
    # define the exposing field
    id   = fields.Integer()
    name = fields.String(required=True)
    

# define the single dump 
singular_lamguage_schema = LanguageSchema()
# define the multiple collection
multiple_language_schema = LanguageSchema(many=True)
    