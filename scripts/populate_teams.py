import json, sys, os
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))

from app import db
from models.team import Team

with open('data/teams.json') as f:
    data = json.load(f)


def load_teams():
    for key in data:
        try:
            team = Team(name=data[key]['name'], code=key, contracts=[])
            db.session.add(team)
        except:
            return False
    db.session.commit()

load_teams()






