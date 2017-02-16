import unittest
#from calculator.parser import parse
from ..parser import get_operator
from ..parser import locate_error
from ..parser import calculate
from ..token_items import Token
#import ..parser

class TestCalculatorParser(unittest.TestCase):
    def setUp(self):
        self.expression = '9+24/(7-3)'
        self.expected_outputqueue = ['9','24','7','3','-','/','+']

#    def test_should_be_able_to_parse(self):
#        self.assertEqual(self.expected_outputqueue, parser.parse(self.expression))

    def test_operator_exists(self):
        self.assertIsNotNone(get_operator('+'))


    def test_operator_does_not_exist(self):
        self.assertIsNone(get_operator('~'))


    def test_error_location(self):
        token = ['4','+','3',')','-','1']
        err = locate_error(token, 3)
        self.assertIsNotNone(err)


    def test_simple_calculate(self):
        expression = '9+24/(7-3)'
        res = calculate(expression)
        self.assertEqual(Token('NUM', '15.0'), res)


    def test_simple_calculate_with_function(self):
        expression = '9+24/(7-3)+max(100,200)'
        res = calculate(expression)
        self.assertEqual(Token('NUM', '215.0'), res)


    def test_simple_calculate_with_function_in_function(self):
        expression = '9+24/(7-3)+max(100,sum(200,100))'
        res = calculate(expression)
        self.assertEqual(Token('NUM', '315.0'), res)

if __name__ == '__main__':
    unittest.main()

