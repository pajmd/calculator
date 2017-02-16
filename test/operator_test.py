import unittest
#from calculator.parser import parse
from ..parser import Operator
from ..functionset import get_function
#import ..parser

class TestCalculatorParser(unittest.TestCase):
    def setUp(self):
        pass

#    def test_should_be_able_to_parse(self):
#        self.assertEqual(self.expected_outputqueue, parser.parse(self.expression))

    def test_function_exists(self):
        self.assertIs(True, callable(get_function('max')))





if __name__ == '__main__':
    unittest.main()

