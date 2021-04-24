from flask import render_template, redirect, flash, url_for
from . import auth
from .forms import RegistrationForm, LoginForm


@auth.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash('Account successfully created!', 'success')
        return redirect(url_for('main.index'))
    return render_template('register.html', title='Register', reg_form=form)


@auth.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'mbuguajoy52@gmail.com' and form.password.data == 'test':
            flash('Login successful!', 'success')
            return redirect(url_for('main.index'))
        else:
            flash('Login failed. Please check email or password', 'danger')
    return render_template('login.html', title='Register', form=form)
