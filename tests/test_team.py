from tests.base import BaseModelTestCase
from unittest import TestCase
from pyteamsnap.models import Team


class TestTeam(BaseModelTestCase, TestCase):
    __test__ = True
    TestClass = Team

    def test_data(self):
        instance = super().test_data()
        self.assertEqual(instance.id, self.TEAMSNAP_TEAM)
        # assertDictContainsSubset is deprecated
        # https://stackoverflow.com/a/59777678
        self.assertEqual(instance.data["id"], self.TEAMSNAP_TEAM)
