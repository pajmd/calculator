import functions
from .operator import Operator

operators = {
    '+': Operator(name='+', precedence=2, arity=2, associativity='L', calculate=functions.add),
    '-': Operator(name='-', precedence=2, arity=2, associativity='L', calculate=functions.substact),
    '*': Operator(name='*', precedence=3, arity=2, associativity='L', calculate=functions.multiply),
    '/': Operator(name='/', precedence=3, arity=2, associativity='L', calculate=functions.divide),
    '(': Operator(name='(', precedence=0, arity=0, associativity='L', calculate=functions.nothing),
    ')': Operator(name=')', precedence=0, arity=0, associativity='L', calculate=functions.nothing),
    ',': Operator(name=',', precedence=0, arity=0, associativity='L', calculate=functions.nothing),
    'max': Operator(name='max', precedence=4, arity=2, associativity='L', calculate=functions.max, function='Y'),
    'sum': Operator(name='sum', precedence=4, arity=0, associativity='L', calculate=functions.sum, function='Y')
}
