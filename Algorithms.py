""" АЛГОРИТМЫ И ТЕОРИЯ ДЛЯ СОБЕСА!!!"""
""" Модификаторы доступа(Data Hiding) и @classmethod и @staticmethod - инструменты ИНКАПСУЛЯЦИИ!!!"""
# class A():
#     def __init__(self, name='somebody'):
#         self.name = name
#
#     public = 123
#     _protected = 321
#     __private = 231
#
#     def some(self):
#         print(f'Hi Dude! I know your name - {self.__private=}? No!!! It`s "{self.name}", right?')
#
#     @classmethod
#     def some_classmethod(cls):
#         print(f"This is class method! {cls._protected=}, {cls.__private=}")
#
#     @staticmethod
#     def some_staticmethod():
#         print('This is staticmethod!')
#
# a = A('Вася')
# print(a.public)
# print(a._protected)
# print(a._A__private)
# a.some()
# A.some_classmethod()
# A.some_staticmethod()
# a.some_staticmethod()
#
# print(A.__dict__)

""" Атрибуты Класса и атрибуты Объекта чем отличаются? могут ли иметь одинаковое имя?"""
# class C:
#     attr = 1         # Атрибут Класса
#
#     def __init__(self):
#         self.attr = 2        #  Атрибут Объекта/Экземпляра
#
# c = C()
# print(C.attr)
# print(c.attr)
# print(C.__dict__)       # Они не пересекаются ибо, хранятся в разных словарях класса!
# print(c.__dict__)

""" Декораторы @property и setter - что и зачем?"""
# class Person:
#     first_name: str
#     last_name: str
#
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#
#     @property
#     def full_name(self):
#         return f"{self.first_name} {self.last_name}"
#
#     @full_name.setter
#     def full_name(self, value):
#         name_surname = value.split(" ")
#         self.first_name = name_surname[0]
#         self.last_name = name_surname[1]
#
# p = Person('Slava', 'Rineisky')
# print(p.full_name)
# d = Person('Вася', 'Вася')
# print(d.full_name)
# # setter
# d.full_name = "Василий Пупкин"
# print(d.first_name)
# print(d.last_name)
# print(d.full_name)

""" Абстрактные классы? Зачем? Как реализуются в Python?"""
# from abc import ABC, abstractmethod
#
""" Абстрактный класс, представляющий геометрическую фигуру"""
# class Shape(ABC):
#
#     @abstractmethod
#     def area(self):
#         pass
#
#     @abstractmethod
#     def perimeter(self):
#         # print("This is abstractmethod")
#         pass
#
""" Подклассы, представляющие конкретные фигуры"""
# class Circle(Shape):
#
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         return 3.14 * self.radius * self.radius
#
#     def perimeter(self):
#         return 2 * 3.14 * self.radius
#
# class Rectangle(Shape):
#
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def area(self):
#         return self.width * self.height
#
#     def perimeter(self):
#         return 2 * (self.width + self.height)
#
# # Использование классов
# circle = Circle(5)
# rectangle = Rectangle(4, 6)
#
# print("Площадь круга:", circle.area())
# print("Периметр круга:", circle.perimeter())
#
# print("Площадь прямоугольника:", rectangle.area())
# print("Периметр прямоугольника:", rectangle.perimeter())

# shape = Shape()
# print("Периметр абстрактный:", shape.perimeter())

""" Разница между __str__ и __repr__?"""
# class Cat:
#     def __repr__(self):
#         return "IT`S A CAT"
#
#     def __str__(self):
#         return "It is my cat!)"
#
# c = Cat()
# print(c)
# print(repr(c))

""" метод super() и MRO (Method Resolution Order)"""
# class A:
#     def show(self):
#         print("Метод show в классе A")
#
# class B(A):
#     def show(self):
#         print("Метод show в классе B")
#         super().show()
#
# class C(A):
#     def show(self):
#         print("Метод show в классе C")
#         super().show()
#
# class D(C, B):
#     pass
#
# # Создаем объект класса D и вызываем его метод show
# obj = D()
# obj.show()

""" Mixin Classes"""
# Пример класса-миксина, предоставляющего логирование
# class LoggingMixin:
#     def log(self, message):
#         print(f"class [{self.__class__.__name__}] {message}")
#
# # Пример класса, использующего класс-миксин
# class Calculator(LoggingMixin):
#     def add(self, x, y):
#         result = x + y
#         self.log(f"Вычисление: {x} + {y} = {result}")
#         return result
#
# # Создаем объект класса Calculator и используем логирование из класса-миксина
# calc = Calculator()
# calc.add(3, 5)

