# import copy
# import sys

# n, m = map(int, input().split())
# l = []
# while n < (m +1):
#     l.append(n ** 2)
#     n += 1
# print(*l)

# x = float(input())
# i = 2
# while i < 11:
#     print(round(x * i, 1), end=' ')
#     i += 1

# x = int(input())
# i, s = 1, 0
# while i < (x + 1):
#     s += 1/i
#     i += 1
# print(round(s, 3))

# i, s = 1, 0
# while i != 0:
#     i = int(input())
#     s += i
# print(s)

# slag = input()
# while "--" in slag:
#     slag = slag.replace("--", "-")
# print(slag)

# x = list(input())
# s, i = 1, 0
# while i < len(x):
#     s *= int(x[i])
#     i += 1
# print(s)

# n = int(input()) - 2
# fib1 = fib2 = 1
# print(fib1, fib2, end=" ")
# i = 0
# while i < n:
#     fib_sum = fib1 + fib2
#     print(fib_sum, end=" ")
#     fib1 = fib2
#     fib2 = fib_sum
#     i += 1

# n = int(input())
# fib = [1, 1]
# i = 2
# while i < n:
#     fib.append(fib[i-2] + fib[i-1])
#     i += 1
# print(*fib)

# t = int(input())
# i, s = 1, 1
# while i <= t // 3:
#     s *= 2
#     i += 1
# print(s)
# print(2 ** (int(input()) // 3)) # То же одной строкой

# print(round(1000 * 1.05 ** int(input()), 2))    # считает простой процент за введенное кол-во лет

# n, m = map(int, input().split())
# l = []
# while n < (m +1):
#     if n % 2 != 0:
#         l.append(n)
#     n += 1
# print(*l)

# i = 100
# while i < 1000:
#     if i % 47 == 43 and i % 3 == 0:
#         print(i, end=" ")
#     i += 1

# p = [0] * 10
# while sum(p) < 5:
#     s = int(input())
#     if p[s] != 0:
#         continue
#     p[s] = 1
# print(*p)

# print('ДА' if min(list(map(len, input().split()))) > 5 else 'НЕТ')
# print(('НЕТ', 'ДА')[len(min(input().split(), key=len)) > 5])
# l = input().split()
# i = 0
# while i < len(l):
#     if len(l[i]) < 6:
#         print("НЕТ")
#         break
#     i += 1
# else:
#     print("ДА")

# ll = input().upper().split()
# i = 0
# while i < len(ll):
#     if ll[i][0] in ll[i][-1]:
#         print("ДА")
#         break
#     i += 1
# else:
#     print("НЕТ")
# print(['НЕТ', 'ДА'][any(i[0] in i[-1] for i in input().lower().split())])
# print('ДА' if any(map(lambda x: x[0] in x[-1], input().upper().split())) else 'НЕТ')

# n = int(input())
# i, l = 1, []
# while i <= n:
#     if not i%3 and not i%5:
#         l.append(i)
#     elif n > 99:
#         print("слишком большое значение n")
#         break
#     i += 1
# else:
#     print(*l)

# n = int(input())
# print([x for x in range(1, n*10) if x ** 2 > n][0]) # Я сделал а вы там идавитесь
# print(int(int(input()) ** .5) + 1)  # Математика рулит)

# x, y = int(input()), 0
# while 10 * 1.1 ** y < x:
#     y += 1
# else:
#     print(y+1)

# import sys
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# # d = len(lst_in)
# # i, l_new = 0, []
# # while i < d:
# #     if " " not in lst_in[i]:
# #         l_new.append(lst_in[i])
# #     i += 1
# # print(*l_new)
# print(*[lst_in[x] for x in range(len(lst_in)) if " " not in lst_in[x]])

# print(*range(11))
# print(*range(10,-1,-1))
# print(*reversed(range(11)))
# print(*range(11)[::-1])
#
# print(*range(-10,0,2))
# print(*range(1,20,3))

# lst = list(map(int, input().split()))
# print(lst)
# sn = 0
# for i, d in enumerate(lst):
#     if d % 2 != 0:
#         sn += d
# print(sn)
# print(sum([i for i in map(int, input().split()) if i % 2 != 0]))    #!

# print(*[len(s) for s in input().split()])

# n = int(input())
# var = [i for i in range(1, n + 1) if not n % i]
# if len(var) <= 2:
#     print("ДА")
# else:
#     print("НЕТ")

# n = int(input())
# print("ДА") if len([i for i in range(1, n + 1) if not n % i]) <= 2 else print("НЕТ")

# l = input().lower().replace('ь', '').replace('ы', '').replace('ъ', '').split()    #Мое творенье))
# print(['ДА', 'НЕТ'][any(True for i in range(len(l)-1) if l[i][-1] != l[i+1][0])])

