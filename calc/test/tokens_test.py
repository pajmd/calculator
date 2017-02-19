import unittest
from ..token_items import TokenNum
from ..tokens import Tokens

class TestTokens(unittest.TestCase):
    def setUp(self):
        self.tokens = Tokens()

    def test_add_token(self):
        self.tokens.append(TokenNum('3'))
        self.assertEqual(1, len(self.tokens))