import unittest
from ..tokeniser import get_operator


class TestTokenItems(unittest.TestCase):
    def setUp(self):
        pass

    def test_operator_exists(self):
        self.assertIsNotNone(get_operator('+'))

    def test_operator_does_not_exist(self):
        self.assertIsNone(get_operator('~'))
