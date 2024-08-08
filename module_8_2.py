def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    count = 0
    for i in numbers:
        try:
            result = result + i
            count += 1
        except TypeError:
            incorrect_data += 1
            print(f'Некорректный тип данных для подсчёта суммы - {incorrect_data}')
            
    return result, incorrect_data, count
    
def calculate_average(numbers):
    
    try:
        sum_num, error, len_num = personal_sum(numbers)
        return sum_num/len_num
    except ZeroDivisionError:
        return 0
    except TypeError:
        print('Некорректный тип данны')
        return None
        


print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать

