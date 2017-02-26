

def calculate(*arg):
    return arg[0]+arg[1]

def zipall():
    l1 = [1, 2, 3, 4, 5]
    l2 = [1, 2, 3, 4]
    l3 = [1, 2, 3, 4, 5]
    l = [v1 + v2 + v3 for v1, v2, v3 in zip(l1,l2,l3)]
    print('zipall: {}'.format(l))

if __name__ == '__main__':
    print('passing 1,4 = {}'.format(calculate(1,4)))
    l = [1,4]
    t=tuple(l)
    print('The tuple: {}'.format(t))
    print('passing (1,4) = {}'.format(calculate(*t)))
    zipall()