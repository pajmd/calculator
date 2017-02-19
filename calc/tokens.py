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
        else:
            raise IndexError('Token list is Empty')

    def last_token_value(self):
        if len(self.tokens) != 0:
            return self.tokens[len(self.tokens) -1 ].val
        else:
            raise IndexError('Token list is Empty')

    def last_token_concatenate_value(self, c):
        if len(self.tokens) != 0:
            self.tokens[len(self.tokens) -1 ].val += c
        else:
            raise IndexError('Token list is Empty')

    def is_last_token_argument(self):
        if len(self.tokens) != 0:
            return self.tokens[len(self.tokens) - 1].is_argument()
        else:
            raise IndexError('Token list is Empty')

    def is_last_token_number(self):
        if len(self.tokens) != 0:
            return self.tokens[len(self.tokens) - 1].is_number()
        else:
            raise IndexError('Token list is Empty')
