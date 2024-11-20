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

# cursor.execute("SELECT * FROM Users")
# users = cursor.fetchall()
# for user in users:
#     print(user)

cursor.execute("DELETE FROM Users WHERE id = ?", (6,))
cursor.execute("SELECT COUNT(*) FROM Users")
all_users = cursor.fetchone()[0]
cursor.execute("SELECT SUM(balance) FROM Users")
sum_balance = cursor.fetchall()[0]
sum_balance = sum_balance[0]    # Ввиду того что запрос возвращает кортеж, в этой строчке мы переприсваеваем число
cursor.execute("SELECT AVG(balance) FROM Users")
average = cursor.fetchone()[0]

print(all_users)
print(sum_balance)
print(average)  # Или воспользоваться уже известными переменными суммой баланс и суммой пользователей
print(sum_balance/all_users)

connection.commit()
connection.close()


