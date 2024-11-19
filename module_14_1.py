import sqlite3
from random import randint


connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER, 
balance INTEGER NOT NULL
)
""")
cursor.execute('''CREATE INDEX IF NOT EXISTS idx_email ON Users(email)''')

# for i in range(1, 11):    # Создание записей в таблице
#     payment = randint(100, 1500)
#     cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES(?,?,?,?)",
#                    (f'Users{i}', f'example{i}@gmail.com', f'{18 + i}', f'{payment}'))

for s in range(1, 11):
    if s % 2 == 0:
        continue
    else:
        cursor.execute("UPDATE Users SET balance = ? WHERE username = ?", (500, f'Users{s}'))

for s in range(1, 11, 3):
    cursor.execute("DELETE FROM Users WHERE username = ?", (f'Users{s}',))

cursor.execute("SELECT * FROM Users")
users = cursor.fetchall()
for user in users:
    print(user)

connection.commit()
connection.close()


