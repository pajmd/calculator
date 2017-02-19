SEPARATOR = ','

class Token(object):
    def __init__(self, token_type, val):
        '''
        Initializes a token a number NUM with a number as a value or as an operator OP and an Operator as a value
        :param token_type:
        :param val:
        '''
        self.token_type = token_type
        self.val = val

    def is_number(self):
        return self.token_type == 'NUM'

    def get_precedence(self):
        if self.token_type == 'OP':
            return self.val.precedence
        else:
            return None

    def is_right_parenthesis(self):
        if self.token_type == 'OP':
            return self.val.name == ')'

    def is_left_parenthesis(self):
        if self.token_type == 'OP':
            return self.val.name == '('

    def is_separator(self):
        if self.token_type == 'OP':
            return self.val.name == SEPARATOR

    def is_function(self):
        if self.token_type == 'OP':
            return self.val.function == 'Y'

    def __repr__(self):
        token_val = ''
        if self.token_type == 'NUM':
            token_val = self.val
        else:
            token_val = self.val.name
        return 'Token( {}, "{}")'.format(self.token_type, token_val)

    def __eq__(self, other):
        '''other should be a Token'''
        if not isinstance(other, Token):
            return False
        return self.val == other.val and self.token_type == other.token_type

    def __ne__(self, other):
        if not isinstance(other, Token):
            return True
        return self.val != other.val or self.token_type != other.token_type

    def __hash__(self):
        return hash(self.token_type, self.val)


class TokenNum(Token):
    def __init__(self, val):
        super(TokenNum, self).__init__('NUM', val)


class TokenOp(Token):
    def __init__(self, val):
        super(TokenOp, self).__init__('OP', val)