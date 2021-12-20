from flask import Flask
from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object("config.Config")

    from app.server import SERVER_BLUEPRINT

    app.register_blueprint(SERVER_BLUEPRINT)

    db = SQLAlchemy(app)
    db.create_all()
    return app
