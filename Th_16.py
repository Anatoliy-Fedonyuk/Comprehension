# This Python file uses the following encoding: utf-8
# Записываем тот же алгоритм чтения текста с использованием функции-генератора!

# def some():
#     list_text = []
#     with open('Dzen.txt') as r:
#         for x in r:
#             list_text.append(x)
#     return list_text


def resome():
    with open('Dzen.txt') as r:
        for x in r:
            yield x


# p = some()
# for i in p:
#     print(i)

for i in resome():
    print(i.split())

print('y = 0')
