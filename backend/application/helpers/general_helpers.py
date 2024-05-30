from faker import Faker
import base64
from PIL import Image
import io
import random



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
def generate_unique_id(length=11):
    chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-_'
    chars_len = len(chars)
    id = ''.join(random.choice(chars) for _ in range(length))
    return id