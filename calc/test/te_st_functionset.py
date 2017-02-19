from unittest import TestCase

from calculator import Operator
from calculator import Token

from calc.functionset import get_function


class TestFunctionset(TestCase):

    def test_function_exists(self):
        f = get_function('max')
        self.assertIs(True, callable(f))


    def test_operator_calculate(self):
        op = Operator('max', 2,0,'L',None)
        self.assertIsNone(op.calculate)
        f = get_function('max')
        op.calculate = f
        self.assertIsNotNone(op.calculate)
        tok1 = Token('NUM', 100)
        tok2 = Token('NUM', 200)
        tok3 = op.calculate(tok1, tok2)
        self.assertEqual(tok2, tok3)