def spisok(my_list, index):
    return my_list[index]


def prover(x, y):
    try:
        return spisok(x, y)
    except IndexError as index_error:
        s = len(list_my)
        print(index_error, " Введите индекс в пределах размера спсиска", s)
        return -1


list_my = [2, 5, 44, -999, 384728, 'ada', 88, True, 945.99, {2, 3, 5, 6, 8, 9}]
index_my = 16
print(prover(list_my, index_my))
