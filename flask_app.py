from flask import Flask, render_template, redirect, url_for, session, request
from flask.ext.sqlalchemy import SQLAlchemy

# import sqlalchemy.exc             sqlalchemy.exc.IntegrityError for duplicates

app = Flask(__name__)
app.config['DEBUG'] = True

SQL = "mysql+mysqlconnector://{0}:{1}@{2}/{3}".format("wugs", "sqlpassword",
    "wugs.mysql.pythonanywhere-services.com", "wugs$users")
app.config["SQLALCHEMY_DATABASE_URI"] = SQL
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299

db = SQLAlchemy(app)

class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), nullable=False, unique=True)
    password = db.Column(db.String(64))

def validate_user(attempt, p):
    if attempt:
        if attempt.password == p:
            return True
    return False


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('main_page.html', active='home')

@app.route('/login', methods=['GET', 'POST'])
def login():
    session.pop('failed', None)
    if request.method == 'POST':
        tryu = User.query.filter_by(username=request.form['username']).first()
        tryp = request.form['password']
        if validate_user(tryu, tryp):
            session['username'] = tryu.username
            return redirect(url_for('index'))
        session['failed'] = True
    return render_template('login.html', active='login')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route('/games')
def games():
    return render_template('main_page.html', active='games')

app.secret_key = '3r3i0bkn%437941ua07k419244w'
