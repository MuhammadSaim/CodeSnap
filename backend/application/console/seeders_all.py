from flask import Blueprint
from application import db
from pygments.styles import get_all_styles
from application.models.theme import Theme
from application.models.snap import Snap
from faker import Faker
from sqlalchemy.sql.expression import func
from application.helpers.general_helpers import generate_base64_image, generate_unique_id

controller = Blueprint("seeders", __name__)


@controller.cli.command("all")
def seeders_all():
    clear_all_tables()
    theme_seeder()
    snaps_seeder()


# theme seeder insert all the supported themes
def theme_seeder():
    print("Inserting themes\n")
    for style in get_all_styles():
        theme = Theme(
            name= style
        )
        db.session.add(theme)
    db.session.commit()
    

# snaps seeder to add snaps
def snaps_seeder():
    print("Inserting snaps\n")
    for _ in range(100):
        theme = Theme.query.order_by(func.random()).first()
        snap = Snap(
            theme_id=theme.id,
            unique_code=generate_unique_id(),
            image_base64=generate_base64_image(600, 400),
            language="Python"
        )
        db.session.add(snap)
    db.session.commit()
    

# clear all the tables
def clear_all_tables():
    print("Deleting Theme table data.\n")
    db.session.query(Theme).delete()
    print("Deleting Snap table data.\n")
    db.session.query(Snap).delete()
    db.session.commit()
    