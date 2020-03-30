# GeekBrains testing

# # # # # #


def simple(x):
    print(x)
    y = yield x * 2
    print(y)
    z = yield y + x
    print(z)


s = simple(2)
next(s)
print(s.send(3))

# # # # # #


def usefull(cls):
    print("Deco for class", cls)
    return True if cls._z > 10 else False


@usefull
class A:
    _z = 333

    def __init__(self, x):
        self.x = x
        print('__init__')

# # # # # #


def create_adders():
    adders = []
    for i in range(10, 14):
        def adder(x):
            return i + x
        adders.append(adder)
    return adders


for adder in create_adders():
    print(adder(1))

# # # # # #


class TrickyManager:
    def __init__(self, lst):
        self.worklist = lst

    def __enter__(self):
        __builtins__.print = lambda x, f=open('trace.log', 'a'), end = '\n': f.write(str(x))
        return 'T-R-I-C-K-Y'

    def __exit__(self, exc_type, exc_value, trace):
        return True


with TrickyManager([1, 2, 3, 4, 5]) as t:  # Ошибка
    for c in t:
        print(c, end='')

print(t)

# # # # # #


class A:
    pass


class B(A):
    pass


class C(A):
    pass


print(B.__bases__[0].__subclasses__()[0])

# # # # # #
