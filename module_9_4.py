first = 'Мама мыла раму'
second = 'Рамена мало было'

print(list(map(lambda x, y: x == y, first, second)))


def get_advanced_write(file_name):
    try:
        file = open(file_name, 'a+', encoding='utf-8')
    except:
        file = open(file_name, 'w+', encoding='utf-8')

    def write_everything(*data_set):
        [file.write(str(c) + '\n') for c in data_set]
        file.close()

    return write_everything


write = get_advanced_write('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'], 12, 2333, 4567)

from random import choice


class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self, *args, **kwargs):
        return choice(self.words)


first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
