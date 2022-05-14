import unittest
from pyteamsnap import TeamSnap
from pyteamsnap.api import Team, Event, Availability, Me, ApiObject, Member
from os import getenv

TEAMSNAP_TOKEN = getenv('TEAMSNAP_TOKEN')
TEAMSNAP_TEAM = getenv('TEAMSNAP_TEAM')
TEAMSNAP_EVENT = getenv('TEAMSNAP_EVENT')

c = TeamSnap(token=TEAMSNAP_TOKEN)
c.bulk_load(team_id=TEAMSNAP_TEAM,types=[Event, Member])

pass
# q2 = c.events.search(team_id=TEAM_ID)
# a = c.availabilities.search(event_id=q2[0]['id'])
# print(q1==q2)
