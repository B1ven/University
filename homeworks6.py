"""
1. В проекте, где вы решаете домашние задания, создайте модуль 'homework6.py' и напишите весь код в нём.

2. Работа со словарями:
  - Создайте переменную my_dict и присвойте ей словарь из нескольких пар ключ-значение.
Например: Имя(str)-Год рождения(int).
  - Выведите на экран словарь my_dict.
  - Выведите на экран одно значение по существующему ключу, одно по отсутствующему из словаря my_dict без ошибки.
  - Добавьте ещё две произвольные пары того же формата в словарь my_dict.
 - Удалите одну из пар в словаре по существующему ключу из словаря my_dict и выведите значение из этой пары на экран.
  - Выведите на экран словарь my_dict.

3. Работа с множествами:
  - Создайте переменную my_set и присвойте ей множество, состоящее из разных типов данных с повторяющимися значениями.
  - Выведите на экран множество my_set (должны отобразиться только уникальные значения).
  - Добавьте 2 произвольных элемента в множество my_set, которых ещё нет.
  - Удалите один любой элемент из множества my_set.
  - Выведите на экран измененное множество my_set.
"""

my_dict = {"Sergey": 1991}
print(my_dict)
print(my_dict["Sergey"])
print(my_dict.get("Age"))

my_dict["Andrey"] = 1990
my_dict["Ivan"] = 2000
print(my_dict)

temp = my_dict.pop("Andrey")
print(my_dict)
print(temp)


my_set = {1, 1, 2, 2, 3, 3, 5, 5, True, True, False, False, "z", 'z'}
print(my_set)

my_set.add("Python")
my_set.update("hello")
print(my_set)

my_set.remove(False)
print(my_set)


