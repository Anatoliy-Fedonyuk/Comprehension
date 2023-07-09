# import sqlite3 as sq

# con = sq.connect("saper.db")
# cur = con.cursor()
#
# cur.execute("""
# """)
#
# con.close()

# with sq.connect("saper.db") as con:
#     cur = con.cursor()
#     cur.execute("""CREATE TABLE IF NOT EXISTS users (
#         name TEXT NOT NULL,
#         sex INTEGER DEFAULT 1,
#         old INTEGER,
#         score INTEGER
#     )""")

    # cur.execute("INSERT INTO users(name, old, score) VALUES('Алексей', 18, 1000)")
    # cur.execute("INSERT INTO users(name, old, score) VALUES('Толян', 48, 10000)")
    # cur.execute("INSERT INTO users(name, old, score) VALUES('Маша', 18, 1500)")
    # cur.execute("DROP TABLE IF EXISTS users")

# with sq.connect("saper.db") as con:
#     cur = con.cursor()
#
#     cur.execute("SELECT * FROM users WHERE score > 100 ORDER BY score DESC LIMIT 5")
    # result = cur.fetchall()
    # print(result)
    # for result in cur:
    #     print(result)
    # result = cur.fetchone()
    # result2 = cur.fetchmany(2)
    # print(result)
    # print(result2)


# import sqlite3 as sq
#
# with sq.connect("saper.db") as con:
#     cur = con.cursor()
#     cur.execute("""CREATE TABLE IF NOT EXISTS games (
#         user_id INTEGER NOT NULL,
#         score INTEGER,
#         time INTEGER
#     )""")
#
#     cur.execute("INSERT INTO games(user_id, score, time) VALUES(1, 350, 110010)")
#     cur.execute("INSERT INTO games VALUES(1, 200, 101040)")
#     cur.execute("INSERT INTO games VALUES(2, 500, 100010)")
#     cur.execute("INSERT INTO games VALUES(1, 400, 201040)")
#
    # cur.execute("DROP TABLE IF EXISTS games")


# import sqlite3 as sq
#
# with sq.connect("saper.db") as con:
#     cur = con.cursor()
#     x = cur.execute("""SELECT name, sex, sum(games.score) as score
#     FROM games
#     JOIN users ON games.user_id = users.rowid
#     GROUP BY user_id
#     ORDER BY score DESC""")
#     print(x)

# import sqlite3 as sq
#
# with sq.connect("student.db") as con:
#     cur = con.cursor()
#     cur.execute("""CREATE TABLE IF NOT EXISTS mans (
#         id INTEGER,
#         name TEXT NOT NULL,
#         sex INTEGER,
#         old INTEGER
#     )""")
#
#     cur.execute("INSERT INTO students VALUES(1, 'Коля', 1, 37)")
#     cur.execute("INSERT INTO students VALUES(2, 'Маша', 2, 25)")
#     cur.execute("INSERT INTO students VALUES(3, 'Вася', 1, 45)")
#     cur.execute("INSERT INTO students VALUES(4, 'Даша', 2, 33)")
    # cur.execute("DROP TABLE IF EXISTS games")

# import sqlite3 as sq
#
# with sq.connect("student.db") as con:
#     cur = con.cursor()
#     cur.execute("""CREATE TABLE IF NOT EXISTS marks (
#         id INTEGER,
#         subject INTEGER,
#         mark INTEGER
#     )""")
#
#     cur.execute("INSERT INTO marks VALUES(1, 'СИ', 4)")
#     cur.execute("INSERT INTO marks VALUES(1, 'Физика', 3)")
#     cur.execute("INSERT INTO marks VALUES(1, 'Вышка', 5)")
#     cur.execute("INSERT INTO marks VALUES(2, 'СИ', 3)")
#     cur.execute("INSERT INTO marks VALUES(2, 'Вышка', 4)")
#     cur.execute("INSERT INTO marks VALUES(2, 'Химия', 5)")
#     cur.execute("INSERT INTO marks VALUES(3, 'СИ', 4)")
#     cur.execute("INSERT INTO marks VALUES(3, 'Черчение', 3)")
#     cur.execute("INSERT INTO marks VALUES(3, 'Физика', 5)")
#     cur.execute("INSERT INTO marks VALUES(5, 'Черчение', 5)")
#     cur.execute("INSERT INTO marks VALUES(5, 'СИ', 4)")
#     cur.execute("INSERT INTO marks VALUES(5, 'История', 5)")
#     cur.execute("INSERT INTO marks VALUES(4, 'СИ', 2)")

