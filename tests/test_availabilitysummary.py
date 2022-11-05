from tests.base import BaseModelTestCase
from unittest import TestCase
from pyteamsnap.models import AvailabilitySummary

class TestAvailabilitySummary(BaseModelTestCase, TestCase):
    __test__ = True
    TestClass = AvailabilitySummary
