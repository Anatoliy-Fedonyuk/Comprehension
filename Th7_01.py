# d = open('text.txt')
# # print(d.read(5))
# # print(d.read())
# for line in d:
#     print(line)
#
# d.close()

f = open('text25.txt', 'w')
l = [str(i) + str(i-1) for i in range(20)]
print(l)

for index in l:
    f.write(index + '\n')

f.close()

h = open('text25.txt', 'r')

print(h.read())