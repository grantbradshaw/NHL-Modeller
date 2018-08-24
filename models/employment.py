from app import db

class Employment(db.Model):
    # table representing a period of employment between a player and a team
    __tablename__ = 'employments'

    id = db.Column(db.Integer, primary_key=True)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    # team employing player for this time range
    team_id = db.Column(db.Integer, db.ForeignKey('teams.id'), nullable=False)
    player_id = db.Column(db.Integer, db.ForeignKey('players.id'), nullable=False)

    def __init__(self, start_date, end_date, team_id, player_id):
        self.start_date = start_date
        self.end_date = end_date
        self.team_id = team_id
        self.player_id = player_id

    def __repr__(self):
        return '<id {}>'.format(self.id)