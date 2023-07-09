# Напишите функцию с сигнатурой factorial(n) которая возвращает факториал числа n. Используйте рекурсию.
# def factorial(n):
#     if n == 0:
#         return 1
#     return factorial(n - 1) * n
#
#
# print(factorial(5))

# Программа рекурсивно вычисляет числа Фибоначчи и выводит 10 из них в консоль. Найдите ошибки в коде:
# def fib(n):
#     if n == 1 or n == 2:
#         return 1
#     return fib(n - 1) + fib(n - 2)
#
# for i in range(1, 11):
#     print(fib(i))

# Дан список my_list. Создайте срез этого списка с названием sub_list 1) sub_list содержит 3 и 4 элемент списка
# my_list 2) sub_list содержит элементы my_list начиная с первого, через один 3) sub_list содержит список my_list
# в обратном порядке 4) sub_list содержит последние три элемента my_list в обратном порядке 5) sub_list содержит
# копию списка my_list.
# my_list = [1, 10, 22, 43, 11, -2, 7]
# 1)
# sub_list = my_list[3: 5]
# 2)
# sub_list = my_list[1::2]
# 3)
# my_list.reverse()
# sub_list = my_list
# 4)
# sub_list = my_list[-1:-4:-1]
# 5)
# sub_list = my_list.copy()
# print(sub_list)
# print(my_list)

# Создайте переменную my_str, которая будет содержать текст - "This is simple text" Напишите проверку вхождения
# подстроки “imp” в my_str. Если данная подстрока присутствует, на консоль выдается фраза - "This text is in string"
# my_str = "This is simple text"
#
# if "imp" in my_str:
#     print("This text is in string")

# Задайте список my_list с элементами от 0 до 9. 1) Добавьте 11 элемент равный 100.
# 2) Удалите третий элемент списка. 3) Измените 10й элемент списка на 99.
# my_list = list(range(10))
# print(my_list)
# my_list.append(100)
# del my_list[3]
# my_list[9] = 99
# print(my_list)

# Дан список my_list, необходимо вывести на консоль все элементы этого списка по очереди, предварительно умножив
# их на 2. Задачу решить с помощью цикла for. Использовать переменную счётчик i.
# my_list = [3, 1, 1, 6, 12, 0, 44, -23]
# for i in my_list:
#     print(i*2)

# Программа вычисляет 10 чисел Фибоначчи с использованием списка. Найдите и исправьте ошибку.
# n = 10
# fibs = [1, 1]
# print(fibs)
#
# for i in range(n - 2):
#     fibs.append(fibs[i] + fibs[i + 1])
#
# print(fibs)


# check for palindrom
# list1 = list("шабаш")
#
# list2 = list1[-1::-1]
# #list2.reverse()
#
#
# print("This word is a palindrome") if list1 == list2 else print("This word is not a palindrome")
#
# print(list1)
# print(list2)

d = {"a": 10, "b": 5, "c": 7}
s = []

for x in d:
    s += x

print(s)









