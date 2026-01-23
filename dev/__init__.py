import os
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from .config import Config

db = SQLAlchemy()
login_manager = LoginManager()
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # setting login for session managment
    login_manager.init_app(app)   

    db.init_app(app)

    # default login redirection in login manager
    login_manager.login_view = "auth.login_page"

    # import database model
    #from .models import User
    from .auth import auth
    from .views import view

    # register the blueprints
    app.register_blueprint(auth, url_prefix="/auth")
    app.register_blueprint(view, url_prefix="/")
    # create the database
    create_database(app)

    return app

def create_database(app):
    if not os.path.exists("users.db"):
        with app.app_context():
            db.create_all()
                                                                                                                                                                                                                                                                        

