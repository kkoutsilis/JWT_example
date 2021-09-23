from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from config import Config


db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app, db)

    from app.auth import auth_bp

    app.register_blueprint(auth_bp)

    from app.api import api_bp

    app.register_blueprint(api_bp)

    return app


from app import models, utils
