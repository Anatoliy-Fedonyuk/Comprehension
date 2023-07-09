d = {1: 5, 2: 4, 3: 3, 4: 2, 5: 1}
for key, value in d.items():
    if key % 2 == 0:
        print(key, value)

s = {'alice': 25, 'mark': 33, 'artur': 11, 'john': 48, 'april': 68}
new_s = {}
for name, age in s.items():
    if name[0] != 'a':
        new_s[name] = age
print(s)
print(new_s)
s = new_s
print(s)

f = {}