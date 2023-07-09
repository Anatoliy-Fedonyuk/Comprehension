### MODULE RE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# import re
# import re

# from string import printable          #!!!!!!
# print(printable)


# text = "<font color=#CC0000>"
# match = re.search(r"(?ai)(\w+)=(#[\da-fA-F]{6})\b", text)
# print(match)
# print(match.group(0,1,2))
# print(match.groups())
# print(match.start(1))
# print(match.end(1))
# print(match.span(2))
# print(match.pos, match.endpos)
# print(match.re)
# print(match.string)

# text = "<font color=#CC0000 bg=#ffffff fuck=#FF2288>"
# match = re.search(r"(?P<key>\w+)=(?P<value>#[\w+]{6})\b", text)
# print(match)
# print(match.re)
# print(match.groupdict())    #Wau metod))
# print(match.lastgroup, match.lastindex)
# print(match.expand(r"\1:\2"))
# print(match.expand(r"\g<key>:\g<value>"))
# mdict_ls = []
# mtuple = tuple()
# for m in re.finditer(r"(?P<key>\w+)=(?P<value>#[\da-fA-F]{6})\b", text):
#     print(m.groups())
#     print(m)
#     mdict_ls += [m.groupdict()]
#     mtuple += tuple(m.groups())
# print(mdict_ls)
# print(mtuple)
# match = re.findall(r"(?P<key>\w+)=(?P<value>#[\da-fA-F]{6})\b", text)
# print(match)
#
# text = "Киев Варшава Одесса Запор Женева"
# list = re.sub(r"\s*(\w+)\s*", r"<option> \1 </option>\n", text)
# print(list)
#
# count = 0
# def replFind(m):
#     global count
#     count += 10
#     return f"<option value='{count}'>{m.group(1).upper().center(15, '_')}</option>\n"
#
# print(re.sub(r"\s*(\w+)\s*", replFind, text))

# text = """Москва
# Казань
# Тверь
# Самара
# Уфа"""
#
# count = 0
# def replFind(m):
#     global count
#     count += 1
#     return f"<option value='{count}'>{m.group(1)}</option>\n"
#
#
# rx = re.compile(r"(?mi)\s*(\w+)\s*")
# list, total = rx.subn(r"<option>\1</option>\n", text)
# list2 = rx.sub(replFind, text)
# print(list, total, list2, sep="\n")
# print(rx.flags)

# a = 10
# b = 5
# print("{a} - {b} = {a - b}")
# a = 10
# b = 5
# print(f'{a} - {b} = {a - b}')
# a = 5
# b = 10
# print(r"{b} - {a} = {b - a}")
# s = r"Последовательность \n используется для переноса строк"
# print(s)
# print(f"{(a:=int(input()))} * {a} = {a*a}")
# print(r'\\\''); print(f"\\\\\\\'")

# (lambda _, d: d(f'{_} * {_} = {_*_}'))(int(input()), print)
# a\n + \nb\n = \nc
# print(rf'{(a:=input())}\n + \n{(b:=input())}\n = \n{int(a)+int(b)}')
# print(r"{}\n + \n{}\n = \n{}".format(a:=input(), b:=input(), int(a)+int(b)))

# text = 'fsdfdsf.mе&r!kX\q<ЫlХювк*ШЛ/PWЖЁRЩ-NнОaбъСНлdй(ф^4{sZjИ`@жЮБF7"ЕoиэП:Ьуь~№[0A+%_сGQv)ё$MuUSТCГя50ЦnДE;9АJ]В'
# print(re.findall(r"(?<=[^ё$MuUSТCГя50ЦnДE;9АJ])(?:\**?)(?=[ШП9В9фвфЛ]*/)", text))

# for match in re.finditer(r"(cat|dog)", "Hi cat and dog live here"):
#     print(match, match.groups(), match.groupdict(), sep='\n')

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# text = """[ x ]
# Набор маркеров 95000-6, 6 цветов в наборе (Набор маркеров 6 цветов
# 95000-6 )
# <https://royaltoys.com.ua/product/nabor-markerov-6-cvetov-95000-6-/>
# Количество: 23,50 грн. x 10
# Итого: 235 грн.
# [ x ]
# Набор маркеров 95000-10, 10 цветов в наборе (Набор маркеров 10 цветов
# 95000-10 )
# <https://royaltoys.com.ua/product/nabor-markerov-10-cvetov-95000-10-/>
# Количество: 38,54 грн. x 10
# Итого: 385,40 грн.
# [ x ]
# Детский магнитный конструктор LT5003 из 36 деталей (Конструктор LT5003
# (12шт) магнитный, 36дет, в кор-ке, 28,5-25-8,5см )
# <https://royaltoys.com.ua/product/konstruktor-lt5003-12sht-magnitnyy-36det-v-kor-ke-28-5-25-8-5sm-/>
# Количество: 737,90 грн. x 1
# Итого: 737,90 грн.
# [ x ]
# """
#
# mdict_ls = []
# mtuple = tuple()
# for m in re.finditer(r"(?s)\[ x \]\n(?P<имя>[\w\W]+?)\n<http.*?во: (?P<цена_за_ед>\d+,?[\d]{0,2}).*?x (?P<количество>\d+)\n.*?го: (?P<сумма>\d+,?[\d]{0,2})", text):
#     print(m.groupdict())


