SEPARATOR = ','
NUM = 'NUM'
ARG = 'ARG'
OP = 'OP'


class Token(object):
    def __init__(self, token_type, val):
        '''
        Initializes a token with type and value, posible types number NUM, operator OP, function argument ARG
        :param token_type:
        :param val:
        '''
        self.token_type = token_type
        self.val = val

    def argument_to_function(self, op):
        self.token_type = OP
        self.val = op

    def get_precedence(self):
        if self.token_type == OP:
            return self.val.precedence
        else:
            return None

    def is_number(self):
        return self.token_type == NUM

    def is_argument(self):
        return self.token_type == ARG

    def is_right_parenthesis(self):
        if self.token_type == OP:
            return self.val.name == ')'

    def is_left_parenthesis(self):
        if self.token_type == OP:
            return self.val.name == '('

    def is_separator(self):
        if self.token_type == OP:
            return self.val.name == SEPARATOR

    def is_function(self):
        if self.token_type == OP:
            return self.val.function == 'Y'

    def __repr__(self):
        token_val = ''
        if self.token_type == NUM:
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
        super(TokenNum, self).__init__(NUM, val)


class TokenOp(Token):
    def __init__(self, val):
        super(TokenOp, self).__init__(OP, val)

class TokenArg(Token):
    def __init__(self, val):
        super(TokenArg, self).__init__(ARG, val)