""" Замыкания, Декораторы, Декораторы с аргументами"""
# def outer_function(x):
#     # Это внешняя функция, которая принимает аргумент x
#     def inner_function(y):
#         # Это внутренняя функция, которая также принимает аргумент y
#         return x + y  # Используется переменная x из внешней области видимости
#
#     return inner_function  # Внешняя функция возвращает внутреннюю функцию
#
#
# # Создаем замыкание, передавая аргумент 10 во внешнюю функцию
# closure = outer_function(10)
# clos2 = outer_function(100)
# # Теперь можем вызывать closure, как обычную функцию, но она имеет доступ к x из outer_function
# result = closure(5)  # Результат будет 15, так как x=10, y=5
# res2 = clos2(-50)
# print(result)
# print(res2)
#

""" Декоратор с аргументом, который определяет, сколько раз функция будет выполнена"""
# def repeat(num):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             for _ in range(num):
#                 print(func(*args, **kwargs))
#             return f"{func(*args, **kwargs)} + я тебя {num} раз)"
#         return wrapper
#     return decorator
#
# @repeat(7)  # Применение декоратора с аргументом: выполнить функцию 3 раза
# def say_hello(name):
#     return f"Привет, {name}!"
#
# print(say_hello("Анна"))

""" Итераторы в отличии от итерируемого объекта - реализуют методы Iter и Next!!!"""
# # a = [1, 2, 3, 4, 5]
# a = {33, 4, 2, 5, 7, 3}
# # a = 'dsdkadjkas'
# # a = {'a': 23, 'b': 83, 'c': 4, 33: "SOS"}
#
# i = iter(a)             # Создаем Итератор тут!
# # i = iter(a.values())
#
# print(i)
# print('__next__' in dir(i))     # Проверка метода Next!
# print(next(i))
# print(next(i))
# print(next(i))
# print(*i)

""" Итератор в классе"""
# class Counter:
#     current: int
#     def __init__(self):
#         self.current = 0
#     def __iter__(self):
#         return self
#     def __next__(self):
#         current = self.current
#         self.current += 1
#         return current
#
# c = Counter()
#
# i = iter(c)
# print(next(i))
# print(next(i))

""" Генераторы - Что? Как? Конструкция "yield from"""
# def get_list():
#     for x in [1,2,3,4,5]:
#         yield x
#
# gen = get_list()
# for x in gen: print(x)
# print(next(gen))    # StopIteration

# def first():
#     yield "a"
#     yield "b"
#     yield "c"
#
# def second():
#     yield 1
#     yield from first()  # Говорит - дай мне все yield из first() !
#     yield 2
#     yield 3
#
# gen = second()
# for i in gen: print(i)

""" Контекстные менеджеры"""
# class Connection:
#     def __enter__(self):
#         self.connection = 1
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.connection = 0
#
#
# with Connection() as obj:
#     print("Some Logic")
#     raise Exception("VAL")

""" Exception - Исключения"""
# try:
#     raise AssertionError(1)
# except (ValueError, TypeError):
#     print("Value or Type Error")

# try:            # Как переподнять исключение в блоке exception? т.е. поднять ексепшн выше по стеку
#     try:
#         raise ValueError(1)
#     except Exception:
#         print("Inner Exception")
#         raise       # Конечно тут с помощью raise? И Outer отработает тоже
# except Exception:
#     print("Outer Exception")
# finally:
#     print("Finally End")

""" работа с ExceptionGroup, BaseExceptionGroup и оператор <except*>"""
# try:
#     eg = ExceptionGroup("exception group", [TypeError(1),
#                         ValueError(2), ZeroDivisionError(3)])
#     raise eg
# except* TypeError as e:
#     print("TypeError", e)
# except* ValueError as ex:
#     print("ValueError", ex)
# except* ZeroDivisionError as z:
#     print("ZeroDivisionError", z)
# finally:
#     print("close all & Finish")
#
""" Кастомная ошибка - как реализовать? """
# class Custom(Exception):
#     def __init__(self, value, message="Specific message about your error"):
#         self.value = value
#         self.message = message
#         super().__init__(self.message)
#
# raise Custom(112233)

