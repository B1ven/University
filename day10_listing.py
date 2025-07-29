# Функции def()
# Функции можно объявлять с параметрами(атрибутами) так и без них
# Примеры функций без параметров
def generate_full_name(): # Блок объявления функции идет всегда перед вызовом
  name = 'Biven'
  last_name = 'Borovskoy'
  space = ' '
  full_name = name + space + last_name
  print(full_name) # результат - "Biven Borovskoy"


generate_full_name() # Вызов функции

def add_two_numbers():
  num1 = 4
  num2 = 6
  total = num1 + num2
  return total # Функция может возвращать, если не указан оператор return функция ничего не возвращает, значение будет None

print(add_two_number())


# В функцию мы можем передавать параметры(аргументы) различные типы данных
# Если в функции указан параметр мы должны вызывать её с аргументом
def function_name(parametr):
  pass

function_name(argument)

def greetings(name):
  message = name + ' welcome to Python Everyone'
  return message

print(greetings('Biven')) # Результат - "Biven welcome to Python Everyon"


def add_ten(num):
  return num + 10

print(add_ten(90)) # результат - 100


def square_number(x):
  return x * x

print(square_number(2)) # Результат - 4


def area_of_circle(r):
  pi = 3.14
  area = pi * r ** 2
  return area

print(area_of_circle(50))


def sum_of_numbers(n):
  total = 0
  for i in range(n+1):
    total += i
  return total

print(sum_of_numbers(10))
print(sum_of_numbers(55))









