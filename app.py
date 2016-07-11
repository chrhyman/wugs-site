from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy

from poker.poker import handler as p_handler

app = Flask(__name__)
app.config.from_object('config')

app.jinja_env.globals.update(p_handler=p_handler)

db = SQLAlchemy(app)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

from views import mod
app.register_blueprint(mod)

from poker.views import mod_poker
app.register_blueprint(mod_poker)

from res.views import mod_res
app.register_blueprint(mod_res)
