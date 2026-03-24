from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.update(
        SECRET_KEY="phase3-dev-key",
        SQLALCHEMY_DATABASE_URI="sqlite:///phase3.db",
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        APP_TITLE="Volunteer Shift Manager",
        APP_SUMMARY="Production-oriented community solution for volunteer shift manager workflows.",
        DOMAIN="Community",
        ENTITY="Community Program",
        ENTITY_PLURAL="Community Programs",
    )

    if test_config:
        app.config.update(test_config)

    db.init_app(app)

    from .routes.web import web_bp
    from .routes.api import api_bp

    app.register_blueprint(web_bp)
    app.register_blueprint(api_bp, url_prefix="/api")

    with app.app_context():
        from . import models

        db.create_all()

    return app
