r = open('Sumat.exe', 'rb')
y = open('Kopi_sumat.exe', 'wb')

while True:
    var = r.read(1048576)
    print(var.__sizeof__())
    if var.__sizeof__() == 33:
        break

    y.write(var)

print('Контроль')

r.close
y.close
