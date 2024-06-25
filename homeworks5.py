"""
Написать программу на языке Python, используя Pycharm, для работы с неизменяемыми и изменяемыми объектами.

1. В проекте, где вы решаете домашние задания, создайте модуль 'homework5.py' и напишите весь код в нём.

2. Задайте переменные разных типов данных:
  - Создайте переменную immutable_var и присвойте ей кортеж из нескольких элементов разных типов данных.
  - Выполните операции вывода кортежа immutable_var на экран.

3. Изменение значений переменных:
  - Попытайтесь изменить элементы кортежа immutable_var. Объясните, почему нельзя изменить значения элементов кортежа.

4. Создание изменяемых структур данных:
  - Создайте переменную mutable_list и присвойте ей список из нескольких элементов.
  - Измените элементы списка mutable_list.
  - Выведите на экран измененный список mutable_list.
"""

immutable_var = (0, 2, 3, "Я кортеж", True, False, [0, 4, 6])
print(immutable_var)  # Котреж является упорядочным, неизменяемым типом данных
immutable_var[-1][0] = 100  # Но мы можем изменять список внутри котрежа если он есть
print(immutable_var)

mutable_list = ["Я список", 1, 2.3, 6.66, 10]
print(mutable_list)  # Список является упорядочным, изменяемым типом данных
print(mutable_list * 2 + mutable_list)  # Список поддерживает простые математические операции "+" и "*"
print([i*2 for i in mutable_list])  # Для изменения значений внутри списка возможно использовать цикл или по индексу
mutable_list[0] = "Теперь здесь что-то другое"  # Изменение по индексу
print(mutable_list)  # Измененый список


