# str_my = 'Let\'s write \na string as "s"'
# print('C:\\Users\\Admin\\PycharmProjects\\Student02')
#
# print(str_my)
# print(r'C:\Users\Admin\PycharmProjects\nStudent02')

def some():
    with open('text2.txt') as r:
        for x in r:
            yield x


p = some()
for i in p:
    print(i)
