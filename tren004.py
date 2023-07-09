# import math
# import json
# import pickle


# a = 7
# b = -4
# c = 3
# print(a, b, c, sep='\n')

# s1 = "Hello"
# s2 = "Balakirev"
# print(s1, end=' ')
# print(s2)

# s1, s2 = map(str.strip, input("Введите слова s1 и s2 : ").split())
# print(f"Word 1: {s1} | Word 2: {s2}")

# x, y = map(int, input("Введите два целых положительных числа X и Y: ").split())
# print("X в степени Y будет: ", x ** y)

# d, f = map(float, input().split())
# print(d + f)

# X, Y = map(int, input().split())
# print(X*3 + Y*5)

# p = float(input())
# r = float(input())
# print(2 * (p + r))

# m = math.pi
# print(round(m, 3))

# p = float(input())
# print(f"Вы ввели число {p}")

# a = float(input('введите число: '))
# print(int(a) % 3 == 0)
# print(not int(float(input())) % 3)

# i = round(float(input()), 2)
# print(100 * (i - int(i)) > 50)

# print(int(input().split('.')[1]) > 50)

# a, b = map(int, input().split())
# print(a % b == 0)

# a, b, c = map(int, input().split())
# print((a + b) > c and (b + c) > a and (c + a) > b)

# y = float(input())
# print(0 <= y <= 2 or 10 <= y <= 20)

# filename = 'Text.txt'
# text_file = open(filename, 'r')
# txt = text_file.read()
# text_file.close()
# print(txt)
# filename = 'Text.txt'
# with open(filename, 'r') as text_file:
#     text = text_file.read()
# print(text)
#
# filename2 = 'Text3.txt'
# with open(filename2, 'w') as text_file:
#     text = "Hello World! \n I`m here"
#     text_file.write(text)

# filename = 'my_file.json'
# with open(filename, 'r', encoding='utf-8') as file:
#     data = json.load(file)
# print(data)

# data = [{'name': 'Jonh', 'age': 25}, {"name": 'Alex', "age": 45}]
# print(data)
# with open('my_file.json', 'w', encoding='utf-8') as file:
#     json.dump(data, file)

# file = open("Text1.txt", encoding='utf-8')
# fil1 = open("Text.txt", encoding='utf-8')
# print(file.read(4))
# # file.seek(0)
# print(file.read(4))
# # file.seek(0)
# print(file.read(4))
# pos = file.tell()
# print(pos)
# print(file.read())
# print(fil1.read())
# print("="*40)
# print(file.readline())
# print(fil1.readline())
# print("="*40)
# print(file.readline())
# print(fil1.readline())
# print("="*40)
# print(file.readline())
# print(fil1.readline())
# for l in file:
#     print(l, end='')
# for i in fil1:
#     print(i, end='')
# print(file.readlines())
# print(fil1.readlines())

try:
    with open("Text1.txt", encoding='utf-8') as file:
# fil1 = open("Text1.txt", encoding='utf-8')
        s = file.readlines()
        # int(s)
        print(s)
except FileNotFoundError:
    print('Невозможно открыть файл')
except Exception:
    print('Ошибки при работе с файлами')
finally:
    print(file.closed)

try:
    with open("save.txt", 'a+') as file:
        file.seek(0)
        file.writelines(["Hallo 4\n", "Hallo 5\n"])
        s = file.readlines()
        print(s)
        # file.write("Hallo 2\n")
        # file.write("Hallo 3\n")
except FileNotFoundError:
    print('Невозможно открыть файл')
except Exception:
    print('Ошибки при работе с файлами')

# book1 = ["Муму", "Тургенев", 250]
# book2 = ["Мертвые души", "Гоголь", 190]
# book3 = ["Нос", "Гоголь", 215]

# try:            # Запись в бинарный файл
#     with open("save.bin", 'wb') as file:
#         pickle.dump(book1, file)
#         pickle.dump(book2, file)
#         pickle.dump(book3, file)
# except FileNotFoundError:
#     print('Невозможно открыть файл')
# except Exception:
#     print('Ошибки при работе с файлами')

# try:            # Чтение из бинарного файла
#     with open("save.bin", 'rb') as file:
#         b1 = pickle.load(file)
#         b2 = pickle.load(file)
#         b3 = pickle.load(file)
# except FileNotFoundError:
#     print('Невозможно открыть файл')
# except Exception:
#     print('Ошибки при работе с файлами')
#
# print([b1, b2, b3])

