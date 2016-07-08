from flask import Blueprint, render_template, redirect, session, url_for

# from poker.cards import Card, Deck, Hand

mod_poker = Blueprint('poker', __name__, url_prefix='/games')

@mod_poker.route('/poker')
def poker():
    if 'username' not in session:
        return redirect(url_for('app.auth'))
    return render_template('poker.html')
