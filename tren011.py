'''Инди-курс по Python'''


# print(a:='Я стану крутым программистом!', a, a, sep='\n')
# print('W'*777)
# print('Лев Николаевич Толстой написал "Война и мир"')
# print(input(), input(), sep='\n')

# s = [input() for _ in '___'][::-1]

# [print(x) for x in [input() for _ in '___'][::-1]]

# print(f"{(a:=input())} {a} {a} {a}")

# print(len(input()))
# print("{1}{0}".format(input(), input()))
# print(input()*3)

# a,b,c = input().split()

# [print(f"Simvol code {x} is {ord(x)}.") for x in input().split()]

# s = input()
# print((s:=input())[-1] + s[:-1])

# print(input().lower())

# print(input().upper()==input().upper())

# print(''.join([(s:=input())[:3].upper(), s[3:-3].lower(), s[-3:].upper()]))

# print(input().title().swapcase())

# print(input().lower().count('e'))

# print(input().rfind('a'))
# print(input().replace(' ',','))
# print(input().replace('w','').replace('z',''))

# print(''.join([s for s in input().lower() if s not in "aoyeui"]).replace('','.')[:-1])

# print(len(input().split()))

# print('-'.join(['Follow', 'the', 'Cops', 'Back', 'Home']))
# print(input().lower().startswith("mam"))

# print(input().endswith(input()))
# print((s:=input()).startswith(input()) and s.endswith(input()))

# print(input().isdigit())
# print(input().isupper())
# print(input().islower())

# print(input().ljust(15, "-"))
# print(input().rjust(10, "!"))
# print(input().center(15, "_"))
# print(input().zfill(10))

# print(input().strip('-_!?'))
# print(input().rstrip('-_!?'))

# def get_RGB(r: str, g: str, b: str) -> str:
# ls = [hex(int(input()))[2:].zfill(2) for _ in '0o0']
# print(F"#{''.join(ls).upper()}")

# print("/\_/\ \n>^,^< \n / \ \n(|_|)_/")
# print(r'''
#   /~~~\
#  //^ ^\\
# (/(_*_)\)
# _/''*''\_
# (/_)^(_\)
# ''')

# a = 255
# print(F'#{a:05X}')

# print("Что Вы сказали? {}? Какое интересное слово".format(input()))

# print("Здравствуйте, {1} {0}!".format(input(), input()))

# print('Для числа {} предыдущим будет число {}.'.format((x:=input()), (int(x)-1)))
# print('Для числа {} следующим будет число {}.'.format(x, (int(x)+1)))

# print(f"Мое имя {input()}!")
# print(f"Hello {input().upper()}. You are {input()} years old.")
# print(f"{input()}, вам исполнится 77 лет в {int(input())+77}")
# print("{} сек - это {} мин. {} сек.".format((s:=input()), int(s)//60, int(s)%60))

# w, h = map(int, input().split())
# print(f"Разрешение экрана: {w} x {h}.\nОбщее количество пикселей = {w*h}.")

# print(f"{(d:=int(input()))} / {(f:=int(input()))} = {d/f}\n{d} // {f} = {d//f}\n{d} % {f} = {d%f}")

# x, y, z = (int(input()) for _ in "xyz")
# print(f"Vector A({x}, {y}, {z})\nVector B({x+5}, {y+5}, {z+5})")

# print(f"""Current dollar rate is {(r:=input())}. You want to buy {(d:=input())} dollars
# You must pay {int(d)*float(r)}""")

# x, y = int(input()), int(input())
# print(f"Точка({x = }, {y = })")
# print(f"{(float(input())):.2f}")

# print(f'Число\tКвадрат\t  Куб')
# for x in range(1, 11):
#    print(f'{x:03}\t\t{x*x:03}\t\t{x*x*x:04}')
# print(f"{(int(input())):010}")

