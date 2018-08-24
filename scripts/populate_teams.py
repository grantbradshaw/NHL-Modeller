import json, sys, os
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))

from app import db
from models.team import Team

with open('data/teams.json') as f:
    data = json.load(f)


def load_teams():
    for key in data:
        try:
            team = Team(code=key, name=data[key]['name'], contracts=[], employments=[], draft_picks = [], team_games=[])
            db.session.add(team)
        except:
            raise Exception('Could not enter team')
    db.session.commit()

load_teams()






