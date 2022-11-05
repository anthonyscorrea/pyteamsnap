import unittest

from tests.base import BaseModelTestCase
from unittest import TestCase
from pyteamsnap.models import EventLineupEntry, Event

@unittest.skip("EventLineupEntry Test Known to Fail, need to figure out how to filter events that have a lineup and therefore entries")
class TestEventLineupEntry(BaseModelTestCase, TestCase):
    __test__ = True
    TestClass = EventLineupEntry

    def test_data(self):
        with self.cassette:
            event_search_results = Event.search(self.client, team_id=self.TEAMSNAP_TEAM)
            event_instance = event_search_results[0]
            search_results = self.TestClass.search(self.client, event_id=event_instance.id)
        instance = search_results[0]
        self.assertIsInstance(instance, self.TestClass)
        self.assertTrue(len(instance.data))
        return instance
