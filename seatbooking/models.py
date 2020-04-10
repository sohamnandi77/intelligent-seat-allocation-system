from datetime import datetime
from seatbooking import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    age = db.Column(db.String(120), nullable=False)
    gender = db.Column(db.String(120), nullable=False)
    ca = db.Column(db.String(120), nullable=False)
    seat = db.Column(db.String(120), nullable=False)
    coach = db.Column(db.String(120), nullable=False)
    berth = db.Column(db.String(120), nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='./static/img/profile_pics/default.jpg')
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"
