# This Python file uses the following encoding: utf-8
import os
# Алгоритм из урока про парсинг файлов можно сделать одной строкой))

g = [os.path.join(z, i)  # Генератор списка
     for z, x, c in os.walk("C:\\Users\\HP\\Desktop\\")
     for i in c if '.txt' in i]

print(len(g))
print(g)
print(g.__sizeof__())

# А можно сделать выражение генератор и просчет будет мгновенным и памяти не займет!!!
n = (os.path.join(z, i)  # Выражение генератор
     for z, x, c in os.walk("C:\\Users\\HP\\Desktop\\")
     for i in c if '.txt' in i)

# print(next(3))
print(n)
print(n.__sizeof__())

for a in range(1, len(g)):
     print(next(n))
