# a, b = map(str, input().split())
# print(a, a, a, b, b)

# a, b = input().split()  # Работает надо разобраться
# a, b = 'hello', 'Python'
# print(' '.join([a]*2 + [b]*3))

# a, b = input().split()
# # Переменная a = 2, переменная b = -5
# print("Переменная a = " + a + ", переменная b = " + b)

# Строка: hello Balakirev. Длина: 15
# c = input()
# print('Строка: ' + c + '. Длина: ' + str(len(c)))

# a, b = input().split()
# print(a in b, a == b, a > b, a < b)

# s1, s2 = input().split() # СТремно но работает
# op = ['in','==', '>', '<']
# for i in op:
#     print(eval(f's1 {i} s2'), end=' ')

# Коды: a = 97, z = 122
# a, b = input().split()
# print(f"Коды: {a} = {ord(a)}, {b} = {ord(b)}")

# c = input()    # I love Python
# print(c[0]+c[-1])

# d = input()
# e = input()
# print(d[::2], e[1::2])

# c = input() # abrakadabra
# c1 = c[0:5]
# print(c1[::-1])

# a, b = input().split()
# print(a[1:len(b):2] == b[1::2])

# q = 'HALLO'
# print(q.capitalize())
# a = input().lower()
# print(a[0].upper()+ a[1::])

# i = input()
# print(i.find("ra"))

# a, b, c = map(str, input().split())
# print(a.rjust(3, '0'))
# print(b.rjust(3, '0'))
# print(c.rjust(3, '0'))

# print(len(input().split()))

# print(";".join(input().split()))
# print(input().replace(" ", ';'))

# t = "\tPanda needs\nPython"
# print(t)
# s = "Тема занятия \"спецсимволы\""
# print(s)
# print(input().replace(" ", "\\"))

# s = input().replace(" ", '\"')
# print(input().replace(" ", '\"').replace("\"", "\'", 1))
# print('\"' + input() + '\"')

# n = input()
# f = input()
# a = int(input())
# print("Уважаемый {name} {family}! Поздравляем Вас с {age}-летием!".format(name=n, family=f, age=a))

# a, b, c = map(str, input().split())
# print("Габариты: {shir} x {glub} x {vis}".format(shir=a, glub=b, vis=c))

# ls = list(map(int, input().split()))
# ls.sort()
# print(ls[0], ls[1])

# a, b = map(int, input().split())
# print(f'{(a < b) * a + b * (b < a)} {(a > b) * a + b * (b > a)}')

# print(*sorted(input().split()))

# city = input()
# street = input()
# house = int(input())
# number = int(input())
# print(f"г. {city}, ул. {street}, д. {house}, кв. {number}")

# print(', '.join([s+' '+input() for s in ['г.', 'ул.', 'д.', 'кв.']]))

# kurs = float(input())
# grn = int(input())
# print(f"Вы можете получить {int(grn // kurs)}$ за {grn} гривен по курсу {kurs}")

# a = [5, 7, 9, 3, 2, 6, 5, 3, 9, 8]
# print(sum(a)/len(a))        # Среднее число по списку

# a, b, c = map(int, input().split())
# lst = [a, b, c]
# print(lst)

# cities = input().split()
# print('Москва' in cities)

# a = [0, True, "Москва", 5, False, "Омск"]
# print(a[3])
# print(a[-3])

# marks = list(map(int, input().split()))
# print(round(sum(marks)/len(marks), 1))

# name = input()
# avtor = input()
# stran = int(input())
# zina = float(input())
# book = [name, avtor, stran, zina]
# del book[2]
# book[1] = 'Пушкин'
# book[2] *= 2
# print(book)

# pipl = list(map(int, input().split()))
# print(f"{max(pipl)} {min(pipl)} {sum(pipl)}")

# lst = list(map(int, input().split()))
# lst = sorted(lst, reverse=True)
# print(*lst)

# lst = input().split()
# cities = ["Москва", "Тверь", "Вологда"]
# lst = lst + cities
# print(*lst)

# v = [1205, 1101, 1434, 1320, 923, 874]
# print(v[-4:])

# c = ["Москва", "Ульяновск", "Самара", "Тверь", "Вологда", "Омск", "Уфа"]
# print(c[1::2])

# lst = list(map(int, input().split()))
# lst.append(lst[0] != lst[-1])
# print(*lst)

# cities = ["Москва", "Казань", "Ярославль"]
# cities.insert(1, "Ульяновск")
# print(*cities)

# lst = list(input())     # Задача обработки номера
# lst.remove('+')
# lst[0] = '8'
# s = lst.count('-')
# for i in range(s):
#     lst.remove('-')
# print("".join(lst))
#
# print(input().replace('+7', '8').replace('-', ''))  # Та же Задача обработки номера

# fio = input().split()
# print(f"{fio[2]} {fio[0][0]}.{fio[1][0]}.")

# lst = list(map(int, input().split()))
# lst.sort()
# print(lst[0], lst[1], lst[2])

# lst = list(map(int, input().split()))
# lst.append(lst.pop() % 2 != 0)
# print(*lst)

