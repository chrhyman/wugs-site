import copy

from flask import Markup

import poker.forms as forms
from poker.cards import Deck, Hand
from poker.pokerwin import Win

CARD_BACK = '<td><img src="/static/cards/cardback.png" width="100px" /></td>\n'

class Poker:
    def __init__(self):
        self.deck = Deck()
        self.deck.standard()
        self.deck.shuffle()
        self.hand = Hand()
        self.win = Win()

    def reset(self):
        self.__init__()

    def deal(self, n=5):
        self.deck.moveNum(self.hand, n)

    def keepAndDraw(self, l):
        self.deck.shuffle()
        drop = [i for i in range(5) if i not in l]
        for index in drop:
            self.hand.cards[index] = self.deck.popIndex()

    def checkwin(self):
        self.win.update(copy.deepcopy(self.hand))
        self.win.getWin()

# gamestate :   0 - no game in progress
#               1 - there is a player, no bankroll
#               2 - first hand
#               3 - bet set, initial cards have been dealt (wait for keep)
#               4 - last hand over, 2 but with cards showing
def handler(data):
    gs = data.gamestate
    if gs == 1:
        output = forms.player_no_bankroll
    else:
        allcards = ''.join('<td \
            onclick="document.getElementById(\'c{c}\').click()">{img}</td>\
            \n'.format(c=index, img=str(card)) for index, card in enumerate(
            data.game.hand.cards))
        kept = 'Kept:'
        checked = ['', '', '', '', '']
        for i in data.keep:
            checked[i] = ' checked'
        cb = forms.no_checkboxes.format(kept=kept, *checked)
        betone, betmax = forms.betone, forms.betmax
        betamt = 1
        invis = forms.invis
        dealbutton = forms.deal
        bank = '{:.2f}'.format(data.creds.bankroll*data.denom/100)
        win = ''
        if gs == 2:
            allcards = ''.join(CARD_BACK for i in range(5))
            kept = ''
            checked = [' style="display:none;"' for i in range(5)]
            cb = forms.no_checkboxes.format(kept=kept, *checked)
        elif gs == 3:
            cb = forms.checkboxes
            betone, betmax, invis = ' ', ' ', ' '
            betamt = data.creds.bet
            dealbutton = forms.redeal
        elif gs == 4:
            betamt = data.creds.bet
            if data.game.win.winstr:
                win = 'WIN: {}'.format(data.game.win.pay * data.creds.bet)
        hand = ' '
        if data.game.win.winstr:
            hand = data.game.win.winstr
        keywords = {'cards': allcards, 'checkboxes': cb, 'hand': hand,
            'betone': betone, 'betmax': betmax, 'betamt': betamt,
            'invis': invis, 'creds': str(data.creds.bankroll),
            'bank': bank, 'deal': dealbutton, 'win': win}
        output = forms.gametable.format(**keywords)
    if data.error:
        output += '<p><br />{}</p>'.format(data.error)
    submitdata = {'username': data.player, 'startmoney': data.bankroll,
        'endmoney': data.creds.bankroll * data.denom, 'handsplayed': data.hands,
        'room': data.room}
    output += forms.quit.format(**submitdata)
    output = Markup(output)
    if gs not in [1, 2, 3, 4]:
        output = 'ERROR! NO GAME IN PROGRESS.'
    return output
