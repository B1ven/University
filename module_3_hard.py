def calculate_structure_sum(x):
    resul = 0
    for i in x:
        if type(i) is int:
            resul += i
        elif type(i) is str:
            resul += len(i)
        elif type(i) is dict:
            resul += calculate_structure_sum(i.values())
            resul += calculate_structure_sum(i) 
        else:
            resul += calculate_structure_sum(i)
    return resul


data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]


result = calculate_structure_sum(data_structure)
print(result)



