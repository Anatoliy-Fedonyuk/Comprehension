# import time
#
# startTime = time.time()  #время начала замера
# numbers = [2, 3, 7, 9, 5, 0, 6, 3, 6, 0, 1, 7, 9, 4, 4, 4, 2, 2, 6, 9, 1, 7, 0, 3, 8, 1, 0, 3, 8, 0, 8, 4, 0, 2, 3, 6,
#            6, 1, 5, 8, 7, 2, 3, 8, 7, 7, 1, 2, 2, 8, 4, 3, 4, 8, 0, 7, 9, 8, 3, 7, 7, 7, 7, 5, 1, 7, 4, 5, 0, 8, 0, 9,
#            2, 4, 7, 6, 6, 5, 9, 7, 1, 7, 8, 8, 3, 4, 9, 7, 6, 4, 2, 0, 0, 0, 9, 4, 0, 9, 4, 4, 4, 5, 5, 4, 2, 5, 9, 4,
#            8, 1, 5, 7, 1, 0, 2, 6, 8, 7, 2, 7, 9, 3, 6, 4, 7, 5, 0, 7, 2, 0, 8, 2, 9, 8, 6, 4, 4, 7, 5, 5, 9, 4, 9, 5,
#            6, 9, 1, 1, 3, 1, 5, 2, 1, 7, 0, 0, 7, 8, 1, 3, 0, 0, 4, 4, 3, 3, 6, 7, 8, 6, 1, 2, 0, 2, 0, 9, 9, 0, 5, 2,
#            4, 1, 7, 4, 9, 9, 4, 9, 6, 9, 2, 7, 1, 2, 4, 5, 4, 0, 9, 0]*1000
#
# while 4 in numbers: numbers.remove(4)     #Время =  13.175898313522339
#
# n = len(numbers)                          #Вайл Время =  0.177109956741333
# while (n := n - 1) >= 0:
#     if numbers[n] == 4:
#         numbers.pop(n)
#
#
# n, new_num = len(numbers), []                          #СамБыстрыйВайл Время = 0.0264739990234375
# while (n := n - 1) > 0:
#     if numbers[n] != 4: new_num.append(numbers[n])
#
#
#
# new_num = []                                #For Время = 0.020205020904541016
# for i, n in enumerate(numbers):
#     if n != 4: new_num.append(n)
#
#
# new_num, ll = [], len(numbers)        #ForСамБыстр c len вынесен.за цикл Время = 0.015265703201293945
# for i in range(ll):
#     if numbers[i] != 4: new_num.append(numbers[i])
#
#
# new_num = []                                   #For Время = 0.022293806076049805
# for i, n in enumerate(numbers):
#     if n != 4: new_num += [n]
#
#
# for i, n in enumerate(numbers):                 #ForНаУдаление Время = 0.15477347373962402
#     if n == 4: del numbers[i]
#
#
# for i, n in enumerate(numbers):                 #ForНаУдаление Время = 0.15438437461853027
#     if n == 4: numbers.pop(i)
#
#
# numbers = [n for n in numbers if n != 4]          #ListComper Время = 0.0060689449310302734
#
#
# [numbers.pop(i) for i, n in enumerate(numbers) if n==4]     #ListComperDel Время = 0.1479654312133789
#
#
# numbers = list(n for n in numbers if n != 4)       #Gener Время = 0.009217500686645508
#
#
# numbers = [*filter(lambda x: x != 4, numbers)]           #Время = 0.010164737701416016
#
# endTime = time.time() #время конца замера
# WorkTime = endTime - startTime #вычисляем затраченное время
# print("Время работы = ", WorkTime)
# print(new_num)
# print(num)
#######################################################################################################################
###### Поработаем с  кэшем!!!!!!!!!!!С самой быстрой и самой медленной функцией!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# from time import time
# from functools import lru_cache


