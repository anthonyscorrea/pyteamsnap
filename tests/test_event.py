from tests.base import BaseModelTestCase
from unittest import TestCase
from pyteamsnap.models import Event


class TestEvent(BaseModelTestCase, TestCase):
    __test__ = True
    TestClass = Event