### НАСТОЯЩИЙ ЧЕК!!!!!
# APPLES = .50
# BREAD = 1.50
# CHEESE = 2.25
# num_apples = 3
# num_bread = 10
# num_cheese = 6
# price_apples = num_apples * APPLES
# price_bread = num_bread * BREAD
# price_cheese = num_cheese * CHEESE
# str_apples = 'Яблоки'
# str_bread = 'Хлеб'
# str_cheese = 'Сыр'
# total = price_bread + price_cheese + price_apples
# print(f'{"Список покупок":^30s}')
# print(f'{"=" * 30}')
# print(f'{str_apples:10s}{num_apples:10d}\t${price_apples:>5.2f}')
# print(f'{str_bread:10s}{num_bread:10d}\t${price_bread:>5.2f}')
# print(f'{str_cheese:10s}{num_cheese:10d}\t${price_cheese:>5.2f}')
# print(f'{"Total:":>20s}\t${total:>5.2f}')

# print(f"|{int(input()):-^15}|")

# text = input()
# print(f"|{text:&^20s}|")
# print(f"|{text:&>20s}|")
# print(f"|{text:&<20s}|")

# print(my_list:=[1]*77)
# print(my_list:=['q', 'w', 't']*15)
# print('777' in input().split())
# print(sum([*map(int, input().split())]))
# print(min(l:=[*map(int, input().split())]), max(l))
# print(sum(l:=[*map(int, input().split())])/len(l))
# print([*map(int, input().split())][::-1])

# top = ['Игра престолов', 'Шерлок', 'Друзья', 'Во все тяжкие', 'Доктор Хаус', 'Теория большого взрыва', 'Бригада']
# match top:
#     case t if 'Бригада' in t: top[t.index('Бригада')] = "Сверхъестественное"
# match top:
#     case t if 'Друзья' in t: top[t.index('Друзья')] = "Настоящий детектив"
# print(top)

# months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
# match int(input()):
#     case m if 0 < m < 13: print(months[m-1])
#     case _: print("Incorrect input")

# numbers = [-214, 181, -139, 448, -20, -917, 32, 422, -895, 198, 284, 472, -986, -964, -989, 29]
# [numbers.append(e) for e in [111, 222, 789, 201]]
# print(numbers)

# num = [-214, 181, -139, 448, -20, -917, 32, 422, -895, 198, 284, 472, -986, -964, -989, 29]
# [num.insert(i, v) for i, v in {5: 111, 8: 222, 0: 789, 11: 201}.items()]; print(num)

# num = [-214, 181, -139, 448, -20, -917, 32, 422, -895, 198, 284, 472, -986, -964, -989, 29]
# # num.extend([43, 54, 23, 87, -4, -832, 90, 32, 543, 432, 4, 76, 8, 0, 21, 90, 32]); print(num)
# s = 0
# for i in [-1, 0, 12, 7]:
#     s += num.pop(i)
# print(num, s, sep="\n")

# num = [-214, 777, 181, 9, 32, -139, 43, 89, 77, 448, -20, -917, 54, 5, 432, 43, 32, 422, -895, 7, 198, 284, 472, 3, -986, -964, -989, 29]
# [num.remove(i) for i in (3,5,7,9)]; print(num)

# numbers = [-214, 181, -139, 448, -20, -917, 32, 422, -895, 198, 284, 472, -986, -964, -989, 29]
# numbers.sort(reverse=True); print(numbers)

# a = [*map(int, input().split())]
# print(list(reversed([*map(int, input().split())])))

# l = [*map(int, input().split())]
# print([*map(int, input().split())].count(999))

# numbers = [-214, 181, -139, 448, -20, -917, 32, 422, -895, 198, 284, 472, -986, -964, -989, 29]
# copy_numbers = numbers[:]; print(copy_numbers)

# print(*map("-".join, input().upper().split()))
# re = input().upper()
# print('-'.join(re).replace('- -',' '))

# fio = input().split()
# print(f"{fio[2]} {fio[0][0]}.{fio[1][0]}.")
# print('{2} {0[0]}.{1[0]}.'.format(*input().split()))

# s = "\n".join(input().split())
# print("\n".join(input().split()))

# a = input().split()
# print('''
# '''.join(a))

### MODULE RE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# import re

# text = "lat = 5, lon=7, a=5"
# print(re.findall(r"(lat|lon)\s*=\s*(\d+)", text))

