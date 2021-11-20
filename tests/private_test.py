import unittest
from credentials import team_id as TEAM_ID
from credentials import token as TOKEN
from teamsnap import TeamSnap
from teamsnap.models import Item
from teamsnap.api import Team, Event, Availability, Me, ApiObject
import teamsnap
TEAM_ID = 7644001
EVENT_1 = 239261604

c = TeamSnap(token=TOKEN)
es = Event.search(c, team_id=TEAM_ID)
q1 = c.query("events", "search", team_id=TEAM_ID)
team = c.teams.get(TEAM_ID)
event = Item(client=c, rel="events", id=EVENT_1)
# event = c.events.get(239261604)
col = c.get_collection(rel="events", id=EVENT_1)
print(event.data)
pass
# q2 = c.events.search(team_id=TEAM_ID)
# a = c.availabilities.search(event_id=q2[0]['id'])
# print(q1==q2)
