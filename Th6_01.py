import os
import time

('C:\\Users\\Admin\\Desktop\\Для примера', ['Папка 1', 'Папка вторая'],
 ['222.jpg', 'save.txt', 'Text.txt', 'Text1.txt', 'Text2.txt', 'Text3.txt'])
spisok = []
spisok2 = []

for adress, dirs, files in os.walk('C:\\Users\\Admin\\Desktop\\Для примера'):
    spisok.append(adress)
    for file in files:
        full = os.path.join(adress, file)
        if time.time() - os.path.getctime(full) < 86400:
            #and 'save' in full:
            spisok2.append(full)

print(spisok)
print(spisok2)