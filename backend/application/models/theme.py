from application import db


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
