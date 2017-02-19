import unittest
from ..calculator import calculate
from ..token_items import Token
from ..data_store import DataStore


class TestCalculatorParser(unittest.TestCase):
    def setUp(self):
        self.expression = '9+24/(7-3)'
        self.expected_outputqueue = ['9', '24', '7', '3', '-', '/', '+']
        dico = {
            'AA' : '1',  # check tokeniser if argument contains number like PARAM_01
            'BB' : '2',
            'CCC' : '3',
            'D4' : '4',
            'E55' : '5',
            'SERIES1' : ['1', '2', '3'],
            'SERIES2': ['11', '12', '13']
        }
        DataStore(dico)
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

    def test_calculate_with_function_arity_gt_2(self):
        expression = '9+24/(7-3)+max(100,sum(200,100))+sum(1,2,3,4,5)'
        res = calculate(expression)
        self.assertEqual(Token('NUM', '330.0'), res)

    def test_simple_calculate_starting_with_parenthesis(self):
        expression = '(9+24/(7-3))*2'
        res = calculate(expression)
        self.assertEqual(Token('NUM', '30.0'), res)

    def test_calculate_with_function_arity_gt_2_starting_with_parenthesis(self):
        expression = '(9+24/(7-3)+max(100,sum(200,100))+sum(1,2,3,4,5))*(5-3)'
        res = calculate(expression)
        self.assertEqual(Token('NUM', '660.0'), res)

    def test_calculate_add_with_variable(self):
        expression = '9+AA'
        res = calculate(expression)
        self.assertEqual(Token('NUM', '10.0'), res)

    def test_calculate_add_with_variable_first_argument(self):
        expression = 'BB+9'
        res = calculate(expression)
        self.assertEqual(Token('NUM', '11.0'), res)

    def test_calculate_add_with_two_variable(self):
        expression = 'BB+AA'
        res = calculate(expression)
        self.assertEqual(Token('NUM', '3.0'), res)

    def test_calculate_sum_with_variables(self):
        expression = 'sum(BB,AA,CCC)'
        res = calculate(expression)
        self.assertEqual(Token('NUM', '6.0'), res)

    def test_calculate_sum_with_variable_containg_didgit(self):
        expression = 'sum(BB,AA,CCC,D4)'
        res = calculate(expression)
        self.assertEqual(Token('NUM', '10.0'), res)

    def test_calculate_function_and_operators_with_variables(self):
        expression = '2*sum(BB,AA,CCC,D4)+E55'
        res = calculate(expression)
        self.assertEqual(Token('NUM', '25.0'), res)

    def test_calculate_series_variables(self):
        expression = 'SERIES1+SERIES2'
        res = calculate(expression)
        expected = ['12.0', '14.0', '16.0']
        self.assertEqual(Token('NUM', expected), res)

if __name__ == '__main__':
    unittest.main()
