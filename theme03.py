q = open('text.txt')
# print(q.read())

r1 = q.read()
list_znk = ['(', ')', '"', '\n', ',', '.']
for i in list_znk:
    r1 = r1.replace(i, '')
print(r1)

r2 = r1.split()
print(r2)

new_text = ' # '.join(r2)
print(new_text)
