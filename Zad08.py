# def find_max(arr, max_=None):
#     if max_ is None:
#         max_ = arr.pop()
#     current = arr.pop()
#     if current > max_:
#         max_ = current
#     if arr:
#         return find_max(arr, max_)
#     return max_
#
#
# list1 = [1, 2, 3, 4, 2, -23, 76, 348, 31 * 89, -5555]
# result = find_max(list1)
# print(result)  # -> 4

# for i in range(1, 4):  # Работа вложенных циклов
#     for j in range(3):
#         print(f"i = {i}, j = {j}", end=" ")
#     print()

# Factorial easy
# n = int(input("Введите натуральное число не более 100: "))
# if n < 1 or n > 100:
#     print("Неверное введено число, попробуйте еще!")
# else:
#     p = 1
#     for u in range(1, n + 1):
#         p *= u
#
#     print(f"Factorial {n}! = {p}")

# for o in range(10):
#     print("*" * o)

frase = "Python give me the strength to take courses and become a genius programmer."
print(frase)
words = frase.split(' ')
print(words)

s = ''
for w in words:
    w = "God" if w == 'Python' else w
    s += " " + w

print(s.lstrip())
print(type(s))

r = " ".join(words)  # Делает тоже самое одним методом))
print(r, type(r))

a = 9
print("a - " + ("четное" if a % 2 == 0 else "нечетное") + " число")

t = ['a', 'b', 'v', 'g', 'd', 'e', 'zh', 'z', 'i', 'y', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't',
     'u', 'f', 'h', 'c', 'ch', 'sh', 'shch', '', 'y', '', 'e', 'yu', 'ya']

start_index = ord('а')
title = "Программирование на 'Python' - лучший курс!"
slug = ''

for s in title.lower():
    if 'а' <= s <= 'я':
        slug += t[ord(s)-start_index]
    elif s == 'ё':
        slug += 'yo'
    elif s in " _?!,.*;:'":
        slug += '-'
    else:
        slug += s


while slug.count('--'):
    slug = slug.replace('--', '-')

print("=" * 30)
print(slug)