# print(input().split().count('2'))

# lst = input().split()
# lst.sort()
# lst.pop(0)
# print(*lst)

# a = [5.4, 6.7, 10.4]
# l = list(map(int, input().split()))
# print(a + [l])

# lst = [list(map(int, input().split()))] + [list(map(int, input().split()))] + [list(map(int, input().split()))]
# [print(lst[i][-1], end=' ') for i in range(len(lst))]

# a = [True, [1, 0, ["True", ["Истина", "Ложь"], "False"]], False]
# print(a[1][2][1][0])

# a = [True, [1, 0, ["True", ["Истина", "Ложь"], "F"]], False]
# del a[1][2][2]
# print(a)

# t = [["Скажи-ка", "дядя", "ведь", "не", "даром"],
#     ["Я", "Python", "выучил", "с", "каналом"],
#     ["Балакирев", "что", "раздавал?"]]
# s = input()
# lst = t[0] + t[1] + t[2]
# print(s in lst)
# print(input() in str(t))
# print(input() in sum(t, []))

# x = int(input())
# if x:
#     print('x True')
# else:
#     print('x False')

# a, b = list(map(float, input().split()))
# if a >= b:
#     print(a)
# else:
#     print(b)

# x = input().upper()
# if x == x[::-1]:
#     print("ДА")
# else:
#     print('НЕТ')

# m, n = map(int, input().split())
# if (m // n) == (m / n):
#     print(int(m/n))
# else:
#     print(f"{m} на {n} нацело не делится")

# a, b, c = map(int, input().split())
# if a**2 + b**2 == c**2:
#     print("ДА")
# else:
#     print("НЕТ")

# x = input()
# if 't' in x and 'h' in x and 'o' in x:
#     print("ДА")
# else:
#     print("НЕТ")

# lst = input().split()
# if 'Москва' in lst:
#     lst.remove('Москва')
# print(lst)

# a, b, c, d = map(int, input().split())
# if c <= a - 2 and d <= b - 2 or c <= b - 2 and d <= a - 2:
#     print("ДА")
# else:
#     print("НЕТ")

# x = list(map(int, input()))
# print("ДА" if sum(x[:3]) == sum(x[-3:]) else "НЕТ")

# x = float(input())
# print("green" if (x % 5) <= 3 else "red")

# m = '''1. Введение в Python
# 2. Строки и списки
# 3. Условные операторы
# 4. Циклы
# 5. Словари, кортежи и множества
# 6. Выход'''
# item = int(input('Введите пункт меню от 1 до 6: '))
# l = list(m.split("\n"))
# if 1 <= item <= 6:
#     print(l[item-1])
# else:
#     print('Неверный пункт')

# a, b, c = map(int, input().split())
# if a <= b:
#     if a <= c:
#         print(a)
#     else:
#         print(c)
# elif b <= a:
#     if b <= c:
#         print(b)
#     else:
#         print(c)

# x = float(input())
# if 0 < x <= 60:
#     print(1)
# elif 60 < x <= 64:
#     print(2)
# elif 64 < x <= 69:
#     print(3)
# else:
#     print(4)

# day = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']
# print(day[int(input())-1])

# days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# print(days[int(input())-1])

# days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
# m, n = map(int, input().split())
# if 1 > m or m > 12 or 1 > n or n > days.get(m):
#     print('Введите корректную дату')
# elif n == 1:
#     m0 = m - 1
#     n0 = days.get(m-1)
#     m1 = m
#     n1 = n + 1
# elif n == days.get(m):
#     m0 = m
#     n0 = n - 1
#     m1 = m + 1
#     n1 = 1
# else:
#     m0 = m
#     n0 = n - 1
#     m1 = m
#     n1 = n + 1
# print(f"{m0:02}.{n0:02} {m1:02}.{n1:02}")

# day = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']
# print(day[(int(input()) - 1) % 7])

# a = float(input())
# b = float(input())
# print(a) if a > b else print(b)

# print("кратно 3") if (int(input())) % 3 == 0 else print("не кратно 3")

# word = input().upper()
# print("палиндром") if word == word[::-1] else print("не палиндром")

# print(bool(int(input())))

# x = int(input())
# print(x + 1) if x != 59 else print(0)
# Вводится текущее время (секунды) в диапазоне [0; 59]. Если значение равно 59, то следующее должно быть 0.
# И так по кругу. Необходимо  вычислить следующее значение с проверкой граничного значения 59.
# Реализуйте это с помощью тернарного условного оператора. Результат отобразите на экране.
# P.S. Попробуйте также реализовать эту же задачу с использованием только арифметических операций.
# n = int(input())
# print((n + 1) % 60)


# m = ['до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']
# # a, b, c = map(int, input().split())
# # A = "#" + m[a-1] if a == 1 or a == 4 else m[a-1]
# # B = "#" + m[b-1] if b == 1 or b == 4 else m[b-1]
# # C = "#" + m[c-1] if c == 1 or c == 4 else m[c-1]
# # print(A, B, C)