# num = (2, 3, 7, 9, 5, 0, 6, 3, 6, 0, 1, 7, 9, 4, 4, 4, 2, 2, 6, 9, 1, 7, 0, 3, 8, 1, 0, 3, 8, 0, 8, 4, 0, 2, 3, 6,
#            6, 1, 5, 8, 7, 2, 3, 8, 7, 7, 1, 2, 2, 8, 4, 3, 4, 8, 0, 7, 9, 8, 3, 7, 7, 7, 7, 5, 1, 7, 4, 5, 0, 8, 0, 9,
#            2, 4, 7, 6, 6, 5, 9, 7, 1, 7, 8, 8, 3, 4, 9, 7, 6, 4, 2, 0, 0, 0, 9, 4, 0, 9, 4, 4, 4, 5, 5, 4, 2, 5, 9, 4,
#            8, 1, 5, 7, 1, 0, 2, 6, 8, 7, 2, 7, 9, 3, 6, 4, 7, 5, 0, 7, 2, 0, 8, 2, 9, 8, 6, 4, 4, 7, 5, 5, 9, 4, 9, 5,
#            6, 9, 1, 1, 3, 1, 5, 2, 1, 7, 0, 0, 7, 8, 1, 3, 0, 0, 4, 4, 3, 3, 6, 7, 8, 6, 1, 2, 0, 2, 0, 9, 9, 0, 5, 2,
#            4, 1, 7, 4, 9, 9, 4, 9, 6, 9, 2, 7, 1, 2, 4, 5, 4, 0, 9, 0)*1000
#
# # @lru_cache(maxsize=100)
# def most_slowly(num):
#     while 4 in num:
#         num.remove(4)                                       #test slowfunc: 49.38264060020447 sec.
#
# def most_quickly(num):
#     kum = [n for n in num if n != 4]                        #test fastfunc: 0.009973764419555664 sec.


# @lru_cache()
# def test(num):
#     res = 0
#     for i in range(num):
#         res += i
#     return res
#
#
# start = time()                              # test time: 6.002902984619141 sec.  with cache
# test(100_000_0000)                           # test time: 6.526479005813599 sec. without cache
# end = time()
#
# print(f'test time: {end - start} sec.')

# from time import time
# from functools import lru_cache
#
#
# @lru_cache(maxsize=None)
# def fib(n):
#     if n < 2:
#         return n
#     return fib(n - 1) + fib(n - 2)
#
#
# start = time()
# [fib(n) for n in range(32)]
# end = time()
#
# print(f'test time: {end - start} sec.')
# print(fib.cache_info())
# print(test.cache_clear())

#######################################################################################################################


# word = input()
# while word:
#     print(word)
#     word = word[1:-1]

# n, i = int(input()), 0
# while (i:=i+1)**2 <= n: print(i**2)

# x, y = map(int, input().split())
# day = 1
# while x < y:
#     x *= 1.15
#     day += 1
# print(day)

# n, m = map(int, input().split())
# day = 0
# while n > 0:
#     n -= 1
#     day += 1
#     if not day % m: n += 1
# print(day)

# a, b = map(int, input().split())
# H = 0
# while a != 0:
#     a -= 1
#     H += 1
#     if not H % b: a += 1
# print(H)

# n, s = int(input()), 0
# while n != 1:
#     if not n % 2:
#         n //= 2
#         s += 1
#     else:
#         print("НЕТ")
#         break
# else:
#     print(s)

# s_n = str(n)
# print(int(str(n)[0]))

# n = int(input())
# while (d1:=str(n)[0]) != '1' and n<1000000000: n *= int(d1)
# print(n)

# n, ls = int(input()), []
# while (l:= int(input())):
#     if sum(ls) + l <= n:
#         ls.append(l)
#     else:
#         print("Довольно!", sum(ls), len(ls), sep='\n')
#         break

# t = [*range(0,55,5)]
# n, k = map(int, input().split())
# timm = [sum(t[:j+1]) for j in range(len(t)) if j<=n]
# while True:
#     if timm[-1]+k <= 240:
#         print(len(timm)-1)
#         break
#     else:
#         timm.pop()

