from tests.base import BaseModelTestCase
from unittest import TestCase
from pyteamsnap.models import Availability


class TestAvailability(BaseModelTestCase, TestCase):
    __test__ = True
    TestClass = Availability


