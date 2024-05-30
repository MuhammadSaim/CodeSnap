from application import db


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

    unique_code = db.Column(
        db.String(255),
        unique=True,
        nullable=False
    )

    image_base64 = db.Column(
        db.Text,
        nullable=False,
    )

    language = db.Column(
        db.String(255),
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

    theme = db.relationship('Theme')
