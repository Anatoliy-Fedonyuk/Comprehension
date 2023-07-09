# import sys
#
# print(sys.getrecursionlimit())
# sys.setrecursionlimit(2000)
# print(sys.getrecursionlimit())

# def rec_count(index):       # макс.глубина рекурсии
#     print(index)
#     index += 1
#     rec_count(index)
#
# rec_count(1)

def some(num, step):  # Возводит число в степень рекурсивно
    if step == 0:
        return 1
    else:
        return num * some(num, step - 1)


print(some(3, 3))

a = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]
b = [[2, 2, 2, 2], [1, 1, 1, 1], [3, 3, 3, 3]]
c = []

for i, row in enumerate(a):     # Складываем множества
    r = []
    for j, x in enumerate(row):
        r.append(x + b[i][j])

    c.append(r)

print(c)

# M, N = list(map(int, input("Введите M и N: ").split()))
#
# zeros = []
# for i in range(M):
#     zeros.append([0] * N)
#
# print(zeros)
#
# for i in range(M):
#     for j in range(N):
#         zeros[i][j] = 1
#
# print(zeros)
print("=" * 20)

A = [[1, 2, 3, 4, ], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

for r in A:  # Транспонируем матрицу (переворачиваем)
    for x in r:
        print(x, end='\t')
    print()

print("=" * 20)

for i in range(len(A)):
    for j in range(i + 1, len(A)):
        A[i][j], A[j][i] = A[j][i], A[i][j]

for r in A:
    for x in r:
        print(x, end='\t')
    print()

print("=" * 20)

N = 10  # Пишем треугольник Паскаля
P = []

for i in range(N):
    row = [1] * (i + 1)
    for j in range(i + 1):
        if j != 0 and j != i:
            row[j] = P[i - 1][j - 1] + P[i - 1][j]

    P.append(row)

for r in P:
    print(r)

print("=" * 40)
# Примеры работы генераторов списков

cities = ['Киев', 'Запорожье', 'Днепр', 'Херсон', 'Винница']
print([city.upper() for city in cities if len(city) <= 6])

print(['чет' if x % 2 == 0 else 'нечет' for x in [4, 3, -1, 5, 8, -12]])
