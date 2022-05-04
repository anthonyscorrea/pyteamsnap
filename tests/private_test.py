import unittest
from teamsnap import TeamSnap
from teamsnap.api import Team, Event, Availability, Me, ApiObject
from os import getenv

TEAMSNAP_TOKEN = getenv('TEAMSNAP_TOKEN')
TEAMSNAP_TEAM = getenv('TEAMSNAP_TEAM')
TEAMSNAP_EVENT = getenv('TEAMSNAP_EVENT')

c = TeamSnap(token=TEAMSNAP_TOKEN)
es = Event.search(c, team_id=TEAMSNAP_TEAM)
q1 = c.query("events", "search", team_id=TEAMSNAP_TEAM)
team = c.teams.get(TEAMSNAP_TEAM)
event = c.events.get(TEAMSNAP_EVENT)
col = c.get_collection(rel="events", id=TEAMSNAP_TEAM)
pass
# q2 = c.events.search(team_id=TEAM_ID)
# a = c.availabilities.search(event_id=q2[0]['id'])
# print(q1==q2)