""" COROUTINE - Что такое Корутина? """
# import asyncio
#
# async def my_coroutine():
#     print("Start Coroutine")
#     await asyncio.sleep(2)
#     print("Coroutine Resumed")
#
# async def main():
#     await asyncio.gather(my_coroutine(), my_coroutine())
#
# asyncio.run(main())
#
# import asyncio
#
# async def foo():
#     await asyncio.sleep(4)
#     return "Foo Result"
#
# async def bar():
#     await asyncio.sleep(1)
#     return "Bar Result"
#
# async def main():
#     await print(bar())
#     await print(foo())
#     await print(bar())
#     await print(foo())
#     await print(bar())
#
#
# asyncio.run(main())

""" Dependency Inversion Principle (SOLID) """
# class Switchable:
#     def turn_on(self):
#         pass
#
#     def turn_off(self):
#         pass
#
# class LightBulb(Switchable):
#     def turn_on(self):
#         print("LightBulb is on")
#
#     def turn_off(self):
#         print("LightBulb is off")
#
# class LightSwitch(Switchable):
#     def __init__(self, device):
#         self.device = device
#         self.is_on = False
#
#     def operate(self):
#         if self.is_on:
#             self.device.turn_off()
#         else:
#             self.device.turn_on()
#
# # device = LightBulb()
# # device.turn_on()
# # device.turn_off()
# switch = LightSwitch(L:=LightBulb())
# switch.operate()

""" Поведение кортежей """
# try:
#     data = (["been"], "py")
#     data[0].extend("sos")
#     print(data)
#     data[0] += ["geek"]
#     # print(data)
# except:
#     print(data)
#     print(data[::-1])

""" Дескрипторы """
# class Celsius:
#     def __get__(self, instance, owner):
#         return 5 * (instance.temperature - 32) / 9
#
#     def __set__(self, instance, value):
#         instance.temperature = 32 + 9 * value
#
# class Temperature:
#     def __init__(self, initial):
#         self.temperature = initial
#
#     # Используем дескриптор для атрибута celsius
#     celsius = Celsius()
#
# # Создаем объект Temperature с начальной температурой в Фаренгейтах
# temp = Temperature(212)
#
# # Обращаемся к атрибуту celsius, который автоматически преобразует температуру
# print(temp.celsius)  # Вывод: 100.0
# print(temp.temperature)
# print("$"*50)
# # Меняем значение атрибута celsius, и оно автоматически преобразуется в Фаренгейты
# temp.celsius = 0
# print(temp.temperature)  # Вывод: 32.0
# print(temp.celsius)
#
# print("$"*50)
# temp.temperature = 0
# print(temp.temperature)
# print(temp.celsius)
#
# print("$"*50)
# # Меняем значение атрибута celsius, и оно автоматически преобразуется в Фаренгейты
# temp.celsius = 0
# print(temp.temperature)  # Вывод: 32.0
# print(temp.celsius)

""" АЛГОРИТМЫ !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! """

""" Сортировка Выбором !!! / максимальная сложность алгоритма O(n^2) вложенный цикл"""
# # Подходит для массивов чисел или однотипных данных которые можно сравнивать на больше-меньше!
# arr = [-3, 5, 0, -8, 1, 10]
#
# N = len(arr)
# for i in range(N-1):
#     minim = arr[i]   # мин.значение
#     index = i       # индекс мин.значения
#     for j in range(i+1, N):
#         if minim > arr[j]:
#             minim = arr[j]
#             index = j
#
#         if index != i:
#             temp = arr[i]
#             arr[i] = arr[index]
#             arr[index] = temp
#
# print(arr)

""" Сортировка Вставками !!! / максимальная O(n^2)"""
# Он лучше алг.сортировки выбором - состоит в том что его удобно применять когда в сортированный список добавляются новые
# занчения или еще список, тогда проверку можно начинать с первого индекса новых значений, что существенно ускорит работу!
# ar = [-3, 5, 0, -8, 1, 10]
# N = len(ar)
#
# for i in range(1, N):
#     for j in range(i, 0, -1):
#         if ar[j] < ar[j - 1]:
#             ar[j], ar[j - 1] = ar[j - 1], ar[j]
#         else:
#             break
#
# print(ar)

