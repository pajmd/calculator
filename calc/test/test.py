

def calculate(*arg):
    return arg[0]+arg[1]

print(calculate(1,4))
l = [1,4]
t=tuple(l)
print(t)
print(calculate(*t))