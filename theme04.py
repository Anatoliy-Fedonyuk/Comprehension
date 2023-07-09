# This Python file uses the following encoding: utf-8
h = [7, 4, 5, 3, 6, 1, 3, -2]

newh = []
for x in h:
    if x % 2 ==0:
        newh.append(x * 2)
print(newh)


z = {x * 2 for x in h}
f = {x:x * 2 for x in h}
n = [x * 2 for x in h if x % 2 == 0 and x > 0]

print(z)
print(f)
print(n)

# string = """Lorem {} ipsum dolor sit amet,
# consectetur adipiscing elit, {} do eiusmod tempor
# incididunt ut labore et dolore magna aliqua."""
#
# print(string.format(3 / 4, "send"))
#
# n = int(input("First number: "))
# m = int(input("Second number: "))
# p = int(input("Third number: "))
# print("{} + {} + {} = {}".format(n, m, p, n + m + p))