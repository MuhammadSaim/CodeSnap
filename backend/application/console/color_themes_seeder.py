from flask import Blueprint

controller = Blueprint("seeders", __name__)


@controller.cli.command("theme")
def seeder():
    print("Theme seeder running")