# text = "Картинка <img src='bg.jpg'> в тексте</p>"
# print(re.findall(r"<img\s+[^>]*src=([\"'])(.+?)\1", text))
# print(re.findall(r"<img\s+[^>]*src=(?P<quote>[\"'])(.+?)(?P=quote)", text))
# print(re.findall(r"<img\s+[^>]*(src=(?P<quote>[\"']).+?)(?P=quote)", text))

# with open("map.xml", "r") as f:
#     lat = []
#     lon = []
#     for text in f:
#         match = re.search(r"<point\s+[^>]*?lon=([\"\'])(?P<lon>[0-9.,]+)\1\s+[^>]*lat=([\"\'])(?P<lat>[0-9.,]+)\1",
#                           text)
#         if match:
#             v = match.groupdict()
#             print(v)
#             if "lon" in v and "lat" in v:
#                 lon.append(v["lon"])
#                 lat.append(v["lat"])
#
#     print(lon, lat, sep="\n")

# text = """<!DOCTYPE html>
# <html>
# <head>
# <meta http-equiv="Content-Type " content="text/html; charset=windows-1251">
# <meta name="viewport" content="width=device-width, initial-scale=1.0">
# <title>Уроки по Python</title>
# </head>
# <body>
# <p align=center>Hello World!</p>
# </body>
# </html>"""
#
# # print(re.findall(r"([-\w]+)[ \t]*=[ \t]*[\"']([^\"']+)(?<![ \t])", text, re.MULTILINE))     #тут корректней так как съедает пробел перед кавычками
# # print(re.findall(r"([-\w]+)[ \t]*=[ \t]*[\"'](.+?)[\"'](?<![ \t])", text, re.MULTILINE))
#
# match = re.findall(r"""([-\w]+)             #выделяем атрибут
#                    [ \t]*=[ \t]*            #далее, должно идти равно и кавычки
#                    (?P<q>[\"'])?            #проверяем наличие кавычки
#                    (?(q)([^\"']+(?<![ \t]))|([^ \t>]+))     #выделяем значение r в зависимости от того были ли кавычки
#                    """,
#                    text, re.MULTILINE|re.VERBOSE)
# print(match)

# text = "Python, python, PYTHON"
# match = re.findall(r"(?im)python", text)
# print(match)

# s = input()
# print(d if (d:=int(input()))<20000 else d*0.87)

# a, b = int(input()), int(input())
# print((a, b)[b > a])

# a, b, c = map(int, input().split())
# print(('YNEOS')[(a+b!=c)::2])

# a = input().split()
# print([int(i) for i in input().split() if i not in '3579'])

# match (s:=int(input())):
#     case s if s < 10001: print(f'Сумма {s} не превышает лимит, проходите')
#     case _: print(f'Ого! {s}! Куда вам столько? Мы заберем {s-10000}')

# match (st:=input()):
#     case s if 'walrus' in s: print('Нашли моржа')
#     case _: print('Никаких моржей тут нет')

# print(('YNEOS')[((s:=input())[::-1]!=(t:=input()))::2])

# print(('YNEOS')[((N:=input())[::-1]!=N)::2])

# match [int(input()) for i in '0_0']:
#     case a, b, c if (a+b)>c and (b+c)>a and (a+c)>b: print('YES')
#     case _: print('NO')

# N = list(map(int, input()))                       #3.1.14 my
# [N.insert(0,0) for x in (6-len(N))*'_']
# print(('YNEOS')[sum(N[:3])!=sum(N[3:])::2])

# n = [int(i) for i in input()]
# print(('NO', 'YES')[sum(n[:-3])==sum(n[-3:])])

# # n = [*map(int, input().zfill(6))]
# # print(n)
# print(('YNEOS')[sum((n:=[*map(int, input().zfill(6))])[:3])!=sum(n[3:])::2])                      #3.1.14 my

# l, a, b = '_abcdefgh', input(), input()
# a_col = 'black' if not (int(a[1])+l.index(a[0])) % 2 else 'white'
# b_col = 'black' if not (int(b[1])+l.index(b[0])) % 2 else 'white'
# print(("YES","NO")[a_col != b_col])

# l, a, b = '_abcdefgh', input(), input()                                 #3.1.15 my
# print(("YES","NO")[(int(a[1])+l.index(a[0])+int(b[1])+l.index(b[0]))%2])

