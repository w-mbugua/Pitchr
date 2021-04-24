from . import db
from datetime import datetime


class User(db.Model):
    __tablename__='users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), unique = True, index = True)
    email = db.Column(db.String(120), unique = True, index = True)
    password = db.Column(db.String(60))
    pitch = db.Relationship('Pitch', backref = 'user', lazy = 'dynamic')

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

class Pitch(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    content =  db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return f"User('{self.date_posted}')"
