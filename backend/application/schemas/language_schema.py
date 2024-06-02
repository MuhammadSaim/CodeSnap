from application.models.language import Language
from application import marshmallow

# define the Langauge schema
class LanguageSchema(marshmallow.SQLAlchemySchema):
    
    # define the meta and register the model
    class Meta:
        model = Language
    
    # define the exposing field
    id   = marshmallow.auto_field()
    name = marshmallow.auto_field()
    

# define the single dump 
singular_lamguage_schema = LanguageSchema()
# define the multiple collection
multiple_language_schema = LanguageSchema(many=True)
    