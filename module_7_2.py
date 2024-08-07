def custom_write(file_name, strings):
    file = open(file_name, 'w+', encoding='utf-8')
    string_position = {}
    for c in range(len(strings)):
        string_position[c+1, file.tell()] = strings[c]
        file.write(strings[c])
        file.write('\n')

    file.close()

    return string_position

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)


