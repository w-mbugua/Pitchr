from flask import render_template, url_for, redirect, flash, abort
from . import main
from ..models import User
from flask_login import login_required

pitches = [
    {'author': 'Sarah',
    'date_posted': 'April 27 2021',
    'pitch': 'I find the work your PR team does to be innovating and refreshing—I’d love the opportunity to put my expertise to work for your company…'
    },
    {
        'author': 'Steve',
        'date_posted': 'February 29, 2020',
        'pitch': 'I’ve always been passionate about the way sports bring cultures together and would love the opportunity to bring my project management and leadership abilities to this position.'
    }
]

@main.route('/')
def index():
    return render_template('index.html', pitches = pitches)

@main.route('/user/<name>')
def profile(name):
    user = User.query.filter_by(username = name).first()
    if user is None:
        abort(404)
    return render_template('profile/profile.html', user = user)

@main.route('/pitch/new', methods = ['GET','POST'])
@login_required
def new_pitch():
    return render_template('post_pitch.html', title = 'New Pitch')








