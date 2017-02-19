from .token_items import Token
from .data_store import DataStore

def add(*args):
    for arg in args:
        if arg.is_argument():
            arg.val  = DataStore.get_argument_value(arg)
    if isinstance(args[0].val, list):
        # [str(float(v1) + float(v2)) for v1, v2 in zip(self.SERIES1, self.SERIES2)]
        l0 = args[0].val
        l1 = args[1].val
        l =  [str(float(v1)+float(v2)) for v1,v2 in zip(l0, l1)]
        return Token('NUM', l)
    else:
        return Token('NUM', str(float(args[0].val) + float(args[1].val)))


def substact(*args):
    return Token('NUM', str(float(args[0].val) - float(args[1].val)))


def multiply(*args):
    return Token('NUM', str(float(args[0].val) * float(args[1].val)))


def divide(*args):
    return Token('NUM', str(float(args[0].val) / float(args[1].val)))


def nothing(*args):
    pass


def max(*args):
    if float(args[0].val) > float(args[1].val):
        return args[0]
    else:
        return args[1]


def sum(*args):
    for arg in args:
        if arg.is_argument():
            arg.val  = DataStore.get_argument_value(arg)
    res = Token('NUM', 0)
    for arg in args:
        res.val += float(arg.val)
    res.val = str(res.val)
    return res
