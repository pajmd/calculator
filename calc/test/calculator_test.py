import unittest
from ..calculator import calculate
from ..token_items import Token


class TestCalculatorParser(unittest.TestCase):
    def setUp(self):
        self.expression = '9+24/(7-3)'
        self.expected_outputqueue = ['9', '24', '7', '3', '-', '/', '+']

#    def test_should_be_able_to_parse(self):
#        self.assertEqual(self.expected_outputqueue, parser.parse(self.expression))


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

    def test_simple_calculate_with_function_arity_gt_2(self):
        expression = '9+24/(7-3)+max(100,sum(200,100))+sum(1,2,3,4,5)'
        res = calculate(expression)
        self.assertEqual(Token('NUM', '330.0'), res)

    def test_simple_calculate_starting_with_parenthesis(self):
        expression = '(9+24/(7-3))*2'
        res = calculate(expression)
        self.assertEqual(Token('NUM', '15.0'), res)

if __name__ == '__main__':
    unittest.main()