############# API SQLite 3 #####################################################

# import sqlite3 as sq
#
# cars = [
#     ('Audi', 52642),
#     ('Mercedes', 57127),
#     ('Skoda', 9000),
#     ('Volvo', 29000),
#     ('Bentley', 350000)
# ]
#
# with sq.connect("cars.db") as con:
#     cur = con.cursor()
#
#     cur.execute("""CREATE TABLE IF NOT EXISTS cars (
#         car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         model TEXT,
#         price INTEGER
#     )""")

    # cur.execute("INSERT INTO cars VALUES(1,'Audi',52642)")
    # cur.execute("INSERT INTO cars VALUES(2,'Mercedes',57127)")
    # cur.execute("INSERT INTO cars VALUES(3,'Skoda',9000)")
    # cur.execute("INSERT INTO cars VALUES(4,'Volvo',29000)")
    # cur.execute("INSERT INTO cars VALUES(5,'Bentley',350000)")

    # for car in cars:
    #     cur.execute("INSERT INTO cars VALUES(NULL, ?, ?)", car)

    # cur.executemany("INSERT INTO cars VALUES(NULL, ?, ?)", cars)

    # cur.execute("UPDATE cars SET price = :Price WHERE model LIKE 'A%'", {'Price': 25000})
    # плєйсхолдер - именованій параметр Price

    # cur.executescript("""DELETE FROM cars WHERE model LIKE 'A%';
    #     UPDATE cars SET price = price+1000""")        #метод executescript

# con = None
# try:
#     con = sq.connect("cars.db")
#     cur = con.cursor()
#
#     cur.executescript("""CREATE TABLE IF NOT EXISTS cars (
#             car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#             model TEXT,
#             price INTEGER
#         );
#         BEGIN;
#         INSERT INTO cars VALUES(NULL,'Audi',52642);
#         UPDATE cars2 SET price = price+1000
#     """)
#     con.commit()
#
# except sq.Error as e:
#     if con: con.rollback()
#     print("Ошибка выполнения запроса")
# finally:
#     if con: con.close()


# import sqlite3 as sq
#
# with sq.connect("cars.db") as con:
#     con.row_factory = sq.Row
#     cur = con.cursor()

    # cur.executescript("""CREATE TABLE IF NOT EXISTS cars (
    #         car_id INTEGER PRIMARY KEY AUTOINCREMENT,
    #         model TEXT,
    #         price INTEGER
    #     );
    #     CREATE TABLE IF NOT EXISTS cust(name TEXT, tr_in INTEGER, buy INTEGER);
    # """)
    #
    # cur.execute("INSERT INTO cars VALUES(NULL,'Запорожец', 1000)")
    #
    # last_row_id = cur.lastrowid
    # buy_car_id = 2
    # cur.execute("INSERT INTO cust VALUES('Федор', ?, ?)", (last_row_id, buy_car_id))

    # cur.execute("SELECT model, price FROM cars")
    # rows = cur.fetchall()
    # print(rows)
    # cur.execute("SELECT * FROM cars")
    # print(cur.fetchmany(3))
    # print(cur.fetchone())
    #
    # cur.execute("SELECT * FROM cars")
    # for result in cur: print(*result)
    #
    # cur.execute("SELECT model, price FROM cars")
    # for result in cur: print(f"марка авто: {result['model']:15s} цена предложения: {result['price']:10d} $")
    # cur.execute("SELECT * FROM cars")
    # print({res['model']: res['price'] for res in cur})

# import sqlite3 as sq