# regex = r'(?>a+)+b'
# print(re.findall(regex, 'a'*50))

# match = re.match(input(), input())
# print(match.group(0))
# print(match.start(0))
# print(match.end(0))
# print(match.pos)
# print(match.endpos)
# print(match.re)
# print(match.string)

# match = re.match(input(), input())
# print(match.group(0)) if match else 0

# import re
# match = re.search(r"#[a-z]+\b", input())
# if match: print(match.group())

# import re, sys
# lines = list(map(str.strip, sys.stdin.readlines()))
# for i in range(len(lines)):
#     match = re.search(r"[Кк]од", lines[i])
#     if match:
#         print(i + 1, match.start(0))
#         break
# if not match: print("код не найден")

# import re
# for i in range(5):
#     match = re.search(r"Activation key: ((?:[A-Z\d]{5}-){4}[A-Z\d]{5})", input())
#     if match: print(match[1])

# import re
# print((__import__('re').search(r't=[\d.+]+', input()))[0])          #3.3.4 fin my

# match (__import__('re').match(r'(?ai)[a-z]+\b', input())):
#     case word if word: print('Первое слово в предложении:', word[0])

# match (__import__('re').match(r"[a-z]+(?: [a-z]+){11}", input())):
#     case word if word: print('возможно, это seed-фраза')

# print((__import__('re').match(r"[^@]+", input()))[0])

# print(bool(__import__('re').fullmatch(r"\d{13,}", input())))

# print(bool(__import__('re').fullmatch(r"(?a)[\w@#$%^&*()_\-+!?]{8,}", input())))

# print(bool(__import__('re').fullmatch(r"\+?\d+ ?\(?\d{3}\)? ?\d{3}[ -]?\d{2}[ -]?\d{2}", input())))

# print(bool(__import__('re').fullmatch(r"-?(?!-)\d*(x\^\d|x)?((\+|-)\d*(x\^\d|x)?)*", input())))

# for match in __import__('re').finditer(r'\w+', input()): print(match[0])

# print(*(__import__('re').findall(r"(?i)\b[a-zа-яё]{5}\b", input())), sep='\n')

# [print(match[0]) for match in __import__('re').finditer(r"\d+,\d+\s₽", input())]

# print(*(__import__('re').findall(r"(?a)\b([\w\-_]+?@\w+\.\w{1,4})\b", input())), sep='\n')

# print(*(__import__('re').findall(r"\d\d[/]?\d\d[/]\d\d[/]?\d\d|\d\d[.]?\d\d[.]\d\d[.]?\d\d", input())), sep='\n')

# print(*(__import__('re').findall(r"(?:[01]\d|2[0-3]):(?:[0-5]\d)", input())), sep='\n')

# print(*(__import__('re').findall(r"<a.*?href=[\"\'](.+?)[\"\']", input())), sep='\n')

# print(__import__('re').split(r"Кат[а-яёА-ЯЁ: ]*\\n", input()))

# print(__import__('re').sub(r"(?i)[ауоыиэяюёеaeiouy]", r'!', input()))

# print(__import__('re').sub(r"<.*?>", '', input()))

# a, b, c = map(lambda x: x[:-2], input().split())
# print(__import__('re').sub(rf"{a}\w+\s(?:{b[0]}.\s{c[0]}.|{b}\w+\s{c}\w+)", 'ФИО', input()))

# print((__import__('re').subn(r"[!,.?:]", '', input()))[1])

# print(__import__('re').subn(r"\d", 'X', input()))

# import re
# a = """<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[]^_`abcdefghijklmnopqrstuvwxyz{|}~абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ !"#$%&\'()*+,-./0123456789:;"""
# print(re.escape(f"{a}"))

# import re
# print(re.escape(input()))

# import re
#
# regex = r'П(?P<name>.+?)в(?P<name2>2 группа)?(?P<name3>ет)?,'
# text = 'Привет, как тебя зовут?'
# match = re.match(regex, text)
# print(match)
# print(match[0])
# print(match.groups(0))
# print(match.groupdict(0))
# print(match.group(1, "name2", 0))

