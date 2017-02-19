from .token_items import Token

class Tokens(object):
    def __init__(self):
        self.tokens = []

    def __len__(self):
        return len(self.tokens)

    def __getitem__(self, n):
        return self.tokens[n]

    def __iter__(self):
        return self.tokens.__iter__()

    def __repr__(self):
        return self.tokens

    def append(self,token):
        if isinstance(token, Token):
            self.tokens.append(token)
        else:
            raise TypeError('Not a Token')

    def last_token(self):
        if len(self.tokens) != 0:
            return self.tokens[len(self.tokens) -1 ]

    def is_last_token_argument(self):
        if len(self.tokens) != 0:
            return self.tokens[len(self.tokens) - 1].is_argument()
