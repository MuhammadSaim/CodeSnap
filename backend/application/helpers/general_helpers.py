from faker import Faker
import base64
from PIL import Image
import io
import random
import re

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
        if isinstance(value, str) and re.match(r'^data:image/.+;base64,', value):
            base64_str = value.split(',')[1]
            base64.b64decode(base64_str)
        else:
            base64.b64decode(value)
        return True
    except (ValueError, base64.binascii.Error):
        return False

# validator for the Schema
def validate_base64_image(value):
    if not is_base64_image(value):
        raise ValueError("Invalid base64 image")