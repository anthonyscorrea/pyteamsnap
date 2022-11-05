from tests.base import BaseModelTestCase
from unittest import TestCase
from pyteamsnap.models import Me, User


class TestMe(BaseModelTestCase, TestCase):
    def test_data(self):
        with self.cassette:
            instance = Me(self.client)
        self.assertIsInstance(instance, User)
        self.assertTrue(len(instance.data))
        pass