# n, k = map(int, input().split())
# c = 0                               #Счетчик переменная - сколько задач успеет решить
# while (k <= 240) * (c <= n):        #Гениально - создаем вайл с двумя условиями! и время проверяем и n
#     c += 1                          #счетчик задач увеличиваем на 1
#     k += c * 5                      #к времени проезда добаляем по одному время на каждое задание!
# print(c - 1)                        # Результат)))


# [print(x) for x in input()[::-1]]
# n = int(input())
# while n > 0:
#     print(n%10)
#     n //= 10

# print(*input()[::-1], sep='\n')

# print('\n'.join(input()[::-1]))

# print(input())
# print(sum(map(int, list(input()))))

# print(eval('*'.join(input())))

# ls = [*map(int, list(input()))]
# print(min(ls), max(ls), sep='\n')

# n = input()                             #УДИВИТЕЛЬНО И НАХ ТОТ INT))
# print(min(*n), max(*n), sep = '\n')

# print(input().count('7'))

# n = int(input())
# i, a = 1, []
# while i*i <= n:
#     if n%i == 0:
#         a.append(i)
#         a.append(n//i)
#         # if i != n//i:
#         #     a.append(n//i)
#     i+=1
# print(*sorted(set(a)))

# n = int(input())
# a = [{x,n//x} for x in range(1, int(n**0.5)+1) if not n%x]
# print(*sorted([y for r in [{x,n//x} for x in range(2, int(n**0.5)+1) if not n%x] for y in r]))
# a = [y for r in [{x,n//x} for x in range(2, int(n**0.5)+1) if not n%x] for y in r]
# print("YNeos"[(a!=[] or n==1)::2])

# n = int(input())
# print(sum([y for r in [{x, n//x} for x in range(1, int(n**0.5)+1) if not n%x] for y in r]))

# empty = None
# empty_too = None
# print(empty is empty_too)
# print(empty is not empty_too)

# print(i_love_none := [None] * 50)

# fr_abra = frozenset('abracadabra')
# print(fr_abra)
#
# fr_nums = frozenset([2, 1, 2, 4, 5, 2, 1])
# print(fr_nums)
#
# lang = {'eng':'Английский', 'ru':'Русский'}
#
# print(frozenset(lang))
#
# my_set = {1, 2, 2, 3}
# print(frozenset(my_set))

# print(my_frozen := frozenset(int('7'*i) for i in range(1, 78)))
# print(type(my_frozen))
# print({int('7'*i) for i in range(1, 78)})

# A = frozenset([1, 2, 3, 4])
# B = frozenset([3, 4, 5, 6])
# print(A | B, A & B)
# print(A ^ B, A - B)


# print("Рассказ про методы множеств")
# stringik = "abcdef"
# listik = ["e", "f", "g", "h", "i", "k"]
# tuplik = ("i", "k", "l", "m", "n", "o")
# settik = {"a", "b", "g", "h", "l", "m", "n", "o", "p", "q", "r", "s"}
# frozik = frozenset({"c", "d", "g", "h", "l", "m", "n", "r", "s", "t", "u", "v"})
# print("Мы будем использовать такие итерируемые объекты:")
# print("Строку stringik:", stringik, type(stringik))
# print("Список listik:", listik, type(listik))
# print("Кортеж tuplik:", tuplik, type(tuplik))
# print("Множество settik:", settik, type(settik))
# print("Замороженное множество frozik:", frozik, type(frozik))
# print()
# print("Будем сохранять в result результаты метода difference(), печатать его и его тип.")
# result = settik.difference(stringik)
# print("result = settik.difference(stringik):", result, type(result))
# result = settik.difference(tuplik)
# print("result = settik.difference(tuplik):", result, type(result))
# result = settik.difference(frozik)
# print("result = settik.difference(frozik):", result, type(result))
# result = frozik.difference(stringik)
# print("result = frozik.difference(stringik):", result, type(result))
# result = frozik.difference(tuplik)
# print("result = frozik.difference(tuplik):", result, type(result))
# result = frozik.difference(settik)
# print("result = frozik.difference(settik):", result, type(result))


