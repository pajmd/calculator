import unittest
from ..token_items import TokenNum
from ..tokens import Tokens

class TestTokens(unittest.TestCase):
    def setUp(self):
        self.tokens = Tokens()

    def test_add_token(self):
        self.tokens.append(TokenNum('3'))
        self.assertEqual(1, len(self.tokens))

    def test_add_none_token_raise_exception(self):
        with self.assertRaises(TypeError) as cm:
            self.tokens.append('stuff')
        ex = cm.exception
        self.assertEqual('Not a Token', ex.message)