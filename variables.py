"""
Задача:
Напишите 4 переменных которые буду обозначать следующие данные:

    Количество выполненных ДЗ (запишите значение 12)
    Количество затраченных часов (запишите значение 1.5)
    Название курса (запишите значение 'Python')
    Время на одно задание (вычислить используя 1 и 2 переменные)

Выведите на экран(в консоль), используя переменные, следующую строку:
Курс: Python, всего задач:12, затрачено часов: 1.5, среднее время выполнения 0.125 часа.
"""

all_homeworks = 12
all_timeleft = 1.5
name_of_course = "Python"
midle_time_works = all_timeleft/all_homeworks

print(
    f"Курс: {name_of_course}\n"
    f"Всего задач: {all_homeworks}\n"
    f"Затрачено часов: {all_timeleft}\n"
    f"Среднее время выполнения: {midle_time_works}")
