import courses

# import pprint
# import sys
# import flask
# import MyModule
# pprint.pprint(dir())

print(courses.Python.get_python())
courses.PHP.get_PHP()
courses.PHP.get_MySQL()
courses.JAVA.get_Java()
print()
print(dir(courses))
print()
print(courses.python_doc.doc)
print(courses.java_doc.doc)





# print(MyModule.NAME)
# a = MyModule.floor(-5.6)
# b = MyModule.math.ceil(-5.6)
# print(a, b)
# pprint.pprint(dir(MyModule))
# pprint.pprint(sys.path)

print("=" * 30)
n, m = map(int, input().split())
# print((n + m) // 20 + 1 * bool((n + m) % 20))   # красиво
print(abs(-(n + m)//20))
