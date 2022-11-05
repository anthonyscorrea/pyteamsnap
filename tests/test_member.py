from tests.base import BaseModelTestCase
from unittest import TestCase
from pyteamsnap.models import Member


class TestMember(BaseModelTestCase, TestCase):
    __test__ = True
    TestClass = Member
