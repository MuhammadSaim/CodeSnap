from flask import Blueprint
from application import db
from pygments.styles import get_all_styles
from application.models.theme import Theme
from application.models.snap import Snap
from application.models.language import Language
from sqlalchemy.sql.expression import func
from application.helpers.general_helpers import (
        generate_image, 
        generate_unique_id,
        get_supported_languages
    )
from config import Config
from pathlib import Path
import os

# initiate the bluerint
controller = Blueprint("seeders", __name__)

# initialize the command
@controller.cli.command("all")
def seeders_all():
    clear_all_tables()
    language_seeder()
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
        language = Language.query.order_by(func.random()).first()
        snap = Snap(
            theme_id=theme.id,
            language_id=language.id,
            unique_code=generate_unique_id(model=Snap),
            snap=generate_image(600, 400),
        )
        db.session.add(snap)
    db.session.commit()
    
# language seeder to add language
def language_seeder():
    print("Inserting language\n")
    for lang in get_supported_languages():
        language = Language(
            name=lang
        )
        db.session.add(language)
    db.session.commit()
    

# remove all the snap images from the directory
def remove_snaps_in_dir():
    for f in Path(os.path.join(Config.BASE_DIR, Config.UPLOAD_FOLDER)).glob('*.png'):
        try:
            f.unlink()
        except OSError as e:
            print("Error: %s : %s" % (f, e.strerror))

# clear all the tables
def clear_all_tables():
    print("Deleting Language table data.\n")
    db.session.query(Language).delete()
    print("Deleting Theme table data.\n")
    db.session.query(Theme).delete()
    print("Deleting Snap table data.\n")
    db.session.query(Snap).delete()
    db.session.commit()
    remove_snaps_in_dir()
    