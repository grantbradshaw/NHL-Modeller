# file should be converted to not execute directly, thus removing line below

import re, json, os, sys, urllib.request
# from requests import get
# from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))

import pprint
pp = pprint.PrettyPrinter(indent=1)

seasons = []

# takes first season to start scraping (for this data set, 2011) and should end with last season data available for
# years are passed in as first half of season (for instance, 2011 is the 2011-2012 season)
def save_seasons(end_season, start_season=2011):
    current_season = start_season
    while current_season <= end_season:
        season_string = str(current_season) + str(current_season + 1)
        url = 'http://live.nhl.com/GameData/SeasonSchedule-{0}.json'.format(season_string)
        with urllib.request.urlopen(url) as f:
            data = json.loads(f.read().decode())

        filename = 'data/shots/{0}/season_overview.json'.format(season_string)
        os.makedirs(os.path.dirname(filename), exist_ok = True)
        with open(filename, 'w') as fr:
            json.dump(data, fr)

        seasons.append(filename)

        current_season += 1

# takes seasons scraped already, and saves all of the relevant games
def save_games():
    for season_file in seasons:
        with open(season_file) as f:
            season = json.load(f)

        for game in season:
            game_id = str(game['id'])
            url = 'http://statsapi.web.nhl.com/api/v1/game/{0}/feed/live'.format(game_id)
            with urllib.request.urlopen(url) as f:
                data = json.loads(f.read().decode())

            filename = season_file.replace('season_overview', game_id)

            with open(filename, 'w') as fr:
                json.dump(data, fr)



save_seasons(2017)
save_games()