# print("Even" if not int(input())%2 else "Odd")

# n = sorted([int(input()) for _ in "!!"])
# minimum, maximum = sorted([int(input()) for _ in "!!"]); print(minimum, maximum)

# s = input().endswith('?')
# print(sentence := 'Вопросительное' if input().endswith('?') else 'Обычное')

# print(experiment:='Отталкиваются' if input() in input() else 'Притягиваются')

# match l:=[int(input()) for _ in "AB"]:
#     case l if (a:=l[0])<(b:=l[1]): print('<')
#     case l if a > b: print('>')
#     case _: print('=')

# match [int(input()) for _ in "123"]:
#     case l if l[2] < l[0] > l[1]: print(l[0])
#     case l if l[1] > l[2]: print(l[1])
#     case _: print(l[2])

# match int(input()):
#     case n if n == 1: print(0)
#     case n if n % 2: print(n)
#     case _: print(n//2)

# match l:=[int(input()) for _ in "AB"]:
#     case l if (a:=l[0])<(b:=l[1]): print('<')
#     case l if a > b: print('>')
#     case _: print('

# match tuple(map(int, input().split())):
#     case a,b,c if a>b>c : print(a-c)
#     case a,b,c if a>c>b : print(a-b)
#     case a,b,c if b>a>c : print(b-c)
#     case a,b,c if b>c>a : print(b-a)
#     case a,b,c if c>a>b : print(c-b)
#     case a,b,c: print(c-a)

# a, b = input().lower(), input().lower()
# print('-1'*(a<b) + '1'*(a>b) + '0'*(a==b))


# match tuple(map(int, input().split())):                      #3.3.7 my
#     case s,v1,v2,t1,t2 if (s*v1+2*t1)<(s*v2+2*t2) : print("First")
#     case s,v1,v2,t1,t2 if (s*v1+2*t1)>(s*v2+2*t2) : print("Second")
#     case _: print("Friendship")

# a, b = input().strip("ь"), input().lower()
# print(('Bad','Good')[input().lower().strip("ь")[-1]==input().lower()[0]])

# def summa_n(t: int) -> None:
#     S = sum([x for x in range(1, t+1)])
#     print(f"Я знаю, что сумма чисел от 1 до {t} равна {S}")
# summa_n(5)

# def exponentiation(n: int) -> None: print(n**2, n**3)

# def sum_num(s): print(sum(map(lambda x: int(x) if x.isdigit() else 0, list(s))))
# print(sum(map(lambda x: int(x) if x.isdigit() else 0, list(input()))))
# def sum_num(s): print(sum(map(int, filter(str.isdigit, s))))
# sum_num("123QwertY321")

# def get_body_mass_index(m, h):              # 7.1.12 Индекс массы тела!!!!!
#     match m/(h/100)**2:
#         case ind if ind < 18.5: print("Недостаточная масса тела")
#         case ind if ind > 25: print("Избыточная масса тела")
#         case _: print("Норма")
#
# get_body_mass_index(60, 174)
# get_body_mass_index(50, 170)
# get_body_mass_index(110, 170)

# def check_password(password):
#     match password:
#         case s if len(s) < 10: print("Easy peasy")
#         case s if len([*filter(str.isdigit,s)]) < 3: print("Easy peasy")
#         case s if not any(map(str.isupper,s)): print("Easy peasy")
#         case s if not any(map(lambda y: y in "!@#$%*",s)): print("Easy peasy")
#         case _: print("Perfect password")
#
# check_password('Qwerty1357!')
# check_password('Qwerty57!')

# def count_letters(st):
#     N, K = len([*filter(str.isupper,st)]), len([*filter(str.islower,st)])
#     print(f"Количество заглавных символов: {N}\nКоличество строчных символов: {K}")
#
# count_letters("Привет, Старина")
# count_letters("QWERTY")

# def repeat_please_n_times(n): [print("Just do it") for _ in range(n)]
# repeat_please_n_times(7)

# def is_between(name, surname, middlename):
#     print(("False","True")[middlename>=name>=surname or surname>=name>=middlename])
# a, b, c = map(int, input().split())
# is_between(a, b, c)

