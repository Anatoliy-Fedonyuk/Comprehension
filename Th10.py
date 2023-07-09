def div(delimoe, delitel):
    return delimoe // delitel
    # return result


def prover(x, y):
    try:
        return div(x, y)
    except ZeroDivisionError as zero_error:
        print(zero_error, " нельзя делить на 0")
        return 0
    except NameError as name_error:
        print(name_error, " ошибка имени переменной")
    except TypeError as type_error:
        print(type_error, " используйте только целыe или дробные числа")


delimoe_01 = 55
delitel_01 = 0

print(prover(delimoe_01, delitel_01))

