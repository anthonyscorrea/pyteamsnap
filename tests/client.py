#!/usr/bin/env python

"""Tests for `pyteamsnap` package."""


import unittest
from unittest import TestCase

from pyteamsnap import client
from os import getenv
from pyteamsnap.models.base import BaseApiObject
import vcr
TEAMSNAP_TOKEN = getenv('TEAMSNAP_TOKEN')
TEAMSNAP_TEAM = getenv('TEAMSNAP_TEAM')
TEAMSNAP_EVENT = getenv('TEAMSNAP_EVENT')

vcr_options = {
    'decode_compressed_response': True,
    'cassette_library_dir':'tests/fixtures/cassettes',
    'filter_headers':['authorization']
}

class ClientTestCase(TestCase):
    """Tests for `pyteamsnap` package."""

    @classmethod
    def setUpClass(cls) -> None:
        """Set up test fixtures, if any."""
        cls.TEAMSNAP_TOKEN = getenv('TEAMSNAP_TOKEN')
        cls.TEAMSNAP_TEAM = int(getenv('TEAMSNAP_TEAM'))
        cls.TEAMSNAP_EVENT = getenv('TEAMSNAP_EVENT')
        with vcr.use_cassette("client.yml", **vcr_options):
            cls.client = client.TeamSnap(token=TEAMSNAP_TOKEN)
        cls.cassette = vcr.use_cassette(f"{cls.__name__}.yml", **vcr_options)
        super().setUpClass()


    def test_bulkload(self):
        from pyteamsnap.models import Event, EventLineup, EventLineupEntry, AvailabilitySummary, Member
        with self.cassette:
            bulk_load = self.client.bulk_load(
                team_id=self.TEAMSNAP_TEAM,
                event__id=self.TEAMSNAP_EVENT,
                types=[
                    Event,
                    EventLineup,
                    EventLineupEntry,
                    AvailabilitySummary,
                    Member
                ])

        self.assertIsInstance(bulk_load, list)
        return bulk_load


