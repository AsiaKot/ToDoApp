from flask import Flask
from flask_sqlalchemy import SQLAlchemy


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object("config.Config")

    from app.server import SERVER_BLUEPRINT
    app.register_blueprint(SERVER_BLUEPRINT)

    return app


def create_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db = SQLAlchemy(app)
    return db



