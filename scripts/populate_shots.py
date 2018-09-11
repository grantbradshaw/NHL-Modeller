import json, sys, os
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))

import pprint
pp = pprint.PrettyPrinter(indent=1)

# this script just to explore json

with open('data/shots/20172018/2017020001.json') as f:
    data = json.load(f)


pp.pprint(data['liveData'])

# pp.pprint(data['liveData']['plays']['allPlays'])

# events = []
# for event in data['liveData']['plays']['allPlays']:
#     event_id = event['result']['eventTypeId']
#     if event_id not in events:
#         events.append(event_id)

# print(events)

# events available for games are,
# ['GAME_SCHEDULED', 'PERIOD_READY', 'PERIOD_START', 'FACEOFF',
# 'BLOCKED_SHOT', 'SHOT', 'HIT', 'STOP', 'MISSED_SHOT', 'GIVEAWAY',
# 'PENALTY', 'GOAL', 'PERIOD_END', 'PERIOD_OFFICIAL', 'TAKEAWAY', 'GAME_END']
