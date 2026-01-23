from . import db
from . import login_manager
from flask_login import UserMixin

# helper function for loading the user session
@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(50))
    email = db.Column(db.String(200), unique=True)
    password = db.Column(db.String(200))

