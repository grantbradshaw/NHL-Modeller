from app import db

class ContractSeason(db.Model):
    __tablename__ = 'contract_seasons'

    id = db.Column(db.Integer, primary_key=True)
    # player salary is signing_bonus + base_salary, then performance bonuses are computed
    signing_bonus = db.Column(db.Integer)
    base_salary = db.Column(db.Integer)
    max_performance_bonus = db.Column(db.Integer)
    minors_salary = db.Column(db.Integer)
    # season being reflected in the entry
    season = db.Column(db.Integer, db.ForeignKey('seasons.id'), nullable=False)
    # contract this season occurs in
    contract = db.Column(db.Integer, db.ForeignKey('contracts.id'), nullable=False)

    def __init__(self, signing_bonus, performance_bonus, base_salary, minors_salary, season, contract):
        self.signing_bonus = signing_bonus
        self.performance_bonus = performance_bonus
        self.base_salary = base_salary
        self.minors_salary = minors_salary
        self.season = season
        self.contract = contract

    def __repr__(self):
        return '<id {}>'.format(self.id)