# c = input().lower().split()
# print(('НЕТ', 'ДА')[[i[0] for i in c[1:]] == [i.strip("ьъы")[-1] for i in c[:-1]]])

# print(sum([i for i in  range(3,int(input())) if not i%3 or not i%5]))

# n = int(input())
# print(sum(set(range(3, n, 3)) | set(range(5, n, 5))))

# st = input().lower()
# s = set(st.find('ра', i) for i in range(len(st)))
# if len(s) > 1:
#     s.discard(-1)
# print(*sorted(s))

# s = input().lower()
# res = [i for i in range(len(s) - 1) if s[i:i+2] == 'ра']
# print(*res or [-1])

# p = input()
# num, sim = p[3:6] + p[7:10] + p[11:13] + p[14:], p[0:3] + p[6] + p[10] + p[13]
# print("ДА" if len(p)==16 and sim=='+7()--' and num.isdigit() else "НЕТ")

# print(sum(map(int, input().replace(' ', '').replace('-', '+-').split("+"))))
#
# print(eval(input())     #???

# print(*list(map(lambda x: int(x)**2, input().split())))

# lst = input().split()
# new = []
# for i, val in enumerate(lst):
#     new += [val, val]
# print(*new)

# print(*[f'{i} {i}' for i in input().split()])       # Гениально и просто

# L = list(map(float, input().split()))
# mi = L[0]
# for i in L:
#     if i < mi:
#         mi = i
# print(mi)

# x = list(map(float, input().split()))
# for i, y in enumerate(x):
#     if y < 0:
#         print(-1.0, end=' ')
#     else:
#         print(y, end=" ")

# it = iter(range(0, -9, -2))
# print(next(it))
# print(next(it))
# print(next(it))
# print(range(11))

# cit = iter(input().split())
# print(next(cit)), print(next(cit))

# it = iter(input().split())
# print(next(it), next(it), sep="\n")     # work separator for print

# print(*iter(input().split()[0:2]),sep='\n')
# print(*iter(range(0, -11, -2)),sep='|')

# print(*iter(input().split()[0]), sep='')

# s = input()
# it = iter(s)
# for j in range(s.find(" ")):
#     print(next(it), end="")

# print(*[i for i in iter(input())])

# print("-"*40)           # Shess table))
# for i in range(1,9):
#     for j in "abcdefgh".upper():
#         print(f"|{j},{i}|", end='')
#     print(), print("-"*40)

# a = [[1,2,3],[2,3,4],[3,4,5]]   # Summ two matrix
# b = [[1,1,1],[2,2,2],[3,3,3]]
# c = []
# for i, row in enumerate(a):
#     r = []
#     for j, x in enumerate(row):
#         r.append(x + b[i][j])
#     c.append(r)
# print(c)

# t = ["Скажи - ка   дядя  ведь  недаром", "я Python    выучил с   каналом", "Балакирев,   что   раздавал"]
# for i, line in enumerate(t):
#     while line.count('  '):
#         line = line.replace('  ', ' ')
#     t[i] = line
# print(t)

# A = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
# # Транспонирование Матрицы квадратной
# for r in A:
#     for x in r:
#         print(x, end= '\t')
#     print()
# print("="*15)
#
# for i in range(len(A)):
#     for j in range(i+1, len(A)):
#         A[i][j], A[j][i] = A[j][i], A[i][j]
#
# for r in A:
#     for x in r:
#         print(x, end= '\t')
#     print()

# N = int(input())
# M = []
# for row in range(N):
#     row = [1]*(N-1) + [5]
#     print(*row)
#     M += [row]

# N = int(input())
# [print(*[1]*(N-1)+[5])for row in range(N)]

# n = int(input())
# lst = [[1] * n] * n
# lst[0][n-1] = 5
#
# for i in lst:
#     print(*i)

# import sys
# # считывание списка из входного потока
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# lst = [lst_in[i].split() for i in range(len(lst_in))]
# print(*["-".join(lst[j]) for j in range(len(lst))], sep="\n")

# import sys
# # считывание списка из входного потока
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# [print('-'.join(lst_in[i].split())) for i in range(len(lst_in))]

# n = int(input())
# for num in range(2, n):
#     flag = True
#     for div in range(2, num):
#         if num % div == 0:
#             flag = False
#     print(num, end=' ') if flag else 0

# [print(i, end=' ') for i in range(2,int(input())) if all(map(lambda x: i % x != 0,range(2,i)))]


# import sys
# # считывание списка из входного потока
# s = sys.stdin.readlines()
# lst = [list(map(int, x.strip().split())) for x in s]
#
# fl = True
# for i in range(len(lst) - 1):
#     for j in range(len(lst) - 1):
#         if (lst[i][j] + lst[i+1][j] + lst[i][j+1] + lst[i+1][j+1]) > 1:
#             fl = False
#             break
# print(['НЕТ', 'ДА'][fl])

