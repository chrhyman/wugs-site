from flask import Blueprint, render_template, redirect, url_for, flash
from flask import session, request

from app import db
from poker.models import PokerGame

from poker.cards import Bank
from poker.poker import Poker

mod_poker = Blueprint('poker', __name__, url_prefix='/games')

class Gamedata:
    def __init__(self, inprog=False, player=None, gamestate=0, bankroll=0,
        denom=0, creds=Bank(0), keep=[], room=0):
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
        self.room = room

    def reset(self):
        self.__init__()

gamedata = [Gamedata(room=i) for i in range(30)]

def getPlayersRooms():
    players = {}
    for room in gamedata:
        if room.inprog:
            players[str(room.room)] = room.player
    if players == {}:
        players = {'none': 'No one.'}
    return players

@mod_poker.route('/poker', methods=['GET', 'POST'])
def poker():
    if request.method == 'POST':
        if request.form.get('newgame', None):
            for index, rooms in enumerate(gamedata):
                if not rooms.inprog:
                    return redirect(url_for('.pokerroom', room=index), code=307)
            flash('Sorry, all rooms are full!')
            return redirect(url_for('.poker'))
    return render_template('poker.html', gamedata=Gamedata(), players=getPlayersRooms())

@mod_poker.route('/poker/room/<room>', methods=['GET', 'POST'])
def pokerroom(room):
    room = int(room)
    if 'username' not in session:
        return redirect(url_for('app.auth'))
    if room > len(gamedata) - 1:
        flash('You somehow got sent to a room that doesn\'t exist! Tell Chris some shit went down.')
        return redirect(url_for('.poker'))
    if request.method == 'POST':
        gamedata[room].error = None
        if request.form.get('quit', None):
            if gamedata[room].gamestate > 1:
                string = 'Thanks for playing! You started with ${:.2f} and ended with ${:.2f} after playing {} hands.'
                flash(string.format(gamedata[room].bankroll/100,
                    gamedata[room].creds.bankroll*gamedata[room].denom/100, gamedata[room].hands))
            gamedata[room].reset()
            return redirect(url_for('.poker'))
        elif request.form.get('newgame', None):
            gamedata[room].inprog = True
            gamedata[room].player = session['username']
            gamedata[room].gamestate = 1
        elif request.form.get('denom', None) and request.form.get('broll', None):
            gamedata[room].bankroll = int(request.form['broll']) * 100
            gamedata[room].denom = int(request.form['denom'])
            gamedata[room].creds.set_to(gamedata[room].bankroll / gamedata[room].denom)
            gamedata[room].gamestate = 2
        elif request.form.get('deal', None):
            if gamedata[room].creds.bankroll - int(request.form['thebet']) < 0:
                gamedata[room].error = '<strong>Error</strong>: You can\'t bet more than you have!'
                gamedata[room].gamestate = 2
            else:
                gamedata[room].creds.doBet(request.form['thebet'])
                gamedata[room].game.reset()
                gamedata[room].game.deal()
                gamedata[room].game.checkwin()
                gamedata[room].gamestate = 3
        elif request.form.get('redeal', None):
            gamedata[room].keep = [int(i) - 1 for i in request.form.getlist('keep')]
            gamedata[room].game.keepAndDraw(gamedata[room].keep)
            gamedata[room].game.checkwin()
            gamedata[room].creds.win(gamedata[room].game.win.pay * gamedata[room].creds.bet)
            gamedata[room].hands += 1
            gamedata[room].gamestate = 4
    return render_template('poker.html', gamedata=gamedata[room], room=room, players=getPlayersRooms())

@mod_poker.route('/poker/submit', methods=['POST'])
def poker_submit():
    payload = {'username': request.form['username'],
        'startmoney': request.form['startmoney'],
        'endmoney': request.form['endmoney'],
        'handsplayed': request.form['handsplayed']}
    db.session.add(PokerGame(**payload))
    db.session.commit()
    message = 'You\'ve successfully submitted your poker game to the rankings!'
    gamedata[int(request.form['room'])].reset()
    flash(message)
    return redirect(url_for('app.stats'))
