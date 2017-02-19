import unittest
from ..error_locator import locate_error

class TestErrorLocator(unittest.TestCase):
    def setUp(self):
        self.expression = '9+24/(7-3)'
        self.expected_outputqueue = ['9','24','7','3','-','/','+']


    def test_error_location(self):
        token = ['4','+','3',')','-','1']
        err = locate_error(token, 3)
        self.assertIsNotNone(err)