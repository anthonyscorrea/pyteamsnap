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

class BaseModelTestCase:
    """Tests for `pyteamsnap` package."""
    __test__= False
    TestClass: BaseApiObject = None

    @classmethod
    def setUpClass(cls) -> None:
        """Set up test fixtures, if any."""
        cls.TEAMSNAP_TOKEN = getenv('TEAMSNAP_TOKEN')
        cls.TEAMSNAP_TEAM = int(getenv('TEAMSNAP_TEAM'))
        with vcr.use_cassette("client.yml", **vcr_options):
            cls.client = client.TeamSnap(token=TEAMSNAP_TOKEN)
        cls.cassette = vcr.use_cassette(f"{cls.__name__}.yml", **vcr_options)
        super().setUpClass()


    def test_data(self):
        with self.cassette:
            search_results = self.TestClass.search(self.client, team_id=self.TEAMSNAP_TEAM)
        instance = search_results[0]
        self.assertIsInstance(instance, self.TestClass)
        self.assertTrue(len(instance.data))
        return instance


