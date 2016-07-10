from flask import Blueprint, render_template, redirect, url_for, flash
from flask import session, request

from app import db
from poker.models import PokerGame

from poker.cards import Bank
from poker.poker import Poker

mod_poker = Blueprint('poker', __name__, url_prefix='/games')

class Gamedata:
    def __init__(self, inprog=False, player=None, gamestate=0, bankroll=0,
        denom=0, creds=Bank(0), keep=[]):
        self.inprog = inprog
        self.player = player
        self.gamestate = gamestate
        self.bankroll = bankroll        # in cents
        self.denom = denom              # in cents
        self.creds = creds
        self.game = Poker()
        self.keep = keep
        self.hands = 0
        self.error = None

    def reset(self):
        self.__init__()

gamedata = Gamedata()

@mod_poker.route('/poker', methods=['GET', 'POST'])
def poker():
    if 'username' not in session:
        return redirect(url_for('app.auth'))
    if request.method == 'POST':
        gamedata.error = None
        if request.form.get('quit', None):
            if gamedata.gamestate > 1:
                string = 'Thanks for playing! You started with ${:.2f} and ended with ${:.2f} after playing {} hands.'
                flash(string.format(gamedata.bankroll/100,
                    gamedata.creds.bankroll*gamedata.denom/100, gamedata.hands))
            gamedata.reset()
            return redirect(url_for('.poker'))
        elif request.form.get('newgame', None):
            gamedata.inprog = True
            gamedata.player = session['username']
            gamedata.gamestate = 1
        elif request.form.get('denom', None) and request.form.get('broll', None):
            gamedata.bankroll = int(request.form['broll']) * 100
            gamedata.denom = int(request.form['denom'])
            gamedata.creds.set_to(gamedata.bankroll / gamedata.denom)
            gamedata.gamestate = 2
        elif request.form.get('deal', None):
            if gamedata.creds.bankroll - int(request.form['thebet']) < 0:
                gamedata.error = '<strong>Error</strong>: You can\'t bet more than you have!'
                gamedata.gamestate = 2
            else:
                gamedata.creds.doBet(request.form['thebet'])
                gamedata.game.reset()
                gamedata.game.deal()
                gamedata.game.checkwin()
                gamedata.gamestate = 3
        elif request.form.get('redeal', None):
            gamedata.keep = [int(i) - 1 for i in request.form.getlist('keep')]
            gamedata.game.keepAndDraw(gamedata.keep)
            gamedata.game.checkwin()
            gamedata.creds.win(gamedata.game.win.pay * gamedata.creds.bet)
            gamedata.hands += 1
            gamedata.gamestate = 4
    return render_template('poker.html', gamedata=gamedata)

@mod_poker.route('/poker/submit', methods=['POST'])
def poker_submit():
    payload = {'username': request.form['username'],
        'startmoney': request.form['startmoney'],
        'endmoney': request.form['endmoney'],
        'handsplayed': request.form['handsplayed']}
    db.session.add(PokerGame(**payload))
    db.session.commit()
    message = 'You\'ve successfully submitted your poker game to the rankings!'
    gamedata.reset()
    flash(message)
    return redirect(url_for('app.stats'))