# def count_letter(text , letter): return text.count(letter)
# text, symbol = input(), input()
# print(count_letter(text, symbol))

# def print_initials(name, surname, middlename): return f"{surname} {name[0]}.{middlename[0]}."
#
# print(print_initials(input().capitalize(), input().capitalize(), input().capitalize()))

# assert 200 > 100
# assert [100] * 4 < [100, 100, 100, 10000]
# assert sum([1, 3, 5]) == sum((6, 3))
# assert min(3, -1, 9) == -1
# print('Проверки пройдены')

# def is_person_teenager(n): return (11 < n < 18)
# print(is_person_teenager(14))

# def factorial(n): return n*factorial(n-1) if n > 0 else 1
# print(factorial(int(input())))

# def generate_fizz_buzz_list(n): return [('Fizz'*(not i%3) + 'Buzz'*(not i%5) or i) for i in range(1,n+1)]
# # print('Fizz'*(not n%3) + 'Buzz'*(not n%5) or n)
# print(generate_fizz_buzz_list(15))

# from functools import reduce          # 7.3.9 variation
# def gcd(a, b):
#     while b > 0:
#         a, b = b, a%b
#     return a
# lst = [int(input()) for i in range(int(input()))]
# y = lst[0]
# for x in range(1, len(lst)):
#     nod = gcd(y,lst[x-1])
#     y = nod
# print(nod)
# nums = [int(input()) for _  in range(int(input()))]
# print(reduce(gcd, nums))
# l = [int(input()) for i in range(int(input()))]
# print(min([gcd(l[i],l[i-1]) for i in range(len(l))]))

# def find_duplicate(lst):
#     ans = []
#     [ans.append(i) for i in lst if lst.count(i) > 1 and i not in ans]
#     return ans
# def find_duplicate(lst):
#     return [i for i in dict.fromkeys(lst) if lst.count(i) > 1]
#
# print(find_duplicate([1, 2, 3, 4]))
#
# assert find_duplicate([1, 1, 1, 1, 1, 2, 2, 2, 2]) == [1, 2]
# assert find_duplicate([2, 1, 1, 1, 1, 1, 2, 2, 2, 2]) == [2, 1]
# assert find_duplicate([1, 2, 3, 4]) == []
# assert find_duplicate([8, 7, 6, 5, 4, 3, 4, 5, 6, 7, 8]) == [8, 7, 6, 5, 4]
# print('Все успешно')

# s = "python"
# def first_unique_char(s):
#     for i in s:
#         if s.count(i)==1:
#             return s.find(i)
#     return -1
#
# print(first_unique_char('aasssddddddddq'))

# def first_unique_char(s):
#     l = [s.find(i) for i in s if s.count(i)==1]
#     return l[0] if l else -1
#
# print(first_unique_char('python'))

# def format_name_list(dy: list):                          # 7.3.12 variation
#     return ' и '.join(i['name'] for i in dy).replace(' и', ',', len(dy) - 2)
# match [names[d]["name"] for d in range(len(names))]:
#     case ls if len(ls)==1: return ls[0]
#     case ls if len(ls)==2: return ls[-2] + " и " + ls[-1]
#     case ls if len(ls)>2: return ", ".join(ls[:-1]) + " и " + ls[-1]
#     case _: return ""


# print(format_name_list([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}]))
# print(format_name_list([]))
# print(format_name_list([{'name': 'Bart'}]))
# print(format_name_list([{'name': 'Lisa'}, {'name': 'Maggie'}]))
# assert format_name_list([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}, {'name': 'Homer'}, {'name': 'Marge'}]) == 'Bart, Lisa, Maggie, Homer и Marge'
# assert format_name_list([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}]) == 'Bart, Lisa и Maggie'

# import re                                                     # 7.3.
# def get_domain_name(url): return re.findall(r"(?a)(?:://www.|www.|://)([\w\-]+)",url)[0]
# def get_domain_name(url):
#     return url.replace("http://","").replace("https://","").replace("www.","").split(".")[0]
# get_domain_name = lambda u: u.replace("http://","").replace("https://","").replace("www.","",1).split(".")[0]

