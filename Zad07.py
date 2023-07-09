def fac(n):
    if n == 0:
        return 1
    return fac(n -1) * n

print(fac(5))


price = {'meat': 3, 'bread': 1.5, 'water': 0.5}
price['potato'] = 1
print(price)

def buy():
    pay = 0
    while True:
        enter = input("Что покупаем??? \n")
        if enter == "end":
            break
        pay += price[enter]
    return pay

# print("Сумма ваших покупок: ", buy())

new = {}
for key, value in price.items():
    new[value] = key

print(new)