# def readAva(n):
#     try:
#         with open(f"avas/{n}.jpg", "rb") as f:
#             return f.read()
#     except IOError as e:
#         print(e)
#         return False
#
#
# def writeAva(name, data):
#     try:
#         with open(name, "wb") as f:
#             f.write(data)
#     except IOError as e:
#         print(e)
#         return False
#
#     return True
#
# with sq.connect("cars.db") as con:
#     con.row_factory = sq.Row
#     cur = con.cursor()
#     cur.executescript("""CREATE TABLE IF NOT EXISTS users (
#         name TEXT,
#         ava BLOB,
#         score INTEGER)
#     """)
#
#     img = readAva(5)
#     if img:
#         binary = sq.Binary(img)
#         cur.execute("INSERT INTO users VALUES ('Алеша', ?, 2000)", (binary,))
#
#     cur.execute("SELECT ava FROM users WHERE name = 'Анатолий'")
#     img = cur.fetchone()['ava']
#     writeAva("out.png", img)

####################### Backup BD ##########################
# import sqlite3 as sq
#
# with sq.connect("cars.db") as con:
#     cur = con.cursor()
#
#     with open("sql_damp.sql", "w", encoding='utf8') as f:
#         for sql in con.iterdump():
#             f.write(sql)

    # with open("sql_damp.sql", "r", encoding='utf8') as f:
    #     sql = f.read()
    #     cur.executescript(sql)

####################### Virtual BD ##########################
# import sqlite3 as sq
#
# data = [("car", "машина"), ("house", "дом"), ("tree", "дерево"), ("color", "цвет")]
#
# con = sq.connect(':memory:')
# with con:
#     cur = con.cursor()
#     cur.execute("""CREATE TABLE IF NOT EXISTS dict(
#         eng TEXT, rus TEXT
#     )""")
#
#     cur.executemany("INSERT INTO dict VALUES(?,?)", data)
#
#     cur.execute("SELECT rus FROM dict WHERE eng LIKE 'c%'")
#     print(cur.fetchall())



####################### ТРЕНАЖЕР SQL SQL SQL ##########################

# import pymysql
#
# from pymysql.cursors import DictCursor
# connection = pymysql.connect(
#     host='localhost',
#     user='user',
#     password='password',
#     db='iata',
#     charset='utf8mb4',
#     cursorclass=DictCursor
# )
# ...
# connection.close()

# CREATE TABLE book (                               #1.1
#     book_id INT PRIMARY KEY AUTO_INCREMENT,
#     title VARCHAR(50),
#     author VARCHAR(30),
#     price DECIMAL(8, 2),
#     amount INT)

# INSERT INTO book (title, author, price, amount)           #1.2
# VALUES ('Мастер и Маргарита', 'Булгаков М.А.', 670.99, 3);
# SELECT * FROM book;
#
# INSERT INTO book (title, author, price, amount)             #1.3
# VALUES ('Белая гвардия', 'Булгаков М.А.', 540.50, 5);
# INSERT INTO book (title, author, price, amount)
# VALUES ('Идиот', 'Достоевский Ф.М.', 460.00, 10);
# INSERT INTO book (title, author, price, amount)
# VALUES ('Братья Карамазовы', 'Достоевский Ф.М.', 799.01, 2);
# SELECT * FROM book

# SELECT title, amount FROM book;
# SELECT author, title, price FROM book;      #2.2
# SELECT title AS Название, amount FROM book;
# SELECT title AS Название, author AS Автор FROM book;    #2.3
# SELECT title, author, price, amount,
#      price * amount AS total
# FROM book;
# SELECT title, amount, 1.65 * amount AS pack FROM book;     #2.4

# SELECT title,
#     price,
#     ROUND((price*18/100)/(1+18/100),2) AS tax,
#     ROUND(price/(1+18/100),2) AS price_tax
# FROM book;

