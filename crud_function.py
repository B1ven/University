import sqlite3

connection = sqlite3.connect('products_place.db')
cursor = connection.cursor()


def initiat_db():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Product(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL);
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL
    );
    """)


def get_all_products():
    return cursor.execute("SELECT * FROM Product")


def user_auth(name, age, email):
    check_member = cursor.execute("SELECT * FROM Users WHERE email=?", (email,))
    if check_member.fetchone() is None:
        cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES(?,?,?,?)",
                       (name, email, age, 1000))
        connection.commit()
        return f'Добро пожаловать {name}!'
    else:
        return f'Пользователь с таким "email" уже существует'


# print(user_auth('qwer', 2, '1221'))

connection.commit()
# connection.close()

