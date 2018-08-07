from app import db

class Team(db.Model):
    __tablename__ = 'teams'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    code = db.Column(db.String(3))
    contracts = db.relationship('Contract', backref='team', lazy=True)


    def __init__(self, name, code, contracts):
        self.name = name
        self.code = code
        self.contracts = contracts

    def __repr__(self):
        return '<id {}>'.format(self.id)