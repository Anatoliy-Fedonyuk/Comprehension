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
class LoggingMixin:
    def log(self, message):
        print(f"class [{self.__class__.__name__}] {message}")

# Пример класса, использующего класс-миксин
class Calculator(LoggingMixin):
    def add(self, x, y):
        result = x + y
        self.log(f"Вычисление: {x} + {y} = {result}")
        return result

# Создаем объект класса Calculator и используем логирование из класса-миксина
calc = Calculator()
calc.add(3, 5)

###


