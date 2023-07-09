import collections
import math
import random
import itertools
import re
from datetime import datetime

# Модуль collections
print('=' * 30)
a = [1, 1, 1, 2, 2, 3, 4, 4, 4, 5, 5, 5, 5, 5, ]
print(a)
count = collections.Counter(a)
print(count)
print(type(count))
# lst = count.keys()
# print(lst)

dict_of_lists = collections.defaultdict(list)
for value in range(1, 21):
    if value % 2 == 0:
        dict_of_lists['четные'].append(value)
    else:
        dict_of_lists['нечетные'].append(value)
print(dict(dict_of_lists))

t = dict.fromkeys(range(1, 11), "тут будет")
print(t)

count2 = collections.defaultdict(int)
for value in a:
    count2[value] += 1
print(dict(count2))

d = collections.deque([1, 2, 3, 4, 5])
d.popleft()
d.appendleft(7)
d.pop()
d.append(0)
print(d)


# help(math)    #Модуль math
print('=' * 30)
print(math.sqrt(81))
print(math.pi)
print(math.e)
print(round(2.6))
print(math.ceil(2.1))
print(math.floor(2.1))
print(math.isnan(math.nan))
print(math.exp(2))
print(math.log(8, 2))


# Модуль random
print('=' * 30)
# random.seed(2)
print(random.random())
print(random.randint(0, 99))
print(random.choice([1, 3, 6, 8, 23, -23, 12, 5, 4, 9]))
# random.seed(42)
seq = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(random.shuffle(seq))
print(seq)


# Модуль itertools
print('=' * 40)
combs = itertools.combinations([1, 2, 3, 4], 2)
print(list(combs))
permutation = itertools.permutations([1, 2, 3, 4], 2)
print(list(permutation))
print(list(itertools.combinations_with_replacement([1, 2, 3, 4], 2)))
print(list(itertools.accumulate([1, 2, 3, 4, 5])))
print(list(itertools.accumulate([1, 2, 3, 4, 5], lambda a, b: a - b)))
print(list(itertools.filterfalse(lambda x: x % 2, range(11))))


# Модуль re
print('=' * 50)
text = "Hi @mr_alex ! My name is John and I love coffee. #coffeelover, #2022"
print(text)
print(re.sub(r"[.!?\\-]", '', text))
print([e for e in re.finditer(r"#[A-Za-z0-9]*", text)])
print(re.split(r"[.,!?\\-]", text))


# help(datetime)  # Модуль datetime
print('=' * 50)
now = datetime.now()
print(now)
print(datetime.time(now))
print(now.day, now.month, now.year)

date_string = "21, June, 2018"
date_object = datetime.strptime(date_string, "%d, %B, %Y")
print(date_object)