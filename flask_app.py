from flask import Flask
from flask import render_template, redirect, url_for
from flask import session, request

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'username' in session:
        return render_template('main_page.html', username=session['username'])
    return render_template('main_page.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form action="" method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

app.secret_key = '3r3i0bkn%437941ua07k419244w'