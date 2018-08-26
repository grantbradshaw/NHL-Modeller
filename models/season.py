from app import db

class Season(db.Model):
    __tablename__ = 'seasons'

    id = db.Column(db.Integer, primary_key=True)
    start_date = db.Column(db.Date)
    start_playoffs = db.Column(db.Date)
    end_playoffs = db.Column(db.Date)
    cap_floor = db.Column(db.Float) # in USD
    cap_ceiling = db.Column(db.Float) # in USD
    games = db.Column(db.Float)
    contract_seasons = db.relationship('ContractSeason', backref='seasons', lazy=True)

    def __init__(self, start_date, start_playoffs, end_playoffs, cap_floor,
                 cap_ceiling, games, contract_seasons):
        self.start_date = start_date
        self.start_playoffs = start_playoffs
        self.end_playoffs = end_playoffs
        self.cap_floor = cap_floor
        self.cap_ceiling = cap_ceiling
        self.games = games
        self.contract_seasons = contract_seasons

    def __repr__(self):
        return '<id {}>'.format(self.id)