# код ниже не стоит удалять, он нужен для проверки
# assert get_domain_name("http://google.com") == "google"
# assert get_domain_name("http://google.co.jp") == "google"
# assert get_domain_name("www.xakep.ru") == "xakep"
# assert get_domain_name("https://youtube.com") == "youtube"
#
# assert get_domain_name("http://github.com/carbonfive/raygun") =='github'
# assert get_domain_name("http://www.zombie-bites.com") == 'zombie-bites'
# assert get_domain_name("https://www.siemens.com") == 'siemens'
# assert get_domain_name("https://www.whatsapp.com") == 'whatsapp'
# assert get_domain_name("https://www.mywww.com") == 'mywww'
# print('Проверки пройдены')
# print(get_domain_name("https://www.mywww.com"))


# def factorial(n): return n*factorial(n-1) if n > 0 else 1                          # 7.3.14 variation
#
# def trailing_zeros(n, c=0):
#     fac = [*map(int, str(factorial(n)))]
#     while fac.pop()==0: c +=1
#     return c
#
# # код ниже не стоит удалять, он нужен для проверки
# assert trailing_zeros(0) == 0
# assert trailing_zeros(6) == 1
# assert trailing_zeros(30) == 7
# assert trailing_zeros(12) == 2
# print('Проверки пройдены')
# print(trailing_zeros(12))

# def count_AGTC(dna): return tuple([dna.count(e)for e in "AGTC"])
# count_AGTC = lambda dna: tuple(dna.count(_) for _ in "AGTC")
# код ниже не стоит удалять, он нужен для проверки
# assert count_AGTC('AGGTC') == (1, 2, 1, 1)
# assert count_AGTC('AAAATTT') == (4, 0, 3, 0)
# assert count_AGTC('AGTTTTT') == (1, 1, 5, 0)
# assert count_AGTC('CCT') == (0, 0, 1, 2)
# print('Проверки пройдены')
# print(count_AGTC('AGTTTTT'))
#
# help(next)
# print(next.__doc__)

# def add_binary(a: int|str, b: int|str) -> int|str:
#     """Возвращает сумму чисел a и b в двоичном виде"""
#     return a + b
#
# first: int = 100
# second: int = 200
# # first = "hello"
# # second = "add"
#
# add_binary(first, second)
# print(add_binary.__annotations__)
#
# def list_upper(lst: list[str]) -> str:
#     for elem in lst:
#         return elem.upper()
#
# d: dict[str: int] = {'a': 777, 'b': 125, 'c': 525}

# def first_repeated_word(st: str) -> str|None:
#     "Находит первый дубль в строке"
#     ls, ls2 = st.split(), []
#     for w in ls:
#         if w not in ls2:
#             ls2.append(w)
#         else:
#             return w
#
# assert first_repeated_word("ab ca bc ab") == "ab"
# assert first_repeated_word("ab ca bc Ab cA aB bc") == "bc"
# assert first_repeated_word("ab ca bc ca ab bc") == "ca"
# assert first_repeated_word("ab ca bc") == None
# print('Проверки пройдены')
# print(first_repeated_word("ab ca bc ab"))

# def shift_letter(letter: str, shift: int) -> str:
#     "Функция сдвигает символ letter на shift позиций"
#     return chr((ord(letter)-ord('a')+shift)%26 + ord('a'))
#
# def caesar_cipher(st: str, shift: int) -> str:
#     "Шифр цезаря"
#     return "".join(shift_letter(i, shift) if i.isalpha() else i for i in st)
#
# assert caesar_cipher('leave out all the rest', -1) == 'kdzud nts zkk sgd qdrs'
# assert caesar_cipher('one more light', 3) == 'rqh pruh oljkw'
# assert caesar_cipher("lost in the echo", 27) == "mptu jo uif fdip"
# assert caesar_cipher("from the inside", 10) == "pbyw dro sxcsno"
# assert caesar_cipher("leave out all the rest", -4) == "hawra kqp whh pda naop"
# print("All is OK")
# print(caesar_cipher('leave out all the rest', -1))

# MIN_DRIVING_AGE = 18
# def allowed_driving(name: str, age: int) -> None:
#     print(f"{name} может водить" if age>=MIN_DRIVING_AGE else f"{name} еще рано садиться за руль")

