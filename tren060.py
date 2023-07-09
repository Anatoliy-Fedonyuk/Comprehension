# Словари!!!!!

# d = {v.split("=")[0]: int(v.split("=")[1]) for v in input().split()}
# print(*sorted(d.items()))

# print([i.split('=') for i in input().split()])    # Создает вложеный список

# import sys
# ls = list(map(str.strip, sys.stdin.readlines()))
# print(*sorted({int(i.split('=')[0]): i.split('=')[1] for i in ls}.items()))

# d = dict(i.split('=') for i in input().split())
# print(("НЕТ", "ДА")[1 if 'house' in d and 'True' in d and '5' in d else 0])

# d = {i.split('=')[0]: i.split('=')[1] for i in input().split()}
# if 'False' in d:
#     del d['False']
# if '3' in d:
#     del d['3']
# print(*sorted(d.items()))

# d = {i.split('=')[0]: i.split('=')[1] for i in input().split() if i.split('=')[0] not in ['False', '3']}
# print(*sorted(d.items()))

# lst = input().split()   # Zad 6.1.7 know metody dict
# d = {}
# for i in range(len(lst)):
#     if d.get(lst[i][:2]) != None:
#         d.get(lst[i][:2]).append(lst[i])
#     else:
#         d.update({lst[i][:2]:[lst[i]]})
# print(d)

# lst, d = input().split(), {}
# for i in lst:
#     if i[:2] in d:
#         d[i[:2]] += [i]
#     else:
#         d[i[:2]] = [i]
# print(*sorted(d.items()))

# lst, d = input().split(), {}    # My onestr)
# [d[i[:2]].append(i) if i[:2] in d else d.update({i[:2]: [i]}) for i in lst]
# print(*sorted(d.items()))

# n = input().split()
# d = dict([(x[:2], [i for i in n if x[:2] == i[:2]]) for x in n])      #Гениально
# print(*sorted(d.items()))

# import sys
# ls2 = [i.split()[::-1] for i in list(map(str.strip, sys.stdin.readlines()))]    #My
# print(*sorted({j[0]: [h[1] for h in ls2 if j[0]==h[0]] for j in ls2}.items()))

# d = {}          # Zad 6.1.9
# while True:
#     n = int(input())
#     if n == 0:
#         break
#     if n in d:
#         print(f"значение из кэша: {d[n]}")
#     else:
#         d[n] = round(n**0.5, 2)
#         print(d[n])

# d = {}
# while n := int(input()):
#     print(f'значение из кэша: {d[n]}' if n in d else (r := round(n**0.5, 2)))    #Лаконично
#     d[n] = r

# import sys
# ls, d = list(map(str.strip, sys.stdin.readlines())), set()
# for i in ls:
#     print(f"Взято из кэша: HTML-страница для адреса {i}" if i in d else f"HTML-страница для адреса {i}")
#     d.add(i)
# print(d)

# d = {'а': '.-', 'б': '-...', 'в': '.--', 'г': '--.', 'д': '-..', 'е': '.',          # Zad 6.2.3
#        'ж': '...-', 'з': '--..', 'и': '..', 'й': '.---', 'к': '-.-',
#        'л': '.-..', 'м': '--', 'н': '-.', 'о': '---', 'п': '.--.', 'р': '.-.',
#        'с': '...', 'т': '-', 'у': '..-', 'ф': '..-.', 'х': '....', 'ц': '-.-.',
#        'ч': '---.', 'ш': '----', 'щ': '--.-', 'ъ': '--.--', 'ы': '-.--',
#        'ь': '-..-', 'э': '..-..', 'ю': '..--', 'я': '.-.-', ' ': '-...-'}

# print(*[d.get(i) for i in input().lower()])

# d_new = {value: key for key, value in d.items()}           # Zad 6.2.4
# print(*[d_new.get(i) for i in input().split()], sep="")

# print(*(dict.fromkeys(input().split())).keys())         # Zad 6.2.5
# print(*{i: None for i in input().split()})

# import sys              # Zad 6.2.6
# ls = [i.split() for i in list(map(str.strip, sys.stdin.readlines()))]
# d = {j[0]: [h[1] for h in ls if j[0]==h[0]] for j in ls}
# [print(f"{key}: {', '.join(value)}") for key, value in d.items()]

# n = int(input())
# ls_cup = [64, 32, 16, 8, 4, 2, 1]
# for cupur in ls_cup:
#     while n - cupur >= 0:
#         print(cupur, end=' ')
#         n -= cupur

# things = {'карандаш': 20, 'зеркальце': 100, 'зонт': 500, 'рубашка': 300,                              # Zad 6.2.7
#           'брюки': 1000, 'бумага': 200, 'молоток': 600, 'пила': 400, 'удочка': 1200,
#           'расческа': 40, 'котелок': 820, 'палатка': 5240, 'брезент': 2130, 'спички': 10}
# N, ans = int(input())*1000, ''
# things = dict(sorted([(value, key) for key, value in things.items()], reverse=True))
# for i in things:
#     if N - i >= 0:
#         N -= i
#         ans += things[i] + ' '
# print(ans)

