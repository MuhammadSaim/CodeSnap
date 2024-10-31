from application import db

class PasswordResetToken(db.Model):

    __tablename__ = 'password_reset_tokens'

    email = db.Column(
        db.String(255),
        nullable=False,
        primary_key=True
    )

    token = db.Column(
        db.String(255)
    )

    created_at = db.Column(
        db.DateTime,
        nullable=True
    )
