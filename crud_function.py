import sqlite3

connection = sqlite3.connect('products_place.db')
cursor = connection.cursor()


def initiate_db():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Product(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL)
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL
    )
    """)


for i in range(1, 5):
    cursor.execute(f"INSERT INTO Product (title, description, price) VALUES(?,?,?)",
               (f'Product{i}', f'Описание продукта{i}', 100 * i))


def get_all_products():
    return cursor.execute("SELECT * FROM Product")


def user_auth(name, age, email):
    cursor.execute("INSERT INTO Users (username, email, age) VALUES(?,?,?)", (name, email, age))

