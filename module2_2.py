"""
Задача "Все ли равны?": На вход программе подаются 3 целых числа и записываются в переменные first, second и third
соответственно. Ваша задача написать условную конструкцию (из if, elif, else), которая выводит кол-во одинаковых
чисел среди 3-х введённых.

Пункты задачи:

    Если все числа равны между собой, то вывести 3
    Если хотя бы 2 из 3 введённых чисел равны между собой, то вывести 2
    Если равных чисел среди 3-х вообще нет, то вывести 0
"""

first, second, third = int(input("1st number: ")), int(input("2nd number: ")), int(input("3rd number: "))
count = 0

if first == second == third:
    count += 3
elif first == second != third:
    count += 2
elif first != second == third:
    count += 2
elif first == third != second:
    count += 2

print(f"Matches found - {count}")