# [print(match["tag"]) for match in __import__('re').finditer(r"<p.*?>(?P<tag>.*?)</p>", input())]


# reg = r"\b(?P<Протокол>https?)://(?P<Домен>[a-z.]+)/(?:[\w\-_/]+)?(?P<Параметры>\?[\w=&]+)?(?P<Якорь>#[a-z]+)?"
# for m in __import__('re').finditer(reg, input()):
#     print(f'Полная ссылка: {m[0]}', ' | '.join(f'{k}: {v}' for k, v in m.groupdict().items()), sep='\n', end='\n\n')

# print(f"Полная ссылка: {m.group(0)}")
# print(f"Протокол: {m['Протокол']} | Домен: {m['Домен']} | Параметры: {m['Параметры']} | Якорь: {m['Якорь']}")
# print()

# print(__import__('re').findall(r"</?([a-z\d]+).*?>", input()))

# print(__import__('re').findall(r"(\d+):([a-zA-Z\d]+):([a-z\d]+)", input()))

# print(__import__('re').split(r"[^\d]*([/+*=\-:])[^\d]*", input()))

# print(__import__('re').split(r"([\?&])", input()))

# print(__import__('re').sub(r"(?i)(?P<C>[а-яё]+)\s(?P=C)", r'\g<C>', input()))

# res = __import__('re').sub(r"\*\*([ \w]+)\*\*", r'<strong>\1</strong>', input())
# print(__import__('re').sub(r"(?<!\*)\*([ \w]+)\*", r'<em>\1</em>', res))

# print(__import__('re').sub(r"([\d.]+:\d+)", r'http://\1', input()))

# print(__import__('re').sub(r"(\d\d[./])(\d\d[./])", r'\2\1', input()))

# print(__import__('re').sub(r"(?i)(его|её|их)[а-яё]*", r'\1', input()))

# m = __import__('re').search(r"(\d+[₽$])", input())
# if m: print(m.expand(r"Цена данного товара \1"))

# print(__import__('re').sub(r"(\d+)", lambda m: str(int(m[1])**2), input()))

# def fun(m): return str(int(m[0])//3) if not int(m[0])%3 else m[0]
# print(__import__('re').sub(r"\d+", fun, input()))

# print(__import__('re').sub(r"\d+", lambda m: (m[0], str(int(m[0])//3))[not int(m[0])%3], input()))

# pattern = __import__('re').compile(r"[\dA-F]{2}(?::[\dA-F]{2}){5}")

# match (__import__('re').compile(r"\b([a-z]+)\b")).search(input(), int(input()), int(input())):    # Моё)
#     case x if x: print(x[0])

# import re                           ##### Перевод числа флага - в человеческий)
# pattern = re.compile(r'[a-zA-Z]{1,}')
# print(pattern.flags) # 32
# print(re.RegexFlag(32)) # re.UNICODE

# import re           # Интересная задача с флагами))
# def get_x(m): return {'o': 'x', 'O':'X'}[m[0]]
# print(re.sub('(?i)O', get_x, input()))

# print(__import__('re').findall(r"(?i)привет", input()))

# import re
# import sys

# pattern = re.compile("^python", flags=re.IGNORECASE | re.MULTILINE)
# print(pattern.findall("Python is a programming language.\nPython is also a snake."))
# pattern = re.compile("^python", flags=re.IGNORECASE | re.MULTILINE)
# print(pattern.search("Python is a programming language.\nPython is also a snake."))

# print(__import__('re').findall(r"(?m)^[$^]+$", ''.join(open(0).readlines())))

# print(__import__('re').findall(r"(?sm)start(.+)end", ''.join(__import__('sys').stdin.readlines())))

# import re
# pattern = re.compile(r"""
# (?:
#     (?:\s*[+>~,]\s*|\s+)
#     |
#     [^:+>~,\s\\[\]]+(?:\\.[^:+>~,\s\\[\]]*)*
# )
# |
# \[(?:
#     [^\\[\]]*(?:\\.[^\\[\]]*)*
#     |
#     [^=]+=~?\s*
#     (?:
#         "[^\\"]*(?:\\.[^"\\]*)*"
#         |
#         '[^\\']*(?:\\.[^'\\]*)*'
#     )
# )\]
# |
# :[^\\:([]+(?:\\.[^\\:([]*)*
# (?:
#     \((?:
#         [^\\()]*(?:\\.[^\\()]*)*
#         |
#         "[^\\"]*(?:\\.[^"\\]*)*"
#         |
#         '[^\\']*(?:\\.[^'\\]*)*'
#     )\)
# )?
# """, re.X)

# print(__import__('re').compile(r'[123]', flags=re.DEBUG))