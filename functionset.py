# not used not needed
from token_items import Token

class Function(object):
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

def get_function(name):
    dict_attributes = vars(Function)
    func = dict_attributes[name]
    if func is not None and callable(func):
        return func
    else:
        raise NotImplemented(name+": this function doesn't exists")
