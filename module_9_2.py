first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(c) for c in first_strings if len(c) > 5]
second_result = [(c, q) for c in first_strings for q in second_strings if len(c) == len(q)]
third_result = {c: len(c) for c in (first_strings + second_strings) if len(c) % 2 == 0}


print(first_result)
print(second_result)
print(third_result)
