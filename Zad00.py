def chek(x):
    if len(set(x)) == len(x):
        return True
    return False


def chek_x_unique(y):
    try:
        return chek(y)
    except TypeError as type_error:
        print(type_error, "use only strings, list or sets")


s = {2, 4, 6, 5, 9, 0}
u = chek_x_unique(s)
print(u)
