# r = open('text2.txt', 'a', encoding='cp1251')
# r.write(" Stroka Текста")
#
# print(r)
#
# r.close()

# h = open('text2.txt', encoding="cp1251")
# print(h.read())
# h.close()

import NewModul
# import time

print(dir(NewModul))
print(help(NewModul))
# print(dir(time))
# print(help(time))

print(NewModul.k)
print(NewModul.newf(7))

print("Конец файла импорта")
