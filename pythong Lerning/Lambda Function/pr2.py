def new(a,value):
    return 10 + a(value)

sqaure = lambda a : a * a

print(sqaure(4))

print(new(sqaure,3))