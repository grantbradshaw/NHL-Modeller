from app import db

class DraftPick(db.Model):
    __tablename__ = 'draft_picks'

    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Date)
    overall_selected = db.Column(db.Integer)
    round_selected = db.Column(db.Integer)
    # team which made this draft pick
    team_id = db.Column(db.Integer, db.ForeignKey('teams.id'), nullable=False)
    # player selected, 1-1 relationship
    player_id = db.Column(db.Integer, db.ForeignKey('players.id'), nullable=False)
    players = db.relationship('Player', back_populates='draft_picks')

    def __init__(self, year, overall_selected, round_selected, team_id, player_id):
        self.year = year
        self.overall_selected
        self.round_selected = round_selected
        self.team_id = team_id
        self.player_id = player_id

    def __repr__(self):
        return '<id {}>'.format(self.id)