""" Сортировка (всплывающим) Пузырьком !!! / максимальная O(n^2)"""
#
# a = [7, 5, -8, 0, 10, 1]
# N, count = len(a) - 1, 0  # число элементов в списке
#
# for i in range(N):  # N итераций работы алгоритма
#     for j in range(N - i):  # проход по оставшимся не отсортированным парам массива
#         # print(f"Сейчас сравниваем {a[j]=} c {a[j+1]=}")
#         if a[j] > a[j + 1]:
#             a[j], a[j + 1] = a[j + 1], a[j]
#             count += 1
#     # print(a)
#
# print(a, "Кол-во замен:", count)


""" Слияние 2 Упорядоченных Списков !!! / максимальная O(n)"""
# # Оба отсортированных либо по возрастанию, либо по убыванию
# a = [1, 4, 10, 11]
# b = [2, 3, 3, 4, 8]
# c, i, j = [], 0, 0
#
# while i < len(a) and j < len(b):
#     if a[i] <= b[j]:
#         c.append(a[i])
#         i += 1
#     else:
#         c.append(b[j])
#         j += 1
#
# c += a[i:] + b[j:]
# print(c)

""" Быстрая сортировка слиянием (merge sort) с рекурсией / O(n*log2(n)) что значительно меньше O(n^2)"""
# # Состоит из двух этапов 1 рекурсивно делим массив до неделимой единицы, а 2 этап резделенные части сортируем
# # предыдущим алгоритмом слияния сортированных списков!
# def merge_list(a, b):  # функция слияния двух отсортированных списков
#     c, i, j = [], 0, 0
#
#     while i < len(a) and j < len(b):
#         if a[i] <= b[j]:
#             c.append(a[i])
#             i += 1
#         else:
#             c.append(b[j])
#             j += 1
#
#     c += a[i:] + b[j:]
#     return c
#
#
# def split_and_merge_list(a):  # функция деления списка и слияния списков в общий отсортированный список
#     N1 = len(a) // 2
#     a1 = a[:N1]  # деление массива на два примерно равной длины
#     a2 = a[N1:]
#
#     if len(a1) > 1:  # если длина 1-го списка больше 1, то делим дальше
#         a1 = split_and_merge_list(a1)
#     if len(a2) > 1:  # если длина 2-го списка больше 1, то делим дальше
#         a2 = split_and_merge_list(a2)
#
#     return merge_list(a1, a2)  # слияние двух отсортированных списков в один
#
#
# a = [9, 5, -3, 4, 7, 8, -8]
# a = split_and_merge_list(a)
#
# print(a)

""" Быстрая сортировка слиянием Хоара с рекурсией/ O(n*log2(n)) что значительно меньше O(n^2)"""
# Этот алгоритм экономит память! Потому что сортирует массив "in place" - не создавая новых массивов
from random import randint


def quick_sort(a):
    if len(a) > 1:
        x = a[randint(0, len(a) - 1)]  # случайное значение (для разделения на малые и большие)
        low = [u for u in a if u < x]     # в настоящем алгор.Хоара так не делают а работают внутри массива))
        eq = [u for u in a if u == x]
        hi = [u for u in a if u > x]
        a = quick_sort(low) + eq + quick_sort(hi)

    return a


a = [9, 5, -3, 4, 7, 8, -8]
a = quick_sort(a)

print(a)

""" Пример использования СТЭК типа LIFO """
# # LIFO - Last-In-First-Out
# flVerify, stack = True, []
#
# for lt in input("Введите: "):
#     if lt in "([{":
#         stack.append(lt)
#     elif lt in ")]}":
#         if len(stack) == 0: flVerify = False; break
#
#         br = stack.pop()
#         if br == '(' and lt == ')': continue
#         elif br == '[' and lt == ']': continue
#         elif br == '{' and lt == '}': continue
#         else: flVerify = False; break
#
# print(("No", "Yes")[flVerify and not len(stack)])

""" Делаем очередь (Queue) / модуль Collections - Deque/В отличии от LIFO - тут FIFO (First-On-First-Out)"""
# Однонаправленные очереди идеально делать с помощью метода Deque (есть методы .popleft, .appendleft)
# C помощью Deque - конечно можно и организовывать и Стэк. Вставка граничных элементов реализована O(1)
# import collections
#
# q = collections.deque()
#
# q.extend((4, -7, 2, 0))
# print(q)
# q.appendleft(-3); print(q.pop()) # Очередь вправо!!!)
# print(q)
# q.append(9); print(q.popleft()) # Очередь влево!!!)
# print(q)