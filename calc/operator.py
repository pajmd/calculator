
class Operator(object):
    def __init__(self, name, precedence, arity, associativity, calculate, function='N'):
        """

        :rtype: object
        """
        self.name = name
        self.precedence = precedence
        self.arity = arity
        self.associativity = associativity
        self.function = function
        self.calculate = calculate

    @classmethod
    def from_string(cls, strform):
        '''
        creates an operator from a string

        ex:strform='+,2,2,R'
        '''
        parts = strform.split(',')
        return cls({part for part in parts})

    def __repr__(self):
        return 'Oprator({}, {}, {}, {}'.format(self.name, self.precedence, self.arity, self.associativity)

    def __str__(self):
        return self.name
