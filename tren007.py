# def my_print():
#     print("It's my first function")
# my_print()

# def my_input():
#     name, family = input().split()
#     print(f"Уважаемый, {name} {family}! Вы верно выполнили это задание!")
# my_input()

# (lambda x: print(f"Предмет имеет вес: {x} кг."))(float(input()))

# ls = list(map(int, input().split()))
# print(ls)

# (lambda x: print(f"Min = {min(x)}, max = {max(x)}, sum = {sum(x)}"))(list(map(int, input().split())))

# def perimetr(width, height):
#     print(f"Периметр прямоугольника, равен {(width+height)*2}")
# w, h = input().split()
# perimetr(int(w), int(h))

# t = {'A', 'E', 'I', 'O', 'U', 'Y', 'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T',
#      'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '_', 'a', 'e', 'i', 'o', 'u', 'y',
#      'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z', '@', '.'}
#
# def adres_valid(ls):
#      if ls.count("@") != 1 or ls.count(".") != 1:
#           return "НЕТ"
#      elif (set(ls) & t)!=set(ls):
#           return "НЕТ"
#      elif ls[0].isalpha()!=True or ls[-1].isalpha()!=True:
#           return "НЕТ"
#      else:
#           return "ДА"
#
# lst = input()
# print(adres_valid(lst))

# def get_max2(a, b):
#     return a if a > b else b
#
# print(get_max2(5, 7))       # И чуть магии )
#
# def get_max4(a, b, c, d):
#     return get_max2(get_max2(a, b), get_max2(c, d))
#
# print(get_max4(5, 7, 10, -23))

# def get_kvadr(x):
#     return x ** 2
# print(get_kvadr(float(input())))

# (lambda x: print(x**2))(float(input()))    # 7.2.1

# def is_triangle(a, b, c):
#     return True if a + b > c and b + c > a and a + c > b else False

# def is_large(ls):
#     return len(ls) >= 3

# def even(x): return x % 2 == 0
#
# while (a := int(input())) != 1:
#     if even(a):
#         print(a)

# def not_even(x): return x % 2 != 0    # 7.2.5
#
#
# ls = list(map(int, input().split()))
# print(*[i for i in ls if not_even(i)])

# (lambda x: print(*[i for i in list(map(int, input().split())) if x(i)]))(lambda x: x % 2 != 0)

# tp = input().strip()    # 7.2.6
# if tp == "RECT":
#     def get_sq(a, b): return a * b
# else:
#     def get_sq(x): return x * x

# tp = input().strip()
# def get_sq(a, b=1): return a*b if tp == 'RECT' else a*a   # 7.2.6 интересно return с тернарником

# get_sq = (lambda a: a ** 2, lambda a, b: a * b)[tp == 'RECT']   # 7.2.6 интересно с лямбдой

# def str6(x): return len(x) >= 6    # 7.2.7
#
# ls = input().split()
# print(*[i for i in ls if str6(i)])

# print(*[i for i in input().split() if (lambda s: len(s) > 5)(i)])    # 7.2.7

# def str_gen(st): return st, len(st)    # 7.2.8
#D
# d = {str_gen(i)[0]: str_gen(i)[1] for i in input().split()}
# print(*sorted(d, key=lambda x: d[x]))

# def inkognito(min, max): return min * max    # 7.2.9
#
# ls = list(map(int, input().split()))

# ### АЛГОРИТМ ЕВКЛИДА
# import time
#
# def get_nod(a, b):
#     """Вычисляется НОД для натуральных чисел a и b по быстрому алгоритму Евклида.
#     :param a: первое натуральное число
#     :param b: второе натуральное число
#     :return : НОД """
#     if a < b:
#         a, b = b, a
#
#     while b != 0:
#         a, b = b, a % b
#
#     return a
#
#
# def test_nod(func):
#     # ----- тест №1 ----------------
#     a, b = 28, 35
#     res = func(a, b)
#     help(get_nod)
#     if res == 7:
#         print("#Test1 - Ok")
#     else:
#         print("#Test1 - Fail")
#
#     # ----- тест №2 ----------------
#     a, b = 1, 100
#     res = func(a, b)
#     if res == 1:
#         print("#Test2 - Ok")
#     else:
#         print("#Test2 - Fail")
#
#     # ----- тест №3 ----------------
#     a = 2
#     b = 1_000_000_000
#     st = time.time()
#     res = func(a, b)
#     et = time.time()
#     dt = et - st
#     if res == 2 and dt < 1:
#         print("#Test3 - Ok")
#     else:
#         print("#Test3 - Fail")
#
# test_nod(get_nod)


#-----------------------------------------------------------------
### ДЕКОРАТОРЫ !!!
#-----------------------------------------------------------------
import time

def test_time(func):
    def wraper(*args, **kwargs):
        st = time.time()
        result = func(*args, **kwargs)
        et = time.time()
        dt = et - st
        print(f"time: {dt} sek")
        return result

    return wraper


@test_time
def get_nod_fast(a, b):
    while b > 0: a, b = b, a % b
    return a


@test_time
def get_nod_slow(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


# get_nod_slow = test_time(get_nod_slow)
# get_nod_fast = test_time(get_nod_fast)

res1 = get_nod_slow(56, 100_000_000)
res2 = get_nod_fast(56, 1_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000)
print(res1, res2)

