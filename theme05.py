import math

PI = math.pi

def radius():
    n = float(input("Диаметр цилтндра в см: "))
    n /= 2
    return n


def height():
    m = float(input("Высота цилндра в см: "))
    return m


def volume():
    r = radius()
    h = height()
    s = PI * r ** 2
    vol = s * h
    return vol

print("Объем цилиндра", volume(), "см3")


def massa(g):
    n = float(input("Удельны вес г/см3 : "))
    return g * n / 1000


print("Вес цилиндра в кг: ", massa(volume()))
