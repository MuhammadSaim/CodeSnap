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

# initiate faker
faker = Faker()

# Generate a fake image using Pillow (Python Imaging Library)
def generate_fake_image(width, height):
    image = Image.new('RGB', (width, height), faker.color_rgb())
    return image

# Convert PIL image to base64 string
def pil_image_to_base64(image):
    buffered = io.BytesIO()
    image.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode('utf-8')

# Generate a fake image and convert it to base64
def generate_base64_image(width, height):
    fake_image = generate_fake_image(width, height)
    base64_image = pil_image_to_base64(fake_image)
    return base64_image

# generate user friendly unique id 
def generate_unique_id(model, length=11):
    chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-_'
    id = ''.join(random.choice(chars) for _ in range(length))
    check = model.query.filter_by(unique_code=id).first()
    if check:
        return generate_unique_id()
    return id

# supported languages from 
def get_supported_languages():
    
    return [
        "Bash", "C", "C#", "C++", "CSS", "Dart", "Elixir", "Erlang", "Fortran", "Go", 
        "Haskell", "HTML", "Java", "JavaScript", "JSON", "Kotlin", "LaTeX", "Lua", 
        "Markdown", "MATLAB", "Objective C", "OCaml", "Perl", "PHP", "PowerShell", 
        "Python", "R", "Ruby", "Rust", "Scala", "Shell", "SQL", "Swift", "Tcl", "TypeScript", 
        "XML", "YAML"
    ]

# validateing the base64 image
def is_base64_image(value):
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
    
    
# generate secure filename
def generate_secure_filename(type = '.png'):
    # Create a unique identifier
    unique_id = uuid.uuid4().hex

    # Create a hash of the filename and current timestamp
    hash_digest = hashlib.sha256((unique_id + str(datetime.now().timestamp())).encode()).hexdigest()
    
    # Construct the new secure filename
    secure_name = f"{hash_digest}{type}"
    return secure_name
    

def base64_file(base64_str):
    
    # Assuming base64_str is the string value without 'data:image/jpeg;base64,'
    img = Image.open(io.BytesIO(base64.decodebytes(bytes(base64_str, "utf-8"))))
    
    new_filename = generate_secure_filename()
    
    file_path = f"{Config.UPLOAD_FOLDER}/{new_filename}"
    
    filepath_to_save = f"assets/uploads/snaps/{new_filename}"
    
    img.save(file_path, quality=100, subsampling=0)
    
    return filepath_to_save
