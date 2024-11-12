"""
Задание: Необходимо создать функцию, которая принимает объект (любого типа) в качестве аргумента и проводит 
интроспекцию этого объекта, чтобы определить его тип, атрибуты, методы, модуль, и другие свойства.

1. Создайте функцию introspection_info(obj), которая принимает объект obj.
2. Используйте встроенные функции и методы интроспекции Python для получения информации о переданном объекте.
3. Верните словарь или строки с данными об объекте, включающий следующую информацию:
  - Тип объекта.
  - Атрибуты объекта.
  - Методы объекта.
  - Модуль, к которому объект принадлежит.
  - Другие интересные свойства объекта, учитывая его тип (по желанию).
  """
import inspect
from pprint import pprint


class Test:
    def __init__(self, name):
        self.name = name

    def say_bay(self):
        print(f'{self.name} Bay bay')


def introspection_info(obj):
    all_info = dict()
    all_info['Тип объекта'] = type(obj) if inspect.isclass(obj) is False else 'class'
    all_info['Модуль'] = inspect.getmodule(obj)
    if callable(obj) is True:
        all_info['Callable'] = 'Вызываемый'
    else:
        all_info['Callable'] = 'Не вызываемый'
    all_info['ALL_INFO'] = dict()
    for attr_name in dir(obj):
        attr = getattr(obj, attr_name)
        if all_info['ALL_INFO'].get(str(type(attr)), False) is False:
            all_info['ALL_INFO'][str(type(attr))] = [str(attr_name)]
        else:
            all_info['ALL_INFO'][str(type(attr))].append(str(attr_name))
    return all_info


pprint(introspection_info(Test))
pprint(introspection_info(introspection_info))
pprint(introspection_info(44))
pprint(introspection_info('GHbdqwe'))
pprint(introspection_info(True))
