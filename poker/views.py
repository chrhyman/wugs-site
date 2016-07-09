from flask import Blueprint, render_template, redirect, url_for
from flask import session, request

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

    def reset(self):
        self.__init__()

gamedata = Gamedata()

@mod_poker.route('/poker', methods=['GET', 'POST'])
def poker():
    if 'username' not in session:
        return redirect(url_for('app.auth'))
    if request.method == 'POST':
        if request.form.get('quit', None):
            gamedata.reset()
        elif request.form.get('newgame', None):
            gamedata.inprog = True
            gamedata.player = session['username']
            gamedata.gamestate = 1
        elif request.form.get('denom', None) and request.form.get('broll', None):
            gamedata.bankroll = int(request.form['broll']) * 100
            gamedata.denom = int(request.form['denom'])
            gamedata.creds.set_to(gamedata.bankroll / gamedata.denom)
            gamedata.gamestate = 2
    return render_template('poker.html', gamedata=gamedata)