# В конце года цену всех книг на складе пересчитывают – снижают ее на 30%. Написать SQL запрос, который из таблицы
# book выбирает названия, авторов, количества и вычисляет новые цены книг. Столбец с новой ценой назвать new_price,
# цену округлить до 2-х знаков после запятой.
# SELECT title, author, amount,                         #2.5
#   round((price*0.7),2) AS new_price
#     FROM book;
# +-----------------------+------------------+--------+-----------+
# | title                 | author           | amount | new_price |
# +-----------------------+------------------+--------+-----------+
# | Мастер и Маргарита    | Булгаков М.А.    | 3      | 469.69    |
# | Белая гвардия         | Булгаков М.А.    | 5      | 378.35    |
# | Идиот                 | Достоевский Ф.М. | 10     | 322.00    |
# | Братья Карамазовы     | Достоевский Ф.М. | 2      | 559.31    |
# | Стихотворения и поэмы | Есенин С.А.      | 15     | 455.00    |
# +-----------------------+------------------+--------+-----------+

# SELECT title, amount, price,
#     ROUND(IF(amount<4, price*0.5, price*0.7),2) AS sale
# FROM book;

# При анализе продаж книг выяснилось, что наибольшей популярностью пользуются книги Михаила Булгакова, на втором месте
# книги Сергея Есенина. Исходя из этого решили поднять цену книг Булгакова на 10%, а цену книг Есенина - на 5%.
# Написать запрос, куда включить автора, название книги и новую цену, последний столбец назвать new_price. Значение
# округлить до двух знаков после запятой.
# SELECT author, title,                               #2.6
# ROUND(IF(author='Булгаков М.А.', price*1.1,
# IF(author='Есенин С.А.', price*1.05, price)),2) AS new_price
# FROM book;
# Query result:
# +------------------+-----------------------+-----------+
# | author           | title                 | new_price |
# +------------------+-----------------------+-----------+
# | Булгаков М.А.    | Мастер и Маргарита    | 738.09    |
# | Булгаков М.А.    | Белая гвардия         | 594.55    |
# | Достоевский Ф.М. | Идиот                 | 460.00    |
# | Достоевский Ф.М. | Братья Карамазовы     | 799.01    |
# | Есенин С.А.      | Стихотворения и поэмы | 682.50    |
# +------------------+-----------------------+-----------+


# Вывести автора, название  и цены тех книг, количество которых меньше 10.
# ELECT author, title, price                             #2.7
# FROM book
# WHERE amount < 10;

# SELECT title, author, price
# FROM book
# WHERE (author = 'Булгаков М.А.' OR author = 'Есенин С.А.') AND price > 600;

# Вывести название, автора,  цену  и количество всех книг, цена которых меньше 500 или больше 600,
# а стоимость всех экземпляров этих книг больше или равна 5000.
# SELECT title, author, price, amount FROM book                      #2.8
# WHERE (price>600 OR price<500) AND price*amount >= 5000

# SELECT title, amount FROM book
# WHERE amount BETWEEN 5 AND 14;
#
# SELECT title, price FROM book
# WHERE author IN ('Булгаков М.А.', 'Достоевский Ф.М.');

# Вывести название и авторов тех книг, цены которых принадлежат интервалу от 540.50 до 800 (включая границы),
# а количество или 2, или 3, или 5, или 7 .
# SELECT title, author                     #2.9
# FROM book
# WHERE (price BETWEEN 540.5 AND 800) AND amount IN (2,3,5,7)
# Query result:
# +--------------------+------------------+
# | title              | author           |
# +--------------------+------------------+
# | Мастер и Маргарита | Булгаков М.А.    |
# | Белая гвардия      | Булгаков М.А.    |
# | Братья Карамазовы  | Достоевский Ф.М. |
# +--------------------+------------------+
# Affected rows: 3

################################# СОРТИРОВКА
# SELECT author, title, amount AS Количество
# FROM book
# WHERE price < 750
# ORDER BY author, Количество DESC;
#
# SELECT author, title, amount AS Количество
# FROM book
# WHERE price < 750
# ORDER BY 1, 3 DESC;

