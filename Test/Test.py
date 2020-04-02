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
# правильно можно создать
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
# Ответ <class '__main__.B'>
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

# Неправильно: Не выполнено commit транзакции
#

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
# # Нет ошибок

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
# answer = "global_resource каждый раз разная"

# s = ' str to int'
# x = s.split().insert(0, 'zzz')
#
# print(x[0])
# answer = "TypeError: 'NoneType' object is not subscriptable"
#
# class CheckCount(type):
#     def __new__(self, cls_name, bases, cls_dict):
#         print(cls_dict)
#         return super().__new__(self, cls_name, bases, cls_dict)
#
# # # Неправильно
# #     @staticmethod
# #     def __prepare__(name, bases):
# #         return {'secret': 777}
#     def __call__(self, *args, **kwargs):
#         self.__dict__['secret'] = 777
#
# print(CheckCount())

# x = 13
# class C:
#     x=2
#     print(x)
#
#     def m(self):
#         print(x)
#
# i = C()
# i.m()
# print(x)
#
# Правильно 2, 13, 13

# import unittest
#
# def gray_rabbit_divider(x):
#     if x>1:
#         return 10/x
#     elif x==1:
#         raise ValueError
#     elif x==0:
#         raise ZeroDivisionError
#     else:
#         pass
#
# class BigTest(unittest.TestCase):
#     def test_me(self):
#         with self.assertRaises(ZeroDivisionError):
#             for x in range(6, -1, -2):
#                 gray_rabbit_divider(x)
#
# if __name__ == '__main___':
#     unittest.main()
#
# class SlackBase:
#     def __init__(self):
#         self.exists = True
#
#     def __getattr__(self, name):
#         value = 'Значение для {}'.format(name)
#         setattr(self, name, value)
#         return value
#
# class LogSlack(SlackBase):
#     def __getattr__(self, name):
#         print('Вызов __getattr__({})'.format(name))
#         return super().__getattr__(name)
#
# data = LogSlack()
# print('foo: ', data.foo)
#
# # Правильно добавить в LogSlack return super().__getattr__(name)
# class Parent():
#     x=1
#     y=2
#
# class Child(Parent):
#     x = 111
#     y = 222
#
#     def mix(self):
#         return Parent.y
#
# c = Child()
# print(c.mix())
#
# # Правильный ответ: 2
#
#
# class A:
#     __secret = 'TopSecret'
#     def __init__(self, x):
#         self.x = x
#
# a = A(13)
# print(a._A__secret)
#
# # Правильно a._A__secret
#
# from socket import *
# import time
#
# s = socket(AF_INET, SOCK_STREAM)
# s.bind(('', 8888))
# s.listen(5)
#
# while True:
#     client, addr = s.accept()
#     print('Получен запрос на соединение с %s' % str(addr))
#     tm = time.localtime()
#     datestr = time.strftime('%Y.%m.%d', tm)
#     client.send(datestr.encode('ascii'))
#     timestr = time.strftime('%H:%M:%S', tm)
#     client.send(timestr.encode('ascii') + '\n')
#     client.close()
#
# x = 10
# a = lambda y: x + y
# x = 20
# b = lambda y: x + y
#
# print('{}, {}'.format(a(10), b(10)))
#
# # правильно 30, 30
#
# from threading import Thread
# from queue import Queue
#
# class Worker:
#     def __init__(self):
#         self.input_queue = Queue()
#
#     def send(self, value):
#         self.input_queue.put(value)
#
#     def close(self):
#         self.input_queue.put(None)
#         self.input_queue.join()
#
#     def __call__(self):
#         while True:
#             item = self.input_queue.get()
#             self.input_queue.task_done()
#             if item is None:
#                 break
#             print('Получено: ', item)
#         return
#
# worker = Worker()
# work = Thread(target=worker)
# work.start()
# worker.send('Simple')
# worker.send('Data')
# worker.close()
# print('Выполнено')
# # Правильно после 17-ой строки добавить  self.input_queue.task_done()
# def make_multiplier_of(n):
#     lst = []
#     def multiplier(x, final=False):
#         lst.append(x*n)
#         if final:
#             print(lst)
#         return x*n
#     return multiplier
#
# times3 = make_multiplier_of(3)
# times5 = make_multiplier_of(5)
#
# times3(9)
# times5(3)
# times5(times3(2), True)
#
# # [15, 30]
# def log(fmt):
#     def deco(func):
#         def call(*args, **kwargs):
#             print('Log: ', fmt.format(args, kwargs))
#             return func(*args, **kwargs)
#         return call
#     return deco
#
# @log
# def f():
#     print('Hello')
# # Строки 6 и 7 нужно поменять местами
#
# def producer(data, next_task):
#     tokens = data.split(';')
#     for token in tokens:
#         next_task.send(token)
#     next_task.close()
#
# def df(tf=int, next_task=None):
#     try:
#         while True:
#             token = (yield)
#             try:
#                 token = tf(token)
#                 except:
#                 pass
#                 else:
#                 next_task.send(token)
#     except GeneratorExit:
#         pass
#
# def pp():
#     try:
#         while True:
#             token = (yield)
#             print('->', token)
#     except GeneratorExit:
#         pass
#
# data = 'Moscow; 1147;-4'
#
# import time
#
# def make_func(x):
#     call_log = []
#
#     def inner_func(y):
#         call_log.append(time.time())
#         res = x + y
#         print('Sum of {} and {} is {}'. format(x, y, res))
#         return res
#
#     def get_call_log():
#         return call_log
#
#     return inner_func, get_call_log
#
# z = func(3)
#
#
# class Base:
#     var = 5
#     def __init__(self):
#         pass
# class X(Base):
#     def __init__(self):
#         super().__init__()
#         self.var = 7
#
# class Y(Base):
#     var = 10
#     def __init__(self):
#         super().__init__()
#
# class Z(X,Y):
#     def __init__(self):
#         self.var = 13
#         super().__init__()
#
# z = Z()
# print(Z.mro())
# # Ответ: [<class '__main__.Z'>, <class '__main__.X'>, <class '__main__.Y'>, <class '__main__.Base'>, <class 'object'>]
# print(super(Z, z).var)
# # Ответ: 10

# class CheckCount(type):
#     def __init__(self, *args, **kwargs):
#         self.count = 0
#         super().__init__(*args, **kwargs)
#
#     def __call__(self, *args, **kwargs):
#         if self.count < 5:
#             self.count +=1
#             return  super().__call__(self, *args, **kwargs)
#         else:
#             return None
#
# class SpaceX(metaclass=CheckCount):
#     def __init__(self):
#         print('Run to Space')
#
#     def __call__(self):
#         print('Yes, I Can')
#
# x=SpaceX()
# x()
# print()
