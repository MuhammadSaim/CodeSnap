from application import db

class JWTBlockedToken(db.Model):

    __tablename__ = 'jwt_blocked_tokens'

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey(
            'users.id',
            ondelete='CASCADE',
            onupdate='CASCADE'
        ),
        nullable=False,
    )

    jti = db.Column(
        db.String(36),
        nullable=False,
        index=True
    )

    type = db.Column(
        db.String(16),
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