# def get_word_indices(strings: list[str]) -> dict:
#     d = {}
#     for i in range(len(strings)):
#         for j in strings[i].lower().split():
#             if j not in d:
#                 d[j] = [i]
#             else:
#                 d[j].append(i)
#     return d

# def get_word_indices(strings: list[str]) -> dict:                     # 7.5.Final!!
#     d = {}
#     for i, k in enumerate(strings):
#         for j in k.lower().split():
#             d.setdefault(j, []).append(i)
#     return d


# def get_word_indices(strings: list[str]) -> dict:
#     res = {}
#     [res.setdefault(s, []).append(i) for i, val in enumerate(strings) for s in val.lower().split()]
#     return res
#
#
#
# print(get_word_indices(['Look at my horse', 'my horse', 'is amazing']))
# assert get_word_indices(['This is a string',
#                              'test String',
#                              'test',
#                              'string']) == {'this': [0], 'is': [0], 'a': [0],
#                                             'string': [0, 1, 3], 'test': [1, 2]}
# assert get_word_indices(['Look at my horse',
#                              'my horse',
#                              'is amazing']) == {'look': [0], 'at': [0], 'my': [0, 1],
#                                                 'horse': [0, 1], 'is': [2], 'amazing': [2]}
# assert get_word_indices([]) == {}
# assert get_word_indices(['Avada Kedavra',
#                              'avada kedavra',
#                              'AVADA KEDAVRA']) == {'avada': [0, 1, 2],
#                                                    'kedavra': [0, 1, 2]}
# print("Проверки пройдены!")

# def f(a,b,c,d,e,j,i,s,r,t,v,x,z,m,p,o,u,y,h,l,k=True,f=False,g="It's experiment!"):
#     print(a,b,c,d,e,j,i,s,r,t,v,x,z,m,p,o,u,y,h,l,k,f,g)
# f(*range(1,40,2))

# def replace(text: str, old: str, new: str = ''):
#     return text.replace(old, new)
#
# assert replace('Нет', 'т') == 'Не'
# assert replace('Bella Ciao', 'a') == 'Bell Cio'
# assert replace('nobody; i myself farewell analysis', 'l', 'z') == 'nobody; i mysezf farewezz anazysis'
# assert replace('commend me to my kind lord meaning', 'M', 'w') == 'commend me to my kind lord meaning'
# print("Проверки пройдены!")


# def make_header(string: str, head: int = 1) -> str:
#     return f"<h{head}>{string}</h{head}>"
#
# print(make_header('Bella Ciao', 3))
# assert make_header('Нет') == '<h1>Нет</h1>'
# assert make_header('Bella Ciao', 4) == '<h4>Bella Ciao</h4>'
# assert make_header('Go little rock star', 6) == '<h6>Go little rock star</h6>'
# assert make_header('Девальвации не будет. Твердо и четко') == '<h1>Девальвации не будет. Твердо и четко</h1>'
# print('Tests completed successfully')

# def create_matrix(size: int = 3, up_fill=0, down_fill=0) -> list:
#     return [[i+1 if i==j else up_fill if j<i else down_fill for i in range(size)] for j in range(size)]
#
#
# # print(create_matrix())
# [print(r) for r in create_matrix(4,7,9)]
# assert create_matrix() == [[1, 0, 0], [0, 2, 0], [0, 0, 3]]
# assert create_matrix(4) == [[1, 0, 0, 0], [0, 2, 0, 0], [0, 0, 3, 0], [0, 0, 0, 4]]
#
# assert create_matrix(up_fill=7) == [[1, 7, 7],
#                                     [0, 2, 7],
#                                     [0, 0, 3]]
#
# assert create_matrix(up_fill=7, down_fill=9) == [[1, 7, 7],
#                                                  [9, 2, 7],
#                                                  [9, 9, 3]]
#
#
# assert create_matrix(size=4, up_fill=7, down_fill=9) == [[1, 7, 7, 7],
#                                                          [9, 2, 7, 7],
#                                                          [9, 9, 3, 7],
#                                                          [9, 9, 9, 4]]
# print("Проверки пройдены на все 100))")

