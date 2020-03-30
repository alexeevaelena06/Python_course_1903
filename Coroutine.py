# https://pymotw.com/3/
# pythontutor.com
# import pathlib
#
# p = pathlib.Path()
#
# print(p)
# print(pathlib.PosixPath('.'))
# print(pathlib.PosixPath('tmp/abc'))


def f():
    yield


def coroutine(f):
    gen = f()
    next(gen)
    return gen


@coroutine
def f():
    i = yield
    print("f: ", i)
    yield i + 1


def main():
    i = f.send(1)
    print("main: ", i)
    i = f.send(i + 1)
    print("main: ", i)


main()
