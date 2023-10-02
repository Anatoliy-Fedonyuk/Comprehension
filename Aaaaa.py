### Модификаторы доступа(Data Hiding) и @classmethod и @staticmethod - инструменты ИНКАПСУЛЯЦИИ!!!
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

### Атрибуты Класса и атрибуты Объекта чем отличаются? могут ли иметь одинаковое имя?
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

### Декораторы @property и setter - что и зачем?
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

### Абстрактные классы? Зачем? Как реализуются в Python?
# from abc import ABC, abstractmethod
#
# # Абстрактный класс, представляющий геометрическую фигуру
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
# # Подклассы, представляющие конкретные фигуры
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

### Разница между __str__ и __repr__?
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

### метод super() и MRO (Method Resolution Order)
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

### Mixin Classes
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

### Замыкания, Декораторы, Декораторы с аргументами
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
# def repeat(num):
#     # Декоратор с аргументом, который определяет, сколько раз функция будет выполнена
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

### Итераторы в отличии от итерируемого объекта - реализуют методы Iter и Next!!!
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

### Генераторы - Что? Как? Конструкция "yield from"
# def get_list():
#     for x in [1,2,3,4,5]:
#         yield x
#
# gen = get_list()
# for x in gen: print(x)
# print(next(gen))    # StopIteration
#
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

### Контекстные менеджеры
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

### Exception - Исключения


