from flask import Flask, redirect, render_template, request, url_for
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
sql = "mysql+mysqlconnector://{0}:{1}@{2}/{3}".format("wugs", "sqlpassword",
    "wugs.mysql.pythonanywhere-services.com", "wugs$comments")
app.config["SQLALCHEMY_DATABASE_URI"] = sql
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299

db = SQLAlchemy(app)

class Comment(db.Model):

    __tablename__ = "comments"

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(4096))


comments = []
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('main_page.html', comments=comments)

    comments.append(request.form['contents'])
    return redirect(url_for('index'))
