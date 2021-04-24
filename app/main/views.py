from flask import render_template, url_for, redirect, flash
from . import main
from ..forms import RegistrationForm, LoginForm


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

@main.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash('Account successfully created!', 'success')
        return redirect(url_for('main.index'))
    return render_template('register.html', title='Register', reg_form=form)

@main.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'mbuguajoy52@gmail.com' and form.password.data == 'test':
            flash('Login successful!', 'success')
            return redirect(url_for('main.index'))
        else:
            flash('Login failed. Please check email or password', 'danger')
    return render_template('login.html', title='Register', form=form)

