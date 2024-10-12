def is_prime(func):
    def wrapper(*args):
        resutl = func(*args)
        flag = False
        count = 0
        for i in range(1, resutl+1):
            if resutl % i == 0 and i != resutl:
                count += 1
            if i == resutl and count == 1:
                flag = True
        is_number = "Простое" if flag else "Сложное"
        return is_number, func(*args)
    return wrapper


@is_prime
def sum_three(*args):
    r = sum(args)
    return r


result = sum_three(2, 3, 6)
print(result)