# def count_args(*args: any) -> int: return len(args)
#
# print(count_args(1,2,3))
# assert count_args(1, 2, 3) == 3
# assert count_args(1, 3) == 2
# assert count_args(2) == 1
# assert count_args() == 0
# assert count_args(True, 2, None, [1, 2, 3], (1, 2, 3), {1, 2, 3}, {1: 1, 2: 2}, frozenset({1, 2, 3})) == 8
# print("Проверки пройдены")

# def check_sum(*args: int) -> str: print("not enough" if sum(args)<50 else "verification passed")
# print(check_sum(8, 11))

# def multiply(*args: int) -> int: return eval('*'.join([str(i) for i in args])) if args else 1
# multiply = lambda *args: __import__('math').prod(args)
#
# assert multiply(1, 2, 3, 4, 5) == 120
# assert multiply(1, 3) == 3
# assert multiply(2) == 2
# assert multiply() == 1

# def only_one_positive(*args: int) -> bool: return len([a for a in args if a>0])==1
# print(only_one_positive(-1, 0, -3, 5, -3))
# assert only_one_positive(1, 2) is False
# assert only_one_positive(-1, 0, -3, 5, -3) is True
# assert only_one_positive() is False
# print("Проверки пройдены")

# def print_goods(*args: any):
#     a = [i for i in args if type(i)==str and len(i)]
#     print("Нет товаров") if not a else [print(f"{j+1}. {h}") for j, h in enumerate(a)]
#
# print_goods(1, True, 'Грушечка', '', 'Pineapple')
# print_goods()
# print_goods([], {}, 1, 2)

# def info_kwargs(**kwargs): [print(f"{k} = {v}") for k, v in sorted(kwargs.items())]
# info_kwargs(first_name="John", last_name="Doe", age=33)


# def create_actor(**kwargs):
#     return {'name': 'Райан', 'surname': 'Рейнольдс', 'age': 46}|kwargs
#
# print(create_actor(height=190, movies=['Дедпул', 'Главный герой'], name='Jack', age=20))
# assert create_actor() == {'name': 'Райан', 'surname': 'Рейнольдс', 'age': 46}
# assert create_actor(name='Jack', age=20) == {'name': 'Jack', 'surname': 'Рейнольдс', 'age': 20}
# print("Проверки пройдены")

# n = 6790
# while (n:=n-5) > 190: print(n)

# a, b = map(int, input().split())
# year = 0
# while a <= b: a, b, year = a*3, b*2, year+1
# print(year)

# numbers = [2, 3, 7, 9, 5, 0, 6, 3, 6, 0, 1, 7, 9, 4, 4, 4, 2, 2, 6, 9, 1, 7, 0, 3, 8, 1, 0, 3, 8, 0, 8, 4, 0, 2, 3, 6,
#            6, 1, 5, 8, 7, 2, 3, 8, 7, 7, 1, 2, 2, 8, 4, 3, 4, 8, 0, 7, 9, 8, 3, 7, 7, 7, 7, 5, 1, 7, 4, 5, 0, 8, 0, 9,
#            2, 4, 7, 6, 6, 5, 9, 7, 1, 7, 8, 8, 3, 4, 9, 7, 6, 4, 2, 0, 0, 0, 9, 4, 0, 9, 4, 4, 4, 5, 5, 4, 2, 5, 9, 4,
#            8, 1, 5, 7, 1, 0, 2, 6, 8, 7, 2, 7, 9, 3, 6, 4, 7, 5, 0, 7, 2, 0, 8, 2, 9, 8, 6, 4, 4, 7, 5, 5, 9, 4, 9, 5,
#            6, 9, 1, 1, 3, 1, 5, 2, 1, 7, 0, 0, 7, 8, 1, 3, 0, 0, 4, 4, 3, 3, 6, 7, 8, 6, 1, 2, 0, 2, 0, 9, 9, 0, 5, 2,
#            4, 1, 7, 4, 9, 9, 4, 9, 6, 9, 2, 7, 1, 2, 4, 5, 4, 0, 9, 0]
# while 4 in numbers: numbers.remove(4)
# print(*numbers)