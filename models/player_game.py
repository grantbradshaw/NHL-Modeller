from app import db

class PlayerGame(db.Model):
    __tablename__ = 'player_games'

    id = db.Column(db.Integer, primary_key=True)
    toi = db.Column(db.Float)
    goals = db.Column(db.Integer)
    assists = db.Column(db.Integer)
    position = db.Column(db.String) # Contrain to only valid positions
    sv_percentage = db.Column(db.Integer) # Contstrain to only if position is goalie
    player_id = db.Column(db.Integer, db.ForeignKey('players.id'), nullable=False)
    team_game_id = db.Column(db.Integer, db.ForeignKey('team_games.id'), nullable=False)

    def __init__(self, toi, goals, assists, position, sv_percentage, player_id, team_game_id):
        self.toi = toi
        self.goals = goals
        self.assists = assists
        self.position = position
        self.sv_percentage = sv_percentage
        self.player_id = player_id
        self.team_game_id = team_game_id

    def __repr__(self):
        return '<id {}>'.format(self.id)