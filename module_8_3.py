class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message


class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message


class Car:
    def __init__(self, model, vin, numbers):
        self.model = model
        self.__vin = vin
        self.__numbers = numbers
        self.__is_valid_vin()
        self.__is_valid_numbers()

    def __is_valid_numbers(self):
        if len(self.__numbers) > 6:
            raise IncorrectCarNumbers('Неверная длина номера')
        elif isinstance(self.__numbers, (int, tuple, list, dict, set, float)):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        else:
            return True

    def __is_valid_vin(self):
        if isinstance(self.__vin, (str, tuple, dict, set, float, list)):
            raise IncorrectVinNumber('Некорректный тип vin номер')
        elif self.__vin < 1000000 or self.__vin > 9999999:
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        else:
            return True


try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')
