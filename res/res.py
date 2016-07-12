import math
import random

class GameError(Exception):
    pass

class Player:

    ROLES = {
            'error: none': 0,
            'RESISTANCE': 10,
            'MERLIN': 11,
            'PERCIVAL': 12,
            'A SPY': 20,
            'ASSASSIN': 21,
            'MORGANA': 22,
            'MORDRED': 23,
            'OBERON': 24,
            'MORDSASSIN': 25,
            'observing': 99
        }

    def __init__(self, name='no name'):
        self.name = name
        self.role = 0

class Game:

    GAMETYPES = {
        'Basic': 0,             # basic resistance, just spies and res
        'Basic+': 1,            # basic resistance + lady of the lake
        'Avalon': 2             # minimum Merl+Assassin, + others possible
        }

    MISSION_TEAM_SIZE = [
            None,               # 0-4 players not possible
            None,               #
            None,               #
            None,               #
            None,               #
            [2, 3, 2, 3, 3],    # 5
            [2, 3, 4, 3, 4],    # 6
            [2, 3, 3, 4, 4],    # 7
            [3, 4, 4, 5, 5],    # 8
            [3, 4, 4, 5, 5],    # 9
            [3, 4, 4, 5, 5]     # 10
        ]

    FAILS_NEEDED = [
            None,               # 0-4 players not possible
            None,               #
            None,               #
            None,               #
            None,               #
            [1, 1, 1, 1, 1],    # 5
            [1, 1, 1, 1, 1],    # 6
            [1, 1, 1, 2, 1],    # 7
            [1, 1, 1, 2, 1],    # 8
            [1, 1, 1, 2, 1],    # 9
            [1, 1, 1, 2, 1]     # 10
        ]

    def __init__(self):
        self.players = []   # A list of Player() objects
        self.p = 0
        self.gameID = 0
        self.game_type = 0

        self.res = []
        self.spies = []
        self.spycount = 0
        self.game_started = False
        self.game_finished = False
        self.public_log = []
        self.mission = 1
        self.round = 1
        self.reswins = 0
        self.spywins = 0

        self.leader_index = 0
        self.lady_index = 0
        self.players_on_current_mission = []

        self.uselady = False
        self.cant_receive_lady = []
        self.usemerlin = False
        self.useassassin = False
        self.usepercival = False
        self.usemorgana = False
        self.usemordred = False
        self.useoberon = False
        self.combinemordassassin = False
        self.prs = []

        self.votelog = {
                'rounds': [0, 0, 0, 0, 0],
                'leader': [],
                'approve': [],
                'reject': [],
                'onmission': []
            }

    def resetGame(self):
        self.__init__()

    def startGame(self, players, gameID=0, game_type=0, gameoptions=None):
        if len(players) > 10 or len(players) < 5:
            raise GameError('Must have from 5 to 10 players.')
        self.players = players
        self.p = len(self.players)
        random.shuffle(self.players)
        self.res = [index for index, obj in enumerate(self.players)]

        self.gameID = gameID
        self.game_type = game_type

        if self.game_type != 0:
            if not gameoptions:
                raise GameError('Must specify game options!')
            self.uselady = gameoptions[0]
            if self.game_type == 2:
                self.usemerlin = True
                self.useassassin = True
                self.usepercival = gameoptions[1]
                self.usemorgana = gameoptions[2] and gameoptions[1]
                self.usemordred = gameoptions[3]
                self.useoberon = gameoptions[4]
                self.combinemordassassin = gameoptions[5] and self.usemordred

        self.team_sizes = Game.MISSION_TEAM_SIZE[self.p]
        self.fails_needed = Game.FAILS_NEEDED[self.p]

        self.game_started = True
        self.spycount = math.ceil(len(players) / 3)

        self.assignRoles()

    def assignRoles(self):
        self.leader_index = random.choice(range(self.p))
        while self.spycount:
            self.spies.append(self.res.pop(random.choice(range(len(self.res)))))
            self.spycount -= 1

        if self.uselady:
            self.lady_index = (self.p if self.leader_index == 0
                else self.leader_index - 1)
            self.cant_receive_lady.append(self.lady_index)
        if self.usemerlin:
            self.pick_role(11)
        if self.usepercival:
            self.pick_role(12)
        if self.usemorgana:
            self.pick_role(22)
        if self.useoberon:
            self.pick_role(24)
        if self.combinemordassassin:
            self.pick_role(25)
        else:
            if self.useassassin:
                self.pick_role(21)
            if self.usemordred:
                self.pick_role(23)

        for i in range(self.p):
            if self.players[i].role == 0:
                self.players[i].role = 10 if i in self.res else 20


    def pick_role(self, role):
        rand_player = random.choice(range(self.p))
        if rand_player in self.prs:
            self.pick_role(role)
        else:
            if ((10 <= role <= 19 and rand_player in self.res)
                or (20 <= role <= 29 and rand_player in self.spies)):
                self.players[rand_player].role = role
                self.prs.append(rand_player)
            else:
                self.pick_role(role)

    def nextLeader(self):
        self.leader_index = (self.leader_index + 1) % self.p
