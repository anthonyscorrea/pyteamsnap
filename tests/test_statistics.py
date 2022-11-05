from tests.base import BaseModelTestCase
from unittest import TestCase
from pyteamsnap.models import Statistics


class TestStatistics(BaseModelTestCase, TestCase):
    __test__ = True
    TestClass = Statistics
