import json, sys, os, re
from scrape_contracts import get_contract_index_pages
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))

import pprint
pp = pprint.PrettyPrinter(indent=1)

from app import db
from models.contract import Contract
from models.contract_season import ContractSeason
from models.player import Player
from models.draft_pick import DraftPick


contract_data = get_contract_index_pages()
# pp.pprint(contract_data[list(contract_data.keys())[0]])

with open('data/teams.json') as f:
    team_dict = json.load(f)

# method to confirm that
def check_data_validity():
    processor = {
            'Birthplace': closure_creator(1, '^[A-Za-z, ]+$'),
            'Born': closure_creator(1, '^[A-Z][a-z]+\ [0-9]{1,2},\ [0-9]{4}'),
            'Draft Round': closure_creator(1, '^[0-9]{1,2}$'),
            'Draft Year': closure_creator(1, '^[0-9]{4}$'),
            'Drafted By': closure_creator(2, list(team_dict.keys())),
            'Drafted Overall': closure_creator(1, '^[0-9]{1,3}$'),
            'Elc Signing Age': closure_creator(1, '^[0-9]{1,2}$'),
            'Height': closure_creator(1, '^[0-9]\'\ ?[0-9]{1,2}\ \([0-9]{3}\ cm\)$'),
            'Shoots': closure_creator(2, ['Left', 'Right']),
            'Catches': closure_creator(2, ['Left', 'Right']),
            'Waivers Signing Age': closure_creator(1, '^[0-9]{2}$'),
            'Weight': closure_creator(1, '^[0-9]{3}\ lbs\ \([0-9]{2,3}\ kg\)$'),
            'name': closure_creator(1, '^[A-Za-z0-9\',\(\):\.\ ]+$')
        }
    for key in contract_data:
        player = contract_data[key] # index to player in dictionary
        for check in processor:
            if check not in player:
                # goalies only have 'catches', players only have 'shoots'
                if (check == 'Shoots' and 'Catches' in player) or (check == 'Catches' and 'Shoots' in player):
                    continue
                print(check)
                pp.pprint(player)
                raise Exception('Key not present')
            else:
                if not processor[check](player[check]):
                    print(check)
                    pp.pprint(player)
                    raise Exception('Data invalid')


def closure_creator(flag, value):
    if flag == 1:
        def confirm_regex_match(string):
            return re.match(value, string)
        return confirm_regex_match
    elif flag == 2:
        def confirm_in_list(string):
            return string in value
        return confirm_in_list

check_data_validity()



