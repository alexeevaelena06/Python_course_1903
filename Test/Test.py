# GeekBrains testing

# # # # # # #
#
#
# def simple(x):
#     print(x)
#     y = yield x * 2
#     print(y)
#     z = yield y + x
#     print(z)
#
#
# s = simple(2)
# next(s)
# print(s.send(3))
#
# # # # # # #
#
#
# def usefull(cls):
#     print("Deco for class", cls)
#     return True if cls._z > 10 else False
#
#
# @usefull
# class A:
#     _z = 333
#
#     def __init__(self, x):
#         self.x = x
#         print('__init__')

# def usefull(cls):
#     def decorated(*args, **kwargs):
#         return cls(*args, **kwargs)
#     return decorated
#
# @usefull
# class A:
#     def __init__(self, x):
#         self.x = x
#
# print(A(5))
#
# # # # # # #
#
#
# def create_adders():
#     adders = []
#     for i in range(10, 14):
#         def adder(x):
#             return i + x
#         adders.append(adder)
#     return adders
#
#
# for adder in create_adders():
#     print(adder(1))
#
# # # # # # #
#
#
# class TrickyManager:
#     def __init__(self, lst):
#         self.worklist = lst
#
#     def __enter__(self):
#         __builtins__.print = lambda x, f=open('trace.log', 'a'), end = '\n': f.write(str(x))
#         return 'T-R-I-C-K-Y'
#
#     def __exit__(self, exc_type, exc_value, trace):
#         return True
#
#
# with TrickyManager([1, 2, 3, 4, 5]) as t:  # Ошибка
#     for c in t:
#         print(c, end='')
#
# print(t)
#
# # # # # # #
#
#
# class A:
#     pass
#
#
# class B(A):
#     pass
#
#
# class C(A):
#     pass
#
#
# print(B.__bases__[0].__subclasses__()[0])
#
# # # # # # # #
#
# print(type.__class__.__base__)
#
# # <class 'object'>
#
# # # # # # # #
#
#
# import pytest
#
#
# @pytest.mark.parametrize('line, paste, res', [('', '', ''),
#                                               ('Some text to be replaced ', 'zzz', 'Some text zzz'),
#                                               ('Some text..', 'zzz', 'Some text.'),
#                                               ('Some text ', 'zzz', 'Some text zzz'),
#                                               ('Some text', 'zzz', 'zzz'),
#                                               ('Some text', 'zzz', 'Some text'),
#                                               ('Some text', 'zzz', 'Some text'),
#                                               ('', 'zzz', ''),
#                                               ('Some text <END> xxx <START>', 'zzz', 'Some text zzz'),
#                                               ('Some text <END> xxx <START>', 'zzz', 'Some text <END> xxx <START>'),
#                                               ('Some text <START> to be <END> replaced <END>', 'zzz', 'Some text zzz'),
#                                               ('Some text <START> to be replaced <END>!', '', 'Some text!'),
#                                               ])
# def test_insert(line, paste, res):
#     data = insert_data(line, paste)
#     assert data == res
#
#
# def insert_data(line, paste):
#     """Заменяет первое вхождение подстроки,
#     обрамлённой тегами - , в строке line на строку paste.
#     Вложенные теги не учитываются.
#     Замена производится вместе с тегами"""
#     res = line
#     start = line.find('')
#     end = line.find('')
#     if -1 < start < end:
#         res = line[:start] + paste + line[end+5:]
#     return res


# # # # # # # #
#
#
# def make_averager():
#     count = 0
#     total = 0
#     def averager(new_value):
#         nonlocal count, total
#         count +=1
#         total += new_value
#         return total/count
#     return averager
#
# avg = make_averager()
# for i in range(4):
#     x = avg(i)
#     print(i, x)
#
# # 1.5

# # # # # # # #
#
# num = input('Укажите артикул товара: ') # 1
# curr = connection.cursor() # 2
# curr.execute('SELECT * FROM GOOD WHERE art_num = {}'.format(num)) # 3
# res = curr.fetchall() # 4
# print(res) # 5
# connection.close() # 6
#
# # Не выполнено commit транзакции

# # # # # # # #
#
# class Grade:
#     def __init(self):
#         self._values = {}
#
#     def __get__(self, instance, instance_type):
#         if instance is None:
#             return self
#         return self._values.get(instance, 1)
#
#     def __set__(self, instance, value):
#         if not (1 <= value <= 5):
#             raise ValueError('Оценка должна быть от 1 до 5')
#         self._values[instance] = value
#
# # Отсутствует метод __delete__

# # # # # # # #
#
# def recv(maxsize, *, block):
#     print('')
#
# # Правильно recv(1024, block=True)

# # # # # # # #
#
# args = input('> ').split()
# if args[0] =='help':
#     print('This is calculator application. ')
#     print('Usage: ')
#     print(' calc - calculates math expression')
#     print(' db - look for different constants in database')
#     print(' help - show this message')
# elif args[0] == 'calc':
#     x = eval(''.join(args[1:]))
# elif args[0] == 'db':
#     # TODO : search in db
#     sql_query = ''
# else:
#     print('Unknown key. Try again!')
#
# def oroc(func):
#     def trats(*args, **kwargs):
#         g = func(*args, **kwargs)
#         next(g)
#         return g
#     return trats
#
# @oroc
# def f():
#     print("Я здесь")
#
# def calc_tax_summ(summ, tax):
#     """Функция вычисления суммы вкл. налога
#     Принимает стоимость товара в налоговую ставку в процентах
#     >>> calc_tax_summ(1, 100)  # Test 1.
#     0.5
#     >>> calc_tax_summ(0, -100)   # Test 2.
#     0.0
#     >>> calc_tax_summ(299, 18) # Test 3.
#     45.61
#     >>> calc_tax_summ(37.09, 18) # Test 4.
#     5.66
#     """
#     res = 0.0
#     if 0 <= tax <= 100:
#         cost = summ/(1+tax/100)
#         res = summ - cost
#     return round(res, 2)
#
# if __name__ == '__main__':
#     import doctest
#     doctest.testmod()
#
# z = 10
# def test(x=5):
#     print(x)
#     print(z)
#     z = 13
#
# test(7)
# print(z)

# class Miracle:
#     __slots__ = ('x', 'y', '__dict__')
#     xx = 10
#
#     def __init__(self, *args, **kwargs):
#         self.y = 11
#
# m = Miracle()
# m.x = 100
# m.y = 7
# m.z = 13
# print(m.x, m.y, m.z)


# from threading import Thread
#
# def just_print():
#     with open('numbers.txt', 'w') as f:
#         for i in range(10000):
#             f.write(str(i) + '\n')
#
# t1 = Thread(target=just_print)
# t1.daemon = True
# t1.start()
#
# for i in range(10):
#     print(i*2)
#
# def zorro():
#     print('Raedy')
#     while True:
#         n = yield 42
#         print("n = %s" % n)
#
# zorro()
#
# from threading import Thread, Lock
#
# COUNT = 100000
# resource_lock = Lock()
# global_resource = 0
#
# def producer():
#     global global_resource
#     for i in range(COUNT):
#         global_resource+=1
#
# def consumer():
#     global global_resource
#     for i in range(COUNT):
#         global_resource -=1
#
# if __name__ == '__main__':
#     t1 = Thread(target=producer)
#     t2 = Thread(target=consumer)
#     t1.start()
#     t2.start()
#
# print(global_resource)

# s = ' str to int'
# x = s.split().insert(0, 'zzz')
# print(x[0])