# Вывести  автора и название  книг, количество которых принадлежит интервалу от 2 до 14 (включая границы).
# Информацию  отсортировать сначала по авторам (в обратном алфавитном порядке), а затем по названиям книг (по алфавиту).
# SELECT author, title                    #2.10
# FROM book
# WHERE amount BETWEEN 2 AND 14
# ORDER BY 1 DESC, 2 ASC;
# +------------------+--------------------+
# | author           | title              |
# +------------------+--------------------+
# | Достоевский Ф.М. | Братья Карамазовы  |
# | Достоевский Ф.М. | Идиот              |
# | Булгаков М.А.    | Белая гвардия      |
# | Булгаков М.А.    | Мастер и Маргарита |
# +------------------+--------------------+

# Шаблоны
# SELECT title FROM book WHERE title LIKE 'Б%'; #/* эквивалентное условие title LIKE 'б%'*/
# SELECT title FROM book WHERE title LIKE "_____"
# SELECT title FROM book WHERE title LIKE "______%"; # эквивалентные условия title LIKE "%______"title LIKE "%______%"
#Вывести названия книг, которые содержат букву "и" как отдельное слово, если считать,
# что слова в названии отделяются друг от друга пробелами
# SELECT title FROM book
# WHERE   title LIKE "_% и _%" /*отбирает слово И внутри названия */
#     OR title LIKE "и _%" /*отбирает слово И в начале названия */
#     OR title LIKE "_% и" /*отбирает слово И в конце названия */
#     OR title LIKE "и" /* отбирает название, состоящее из одного слова И */

#Вывести названия книг, которые состоят ровно из одного слова, если считать, что слова в названии отделяются друг от друга пробелами .
# SELECT title FROM book WHERE title NOT LIKE "% %";

# SELECT CONCAT("Тарас Бульба та непотріб ",title) AS назва, author AS автори,        #2.12 Свое условие))
# ROUND(price*amount*0.012, 2) AS 'бабло на ЗСУ $'
# FROM book
# ORDER BY 3 DESC
# +------------------------------------------------+------------------+----------------+
# | назва                                          | автори           | бабло на ЗСУ $ |
# +------------------------------------------------+------------------+----------------+
# | Тарас Бульба та непотріб Стихотворения и поэмы | Есенин С.А.      | 117.00         |
# | Тарас Бульба та непотріб Идиот                 | Достоевский Ф.М. | 55.20          |
# | Тарас Бульба та непотріб Белая гвардия         | Булгаков М.А.    | 32.43          |
# | Тарас Бульба та непотріб Мастер и Маргарита    | Булгаков М.А.    | 24.16          |
# | Тарас Бульба та непотріб Братья Карамазовы     | Достоевский Ф.М. | 19.18          |
# +------------------------------------------------+------------------+----------------+

# SELECT car_id, model, price,        #Work in SQLite too
#   round((price*0.713784),2) AS new_price
#     FROM cars;

# SELECT DISTINCT amount      #Work in SQLite too, selection of unique elements
# FROM book;
# SELECT  author FROM book GROUP BY author

# SELECT 'СЛАВА УКРАЇНІ - ' || model AS назва, price        #Work in SQLite too
# FROM cars
# ORDER BY 2 DESC;

# SELECT author, sum(amount), count(amount) FROM book GROUP BY author;
# +------------------+-------------+---------------+
# | author           | sum(amount) | count(amount) |
# +------------------+-------------+---------------+
# | Булгаков М.А.    | 8           | 2             |
# | Достоевский Ф.М. | 23          | 3             |
# | Есенин С.А.      | 15          | 1             |
# +------------------+-------------+---------------+

# Посчитать, количество различных книг и количество экземпляров книг каждого автора , хранящихся на складе.
# Столбцы назвать Автор, Различных_книг и Количество_экземпляров соответственно.
# SELECT author AS Автор, COUNT(author) AS Различных_книг, SUM(amount) AS Количество_экземпляров
# FROM book GROUP BY author;            #Мое решение
# +------------------+----------------+------------------------+
# | Автор            | Различных_книг | Количество_экземпляров |
# +------------------+----------------+------------------------+
# | Булгаков М.А.    | 2              | 8                      |
# | Достоевский Ф.М. | 3              | 23                     |
# | Есенин С.А.      | 1              | 15                     |
# +------------------+----------------+------------------------+

