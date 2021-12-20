from flask import Flask

from app.db import DB


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object("config.Config")

    from app.server import SERVER_BLUEPRINT

    app.register_blueprint(SERVER_BLUEPRINT)

    DB.init_app(app)
    with app.app_context():
        DB.create_all()
    return app
