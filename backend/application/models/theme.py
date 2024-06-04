from application import db


# define the theme model
class Theme(db.Model):

    __tablename__ = "themes"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(255),
        unique=True,
        nullable=False
    )

    created_at = db.Column(
        db.DateTime,
        default=db.func.now(),
        nullable=True
    )

    updated_at = db.Column(
        db.DateTime,
        default=db.func.now(),
        nullable=True
    )
    
    # class method for getting all the records
    @classmethod
    def get_all(cls):
        return cls.query.all()
    
    # class method for find by id
    @classmethod
    def get_by_id(cls, id):
        return cls.query.filter_by(id=id).first()
