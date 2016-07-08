from flask import Blueprint, render_template, redirect, url_for, flash
from flask import session, request

from app import db
from models import User

def validate_user(attempt, p):
    if attempt:
        if attempt.password == p:
            return True
    return False

mod = Blueprint('app', __name__, template_folder='templates',
    static_folder='static')

@mod.route('/', methods=['GET', 'POST'])
def index():
    return render_template('main_page.html', active='home')

@mod.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        tryu = User.query.filter_by(username=request.form['username']).first()
        tryp = request.form['password']
        if validate_user(tryu, tryp):
            session['username'] = tryu.username
            flash('Successfully logged in!')
            return redirect(url_for('.index'))
        flash('Login attempt failed. If you don\'t have an account, click \
            "register". If you have been locked out of your account, contact \
            Chris.')
    return render_template('login.html', active='login')

@mod.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        newu = request.form['username']
        newp = request.form['password']
        if User.query.filter_by(username=request.form['username']).first():
            flash('That username is already taken.')
            return redirect(url_for('.register'))
        db.session.add(User(username=newu, password=newp))
        db.session.commit()
        message = 'Congrats %s! Your account has been created.' % newu
        flash(message)
        return redirect(url_for('.index'))
    return render_template('register.html', active='register')

@mod.route('/logout')
def logout():
    session.pop('username', None)
    flash('Logged out.')
    return redirect(url_for('.index'))

@mod.route('/games')
def games():
    return render_template('games.html', active='games')

@mod.route('/stats')
def stats():
    return render_template('stats.html', active='stats')

@mod.route('/settings')
def settings():
    return render_template('settings.html', active='settings')
