# This Python file uses the following encoding: utf-8
def decor(f):
    def wrapper():
        try:
            h = f()
        except Exception:
            print("Повторите ввод числа...")
            h = f()
        return h

    return wrapper()


@decor
def make():
    enter = float(input('Введите число: '))
    return enter


@decor
def make2():
    ent = int(input('Введите число снова: '))
    return ent


make2()
make()
