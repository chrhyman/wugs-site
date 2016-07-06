from flask import Flask
from flask import render_template, redirect, url_for
from flask import session, request

app = Flask(__name__)
app.config['DEBUG'] = True

data = {}

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'username' in session:
        data['username'] = session['username']
    else:
        try:
            del data['username']
        except KeyError:
            pass
    return render_template('main_page.html', data=data, active='home')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return render_template('login.html', data=data, active='login')

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route('/games')
def games():
    return render_template('main_page.html', data=data, active='games')

app.secret_key = '3r3i0bkn%437941ua07k419244w'
