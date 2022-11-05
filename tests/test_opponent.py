from tests.base import BaseModelTestCase
from unittest import TestCase
from pyteamsnap.models import Opponent


class TestOpponent(BaseModelTestCase, TestCase):
    __test__ = True
    TestClass = Opponent
