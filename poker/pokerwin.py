from itertools import groupby

class Win:
    pays = {'royal': 800, 'straight flush': 50, 'quads': 25,
        'full house': 9, 'flush': 6, 'straight': 4, 'trips': 3, 'two pair': 2,
        'jacksbetter': 1, 'pair': 0, 'high card': 0}

    def __init__(self):
        self.hands = {'royal': False, 'strfl': False, 'quads': False,
            'full': False, 'flush': False, 'strt': False, 'trips': False,
            'twopair': False, 'pair': False, 'error': False}
        self.data = {'flsuit': None, 'strhi': None, 'quad': None, 'trip': None,
            'pairs': None}
        self.currhand = None
        self.winstr = None
        self.pay = 0

    def __str__(self):
        return self.winstr

    def update(self, chand):
        self.__init__()
        self.currhand = chand
        ranks = sorted([self.currhand.cards[i].rank
            for i in range(len(self.currhand))])
        suits = [self.currhand.cards[i].suit
            for i in range(len(self.currhand))]
        groups = [[key, len(list(group))] for key, group in groupby(ranks)]
        freq = [y for [x, y] in groups]

        if len(self.currhand) != 5:
            self.hands['error'] = True
        if len(set(suits)) == 1:
            self.hands['flush'] = True
            self.data['flsuit'] = suits[0]
        acetofive = ranks == [2, 3, 4, 5, 14]
        if (max(ranks) - min(ranks) == 4 or acetofive) and len(groups) == 5:
            self.hands['strt'] = True
            self.data['strhi'] = max(ranks)
        if self.hands['flush'] and self.hands['strt']:
            self.hands['strfl'] = True
        if self.hands['strfl'] and min(ranks) == 10:
            self.hands['royal'] = True

        if 5 in freq:
            self.hands['error'] = True
        elif 4 in freq:
            self.hands['quads'] = True
            self.data['quad'] = [x for [x, y] in groups if y == 4][0]
        elif 3 in freq:
            self.hands['trips'] = True
            self.data['trip'] = [x for [x, y] in groups if y == 3][0]
            if 2 in freq:
                self.hands['full'] = True
        elif freq.count(2) == 2:
            self.hands['twopair'] = True

        if 2 in freq:
            self.hands['pair'] = True
            self.data['pairs'] = [x for [x, y] in groups if y == 2]

    def getWin(self):
        h = self.hands
        d = self.data
        p = Win.pays
        if not h['error']:
            if h['royal']:
                self.winstr = 'Royal Flush'
                self.pay = p['royal']
            elif h['strfl']:
                self.winstr = 'Straight Flush'
                self.pay = p['straight flush']
            elif h['quads']:
                self.winstr = 'Four of a Kind'
                self.pay = p['quads']
            elif h['full']:
                self.winstr = 'Full House'
                self.pay = p['full house']
            elif h['flush']:
                self.winstr = 'Flush'
                self.pay = p['flush']
            elif h['strt']:
                self.winstr = 'Straight'
                self.pay = p['straight']
            elif h['trips']:
                self.winstr = 'Three of a Kind'
                self.pay = p['trips']
            elif h['twopair']:
                self.winstr = 'Two Pair'
                self.pay = p['two pair']
            elif h['pair']:
                if d['pairs'][0] >= 11:
                    self.winstr = 'Jacks or Better'
                    self.pay = p['jacksbetter']
                else:
                    self.winstr = None
            else:
                self.winstr = None
        else:
            self.winstr = 'ERROR'
