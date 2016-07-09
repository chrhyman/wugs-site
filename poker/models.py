from app import db

class PokerGame(db.Model):

    __tablename__ = "pokergame"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64))
    startmoney = db.Column(db.Integer)
    endmoney = db.Column(db.Integer)
    handsplayed = db.Column(db.Integer)
