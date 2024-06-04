from application import db

# define the Language model class
class Language(db.Model):
    
    __tablename__ = 'languages'
    
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    
    name = db.Column(
        db.String(255),
        nullable=False
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
    
    # class method for getting all the records
    @classmethod
    def get_all(cls):
        return cls.query.all()
    
    # class method for find by id
    @classmethod
    def get_by_id(cls, id):
        return cls.query.filter_by(id=id).first()
    