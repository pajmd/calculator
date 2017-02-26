from .token_items import Token
from .data_store import DataStore


def get_variable_argument_value_from_store(*args):
    for arg in args:
        if arg.is_argument():
            arg.val  = DataStore.get_argument_value(arg)

def are_time_series(*args):
    time_series_counter = 0
    for arg in args:
        if isinstance(arg.val, list):
            time_series_counter += 1
    if len(args) == time_series_counter:
        return True
    elif time_series_counter == 0:
        return False
    raise ValueError('Mismatch series and other type of data')


def add(*args):
    get_variable_argument_value_from_store(*args)
    if are_time_series(*args):
        l = [str(float(v1)+float(v2)) for v1,v2 in zip(args[0].val, args[1].val)]
        return Token('NUM', l)
    else:
        return Token('NUM', str(float(args[0].val) + float(args[1].val)))

def add__(*args):
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
    get_variable_argument_value_from_store(*args)
    if are_time_series(*args):
        l = [str(float(v1)-float(v2)) for v1,v2 in zip(args[0].val, args[1].val)]
        return Token('NUM', l)
    else:
        return Token('NUM', str(float(args[0].val) - float(args[1].val)))


def multiply(*args):
    get_variable_argument_value_from_store(*args)
    if are_time_series(*args):
        l = [str(float(v1)*float(v2)) for v1,v2 in zip(args[0].val, args[1].val)]
        return Token('NUM', l)
    else:
        return Token('NUM', str(float(args[0].val) * float(args[1].val)))


def divide(*args):
    get_variable_argument_value_from_store(*args)
    if are_time_series(*args):
        l = [str(float(v1)/float(v2)) for v1,v2 in zip(args[0].val, args[1].val)]
        return Token('NUM', l)
    else:
        return Token('NUM', str(float(args[0].val) / float(args[1].val)))


def nothing(*args):
    pass


def max(*args):
    get_variable_argument_value_from_store(*args)
    if are_time_series(*args):
        l = [str(float(v1) if float(v1) > float(v2) else float(v2) ) for v1, v2 in zip(args[0].val, args[1].val)]
        return Token('NUM', l)
    else:
        if float(args[0].val) > float(args[1].val):
            return args[0]
        else:
            return args[1]


def sum(*args):
    get_variable_argument_value_from_store(*args)
    if are_time_series(*args):
        # TODO assunimg falsely of all timeseries have the same length
        list_of_tot = None
        for arg in args:
            if list_of_tot is None:
                list_of_tot = list()
                for v in arg.val:
                    list_of_tot.append(0.0)
            i = 0
            for t in arg.val:
                list_of_tot[i] += float(t)
                i += 1
        return Token('NUM', [str(v) for v in list_of_tot])
    else:
        # for arg in args:
        #     if arg.is_argument():
        #         arg.val  = DataStore.get_argument_value(arg)
        res = Token('NUM', 0)
        for arg in args:
            res.val += float(arg.val)
        res.val = str(res.val)
        return res