# lst = [[2, 3, 4, 5, 0],
#        [3, 2, 7, 8, 9],
#        [4, 7, 2, 0, 4],
#        [5, 8, 0, 2, 1],
#        [6, 9, 4, 1, 2]]


# s = sys.stdin.readlines()
# lst = [list(map(int, x.strip().split())) for x in s]
#
# ls2 = copy.deepcopy(lst)
# ls2 = [[row[i] for row in ls2] for i in range(len(ls2[0]))]
# print(('НЕТ', 'ДА')[ls2 == lst])

# n = int(input())
# ls_cup = [64, 32, 16, 8, 4, 2, 1]
# for cupur in ls_cup:
#     while n - cupur >= 0:
#         print(cupur, end=' ')
#         n -= cupur

#-------------------------------------------------
# Алгоритм сортировки выбором
#-------------------------------------------------
# a = [-3, 5, 0, -8, 1, 10]
# N = len(a)      # число элементов в списке
#
# for i in range(N-1):
#     m = a[i]            # запоминаем минимальное значение
#     p = i               # запоминаем индекс минимального значения
#     for j in range(i+1, N):  # поиск миимального среди оставшихся элементов
#         if m > a[j]:
#             m = a[j]
#             p = j
#
#     if p != i:          # обмен значениями, если был найден минимальный не в i-й позиции
#         t = a[i]
#         a[i] = a[p]
#         a[p] = t
#
# print(a)

# print(*sorted(list(map(int, input().split()))))

# -------------------------------------------------
# Алгоритм сортировки пузырьком
#-------------------------------------------------
#
# a = list(map(int, input().split()))
# for i in range(0, len(a)-1):
#     for j in range(0, len(a)-1-i):
#         if a[j] > a[j+1]:
#             a[j], a[j+1] = a[j+1], a[j]
# print(*a)

# print([abs(x) for x in list(map(float, input().split()))])

# print([int(i) for i in  input()])

# N = int(input())
# [print(*row) for row in [[1 if i==j else 0 for i in range(N)] for j in range(N)]]

# print(*[l for l in input().split() if len(l) > 5])

# n = int(input())
# print(*[i for i in range(1, n+1) if n % i == 0])

# N = int(input())
# [print(*r) for r in [[i]*N for i in range(N)]]

# [print(i, end=' ') for i in  list(map(float, input().split()))[::2]]

# a = list(map(int, input().split()))
# b = list(map(int, input().split()))
# print(*[a[i] + b[i] for i in range(len(a))])

# print(*[int(i)+int(j) for i, j in zip(input().split(), input().split())])   #Супер

# L = input().split()
# X, Y = L[::2], L[1::2]
# print([[X[i], int(Y[i])] for i in range(len(X))])
# n = input().split()
# print([[*i] for i in list(zip(n[::2], map(int, n[1::2])))])

# [[print(f"{j} * {i} = {i*j}") for i in range(1,10)] for j in range(1,10)]   # Таблица умножения)

# print([y**2 for y in [x for x in range(10) if x % 2 == 0]])

# L = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 8, 7, 6], [5, 4, 3, 2]]
# print(*[x for row in L[::-1] for x in row[::-1]])
# print(*list(reversed([x for row in L for x in row])))
# print(*[x for row in L for x in row][::-1])

# k = list(map(int, input().split()))   # My
# n = int(len(k)**0.5)
# print([[k[x+row*n] for x in range(n)] for row in range(n)])

# k = list(map(int, input().split()))
# n, it = int(len(k) ** 0.5), iter(k)
# print([[next(it) for i in range(n)] for j in range(n)])

# t = ["– Скажи-ка, дядя, ведь не даром",       # My
#     "Я Python выучил с каналом",
#     "Балакирев что раздавал?",
#     "Ведь были ж заданья боевые,",
#     "Да, говорят, еще какие!",
#     "Недаром помнит вся Россия",
#     "Как мы рубили их тогда!"
#     ]
# print([[x for x in row if len(x) > 3] for row in [s.split() for s in t]])

# import sys
# s = sys.stdin.readlines()
# L = [list(map(int, x.strip().split())) for x in s]
# [print(*r) for r in [[row[i] for row in L] for i in range(len(L[0]))]]

# s = open(0).readlines()         # СЧИТЫВАНИЕ БЕЗ ВСЯКИХ SYS
# mtx = [list(map(int, x.strip().split())) for x in s]
# print(*mtx)
# arr = [*zip(*mtx)]
# print(*arr)
# [print(*r) for r in arr]

