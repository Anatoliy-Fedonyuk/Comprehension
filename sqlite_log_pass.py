import sqlite3 as sq

with sq.connect("log_pass.db") as con:
    cur = con.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS users
        (name TEXT NOT NULL,
        login TEXT NOT NULL,
        password TEXT NOT NULL
        )""")

    # con.commit()

    new_users = [("Artur", 'artur', '54321'),
                 ("Sveta", 'durbez', '12345'),
                 ("Vasya", 'vasil01', '01vasil')]

    # cur.executemany("INSERT INTO users (name, login, password) VALUES (?,?,?)", new_users)

    if input("Login or Register? 1 / 2: ") == '1':
        name = input("Enter your Name: ")
        login = input("Enter Login: ")

        cur.execute(f"SELECT login FROM users WHERE login = '{login}'")
        if not cur.fetchone() is None:
            password = input("Enter Password: ")

            cur.execute(f"SELECT login, password FROM users WHERE login = '{login}'")
            if cur.fetchone()[1] == password:
                print("You entered system !")
            else:
                print("Wrong password !")
        else:
            print("This username not exist !")

    else:
        inp_name = input("Enter your Name: ")
        inp_login = input("Enter Login: ")
        inp_password = input("Enter Password: ")

        cur.execute(f"SELECT login FROM users WHERE login = '{inp_login}'")
        if cur.fetchone() is None:
            cur.execute("INSERT INTO users VALUES (?,?,?)", (inp_name, inp_login, inp_password))
        else:
            print("This username already exist !")

    cur.execute("SELECT * FROM users")
    print(cur.fetchall())

    # cur.execute("DROP TABLE IF EXISTS users")
