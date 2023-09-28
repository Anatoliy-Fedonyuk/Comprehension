### Модификаторы доступа и @classmethod и @staticmethod
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
class Person:
    first_name: str
    last_name: str

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
