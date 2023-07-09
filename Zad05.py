d = {'a': 3, 'b': "hello", 'c': 4, 'd': -3}
maxim = d['a']
minim = d['a']

for key, value in d.items():
    if type(value) != int and type(value) != float:
        print([key, value])
        continue
    elif value > maxim:
        maxim = value
    elif value < minim:
        minim = value
print(maxim)
print(minim)
