from flask import Flask

from app.main.routes import main
from app.errors.routes import errors

def create_app():
    app = Flask(__name__)

    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app

