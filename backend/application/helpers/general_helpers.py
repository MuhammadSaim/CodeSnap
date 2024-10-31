from faker import Faker
import base64
from PIL import Image
import io
import random
import re
import hashlib
import uuid
from datetime import datetime
from config import Config
import bcrypt
from typing import Type, Tuple
import string
from flask import jsonify
from application import (
    db,
    jwt
)
from application.models.jwt_blocked_token import JWTBlockedToken

# initiate faker
faker = Faker()

# Generate a fake image using Pillow (Python Imaging Library)
def generate_fake_image(width: int, height: int) -> Image.Image:
    image = Image.new('RGB', (width, height), faker.color_rgb())
    return image

# Convert PIL image to base64 string
def pil_image_to_base64(image: Image.Image):
    buffered = io.BytesIO()
    image.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode('utf-8')

# Generate a fake image and convert it to base64
def generate_image(width: int, height: int) -> str:
    fake_image = generate_fake_image(width, height)
    base64_image = pil_image_to_base64(fake_image)
    return base64_file(base64_image)

# generate user friendly unique id
def generate_unique_id(model: Type[db.Model], length: int =11) -> str:
    chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-_'
    id = ''.join(random.choice(chars) for _ in range(length))
    check = model.query.filter_by(unique_code=id).first()
    if check:
        return generate_unique_id(model)
    return id

# supported languages from
def get_supported_languages() -> list:

    return [
        "Bash", "C", "C#", "C++", "CSS", "Dart", "Elixir", "Erlang", "Fortran", "Go",
        "Haskell", "HTML", "Java", "JavaScript", "JSON", "Kotlin", "LaTeX", "Lua",
        "Markdown", "MATLAB", "Objective C", "OCaml", "Perl", "PHP", "PowerShell",
        "Python", "R", "Ruby", "Rust", "Scala", "Shell", "SQL", "Swift", "Tcl", "TypeScript",
        "XML", "YAML"
    ]

# validateing the base64 image
def is_base64_image(value: str) -> bool:
    # Check if value is a valid base64 string
    try:
        base64_pattern = re.compile(r'^[A-Za-z0-9+/]*={0,2}$')
        if len(value) % 4 != 0 or not base64_pattern.match(value):
            return False
        try:
            base64.b64decode(value, validate=True)
            return True
        except Exception:
            return False
    except (ValueError, base64.binascii.Error):
        return False

# validator for the Schema
def validate_base64_image(value):
    if not is_base64_image(value):
        raise ValueError("Invalid base64 image")
    return True


# generate secure filename
def generate_secure_filename(type: str = '.png') -> str:
    # Create a unique identifier
    unique_id = uuid.uuid4().hex

    # Create a hash of the filename and current timestamp
    hash_digest = hashlib.sha256((unique_id + str(datetime.now().timestamp())).encode()).hexdigest()

    # Construct the new secure filename
    secure_name = f"{hash_digest}{type}"
    return secure_name


def base64_file(base64_str: str) -> str:

    # Assuming base64_str is the string value without 'data:image/jpeg;base64,'
    img = Image.open(io.BytesIO(base64.decodebytes(bytes(base64_str, "utf-8"))))

    new_filename = generate_secure_filename()

    file_path = f"{Config.UPLOAD_FOLDER}/{new_filename}"

    img.save(file_path, quality=100, subsampling=0)

    return file_path


# create a hash password
def create_password_hash(password: str) -> str:

    # convert the string into bytes
    password_bytes = password.encode()

    # generate a salt
    salt = bcrypt.gensalt(14)

    #calculate hash as a bytes
    password_hash_bytes = bcrypt.hashpw(password_bytes, salt)

    # decode bytes to string
    password_hash_str = password_hash_bytes.decode()

    return password_hash_str


# verify the password is correct
def verify_password(plain_password: str, hash_password: str) -> bool:

    # decode both string password into bytes
    plain_password_bytes = plain_password.encode()
    hash_password_bytes = hash_password.encode()

    return bcrypt.checkpw(plain_password_bytes, hashed_password=hash_password_bytes)


