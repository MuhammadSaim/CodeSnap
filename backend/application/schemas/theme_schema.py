from application.models.theme import Theme
from application import marshmallow

# define the theme scheam
class ThemeSchema(marshmallow.SQLAlchemySchema):
    
    # define the meta class
    class Meta:
        model = Theme
    
    # define the fields
    id   = marshmallow.auto_field()
    name = marshmallow.auto_field()

# define the single dump
singular_theme_schema = ThemeSchema()
# define the multiple dump
multiple_theme_Schema = ThemeSchema(many=True)