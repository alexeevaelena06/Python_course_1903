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
