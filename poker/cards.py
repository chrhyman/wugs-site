import random

class Card:
    suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    psuits = ['♣', '♦', '❤', '♠']
    ranks = ['BACK', 'A', '2', '3', '4', '5', '6', '7', '8', '9', 'T',
        'J', 'Q', 'K', 'A']
    longranks = ['BACK', 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10',
        'Jack', 'Queen', 'King', 'Ace']
    colors = ['red', 'black']

    def __init__(self, rank=2, suit=0, acehi=True, width=100):
        self.suit = suit
        self.width = width
        if acehi and rank == 1:
            self.rank = 14
        else:
            self.rank = rank
        if suit in [1, 2]:
            self.color = Card.colors[0]
        elif suit in [0, 3]:
            self.color = Card.colors[1]

    def __str__(self):
        if self.rank == 0:
            base = '<img src="/static/cards/cardback.png" width="{2}px" />'
        else:
            base = '<img src="/static/cards/{0}_of_{1}.png" width="{2}px" />'
        return base.format(Card.longranks[self.rank].lower(),
            Card.suits[self.suit].lower(), self.width)

    def __eq__(self, other):
        return (self.rank, self.suit) == (other.rank, other.suit)

    def __ne__(self, other):
        return (self.rank, self.suit) != (other.rank, other.suit)

    def __lt__(self, other):
        return (self.rank, self.suit) < (other.rank, other.suit)

    def __le__(self, other):
        return (self.rank, self.suit) <= (other.rank, other.suit)

    def __gt__(self, other):
        return (self.rank, self.suit) > (other.rank, other.suit)

    def __ge__(self, other):
        return (self.rank, self.suit) >= (other.rank, other.suit)

class Deck:
    def __init__(self):
        self.cards = []

    def __len__(self):
        return len(self.cards)

    def __contains__(self, acard):
        return any(card == acard for card in self.cards)

    def __getitem__(self, index):
        return self.cards[index]

    def __str__(self):
        res = []
        for card in self:
            res.append(str(card))
        return '\n'.join(res)

    def add(self, newcard):
        self.cards.append(newcard)

    def remove(self, oldcard):
        self.cards.remove(oldcard)

    def popIndex(self, i=0):
        return self.cards.pop(i)

    def popCard(self, findfirst):
        return self.cards.pop(self.cards.index(findfirst))

    def shuffle(self):
        n = len(self)
        newcards = []
        for i in randperm(n):
            newcards.append(self.cards[i])
        self.cards = newcards

    def sort(self):
        self.cards.sort()

    def moveNum(self, dest, num):
        for i in range(num):
            dest.add(self.popIndex())

    def moveCard(self, dest, card):
        dest.add(self.popCard(card))

    def standard(self, acehi=True, width=100):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                self.cards.append(Card(rank, suit, acehi, width))

    def empty(self):
        self.__init__()

class Hand(Deck):
    def __init__(self, name=''):
        self.cards = []
        self.name = name

class Bank:
    def __init__(self, bankroll):
        self.bankroll = int(bankroll)
        self.bet = 0

    def __str__(self):
        return str(self.bankroll)

    def set_to(self, s):
        self.bankroll = int(s)

    def bet(self, b):
        self.bet = int(b)
        self.bankroll = self.bankroll - int(b)

    def win(self, w):
        self.bankroll = self.bankroll + int(w)

def randperm(n):
    r = list(range(n))
    x = []
    while r:
        i = random.choice(r)
        x.append(i)
        r.remove(i)
    return x