# ----------------------------------------------------
######   ООП    #######
# ----------------------------------------------------
# from tkinter import Tk
#
# root = Tk()
# root.mainloop()

# class Purse:
#
#     def __init__(self, valuta, name='Unknown'):
#         if valuta not in ('USD', 'EUR'):
#             raise ValueError
#         self.__money = 0.00
#         self._valuta = valuta
#         self.name = name
#
#     def top_up_balance(self, howmany):
#         self.__money = self.__money + howmany
#         return howmany
#
#     def top_down_balance(self, howmany):
#         if self.__money - howmany < 0:
#             print("На счету не достаточно средств")
#             raise ValueError("На счету не достаточно средств")
#         self.__money = self.__money - howmany
#         return howmany
#
#     def info(self):
#         print(self.__money, self._valuta)
#
#     def __del__(self):
#         print("Кошелек удален")
#         # return self.__money
#
#
# x = Purse('USD')
# y = Purse('USD', 'Bill')
# x.top_up_balance(100)
# y.top_up_balance(100)
# x.top_up_balance(y.top_down_balance(25))
# x._valuta = 'Юань'
# x.info()
# y.info()
# print(x._valuta)
# print(y._Purse__money)          #АААААААААААА!!!!! так находка для шпиона))

# d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# print(('a', 1) in d.items())                        #Вона оно как)) True!!!!

# from class3 import Verification
# # from tkinter import Tk, Button
#
#
# class V2(Verification):
#
#     def __init__(self, login, password, age=100): # Переопределение конструктора и чтоб не дублировать часть кода вызовем родительский метод
#         super().__init__(login, password, age)
#         self.__save()                     # переопределяем добавляя функционал, чтобы не вызывать методы извне...
#         print(self.show())
#
#     def __save(self):                                        # Переопределение метода save
#         with open('users') as r:                            # по умолчанию 'rt'
#             for i in r:
#                 if i == f'{self.login, self.password, self.age}'+'\n':
#                     raise ValueError ('Такой пользователь уже есть')
#         super().save()                # Чтобы не дублировать код записываем с помощью родительского save
#
#
#     def show(self):
#         return (self.login, self.password, self.age)
#
# y = V2('Givi', '33333333333')

# class My_app(Tk):
#
#     def __init__(self):
#         Tk.__init__(self)
#         self.geometry('400x400')
#         self.setUI()
#
#     def setUI(self):
#         Button(self, text='OK').pack()
#
#
# root = My_app()
# root.mainloop()

# def parse_response(value):
#     match value:
#         case {'key': 1000, **rest}:
#             return rest['id']
#         case ('error', message) | ('error', message, *_):
#             raise ValueError(message)
#         case {'meta': val, **rest} if not rest:
#             return val['id']
#         case {'meta': {'code': _, 'error': error}, 'info': [{'allowed': allowed}, *_]}:
#             return f'{error}, {allowed}'
#         case (set() as x, y) if len(x) == 2:
#             return max(x)/y
#         case _:
#             raise ValueError(f'Unknown value: {value}')
#
#
# if __name__ == '__main__':
#     a = {'key': 1000, 'id': 999}
#     b = ['error', 'Slow network connection!']
#     c = {'meta': {'id': 999}}
#     d = {'meta': {'code': 200, "error": 'no'}, 'info': [{'allowed': 'yes'}, 111, 222]}
#     e = ({100, 12}, 5)
#     print(parse_response(e))
import datetime

today = datetime.datetime.now()
print(f'{today=:%d.%m.%Y %H:%M}')
t = f'{today:%d-%m-%Y}'
print(t)
real = 217.86; full = 344.5
proc = f'{real/full:.2%}'
print(proc)

now = datetime.datetime.now()
print(now.time(), now.hour, now.minute, now.second)