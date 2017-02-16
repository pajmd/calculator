from .token_items import Token

def add(*args):
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
    res = Token('NUM', 0)
    for arg in args:
        res.val += float(arg.val)
    res.val = str(res.val)
    return res
