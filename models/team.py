from app import db

class Team(db.Model):
    __tablename__ = 'teams'

    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(3))
    name = db.Column(db.String)
    contracts = db.relationship('Contract', backref='teams', lazy=True)
    employments = db.relationship('Employment', backref='teams', lazy=True)
    draft_picks = db.relationship('DraftPick', backref='teams', lazy=True)
    team_games = db.relationship('TeamGame', backref='teams', lazy=True)

    def __init__(self, code, name, contracts, employments, draft_picks, team_games):
        self.code = code
        self.name = name
        self.contracts = contracts
        self.employments = employments
        self.draft_picks = draft_picks
        self.team_games = team_games

    def __repr__(self):
        return '<id {}>'.format(self.id)