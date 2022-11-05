from tests.base import BaseModelTestCase
from unittest import TestCase
from pyteamsnap.models import User, Me


class TestUser(BaseModelTestCase, TestCase):
    __test__ = True
    TestClass = User

    def test_data(self):
        with self.cassette:
            instance = Me(self.client)
        self.assertIsInstance(instance, User)
        self.assertTrue(len(instance.data))
        pass
