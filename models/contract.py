from app import db

class Contract(db.Model):
    __tablename__ = 'contracts'

    id = db.Column(db.Integer, primary_key=True)
    sign_date = db.Column(db.Date)
    # indicates the team which signed the contract
    team_id = db.Column(db.String(3), db.ForeignKey('teams.id'), nullable=False)
    # indicates the player who signed the contract
    player_id = db.Column(db.Integer, db.ForeignKey('players.id'), nullable=False)
    # all seasons in this contract
    contract_seasons = db.relationship('ContractSeason', backref='contracts', lazy=True)

    def __init__(self, sign_date, team_id, player_id, start_season, contract_seasons):
        self.sign_date = sign_date
        self.team_id = team_id
        self.player_id = player_id
        self.start_season = start_season
        self.contract_seasons = contract_seasons

    def __repr__(self):
        return '<id {}>'.format(self.id)