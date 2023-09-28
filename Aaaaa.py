class A():
    def __init__(self, name='somebody'):
        self.name = name

    public = 123
    _protected = 321
    __private = 231

    def some(self):
        print(f'Hi Dude! I know your name - {self.__private=}? No!!! It`s "{self.name}", right?')

    @classmethod
    def some_classmethod(cls):
        print(f"This is class method! {cls._protected=}, {cls.__private=}")

    @staticmethod
    def some_staticmethod():
        print('This is staticmethod!')

a = A('Вася')
print(a.public)
print(a._protected)
print(a._A__private)
print(a.some())
print(A.some_classmethod())
print(A.some_staticmethod())
print(a.some_staticmethod())


