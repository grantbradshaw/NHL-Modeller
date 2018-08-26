import json, sys, os, datetime
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))

from app import db
from models.season import Season

with open('data/seasons.json') as f:
    data = json.load(f)

def load_seasons():
    for key in data.keys():
        try:
            start_date = data[key]['Start Date']
            if start_date: # keep empy string if no date
                # takes date of form 'yyyy-mm-dd', no leading 0
                date_list = start_date.split('-')
                start_date = datetime.datetime(int(date_list[0]),
                                               int(date_list[1]),
                                               int(date_list[2]))
            else:
                start_date = None

            start_playoffs = data[key]['Start Playoffs']
            if start_playoffs:
                date_list = start_playoffs.split('-')
                start_playoffs = datetime.datetime(int(date_list[0]),
                                               int(date_list[1]),
                                               int(date_list[2]))
            else:
                start_playoffs = None

            end_playoffs = data[key]['End Playoffs']
            if end_playoffs:
                date_list = end_playoffs.split('-')
                end_playoffs = datetime.datetime(int(date_list[0]),
                                               int(date_list[1]),
                                               int(date_list[2]))
            else:
                end_playoffs = None

            season = Season(start_date = start_date,
                            start_playoffs = start_playoffs,
                            end_playoffs = end_playoffs,
                            cap_floor = data[key]['Cap Floor'],
                            cap_ceiling = data[key]['Cap Ceiling'],
                            games = data[key]['Games'],
                            contract_seasons = [])
            db.session.add(season)
        except:
            raise Exception('At least one season(s) could not be added, none commited to database')
    db.session.commit()

load_seasons()