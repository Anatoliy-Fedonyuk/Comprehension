list_of = [['Adam', 29], ['Jonny', 3*1/12], ['Jess', 45], ['Artur', 11]]

def s(x):  # Variant 1
    return x[1]

r = sorted(list_of, key = s)
print(r)

d = sorted(list_of, key = lambda y: y[1])   # Variant 2 s Lambda
print(d)

a = list(filter(lambda a: a[1] > 18, list_of))

print(a)
