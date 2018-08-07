from app import db

class Contract(db.Model):
    __tablename__ = 'contracts'

    id = db.Column(db.Integer, primary_key=True)
    # indicates the team which signed the contract
    team_id = db.Column(db.Integer, db.ForeignKey('teams.id'), nullable=False)
    # indicates the player who signed the contract
    player_id = db.Column(db.Integer, db.ForeignKey('players.id'), nullable=False)
    start_date = db.Column(db.DateTime)
    years = db.Column(db.Integer)



    def __init__(self, team_id, player_id, start_date, years):
        self.team_id = team_id
        self.player_id = player_id
        self.start_date = start_date
        self.years = years

    def __repr__(self):
        return '<id {}>'.format(self.id)