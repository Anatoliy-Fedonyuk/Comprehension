### INHERITANCE  &  ENCAPSULATION

# class Verification:
#
#     def __init__(self, login, password, age=100):
#         self.login = login
#         self.password = password
#         self.age = age
#         self.__lenPassword()
#
#     def __lenPassword(self):
#         if len(self.password) < 8:
#             raise ValueError('Слабый пароль')
#
#     def save(self):
#         with open('users', 'a') as r:
#             r.write(f'{self.login, self.password, self.age}' + '\n')
#
#
# class A:
#     def a(self):
#         print('A')
#
#
# class B:
#     def a(self):
#         print('B')
#
#
# class C(B):
#     def a(self):
#         print('C')
#
#
# class D(C, A):
#
#     def a(self):
#         super(B, self).a()


# D().a()
# print(D.__mro__)


### GETTER, SETTER, STATIC METOD & CLASS METOD


# from datetime import datetime as dt


# class Player:  ### Модуль игроков и их свойств - упрощенно))
#
#     __LVL, __HEALTH = 1, 100  # Определяем константы игровые, они же свойства класса
#     __slots__ = ['__lvl', '__health', '__born']  # Слотируем перса, опред. макс кол-во свойств объекта\игрока
#
#     def __init__(self):
#         self.__lvl = Player.__LVL
#         self.__health = Player.__HEALTH
#         self.__born = dt.now()
#
#     @property
#     def lvl(self):  # Getter
#         return self.__lvl, self.__health, f'{dt.now() - self.__born}'  # lvl and time live player
#
#     @lvl.setter
#     def lvl(self, numeric):  # Setter
#         self.__lvl += Player.__typeTest(numeric)
#         if self.__lvl >= 100: self.__lvl = 100
#
#     @classmethod
#     def set_cls_field(cls, lvl=1, health=100):
#         cls.__LVL = Player.__typeTest(lvl)
#         cls.__HEALTH = Player.__typeTest(health)
#
#     @staticmethod
#     def __typeTest(value):
#         if value > 100: return 100
#         if isinstance(value, int):
#             return value
#         else:
#             raise TypeError('Mast be int!')


# Player.set_cls_field(10, 200)
# x = Player()
# print(x.lvl)
#
# Player.set_cls_field()
# y = Player()
# y.lvl = 4
# print(y.lvl)

# class Person:
#     def __init__(self, first_name, last_name, age):
#         self.first_name = first_name
#         self._last_name = last_name
#         self.__age = age
#         self.__one__ = 1
#
#     def set_age(self, age):
#         if 1 < age < 120:
#             raise ValueError(f'Age must be in range 1-120')
#         self.__age = age
#
#     def describe(self):
#         print(f'I am {self.first_name} {self._last_name}, I am {self.__age} years old!')


# if __name__ == '__main__':
#     ivan = Person('Ivan', 'Ivanov', 27)
#     ivan.describe()
#     print(dir(ivan))
#     print(ivan.first_name)
#     print(ivan._last_name)
#     print(ivan.__one__)
#     print(ivan._Person__age)


class BankAccount:
    def __init__(self, owner, balance=0):
        self.__owner = owner
        self._balance = balance

    def _deposit(self, amount):
        self._balance += amount
        print(f'Your account deposit the {amount}$')
        self.state_account()

    def _withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            print(f'The amount {amount}$ is debit from your account!')
            self.state_account()
        else:
            print("There isn't enough money in this account!")

    def state_account(self):
        print(f'{self.__owner} on your account {self._balance} $')


# if __name__ == '__main__':
#     sveta = BankAccount('Sveta Fedonyuk')
#     print(sveta._BankAccount__owner)
#     print(sveta._balance)
#     sveta.state_account()
#     sveta._deposit(1000)
#     sveta._withdraw(777)
#     sveta.state_account()

###    Closure    ###n

def names():
    all_names = []

    def inner(name: str) -> list:
        all_names.append(name)
        return all_names

    return inner


def pow_(base: int) -> int:  # Тоже замыкание))
    return lambda value: value ** base


# if __name__ == '__main__':
#     cube = pow_(3)
#     print(cube(5))
#     print(cube(7))
#     print(dir(cube))
#     boys = names()
#     print(boys('Vasya'))
#     print(boys('Petya'))
#     print(boys('Sasha'))
#     girls = names()
#     print(girls('Valya'))
#     print(girls('Anna'))
#     print(girls('Michell'))
#     print(dir(girls))
#     print(girls.__closure__[0].cell_contents[2])
#     print(girls.__hash__())


class Employee:
    def __init__(self, name, salary, bonus):
        self.name = name
        self.salary = salary
        self.bonus = bonus

    def calculate_bonus(self):
        return self.salary // 100 * self.bonus

    def __str__(self):  # Надо разобраться дандер метод?
        return f'{self.__class__.__name__} {self.name}, salary={self.salary}$, bonus={self.bonus}%, ' \
               f'total bonus={self.calculate_bonus()}$'

    def calc_bonuses(self, employees):
        for employee in employees:
            print(f"Calc bonus for {self.name}, it is = {self.calculate_bonus()}")


class Cleaner(Employee):
    def __init__(self, name):
        super().__init__(name, 1500, 3)


class Manager(Employee):
    def __init__(self, name):
        super().__init__(name, 4500, 15)


class CEO(Employee):
    def __init__(self, name):
        super().__init__(name, 10500, 'fixed')

    def calculate_bonus(self):
        return 20_000  # Переопределение метода))


# def calc_bonuses(employees: list[Employee]):
#     for employee in employees:
#         print(f"Calc bonus for {employee.name}, it is = {employee.calculate_bonus()}")


