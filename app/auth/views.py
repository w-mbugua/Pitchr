from flask import render_template, redirect, request, flash, url_for
from . import auth
from .forms import RegistrationForm, LoginForm
from ..models import User
from .. import db
from flask_login import login_user, logout_user

@auth.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        if form.validate_on_submit():
            user = User(email = form.email.data, username = form.username.data,password = form.password.data)
            db.session.add(user)
            db.session.commit()
            flash('Account successfully created!', 'success')
        
            return redirect(url_for('auth.login'))
    return render_template('register.html', title='Register', reg_form=form)


@auth.route('/login', methods = ['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email = login_form.email.data).first()
        
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user,login_form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))

        flash('Invalid username or Password')

    title = "Logged in"
    return render_template('login.html', form = login_form,title=title)

@auth.route('/logout')
def logout():
    logout_user()
    return render_template('index.html')

