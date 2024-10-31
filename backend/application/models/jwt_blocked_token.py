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

    def __init__(self, user_id: int, jti: str, token_type: str):
        self.user_id = user_id
        self.jti = jti
        self.type = token_type

    @classmethod
    def add_token(cls, user_id: int, jti: str, token_type: str):

        new_token = cls(user_id, jti, token_type)
        db.session.add(new_token)
        db.session.commit()