# check that token is revoked or not
@jwt.token_in_blocklist_loader
def check_if_token_revoked(jwt_header, jwt_payload: dict) -> bool:
    jti = jwt_payload['jti']
    token = db.session.query(JWTBlockedToken.id).filter_by(jti=jti).scalar()
    return token is not None


# validate the username
def username_validation(username: str):
    from application.models.user import User

    """
        Validates the username based on the following criteria:
        - Must be between 5 and 20 characters long.
        - Must contain only alphanumeric characters (letters and digits).
        - Cannot contain spaces or special characters.

        :param username: The username to validate.
        :return: True if the username is valid, False otherwise.
    """

    # Check if the username length is between 3 and 20 characters
    if len(username) < 5:
        raise ValueError("Username must be at least 5 characters long.")
    if len(username) > 20:
        raise ValueError("Username must not exceed 20 characters.")


    # Check if the username contains only alphanumeric characters
    if not re.match("^[a-zA-Z0-9]+$", username):
        raise ValueError("Username can only contain letters and numbers (no spaces or special characters).")

    # check username exists in db
    check_db = User.query.filter_by(username=username).first()
    if check_db:
        raise ValueError("Username is already taken.")

    return True


# validate the username
def email_validation(email: str):
    from application.models.user import User

    """
    Validates the email address based on a standard format.

    Criteria:
    - The email should be in the format: local-part@domain.
    - Local part may contain letters, numbers, periods, hyphens, and underscores.
    - Domain should contain letters, numbers, periods, and hyphens.
    - A domain extension of 2-24 characters is allowed (e.g., .com, .co.uk).

    :param email: The email address to validate.
    :return: An error message if the email is invalid, or an empty string if valid.
    """

    # Regular expression for validating email
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,24}$'


    # Check if the email matches the pattern
    if not re.match(email_regex, email):
        raise ValueError("Please provide a valid email.")


    # check username exists in db
    check_db = User.query.filter_by(email=email).first()
    if check_db:
        raise ValueError("Email is already taken.")

    return True


# generate uuid4 for uniquely identify the users
def get_uuid_for_user() -> str:
    import uuid
    from application.models.user import User
    uuid4 = uuid.uuid4()

    user = User.query.filter_by(uuid=uuid4).first()

    if user:
        return get_uuid_for_user()

    return str(uuid4)


# Register a callback function that takes whatever object is passed in as the
# identity when creating JWTs and converts it to a JSON serializable format.
@jwt.user_identity_loader
def user_identity_lookup(user):
    return user.uuid

# Handle invalid token error
@jwt.invalid_token_loader
def custom_invalid_token_callback(reason):
    return jsonify({"error": "invalid_token", "message": reason}), 401

# Handle revoked token error
@jwt.revoked_token_loader
def custom_revoked_token_callback(jwt_header, jwt_payload):
    return jsonify({"error": "revoked_token", "message": "Please log in again"}), 401

# Register a callback function that loads a user from your database whenever
# a protected route is accessed. This should return any python object on a
# successful lookup, or None if the lookup failed for any reason (for example
# if the user has been deleted from the database).
@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    from application.models.user import User
    identity = jwt_data["sub"]
    return User.query.filter_by(uuid=identity).one_or_none()

# Register a callback function that loads when access and refresh token
# is expired
@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_payload):
    token_type = jwt_payload["type"]
    if token_type == "access":
        return jsonify({
            "message": "The access token has expired. Please refresh your token.",
            "error": "access_token_expired"
        }), 401
    elif token_type == "refresh":
        return jsonify({
            "message": "The refresh token has expired. Please log in again.",
            "error": "refresh_token_expired"
        }), 401

# generate a random unique string
def random_string(length: int = 16) -> str :
    letters = string.ascii_lowercase + string.ascii_uppercase + string.digits
    return ''.join(random.choice(letters) for i in range(length))

# determine the login type is username or password
def determine_login_type(login_type: str) -> str:
    if not re.match(r'[^@]+@[^@]+\.[^@]+', login_type):
        return 'username'
    else:
        return 'email'