# a = ('abc', 2, [1, 2], True, 2, 5)
# print(a.count(2))
# print(a.count(3))
# print(a.index(3, 2, -1))

# t = (3.4, -56.7)
# print(t + tuple(map(int, input().split())))

# t = tuple(input().split())
# print(*(t + ('Москва',) if 'Москва' not in t else t))

# t = tuple(input().split())
# print(*tuple(i for i in tuple(input().split()) if i != "Ульяновск"))

# [print(i, end=' ') for i in tuple(input().lower().split()) if "ва" in i]

# t, ans = tuple(input().split()), []
# [ans.append(i) for i in t if i not in ans]
# print(*ans)

# print(*dict.fromkeys(input().split()))

# t = tuple(input().split())                # Zad 6.3.8
# [print(i, end=' ') for i in range(len(t)) if t.count(t[i]) > 1]

# t = ((1, 0, 0, 0, 0),           # Zad 6.3.9
#      (0, 1, 0, 0, 0),
#      (0, 0, 1, 0, 0),
#      (0, 0, 0, 1, 0),
#      (0, 0, 0, 0, 1))
# N, t2 = int(input()), ()
# for i in range(N):
#     row = ()
#     for j in range(N):
#         row += (t[i][j],)
#     t2 += (row,)
#     print(*row)
#
# print(tuple([x[:N] for x in t][:N]))     # Вариант одним циклом!!! со срезами = t2

# import sys                # Zad 6.3.10
# print(tuple(tuple(i.split()) for i in list(map(str.strip, sys.stdin.readlines()))))

# import sys
# ls = list(map(str.strip, sys.stdin.readlines()))
# print(tuple(map(tuple, map(str.split, ls))))

# print(*sorted(set(map(float, input().split()))))  # 6.4.3
# print(len(set(input().lower().split())))      # 6.4.4

# m, n = set(input()), set("0123456789")          # 6.4.5 my
# print("НЕТ") if m & n == set() else print(*sorted(m & n))

# print(*sorted(set(int(c) for c in input() if c.isdigit())) or ['НЕТ'])  # 6.4.5 лог.оператор прямо в принт и работа с исдижит

# m = {int(x) for x in input() if x.isdigit()}        # 6.4.5 my
# print(*sorted(m) if len(m) else ["НЕТ"])

# import sys
# print(len(set(map(str.strip, sys.stdin.readlines()))))

# import sys
# ls = list(map(str.strip, sys.stdin.readlines()))
# print(len({i.split(':')[0]: i.split(':')[1] for i in ls}))

# print(len(set(line.split(':')[0] for line in open(0)))) #не пашет

# a = set()    # 6.4.8
# while True:
#     s = input().lower()
#     if s == 'q':
#         break
#     a.add(s)
# print(len(a))

# print(len(set(iter(input, 'q'))))       # Analog ))

# sex = set(input().split())    # 6.5.1
# six = set(input().split())
# print(*sorted(sex & six))

# sex = set(input().split())        # 6.5.2
# six = set(input().split())
# print(*sorted(map(int, (sex - six))))

# sex = set(input().split())      # 6.5.3
# six = set(input().split())
# print(*sorted(map(int, (sex ^ six))))

# sex = set(input().split())      # 6.5.4
# sexy = set(input().split())
# print(("НЕТ", "ДА")[sex == sexy])

# 6.5.5
# print(['ДОПУЩЕН', 'НЕ ДОПУЩЕН']['2' in set(input().split())])

# sex = set(input().split())      # 6.5.6
# sexy = set(input().split())
# print(("НЕТ", "ДА")[sex <= sexy])

# N = int(input())
# print(("НЕТ", "ДА")[{i for i in range(1, 8) if N%i == 0} >= {2, 3, 5}])

# s = input().split()       # 6.6.2
# print(dict(enumerate(s[1:], start=int(s[0])))[4])

# a, *s = input().split()      # 6.6.2
# print({int(a) + i: s[i] for i in range(len(s))}[4])

# import sys
# print(len(set(map(str.strip, sys.stdin.readlines()))))

# s = input().lower().split()
# print(len({i for i in s if len(i) > 2}))

# st = input().lower().split()        # 6.6.5
# print({i: st.count(i) for i in st}['и']) if 'и' in st else print("0")

# lst = input().lower().split()       # 6.6.5 интересно
# print({w: lst.count(w) for w in lst}.get('и', 0))

# import sys            # Final задание раздела 6!!! результат будет далее использоваться!!!
# ls = list(map(str.strip, sys.stdin.readlines()))
# d = {j.split(': ')[0]: {i.split(': ')[1] for i in ls if i.split(': ')[0]==j.split(': ')[0]} for j in ls}

