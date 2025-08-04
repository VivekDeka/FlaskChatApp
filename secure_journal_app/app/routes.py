from flask import Blueprint, render_template, redirect, url_for, flash, session, request
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from .models import User, Entry
from .forms import RegisterForm, LoginForm, EntryForm
from . import db

main = Blueprint('main', __name__)

# Define the routes
@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password, form.password.data):
            session['user_id'] = user.id
            session['username'] = user.username
            return redirect(url_for('main.dashboard'))
        flash('Invalid credentials')

    return render_template('login.html', form=form)

@main.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed = generate_password_hash(form.password.data)
        user = User(username = form.username.data, password=hashed)
        db.session.add(user)
        db.session.commit()
        flash('Account Created. Please Log in')
        return redirect(url_for('main.login'))
    return render_template('register.html', form=form)

@main.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('main.login'))

@main.route('/dashboard', methods = ['GET','POST'])
def dashboard():
    if 'user_id' not in session:
        flash('Please log in.')
        return redirect(url_for('main.login'))
    
    form = EntryForm()
    if form.validate_on_submit():
        entry = Entry(
            title = form.title.data,
            content = form.content.data,
            date = datetime.utcnow(),
            user_id = session['user_id']            
            
        )
        db.session.add(entry)
        db.session.commit()
        flash('Entry saved!')
        
        return redirect(url_for('main.dashboard'))
    
    entries = Entry.query.filter_by(user_id=session['user_id']).all()
    return render_template('dashboard.html', entries=entries, form = form)

@main.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_entry(id):
    
    entry = Entry.query.get_or_404(id)
    form = EntryForm(obj = entry)
    
    if form.validate_on_submit():
        entry.title = form.title.data
        entry.content = form.content.data
        db.session.commit()
        flash('Entry Updated')
        return redirect(url_for('main.dashboard'))
    return render_template('entry_form.html', form=form, edit=True)

@main.route('/delete/<int:id>')
def delete_entry(id):
    entry = Entry.query.get_or_404(id)
    db.session.delete(entry)
    db.session.commit()
    flash('Entry deleted.')
    return redirect(url_for('main.dashboard'))
