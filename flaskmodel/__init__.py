from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

from .main.routes import main
from .errors.routes import errors
from .users.routes import users

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'senha_muito_segura'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco_de_dados.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    bootstrap = Bootstrap(app) 

    db = SQLAlchemy(app)

    app.register_blueprint(main)
    app.register_blueprint(errors)
    app.register_blueprint(users)

    return app

