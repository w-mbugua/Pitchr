from sqlalchemy.orm import backref
from . import db
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin, db.Model):
    __tablename__='users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), unique = True, index = True)
    email = db.Column(db.String(120), unique = True, index = True)
    password_hash = db.Column(db.String(255))
    pitch = db.relationship('Pitch', backref = 'user', lazy = 'dynamic')
    comment = db.relationship('Comment', backref = 'user', lazy = 'dynamic')
    
    @property
    def password(self):
        raise AttributeError('You cannnot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)


    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"


class Pitch(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    post =  db.Column(db.String(500))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    likes = db.Column(db.Integer, default = 0)
    dislikes = db.Column(db.Integer, default = 0)
    comments = db.relationship('Comment', backref = 'pitch', lazy = 'dynamic')
    category = db.Column(db.String(120))

    def __repr__(self):
        return f"User('{self.date_posted}')"

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    content = db.Column(db.String(255))
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitch.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    

    def __repr__(self):
        return f"User('{self.date_posted}')"

