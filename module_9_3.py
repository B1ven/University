first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = [len(c) - len(q) for c, q in zip(first, second) if len(c) != len(q)]
second_result = [len(first[c]) == len(second[c]) for c in range(len(first))]

print(first_result)
print(second_result)
