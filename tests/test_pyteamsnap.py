#!/usr/bin/env python

"""Tests for `pyteamsnap` package."""


import unittest

from pyteamsnap import client
from os import getenv
TEAMSNAP_TOKEN = getenv('TEAMSNAP_TOKEN')
TEAMSNAP_TEAM = getenv('TEAMSNAP_TEAM')
TEAMSNAP_EVENT = getenv('TEAMSNAP_EVENT')

class TestPyteamsnap(unittest.TestCase):
    """Tests for `pyteamsnap` package."""

    def setUp(self):
        """Set up test fixtures, if any."""
        self.TEAMSNAP_TOKEN = getenv('TEAMSNAP_TOKEN')
        self.TEAMSNAP_TEAM = getenv('TEAMSNAP_TEAM')
        self.TEAMSNAP_EVENT = getenv('TEAMSNAP_EVENT')

        self.client = client.TeamSnap(token=TEAMSNAP_TOKEN)

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_me(self):
        """Test something."""
        from pyteamsnap.objects import Me
        me = Me(self.client)
        pass

    def test_001_bulk_load(self):
        from pyteamsnap.objects import Event
        events = self.client.bulk_load(team_id=self.TEAMSNAP_TEAM, types=[objects.Event])
        pass