# if __name__ == '__main__':
#     print(masha := Cleaner('Maria Ivanovna'))
#     print(grisha := Manager('Grigoriy Petrovich'))
#     print(ivan_palych := CEO('Ivan Padlovich'))
#     print(tolya := Manager('Anatoliy Vasilievich'))
#     a_list = [masha, grisha, tolya, ivan_palych]
#     Employee.calc_bonuses(a_list)


class Shape:
    def perimeter(self):
        pass

    def area(self):
        pass

    def __str__(self):
        return f'Shape - {self.__class__.__name__}, perimetr = {self.perimeter()}, area = {self.area()}'


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return round(self.a + self.b + self.c, 2)

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return round((s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5, 2)


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def perimeter(self):
        return round(2 * (self.width + self.height), 2)

    def area(self):
        return round(self.width * self.height, 2)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        return round(2 * 3.14 * self.radius, 2)

    def area(self):
        return round(3.14 * (self.radius ** 2), 2)


# if __name__ == '__main__':
#     print(tri := Triangle(5, 7, 9))
#     print(rec := Rectangle(5, 7))
#     print(cir := Circle(4))
#     print(cir.area())
#     print([1,2,3,] + [4,5])


class Banknote:

    def __init__(self, value: int):
        self.value = value

    def __repr__(self):
        return f'Banknote({self.value})'

    # def __str__(self):
    #     return f'Банкнота номиналом в {self.value} $'

    def __eq__(self, other):
        if other is None or not isinstance(other, Banknote):
            return False
        return self.value == other.value

    def __hash__(self):
        return hash(self.value)

    def __lt__(self, other):
        if other is None or not isinstance(other, Banknote):
            return False
        return self.value < other.value

    def __gt__(self, other):
        if other is None or not isinstance(other, Banknote):
            return False
        return self.value > other.value

    def __le__(self, other):
        if other is None or not isinstance(other, Banknote):
            return False
        return self.value <= other.value

    def __ge__(self, other):
        if other is None or not isinstance(other, Banknote):
            return False
        return self.value >= other.value

    def __add__(self, other: 'Banknote'):
        if other is None or not isinstance(other, Banknote):
            raise TypeError
        if self.value == other.value:
            return Banknote(self.value + other.value)
        else: raise ValueError('Банкноты разного номинала не складываются!')


# class Iterator:
#
#     def __init__(self, container):
#         self.container = container
#         self.index = 0
#
#     def __next__(self):
#         if 0 <= self.index < len(self.container):
#             value = self.container[self.index]
#             self.index += 1
#             return value
#         raise StopIteration


# class Wallet:
#
#     def __init__(self, *banknotes: Banknote):
#         self.container = []
#         self.container.extend(banknotes)
#         self.index = 0
#
#     def __repr__(self):
#         return f'Wallet({self.container})'
#
#     def __contains__(self, item):
#         return item in self.container
#
#     def __bool__(self):
#         return len(self.container) > 0
#
#     def __len__(self):
#         return len(self.container)
#
#     def __call__(self):
#         return f'{sum(e.value for e in self.container)} $'
#
#     # def __iter__(self):
#     #     return Iterator(self.container)
#
#     def __getitem__(self, item: int):           # GETITEM work that as an ITERATOR !!!!!!
#         #print('GETITEM work that as an ITERATOR !!!!!!')
#         if 0 > item > len(self.container):
#             raise IndexError
#         return self.container[item]
#
#     def __setitem__(self, key: int, value: Banknote):
#         if 0 > key > len(self.container):
#             raise IndexError
#         self.container[key] = value


class Wallet:

    def __init__(self, *banknotes: Banknote):
        self.container = set()
        self.container.update(banknotes)
        # self.index = 0

    def __repr__(self):
        return f'Wallet({self.container})'

    # def __hash__(self):


    def __contains__(self, item):
        return item in self.container

    def __bool__(self):
        return len(self.container) > 0

    def __len__(self):
        return len(self.container)

    def __call__(self):
        return f'{sum(e.value for e in self.container)} $'

    # def __iter__(self):
    #     return Iterator(self.container)

    # def __getitem__(self, item: int):           # GETITEM work that as an ITERATOR !!!!!!
    #     #print('GETITEM work that as an ITERATOR !!!!!!')
    #     if 0 > item > len(self.container):
    #         raise IndexError
    #     return self.container[item]
    #
    # def __setitem__(self, key: int, value: Banknote):
    #     if 0 > key > len(self.container):
    #         raise IndexError
    #     self.container[key] = value



# if __name__ == '__main__':
#     banknote = Banknote(100)
#     thousand = Banknote(1000)
#     # other = Banknote(100)
#     # print(banknote == other)    # False
#     hundred = Banknote(100)
#     print(hundred == banknote)  # True
#     fifty = Banknote(50)
#     five_hundred = Banknote(500)
#     # print(hundred == fifty)  # False
#     # print(hundred >= fifty)  # True
#     # print(hundred <= fifty)  # False
#     # print(hundred < fifty)  # False
#     # print(hundred > fifty)  # True
#     # print(hundred >= banknote)  # True
#     # print(hundred <= banknote)  # True
#     wallet = Wallet(fifty, hundred, banknote, five_hundred, thousand, fifty)
#     print(wallet)
#     print(banknote in wallet)
#     if wallet: print('!')
#     print(len(wallet))
#     print(wallet())
#     print('='*50)
#     # print(wallet[3])
#     # wallet[0] = Banknote(500)
#     print(wallet)
#     # for money in wallet:
#     #     print(money)
#     # for money in wallet:
#     #     print(money)
#     print(thousand + thousand)
#     print(hash(wallet()))
#     print(wallet().__hash__())
#

class Frozendict(dict):
    def __init__(self, key, value):
        self.container = set()
        self.container.update(banknotes)
