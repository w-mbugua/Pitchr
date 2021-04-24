from flask import render_template
from app import app

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
@app.route('/')
def index():
    return render_template('index.html', pitches = pitches)

