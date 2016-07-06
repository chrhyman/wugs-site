from flask import Flask
from flask import render_template, redirect, url_for
from flask import session, request
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True

SQL_URI = "mysql+mysqlconnector://{0}:{1}@{2}/{3}".format("wugs", "sqlpassword",
    "wugs.mysql.pythonanywhere-services.com", "wugs$users")
app.config["SQLALCHEMY_DATABASE_URI"] = SQL_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299

db = SQLAlchemy(app)

class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), nullable=False, unique=True)
    password = db.Column(db.String(64))

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
