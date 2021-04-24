from . import db
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash


class User(db.Model):
    __tablename__='users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), unique = True, index = True)
    email = db.Column(db.String(120), unique = True, index = True)
    password_hash = db.Column(db.String(255))
    pitch = db.relationship('Pitch', backref = 'user', lazy = 'dynamic')

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)


class Pitch(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    content =  db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return f"User('{self.date_posted}')"
