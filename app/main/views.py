from flask import render_template, url_for, redirect, flash, abort
from . import main
from ..models import Pitch, User, Comment
from flask_login import login_required, current_user
from .forms import PitchForm, CommentForm
from .. import db


@main.route('/')
def index():
    pitches = Pitch.query.order_by(Pitch.date_posted.desc()).all()
    return render_template('index.html', pitches = pitches)

@main.route('/user/<name>')
def profile(name):
    user = User.query.filter_by(username = name).first()
    pitches = Pitch.query.order_by(Pitch.date_posted.desc()).filter_by(user_id = user.id)
    if user is None:
        abort(404)
    return render_template('profile/profile.html', user = user, pitches = pitches)

@main.route('/pitch/new', methods = ['GET','POST'])
@login_required
def new_pitch():
    form = PitchForm()
    if form.validate_on_submit():
        pitch = Pitch(post = form.post.data, user = current_user, category = form.category.data)
        db.session.add(pitch)
        db.session.commit()
        flash('Your pitch has been posted!', 'success')
        return redirect(url_for('main.index'))
    return render_template('post_pitch.html', title = 'New Pitch', form = form)

@main.route('/<category>')
def category(category):
    pitches = Pitch.query.filter_by(category = category).all()
    return render_template('category.html', pitches = pitches)

@main.route('/pitch/<int:id>')
def pitch(id):
    pitch = Pitch.query.get_or_404(id)
    comments = Comment.query.filter_by(pitch_id = pitch.id).all()
    return render_template('pitch.html', pitch = pitch, comments = comments)

@main.route('/pitch/<int:id>/update', methods = ['GET','POST'])
@login_required
def pitchupdate(id):
   pitch = Pitch.query.get_or_404(id)
   if pitch.user != current_user:
       abort(403)
   form = PitchForm()
   if form.validate_on_submit():
       pitch.post = form.post.data
       db.session.commit()
       return redirect(url_for('main.pitch', id = pitch.id))
   form.post.data = pitch.post
   return render_template('post_pitch.html', form = form)

@main.route('/pitch/<int:id>/delete', methods = ['POST'])
@login_required
def delete(id):
    pitch = Pitch.query.get_or_404(id)
    if pitch.user != current_user:
       abort(403)
    db.session.delete(pitch)
    db.session.commit()
    flash('Pitch has been deleted!', 'success')
    return redirect(url_for('main.index'))
  
    

@main.route('/pitch/<int:id>/comment', methods = ['GET','POST'])
@login_required
def comment(id):
   pitch = Pitch.query.get_or_404(id)
   form = CommentForm()
   if form.validate_on_submit():
       comment = Comment(content = form.content.data, pitch_id = pitch.id, user = current_user)
       db.session.add(comment)
       db.session.commit()
       return redirect(url_for('main.index'))
   return render_template('post_pitch.html', form = form)











