from app import db

class Player(db.Model):
    __tablename__ = 'players'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    dob = db.Column(db.Date)
    country_born = db.Column(db.String)
    height_cm = db.Column(db.Float)
    weight_kg = db.Column(db.Float)
    contracts = db.relationship('Contract', backref='players', lazy=True)
    employments = db.relationship('Employment', backref='players', lazy=True)
    player_games = db.relationship('PlayerGame', backref='players', lazy=True)
    draft_picks = db.relationship('DraftPick', uselist=False, back_populates='players')

    def __init__(self, first_name, last_name, dob, country_born, height_cm, weight_kg, contracts, employments, player_games):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.country_born
        self.height_cm = height_cm
        self.weight_kg = weight_kg
        self.contracts = contracts
        self.employments = employments
        self.player_games = player_games

    def __repr__(self):
        return '<id {}>'.format(self.id)