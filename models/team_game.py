from app import db

class TeamGame(db.Model):
    __tablename__ = 'team_games'

    id = db.Column(db.Integer, primary_key=True)
    home = db.Column(db.Boolean)
    goals = db.Column(db.Integer)
    game_id = db.Column(db.Integer, db.ForeignKey('games.id'), nullable=False)
    team_id = db.Column(db.Integer, db.ForeignKey('teams.id'), nullable=False)
    player_games = db.relationship('PlayerGame', backref='team_games', lazy=True)

    def __init__(self, home, goals, game_id, team_id, player_games):
        self.home = home
        self.goals = goals
        self.game_id = game_id
        self.team_id = team_id
        self.player_games = player_games

    def __repr__(self):
        return '<id {}>'.format(self.id)