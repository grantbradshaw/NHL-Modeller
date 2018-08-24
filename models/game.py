from app import db

class Game(db.Model):
    __tablename__ = 'games'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    team_games = db.relationship('TeamGame', backref='games', lazy=True)

    def __init__(self, date):
        self.date = date

    def __repr__(self):
        return '<id {}>'.format(self.id)