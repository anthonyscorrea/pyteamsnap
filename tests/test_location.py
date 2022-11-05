from tests.base import BaseModelTestCase
from unittest import TestCase
from pyteamsnap.models import Location


class TestLocation(BaseModelTestCase, TestCase):
    __test__ = True
    TestClass = Location