# SELECT author,
# MIN(price) AS Минимальная_цена,
# MAX(price) AS Максимальная_цена,
# AVG(price) AS Средняя_цена
# FROM book
# GROUP BY author;
# +------------------+------------------+-------------------+--------------+
# | author           | Минимальная_цена | Максимальная_цена | Средняя_цена |
# +------------------+------------------+-------------------+--------------+
# | Булгаков М.А.    | 540.50           | 670.99            | 605.745000   |
# | Достоевский Ф.М. | 460.00           | 799.01            | 579.836667   |
# | Есенин С.А.      | 650.00           | 650.00            | 650.000000   |
# +------------------+------------------+-------------------+--------------+

# SELECT author, SUM(price * amount*0.012) AS Стоимость_$ FROM book GROUP BY author;
# +------------------+-------------+
# | author           | Стоимость_$ |
# +------------------+-------------+
# | Булгаков М.А.    | 56.58564    |
# | Достоевский Ф.М. | 141.62436   |
# | Есенин С.А.      | 117.00000   |
# +------------------+-------------+

# SELECT author, SUM(price * amount) AS Стоимость,
# round((SUM(price * amount)*0.18/1.18),2) AS НДС,
# round((SUM(price * amount)/1.18),2) AS Стоимость_без_НДС
# FROM book GROUP BY author;
# +------------------+-----------+---------+-------------------+
# | author           | Стоимость | НДС     | Стоимость_без_НДС |
# +------------------+-----------+---------+-------------------+
# | Булгаков М.А.    | 4715.47   | 719.31  | 3996.16           |
# | Достоевский Ф.М. | 11802.03  | 1800.31 | 10001.72          |
# | Есенин С.А.      | 9750.00   | 1487.29 | 8262.71           |
# +------------------+-----------+---------+-------------------+

# SELECT MIN(price) AS Минимальная_цена,
# MAX(price) AS Максимальная_цена,
# round(AVG(price),2) AS Средняя_цена
# FROM book;
# +------------------+-------------------+--------------+
# | Минимальная_цена | Максимальная_цена | Средняя_цена |
# +------------------+-------------------+--------------+
# | 460.00           | 799.01            | 600.17       |
# +------------------+-------------------+--------------+

# SELECT author,
#     MIN(price) AS Минимальная_цена,
#     MAX(price) AS Максимальная_цена
# FROM book
# GROUP BY author
# HAVING SUM(price * amount) > 5000;

# Вычислить среднюю цену и суммарную стоимость тех книг, количество экземпляров которых принадлежит интервалу
# от 5 до 14,включительно. Столбцы назвать Средняя_цена и Стоимость, значения округлить до 2-х знаков после запятой.
# SELECT round(AVG(price),2) AS Средняя_цена,
# SUM(price*amount) AS Стоимость
# FROM book
# WHERE amount BETWEEN 5 AND 14;
# +--------------+-----------+
# | Средняя_цена | Стоимость |
# +--------------+-----------+
# | 493.67       | 12107.50  |
# +--------------+-----------+

# Посчитать стоимость всех экземпляров каждого автора без учета книг «Идиот» и «Белая гвардия».
# В результат включить только тех авторов, у которых суммарная стоимость книг (без учета книг «Идиот» и «Белая гвардия»)
# более 5000 руб. Вычисляемый столбец назвать Стоимость. Результат отсортировать по убыванию стоимости.
# SELECT author, SUM(price*amount) AS Стоимость
# FROM book
# WHERE title NOT IN ('Идиот', 'Белая гвардия')
# GROUP BY author
# HAVING SUM(price*amount) > 5000
# ORDER BY Стоимость DESC
# +------------------+-----------+
# | author           | Стоимость |
# +------------------+-----------+
# | Есенин С.А.      | 9750.00   |
# | Достоевский Ф.М. | 7202.03   |
# +------------------+-----------+


