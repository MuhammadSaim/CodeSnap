from application import db
from application.models.theme import Theme
from application.models.language import Language


# define the Snap model
class Snap(db.Model):

    __tablename__ = 'snaps'

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    theme_id = db.Column(
        db.Integer,
        db.ForeignKey(
            'themes.id',
            ondelete='CASCADE',
            onupdate='CASCADE'
        ),
        nullable=False,
        
    )
    
    language_id = db.Column(
        db.Integer,
        db.ForeignKey(
            'languages.id',
            ondelete='CASCADE',
            onupdate='CASCADE'
        ),
        nullable=False,   
    )

    unique_code = db.Column(
        db.String(255),
        unique=True,
        nullable=False
    )

    image_base64 = db.Column(
        db.Text,
        nullable=False,
    )

    created_at = db.Column(
        db.DateTime,
        server_default=db.func.now(),
        nullable=False
    )

    updated_at = db.Column(
        db.DateTime,
        server_default=db.func.now(),
        nullable=False
    )

    theme = db.relationship(Theme)
    language = db.relationship(Language)
    
    # class method for getting all the records
    @classmethod
    def get_all(cls):
        return cls.query.all()
    
    # class method for find by id
    @classmethod
    def get_by_id(cls, code):
        return cls.query.filter_by(unique_code=code).first()
