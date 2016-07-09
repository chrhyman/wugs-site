import copy

from flask import Markup

import poker.forms as forms
from poker.cards import Deck, Hand, Bank
import poker.pokerwin

CARD_BACK = '<td><img src="/static/cards/cardback.png" width="100px" /></td>\n'

class Poker:
    def __init__(self):
        self.deck = Deck()
        self.deck.standard()
        self.deck.shuffle()
        self.hand = Hand()
        self.draw = 0
        self.win = poker.pokerwin.Win()

    def reset(self):
        self.__init__()

    def deal(self, n=5):
        self.deck.moveNum(self.hand, n)

    def keep(self):
        keeps = input('Which cards would you like to keep? ')
        stay = []
        for char in keeps:
            if char in ['1', '2', '3', '4', '5']:
                stay.append(int(char) - 1)
        stay = list(set(stay))
        self.draw = 5 - len(stay)
        rem = []
        for i in range(5):
            if i not in stay:
                rem.append(self.hand.cards[i])
        for drop in rem:
            self.hand.remove(drop)

    def __str__(self):
        res = '\n'
        for card in self.hand:
            res += '\t'
            res += str(card)
        res += '\n'
        for card in self.hand:
            res += '\t   '
            res += str(self.hand.cards.index(card) + 1)
        return res

    def checkwin(self):
        self.win.update(copy.deepcopy(self.hand))
        self.win.getWin()

def playGame(money):
    game = Poker()
    money = Bank(money)
    while True:
        print('You have $' + str(money.bankroll))
        x = int(input('bet'))
        money.bet(x)
        game.deal()
        print('Your starting hand:', str(game))
        game.checkwin()
        print(str(game.win))
        game.keep()
        print('You kept:', str(game))
        game.deal(game.draw)
        print('Your final hand:', str(game))
        game.checkwin()
        print(str(game.win))
        w = game.win.pay * money.bet
        print('You win: $' + str(w))
        money.win(w)
        if input('Continue? ').lower() in ['n', 'no', 'exit', 'quit']:
            print('Final bank: $' + str(money))
            break
        game.reset()

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
        allcards = ''.join('<td>{}</td>\n'.format(
            str(card)) for card in data.game.hand.cards)
        cb = forms.no_checkboxes
        betone, betmax = forms.betone, forms.betmax
        betamt = 1
        invis = forms.invis
        dealbutton = forms.deal
        bank = '{:.2f}'.format(data.creds.bankroll*data.denom/100)
        if gs == 2:
            allcards = ''.join(CARD_BACK for i in range(5))
        elif gs == 3:
            cb = forms.checkboxes
            betone, betmax, invis = ' ', ' ', ' '
            betamt = data.creds.bet
            dealbutton = forms.redeal
        elif gs == 4:
            pass
        hand = ' '
        if data.game.win.winstr:
            hand = data.game.win.winstr
        keywords = {'cards': allcards, 'checkboxes': cb, 'hand': hand,
            'betone': betone, 'betmax': betmax, 'betamt': betamt,
            'invis': invis, 'creds': str(data.creds.bankroll),
            'bank': bank, 'deal': dealbutton}
        output = forms.gametable.format(**keywords)
    if data.error:
        output += '<p><br />{}</p>'.format(data.error)
    output += forms.quit
    output = Markup(output)
    if gs not in [1, 2, 3, 4]:
        output = 'ERROR! NO GAME IN PROGRESS.'
    return output
