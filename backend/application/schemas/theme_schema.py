from application.models.theme import Theme
from marshmallow import fields
from marshmallow_sqlalchemy import SQLAlchemySchema

# define the theme scheam
class ThemeSchema(SQLAlchemySchema):
    
    # define the meta class
    class Meta:
        model = Theme
    
    # define the fields
    id   = fields.Integer()
    name = fields.Str(required=True)

# define the single dump
singular_theme_schema = ThemeSchema()
# define the multiple dump
multiple_theme_Schema = ThemeSchema(many=True)