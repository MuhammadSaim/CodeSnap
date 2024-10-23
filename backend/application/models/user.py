from application import db
from typing import Tuple, Optional
from application.helpers.general_helpers import (
    create_password_hash,
    verify_password,
    get_uuid_for_user
)

class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(
        db.Integer,
        primary_key=True
    )
    
    uuid = db.Column(
        db.String(36),
        unique=True
    )

    username = db.Column(
        db.String(255),
        unique=True,
        nullable=False
    )

    name = db.Column(
        db.String(255),
        nullable=False
    )

    email = db.Column(
        db.String(255),
        unique=True,
        nullable=False
    )

    password = db.Column(
        db.String(255),
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

    
    def __init__(self, username: str, name: str, email: str, password: str, uuid: str) -> None:
        self.username = username
        self.email = email
        self.name = name
        self.password = password
        self.uuid = uuid
    

    # register a user
    @classmethod
    def regsiter_user(cls, username: str, name: str, email: str, password: str, uuid: str) -> Optional['User']:
            
        # get a hashed password
        password_hash = create_password_hash(password=password)
        
        
        # create a new user
        new_user = cls(username=username, name=name, email=email, password=password_hash, uuid=uuid)        
        db.session.add(new_user)
        db.session.commit()
        

        return new_user
